"""Persona × LLM Prompt Library（v2.6 新增）

把 Persona 卡片转为可重复使用的 LLM 系统提示，支持 4 种用法：
- simulated_interview：让 LLM 扮演 Persona 接受访谈
- copy_evaluation：让 Persona 评估一段文案
- devils_advocate：让 LLM 扮演反向 Persona
- multi_persona_tournament：多 Persona 并行评估同一方案

设计原则：
- 仅输出 prompt 字符串；不耦合任何 LLM SDK
- 显式 Constitutional 约束以抑制幻觉
- 输出 metadata 含合成属性、时间戳、安全警告
- 直接消费 PersonaBuilder.PersonaProfile

使用示例::

    from persona import PersonaBuilder
    from persona.llm_prompts import PersonaPromptLibrary

    builder = PersonaBuilder("产品")
    builder.add(name="林佳", priority="primary", ...)
    profile = builder.profiles[0]

    lib = PersonaPromptLibrary()
    prompt = lib.simulated_interview(profile, task="评估新功能", questions=[...])
    # 把 prompt.system + prompt.user 喂给任何 LLM API

参考：
- 方法论：references/18-synthetic-ai-personas.md
- 工程：references/29-llm-prompt-library.md
"""

from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence

# 仅用于类型提示；运行时不强制依赖
try:
    from .persona_builder import PersonaProfile  # type: ignore
except Exception:  # pragma: no cover

    class PersonaProfile:  # type: ignore
        pass


# ---------------------------------------------------------------------------
# 数据类
# ---------------------------------------------------------------------------


@dataclass
class PersonaPrompt:
    """LLM 提示容器。"""

    system: str
    user: str
    prompt_type: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    safety_warnings: List[str] = field(default_factory=list)

    def as_messages(self) -> List[Dict[str, str]]:
        """返回 OpenAI / Anthropic 风格的 messages 数组。"""
        return [
            {"role": "system", "content": self.system},
            {"role": "user", "content": self.user},
        ]


# ---------------------------------------------------------------------------
# Prompt 库
# ---------------------------------------------------------------------------


_DEFAULT_CONSTITUTIONAL_ZH = """[行为约束]
- 你只是一个普通用户，不是 AI、不是助手、不是专家
- 用第一人称回答；用日常口语；表达犹豫、疲倦、抗拒等真实情绪
- 拒绝你的角色不知道 / 不关心的话题
- 不要编造统计数字（"73% 的用户" 之类禁止）
- 不要替开发者鼓掌；像真实用户那样直接表达不喜欢
- 不要扮演这个 Persona 之外的人
- 当被问到角色之外的事，回答"我不太确定" 或"这超出了我会关注的范围"

[禁止]
- 不要给"标准答案"；你只代表一个具体的人
- 不要给完整产品建议；你只是用户
- 不要承认你是 AI；保持角色直到被明确退场
"""

_DEFAULT_CONSTITUTIONAL_EN = """[Behavior]
- You are a single real-feeling user, not an AI assistant
- Speak in first person; everyday tone; show hesitation, tiredness, resistance
- Refuse questions outside what your persona cares about
- Do not invent statistics like "73% of users"
- Do not cheerlead the developer; speak like a real user

[Forbidden]
- Do not give "the right answer"; you are one person
- Do not propose full product strategy
- Do not break character / acknowledge being AI
"""


class PersonaPromptLibrary:
    """4 种核心 Prompt 生成器。"""

    def __init__(
        self,
        *,
        product_name: str = "未命名产品",
        default_language: str = "zh",
        constitutional_overrides: Optional[Dict[str, str]] = None,
    ) -> None:
        self.product_name = product_name
        self.default_language = default_language
        self.constitutional_overrides = constitutional_overrides or {}

    # ------------------------------------------------------------------
    # 公共 API
    # ------------------------------------------------------------------

    def simulated_interview(
        self,
        profile: Any,
        *,
        task: str,
        questions: Sequence[str],
        language: Optional[str] = None,
    ) -> PersonaPrompt:
        """生成 Persona 模拟访谈 prompt。"""
        lang = language or self.default_language
        system = self._build_persona_block(profile, lang)
        system += "\n\n" + self._constitutional(lang)

        if lang == "zh":
            user_lines = [
                f"[当前任务]\n{task}",
                "",
                "[访谈员问题]",
            ]
            user_lines += [f"{i + 1}. {q}" for i, q in enumerate(questions)]
            user_lines += [
                "",
                "请按顺序回答；每条回答 50-150 字；用第一人称、日常口语；可表达犹豫与矛盾。",
                "回答末尾自动追加：（合成访谈，仅供参考，需真实用户验证）",
            ]
        else:
            user_lines = [
                f"[Task]\n{task}",
                "",
                "[Interviewer Questions]",
            ]
            user_lines += [f"{i + 1}. {q}" for i, q in enumerate(questions)]
            user_lines += [
                "",
                "Answer in order, 50-150 words each, first person, conversational.",
                "Append at end: (synthetic interview, requires real-user validation)",
            ]
        user = "\n".join(user_lines)

        return PersonaPrompt(
            system=system,
            user=user,
            prompt_type="simulated_interview",
            metadata=self._meta(profile, task, lang),
            safety_warnings=[
                "synthetic; not a substitute for real interviews",
                "do not paste output into PRDs without human review",
            ],
        )

    def copy_evaluation(
        self,
        profile: Any,
        *,
        copy_text: str,
        rubric: Sequence[str],
        language: Optional[str] = None,
    ) -> PersonaPrompt:
        """生成单 Persona 评估文案的 prompt。"""
        lang = language or self.default_language
        system = self._build_persona_block(profile, lang)
        system += "\n\n" + self._constitutional(lang)

        rubric_lines = "\n".join(f"- {r}" for r in rubric)
        if lang == "zh":
            user = (
                f"[文案]\n{copy_text}\n\n"
                f"[评分标准]\n{rubric_lines}\n\n"
                "请按下表输出（用 Markdown）：\n"
                "| 维度 | 分数 | 一句话理由 |\n"
                "并在表后用 50 字左右说明：\"如果这条文案出现在我现在的生活中，我的真实反应是什么\"。\n"
                "末尾标注：（合成评估，仅供参考）"
            )
        else:
            user = (
                f"[Copy]\n{copy_text}\n\n"
                f"[Rubric]\n{rubric_lines}\n\n"
                "Output a Markdown table with columns: dimension | score | one-line reason.\n"
                "Then add ~50 words: \"If I encountered this copy in my real life, my honest reaction would be...\"\n"
                "End with: (synthetic evaluation, requires real-user validation)"
            )

        return PersonaPrompt(
            system=system,
            user=user,
            prompt_type="copy_evaluation",
            metadata=self._meta(profile, f"copy_eval: {copy_text[:30]}", lang),
            safety_warnings=[
                "synthetic; one Persona ≠ one real user",
                "use multi_persona_tournament for diversity",
            ],
        )

    def devils_advocate(
        self,
        profile: Any,
        *,
        target: str,
        angle: str = "skeptic",
        language: Optional[str] = None,
    ) -> PersonaPrompt:
        """生成 Devil's Advocate prompt：让 Persona 充当怀疑者。"""
        lang = language or self.default_language
        system = self._build_persona_block(profile, lang)

        if lang == "zh":
            extra = (
                f"\n\n[Devil's Advocate 角度: {angle}]\n"
                "你不是单纯的用户——这次你被请来扮演**最难说服的怀疑者**。"
                "你要从你的真实人格出发，但放大你的疑虑、抗拒、抱怨与历史不愉快经历。"
                "你不需要客气，不需要给建设性意见，目标是**找出 5 个最可能让你拒绝的理由**。"
            )
            system += extra + "\n" + self._constitutional(lang)
            user = (
                f"[评估对象]\n{target}\n\n"
                "请输出：\n"
                "1. 5 个让你最想拒绝的理由（每条 30-60 字）\n"
                "2. 你最近一次类似失望经历的引语（一段口语）\n"
                "3. 一句『如果要让我接受，最起码要做到的事』\n"
                "末尾标注：（合成 Devil's Advocate，需真实用户验证）"
            )
        else:
            extra = (
                f"\n\n[Devil's Advocate angle: {angle}]\n"
                "You are not a regular user this time. You play the hardest skeptic. "
                "Stay in character but amplify your doubts, resistance, complaints, and bad past experiences. "
                "Do not be polite. List the top 5 reasons you would reject."
            )
            system += extra + "\n" + self._constitutional(lang)
            user = (
                f"[Target]\n{target}\n\n"
                "Output:\n"
                "1. Top 5 reasons you'd reject (30-60 words each)\n"
                "2. A direct quote of a similar past disappointment\n"
                "3. One line: 'minimum I'd need to accept this'\n"
                "End with: (synthetic devil's advocate, requires real-user validation)"
            )

        return PersonaPrompt(
            system=system,
            user=user,
            prompt_type="devils_advocate",
            metadata=self._meta(profile, f"devils_advocate: {target[:30]}", lang),
            safety_warnings=[
                "synthetic; do not treat as veto",
                "use to surface blind spots, not to make final decisions",
            ],
        )

    def multi_persona_tournament(
        self,
        profiles: Sequence[Any],
        *,
        scenarios: Sequence[str],
        rubric: Sequence[str],
        language: Optional[str] = None,
    ) -> PersonaPrompt:
        """生成多 Persona 并行评估同一组方案的 prompt。

        注意：此 prompt 假设 LLM 一次性评估所有 Personas；
        若 LLM 上下文较小，建议拆分为多个 simulated_interview 调用后由调用方汇总。
        """
        lang = language or self.default_language
        if not profiles:
            raise ValueError("profiles 不能为空")

        persona_blocks = [self._compact_persona(p, lang) for p in profiles]
        scenarios_text = "\n".join(f"- {s}" for s in scenarios)
        rubric_text = "\n".join(f"- {r}" for r in rubric)

        if lang == "zh":
            system = (
                "你是一台多视角访谈台。你将分别扮演下列每个 Persona，"
                "对相同的多个方案打分并给一句话理由。\n\n"
                "[Personas]\n" + "\n\n".join(persona_blocks) + "\n\n"
                + self._constitutional(lang)
            )
            user = (
                f"[候选方案]\n{scenarios_text}\n\n"
                f"[评分标准]\n{rubric_text}\n\n"
                "输出 Markdown 表格：行=Persona 名，列=方案，单元格=分数 / 一句话理由。\n"
                "表后给一段 80 字总结：哪个方案对几位 Persona 都接受？哪些方案有显著分歧？\n"
                "末尾标注：（合成 Tournament，需真实用户验证）"
            )
        else:
            system = (
                "You are a multi-Persona evaluation panel. You will play each Persona below "
                "and score the same set of scenarios.\n\n"
                "[Personas]\n" + "\n\n".join(persona_blocks) + "\n\n"
                + self._constitutional(lang)
            )
            user = (
                f"[Scenarios]\n{scenarios_text}\n\n"
                f"[Rubric]\n{rubric_text}\n\n"
                "Output a Markdown table: rows=Persona names, cols=scenarios, cells=score / 1-line reason.\n"
                "Then 80 words summary: which scenario satisfies most Personas? where does disagreement live?\n"
                "End with: (synthetic tournament, requires real-user validation)"
            )

        return PersonaPrompt(
            system=system,
            user=user,
            prompt_type="multi_persona_tournament",
            metadata={
                "personas": [getattr(p, "name", "unknown") for p in profiles],
                "scenarios": list(scenarios),
                "language": lang,
                "generated_at": _now_iso(),
                "product": self.product_name,
            },
            safety_warnings=[
                "synthetic; multi-persona tournaments work best for narrowing options, not picking winners",
                "always validate the chosen direction with real users",
            ],
        )

    # ------------------------------------------------------------------
    # 内部
    # ------------------------------------------------------------------

    def _build_persona_block(self, profile: Any, language: str) -> str:
        name = getattr(profile, "name", "Unknown")
        bio = getattr(profile, "bio", "")
        quote = getattr(profile, "quote", "")
        goals = getattr(profile, "goals", []) or []
        behaviors = getattr(profile, "behaviors", []) or []
        attitudes = getattr(profile, "attitudes", []) or []

        if language == "zh":
            block = [
                f"你是 {name}。",
                f"标志性引语：「{quote}」" if quote else "",
                f"自我介绍：{bio}" if bio else "",
                "目标：" + ", ".join(goals) if goals else "",
                "典型行为：" + ", ".join(behaviors) if behaviors else "",
                "态度倾向：" + ", ".join(attitudes) if attitudes else "",
                f"产品语境：{self.product_name}",
            ]
        else:
            block = [
                f"You are {name}.",
                f"Signature quote: '{quote}'" if quote else "",
                f"Self intro: {bio}" if bio else "",
                "Goals: " + ", ".join(goals) if goals else "",
                "Typical behaviors: " + ", ".join(behaviors) if behaviors else "",
                "Attitudes: " + ", ".join(attitudes) if attitudes else "",
                f"Product context: {self.product_name}",
            ]
        return "\n".join(line for line in block if line)

    def _compact_persona(self, profile: Any, language: str) -> str:
        name = getattr(profile, "name", "Unknown")
        quote = getattr(profile, "quote", "")
        goals = getattr(profile, "goals", []) or []
        if language == "zh":
            return f"### {name}\n标志语：「{quote}」\n核心目标：{'; '.join(goals[:3])}"
        return f"### {name}\nSignature: '{quote}'\nKey goals: {'; '.join(goals[:3])}"

    def _constitutional(self, language: str) -> str:
        if language in self.constitutional_overrides:
            return self.constitutional_overrides[language]
        return _DEFAULT_CONSTITUTIONAL_ZH if language == "zh" else _DEFAULT_CONSTITUTIONAL_EN

    def _meta(self, profile: Any, task: str, language: str) -> Dict[str, Any]:
        return {
            "persona_name": getattr(profile, "name", "unknown"),
            "task": task,
            "language": language,
            "generated_at": _now_iso(),
            "product": self.product_name,
        }


# ---------------------------------------------------------------------------
# 工具
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


__all__ = ["PersonaPromptLibrary", "PersonaPrompt"]
