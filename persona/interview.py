"""Persona 访谈提纲生成器

对应 SKILL.md 模块B：定性用户研究执行。
根据研究主题和目标用户自动生成定制化的访谈提纲，
支持按章节筛选、自定义追加和多格式输出。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .config import AnalysisConfig, INTERVIEW_SECTIONS
from .templates import INTERVIEW_QUESTIONS


@dataclass
class InterviewQuestion:
    """单个访谈问题"""

    section: str
    question: str
    is_custom: bool = False
    priority: int = 1
    follow_up: str = ""


@dataclass
class InterviewGuide:
    """完整的访谈指南"""

    title: str
    context: str
    target_users: str
    questions: List[InterviewQuestion] = field(default_factory=list)
    tips: List[str] = field(default_factory=list)
    duration: str = "45-60分钟"

    def get_by_section(self, section: str) -> List[InterviewQuestion]:
        """按章节筛选问题"""
        return [q for q in self.questions if q.section == section]

    def get_high_priority(self, min_priority: int = 2) -> List[InterviewQuestion]:
        """获取高优先级问题"""
        return [q for q in self.questions if q.priority >= min_priority]


SECTION_LABELS: Dict[str, str] = {
    "warmup": "暖场",
    "background": "背景与习惯",
    "goals": "目标与需求",
    "behavior": "行为与体验",
    "opinion": "观点与态度",
    "pain_point": "痛点与期望",
    "closing": "收尾",
}

DEFAULT_TIPS: List[str] = [
    "让用户讲故事——请他们描述具体经历而非抽象观点",
    "追问'为什么'——至少追问2-3层以挖掘深层目标",
    "注意非语言信号——表情、语气变化、停顿往往暗示关键信息",
    "允许偏离议题——用户主动提及的话题往往最有价值",
    "问做过什么而非想要什么——揭示偏好优于陈述偏好",
    "保持好奇心，不要引导受访者的回答",
    "关注具体事件和行为，而非抽象观点",
    "当受访者说'我觉得...'时，追问'能举个例子吗？'",
]


class InterviewBuilder:
    """访谈提纲构建器

    用法示例::

        builder = InterviewBuilder("电商平台用户访谈")
        builder.set_context("针对过去3个月内有过购物体验的用户")
        builder.set_target_users("25-40岁职场女性")
        builder.include_sections(["background", "goals", "behavior", "pain_point"])
        builder.add_custom_question(
            "goals", "你在网购时最看重的三个因素是什么？", priority=3
        )
        guide = builder.build()
        print(InterviewBuilder.render_markdown(guide))
    """

    def __init__(self, title: str, config: Optional[AnalysisConfig] = None):
        self.title = title
        self.config = config or AnalysisConfig()
        self._context = ""
        self._target_users = ""
        self._sections: List[str] = list(self.config.interview_sections)
        self._custom_questions: List[InterviewQuestion] = []
        self._extra_tips: List[str] = []

    def set_context(self, context: str) -> "InterviewBuilder":
        """设置访谈背景"""
        self._context = context
        return self

    def set_target_users(self, target: str) -> "InterviewBuilder":
        """设置目标用户群体"""
        self._target_users = target
        return self

    def include_sections(self, sections: List[str]) -> "InterviewBuilder":
        """指定要包含的访谈章节"""
        for s in sections:
            if s not in INTERVIEW_SECTIONS:
                raise ValueError(
                    f"未知章节: {s}，可选: {', '.join(INTERVIEW_SECTIONS)}"
                )
        self._sections = sections
        return self

    def add_custom_question(
        self,
        section: str,
        question: str,
        priority: int = 1,
        follow_up: str = "",
    ) -> "InterviewBuilder":
        """添加自定义问题"""
        self._custom_questions.append(
            InterviewQuestion(
                section=section,
                question=question,
                is_custom=True,
                priority=priority,
                follow_up=follow_up,
            )
        )
        return self

    def add_tip(self, tip: str) -> "InterviewBuilder":
        """添加额外的访谈技巧提示"""
        self._extra_tips.append(tip)
        return self

    def build(self) -> InterviewGuide:
        """构建完整的访谈指南"""
        questions: List[InterviewQuestion] = []

        for section in self._sections:
            template_qs = INTERVIEW_QUESTIONS.get(section, [])
            max_q = self.config.max_questions_per_section
            for q_text in template_qs[:max_q]:
                questions.append(
                    InterviewQuestion(section=section, question=q_text, priority=1)
                )

        for cq in self._custom_questions:
            questions.append(cq)

        tips = list(DEFAULT_TIPS) + self._extra_tips

        q_count = len(questions)
        duration = f"{max(30, q_count * 3)}~{max(45, q_count * 4)}分钟"

        return InterviewGuide(
            title=self.title,
            context=self._context,
            target_users=self._target_users,
            questions=questions,
            tips=tips,
            duration=duration,
        )

    @staticmethod
    def render_markdown(guide: InterviewGuide) -> str:
        """将访谈指南渲染为 Markdown 格式"""
        lines = [f"# {guide.title}\n"]

        if guide.context:
            lines.append(f"**访谈背景:** {guide.context}")
        if guide.target_users:
            lines.append(f"**目标用户:** {guide.target_users}")
        lines.append(f"**预计时长:** {guide.duration}\n")

        sections_in_order = []
        seen: set = set()
        for q in guide.questions:
            if q.section not in seen:
                sections_in_order.append(q.section)
                seen.add(q.section)

        for section in sections_in_order:
            label = SECTION_LABELS.get(section, section)
            lines.append(f"## {label}\n")
            section_qs = [q for q in guide.questions if q.section == section]
            for i, q in enumerate(section_qs, 1):
                marker = " ⭐" if q.priority >= 3 else ""
                custom_tag = " [自定义]" if q.is_custom else ""
                lines.append(f"{i}. {q.question}{marker}{custom_tag}")
                if q.follow_up:
                    lines.append(f"   - 追问: {q.follow_up}")
            lines.append("")

        if guide.tips:
            lines.append("## 访谈技巧\n")
            for tip in guide.tips:
                lines.append(f"- {tip}")
            lines.append("")

        return "\n".join(lines)

    @staticmethod
    def render_json(guide: InterviewGuide) -> Dict:
        """将访谈指南渲染为 JSON 可序列化字典"""
        return {
            "title": guide.title,
            "context": guide.context,
            "target_users": guide.target_users,
            "duration": guide.duration,
            "questions": [
                {
                    "section": q.section,
                    "question": q.question,
                    "is_custom": q.is_custom,
                    "priority": q.priority,
                    "follow_up": q.follow_up,
                }
                for q in guide.questions
            ],
            "tips": guide.tips,
        }
