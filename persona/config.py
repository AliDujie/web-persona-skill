"""Persona Skill 配置模块

定义知识库路径、角色优先级、研究方法、分析维度等全局配置。
"""

from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List


KNOWLEDGE_BASE_DIR = Path(__file__).parent.parent / "references"

KNOWLEDGE_FILES: Dict[str, str] = {
    "persona_basics": "01-persona-basics.md",
    "measuring_results": "02-measuring-results.md",
}

# ── 角色优先级 ──────────────────────────────────────────────

PERSONA_PRIORITIES = ("primary", "secondary", "unimportant", "negative")

PRIORITY_LABELS: Dict[str, str] = {
    "primary": "首要角色 (Primary)",
    "secondary": "次要角色 (Secondary)",
    "unimportant": "不重要角色 (Unimportant)",
    "negative": "负面角色 (Negative)",
}

# ── 研究方法 ────────────────────────────────────────────────

RESEARCH_METHODS = ("qualitative", "quantitative_validated", "quantitative")

RESEARCH_METHOD_LABELS: Dict[str, str] = {
    "qualitative": "定性研究 (Qualitative)",
    "quantitative_validated": "定量验证 (Quantitative Validated)",
    "quantitative": "定量研究 (Quantitative)",
}

# ── 角色核心维度 ────────────────────────────────────────────

PERSONA_DIMENSIONS = ("goals", "behaviors", "attitudes")

DIMENSION_LABELS: Dict[str, str] = {
    "goals": "目标 (Goals)",
    "behaviors": "行为 (Behaviors)",
    "attitudes": "态度 (Attitudes)",
}

# ── 访谈段落 ────────────────────────────────────────────────

INTERVIEW_SECTIONS = (
    "warmup",
    "background",
    "goals",
    "behaviors",
    "attitudes",
    "pain_points",
    "expectations",
    "closing",
)

SECTION_LABELS: Dict[str, str] = {
    "warmup": "暖场 (Warm-up)",
    "background": "背景信息 (Background)",
    "goals": "目标探索 (Goals)",
    "behaviors": "行为模式 (Behaviors)",
    "attitudes": "态度与动机 (Attitudes)",
    "pain_points": "痛点挖掘 (Pain Points)",
    "expectations": "期望收集 (Expectations)",
    "closing": "收尾总结 (Closing)",
}

# ── 问卷类型 ────────────────────────────────────────────────

SURVEY_TYPES = ("needs", "validation", "satisfaction")

# ── 功能优先级 ──────────────────────────────────────────────

FEATURE_PRIORITY_LEVELS = ("P0", "P1", "P2", "P3")


@dataclass
class AnalysisConfig:
    """角色分析任务的运行时配置"""

    include_dimensions: List[str] = field(
        default_factory=lambda: list(PERSONA_DIMENSIONS)
    )
    interview_sections: List[str] = field(
        default_factory=lambda: list(INTERVIEW_SECTIONS)
    )
    max_questions_per_section: int = 5
    output_format: str = "markdown"
    language: str = "zh"

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        """校验配置合法性。"""
        for d in self.include_dimensions:
            if d not in PERSONA_DIMENSIONS:
                raise ValueError(
                    f"未知的角色维度: {d}，可选: {PERSONA_DIMENSIONS}"
                )
        for s in self.interview_sections:
            if s not in INTERVIEW_SECTIONS:
                raise ValueError(
                    f"未知的访谈段落: {s}，可选: {INTERVIEW_SECTIONS}"
                )
        if self.output_format not in ("markdown", "json", "text"):
            raise ValueError(
                f"未知的输出格式: {self.output_format}，可选: markdown, json, text"
            )
