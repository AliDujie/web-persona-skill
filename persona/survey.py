"""Persona 问卷设计生成模块

对应 SKILL.md 模块C：定量用户研究执行。
支持需求探索型、细分验证型、满意度型三种问卷的自动生成。
"""

from dataclasses import dataclass, field
from typing import Dict, List


SURVEY_TYPES = ("needs", "validation", "satisfaction")

SURVEY_TYPE_LABELS: Dict[str, str] = {
    "needs": "需求探索问卷",
    "validation": "细分验证问卷",
    "satisfaction": "满意度问卷",
}

SURVEY_TYPE_DESCRIPTIONS: Dict[str, str] = {
    "needs": "探索用户目标、行为和观点，为人物角色细分提供定量数据",
    "validation": "验证定性研究中发现的细分假设，确认群体差异的统计显著性",
    "satisfaction": "产品发布后衡量各人物角色群体的满意度和需求满足程度",
}

QUESTION_FORMATS = ("single_choice", "multiple_choice", "scale", "ranking", "open_ended")

FORMAT_LABELS: Dict[str, str] = {
    "single_choice": "单选",
    "multiple_choice": "多选",
    "scale": "量表1-5",
    "ranking": "排序",
    "open_ended": "开放题",
}


@dataclass
class SurveyQuestion:
    """单个问卷题目"""
    question_format: str
    text: str
    options: List[str] = field(default_factory=list)
    scale_labels: Dict[int, str] = field(default_factory=dict)
    required: bool = True
    skip_logic: str = ""


@dataclass
class Survey:
    """完整问卷"""
    title: str
    survey_type: str
    description: str = ""
    target_audience: str = ""
    estimated_time: str = ""
    questions: List[SurveyQuestion] = field(default_factory=list)
    closing_text: str = "感谢您的参与！您的回答将帮助我们更好地理解用户需求并改进产品。"


class SurveyBuilder:
    """问卷构建器

    用法示例::

        builder = SurveyBuilder("电商平台用户调研", "needs")
        builder.set_target("过去3个月有过网购经历的用户")
        builder.set_product("某某商城")
        builder.set_pain_points(["找商品耗时", "价格比较困难", "售后体验差"])
        survey = builder.build()
        print(SurveyBuilder.render_markdown(survey))
    """

    def __init__(self, title: str, survey_type: str):
        if survey_type not in SURVEY_TYPES:
            raise ValueError(f"未知问卷类型: {survey_type}，可选: {SURVEY_TYPES}")
        self.title = title
        self.survey_type = survey_type
        self._target = ""
        self._product = ""
        self._pain_points: List[str] = []
        self._hypotheses: List[str] = []
        self._segments: List[str] = []
        self._custom_questions: List[SurveyQuestion] = []

    def set_target(self, target: str) -> "SurveyBuilder":
        self._target = target
        return self

    def set_product(self, product: str) -> "SurveyBuilder":
        self._product = product
        return self

    def set_pain_points(self, pain_points: List[str]) -> "SurveyBuilder":
        self._pain_points = pain_points
        return self

    def set_hypotheses(self, hypotheses: List[str]) -> "SurveyBuilder":
        self._hypotheses = hypotheses
        return self

    def set_segments(self, segments: List[str]) -> "SurveyBuilder":
        self._segments = segments
        return self

    def add_question(self, question: SurveyQuestion) -> "SurveyBuilder":
        self._custom_questions.append(question)
        return self

    def _build_needs(self) -> List[SurveyQuestion]:
        """需求探索问卷：目标/行为/观点/功能验证/人口统计"""
        product = self._product or "该产品"
        qs: List[SurveyQuestion] = []

        qs.append(SurveyQuestion(
            question_format="multiple_choice",
            text=f"您使用{product}的主要目的是什么？（最多选3项）",
            options=["完成工作需求", "获取信息", "娱乐消遣", "社交沟通", "购物交易", "其他"],
        ))
        qs.append(SurveyQuestion(
            question_format="single_choice",
            text=f"您使用{product}的频率是？",
            options=["每天多次", "每天一次", "每周几次", "每月几次", "更少"],
        ))
        qs.append(SurveyQuestion(
            question_format="multiple_choice",
            text="您通常通过什么设备使用？",
            options=["手机", "电脑", "平板", "其他"],
        ))
        qs.append(SurveyQuestion(
            question_format="scale",
            text="我愿意花更多时间来获得更好的结果",
            scale_labels={1: "非常不同意", 3: "中立", 5: "非常同意"},
        ))
        if self._pain_points:
            qs.append(SurveyQuestion(
                question_format="ranking",
                text="请按困扰程度排列以下问题：",
                options=list(self._pain_points) + ["其他"],
            ))
        qs.append(SurveyQuestion(
            question_format="single_choice",
            text="您的年龄段？",
            options=["18岁以下", "18-24岁", "25-34岁", "35-44岁", "45-54岁", "55岁以上"],
        ))
        qs.append(SurveyQuestion(
            question_format="single_choice",
            text="您的职业类型？",
            options=["学生", "职场新人", "资深职场人", "自由职业", "管理层", "其他"],
            required=False,
        ))
        return qs

    def _build_validation(self) -> List[SurveyQuestion]:
        """细分验证问卷：验证定性细分假设"""
        product = self._product or "该产品"
        qs: List[SurveyQuestion] = []

        if self._hypotheses:
            qs.append(SurveyQuestion(
                question_format="single_choice",
                text=f"以下哪个描述最符合您使用{product}的方式？",
                options=self._hypotheses,
            ))
        if self._segments:
            qs.append(SurveyQuestion(
                question_format="single_choice",
                text="以下哪种用户类型最接近您？",
                options=self._segments,
            ))
        qs.append(SurveyQuestion(
            question_format="scale",
            text=f"您对{product}的依赖程度如何？",
            scale_labels={1: "几乎不依赖", 3: "有一定依赖", 5: "高度依赖"},
        ))
        if self._pain_points:
            qs.append(SurveyQuestion(
                question_format="ranking",
                text="请按重要性排列以下因素：",
                options=self._pain_points,
            ))
            qs.append(SurveyQuestion(
                question_format="scale",
                text=f"使用{product}之前，以下问题对您的困扰程度：",
                scale_labels={1: "完全不困扰", 3: "有些困扰", 5: "非常困扰"},
            ))
        qs.append(SurveyQuestion(
            question_format="scale",
            text=f"您对{product}当前体验的满意程度：",
            scale_labels={1: "非常不满意", 3: "一般", 5: "非常满意"},
        ))
        qs.append(SurveyQuestion(
            question_format="open_ended",
            text=f"您认为{product}最需要改进的一个方面是什么？",
            required=False,
        ))
        return qs

    def _build_satisfaction(self) -> List[SurveyQuestion]:
        """满意度问卷：发布后衡量各角色群体的满意度"""
        product = self._product or "该产品"
        qs: List[SurveyQuestion] = []

        qs.append(SurveyQuestion(
            question_format="scale",
            text=f"总体而言，您对{product}的满意程度如何？",
            scale_labels={1: "非常不满意", 3: "一般", 5: "非常满意"},
        ))
        qs.append(SurveyQuestion(
            question_format="scale",
            text=f"您有多大可能向朋友或同事推荐{product}？",
            scale_labels={1: "完全不可能", 3: "可能", 5: "非常可能"},
        ))
        qs.append(SurveyQuestion(
            question_format="scale",
            text="易用性：操作是否简单直观？",
            scale_labels={1: "非常困难", 3: "一般", 5: "非常简单"},
        ))
        qs.append(SurveyQuestion(
            question_format="scale",
            text="功能性：功能是否满足您的需求？",
            scale_labels={1: "完全不满足", 3: "基本满足", 5: "完全满足"},
        ))
        if self._pain_points:
            qs.append(SurveyQuestion(
                question_format="multiple_choice",
                text=f"使用{product}过程中，您遇到过以下哪些问题？",
                options=list(self._pain_points) + ["没有明显问题", "其他"],
            ))
        qs.append(SurveyQuestion(
            question_format="single_choice",
            text=f"与之前使用的方案相比，{product}的表现如何？",
            options=["好很多", "好一些", "差不多", "差一些", "差很多", "首次使用此类产品"],
        ))
        qs.append(SurveyQuestion(
            question_format="open_ended",
            text=f"您最希望{product}增加或改进的功能是什么？",
            required=False,
        ))
        return qs

    def build(self) -> Survey:
        """构建完整问卷"""
        builders = {
            "needs": self._build_needs,
            "validation": self._build_validation,
            "satisfaction": self._build_satisfaction,
        }
        questions = builders[self.survey_type]()
        questions.extend(self._custom_questions)

        q_count = len(questions)
        estimated = f"{max(3, q_count * 1)}~{q_count * 2}分钟"

        return Survey(
            title=self.title,
            survey_type=self.survey_type,
            description=SURVEY_TYPE_DESCRIPTIONS[self.survey_type],
            target_audience=self._target,
            estimated_time=estimated,
            questions=questions,
        )

    @staticmethod
    def render_markdown(survey: Survey) -> str:
        """将问卷渲染为 Markdown 格式"""
        lines = [f"# {survey.title}\n"]
        lines.append(
            f"**问卷类型:** {SURVEY_TYPE_LABELS[survey.survey_type]}"
            f" — {survey.description}"
        )
        if survey.target_audience:
            lines.append(f"**目标人群:** {survey.target_audience}")
        lines.append(f"**预计填写时长:** {survey.estimated_time}\n")
        lines.append("---\n")

        for i, q in enumerate(survey.questions, 1):
            fmt = FORMAT_LABELS.get(q.question_format, q.question_format)
            lines.append(f"**Q{i}. [{fmt}]** {q.text}")
            if q.options:
                for opt in q.options:
                    if q.question_format == "multiple_choice":
                        lines.append(f"   - [ ] {opt}")
                    else:
                        lines.append(f"   - {opt}")
            if q.scale_labels:
                parts = [f"{k}={v}" for k, v in sorted(q.scale_labels.items())]
                lines.append(f"   ({' / '.join(parts)})")
            if q.skip_logic:
                lines.append(f"   *跳转逻辑: {q.skip_logic}*")
            if not q.required:
                lines.append("   *（选填）*")
            lines.append("")

        lines.append("---")
        lines.append(f"\n{survey.closing_text}")
        return "\n".join(lines)

    @staticmethod
    def render_json(survey: Survey) -> Dict:
        """将问卷渲染为 JSON 可序列化字典"""
        return {
            "title": survey.title,
            "type": survey.survey_type,
            "description": survey.description,
            "target_audience": survey.target_audience,
            "estimated_time": survey.estimated_time,
            "questions": [
                {
                    "format": q.question_format,
                    "text": q.text,
                    "options": q.options,
                    "scale_labels": {str(k): v for k, v in q.scale_labels.items()},
                    "required": q.required,
                    "skip_logic": q.skip_logic,
                }
                for q in survey.questions
            ],
            "closing_text": survey.closing_text,
        }
