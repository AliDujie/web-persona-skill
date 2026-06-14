"""Web Persona 人物角色创建与应用工具包

基于《赢在用户：Web人物角色创建与应用实践指南》全书知识体系构建。
覆盖 SKILL.md 全部 A-J 模块的执行能力。

快速开始::

    from persona import PersonaSkill
    skill = PersonaSkill("我的产品")

    # 生成访谈提纲
    guide = skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"])

    # 设计调查问卷
    survey = skill.generate_survey("需求调研", "needs", pain_points=["找酒店耗时"])

    # 创建人物角色
    skill.add_persona("小明", "效率型用户", "primary", "我只想快速完成",
                      goals=["快速完成任务"], behaviors=["频繁使用"],
                      attitudes=["追求效率"], bio="小明是一位忙碌的白领...")
    print(skill.render_all_personas())
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional

from persona.persona_builder import PersonaBuilder
from persona.survey import SurveyBuilder
from persona.interview import InterviewBuilder
from persona.measure import MeasureSystem
from persona.segment import SegmentAnalyzer
from persona.strategy import StrategyAnalyzer

__version__ = "3.3.39"

__all__ = ["PersonaSkill", "__version__"]


class PersonaSkill:
    """Facade / 门面类 — 统一入口聚合 Persona 全部执行能力。

    Every method is a thin wrapper around the underlying module classes,
    keeping the public API identical to what the README and examples expect.
    """

    def __init__(self, product_name: str) -> None:
        self.product_name = product_name
        self._builder = PersonaBuilder(product_name)
        self._segmenter = SegmentAnalyzer()
        self._measure = MeasureSystem(product_name)
        self._feature = StrategyAnalyzer(product_name)

    # ── 角色管理 / Persona Management ──
    def add_persona(
        self,
        name: str,
        short_desc: str,
        priority: str = "primary",
        quote: str = "",
        goals: Optional[List[str]] = None,
        behaviors: Optional[List[str]] = None,
        attitudes: Optional[List[str]] = None,
        bio: str = "",
        demographics: Optional[Dict[str, str]] = None,
        tech_usage: Optional[Dict[str, str]] = None,
        business_goals: Optional[List[str]] = None,
    ) -> None:
        """添加一个人物角色。"""
        self._builder.add_persona(
            name=name,
            short_desc=short_desc,
            priority=priority,
            quote=quote,
            goals=goals,
            behaviors=behaviors,
            attitudes=attitudes,
            bio=bio,
            demographics=demographics,
            tech_usage=tech_usage,
            business_goals=business_goals,
        )

    def render_all_personas(self) -> str:
        """渲染所有角色的 Markdown 文档。"""
        return self._builder.render_all_markdown()

    def review_personas(self) -> str:
        """评审角色质量并输出报告。"""
        review = self._builder.review_quality()
        return self._builder.render_review_markdown(review)

    # ── 用户分段 / User Segmentation ──
    def add_user(
        self,
        user_id: str,
        goals: Optional[List[str]] = None,
        behaviors: Optional[List[str]] = None,
        attitudes: Optional[List[str]] = None,
        demographics: Optional[Dict[str, str]] = None,
        quotes: Optional[List[str]] = None,
    ) -> None:
        """录入单个用户的研究数据。"""
        self._segmenter.add_user(
            user_id=user_id,
            goals=goals,
            behaviors=behaviors,
            attitudes=attitudes,
            demographics=demographics,
            quotes=quotes,
        )

    def add_segment(
        self,
        name: str,
        description: str,
        core_goals: Optional[List[str]] = None,
        typical_behaviors: Optional[List[str]] = None,
        key_attitudes: Optional[List[str]] = None,
        percentage: float = 0.0,
        users: Optional[List[str]] = None,
    ) -> None:
        """定义用户分段。"""
        self._segmenter.add_segment(
            name=name,
            description=description,
            core_goals=core_goals,
            typical_behaviors=typical_behaviors,
            key_attitudes=key_attitudes,
            percentage=percentage,
            users=users,
        )

    def render_segments(self) -> str:
        """渲染分段结果。"""
        return self._segmenter.render_markdown()

    # ── 访谈提纲 / Interview Guide ──
    def generate_interview(
        self,
        title: str,
        sections: Optional[List[str]] = None,
        context: str = "",
        target_users: str = "",
    ) -> str:
        """生成结构化访谈提纲。"""
        ib = InterviewBuilder(title)
        if context:
            ib.set_context(context)
        if target_users:
            ib.set_target_users(target_users)
        if sections:
            ib.include_sections(sections)
        interview = ib.build()
        return InterviewBuilder.render_markdown(interview)

    # ── 问卷设计 / Survey Design ──
    def generate_survey(
        self,
        title: str,
        survey_type: str = "needs",
        pain_points: Optional[List[str]] = None,
        hypotheses: Optional[List[str]] = None,
        segments: Optional[List[str]] = None,
    ) -> str:
        """生成调查问卷。"""
        sb = SurveyBuilder(title, survey_type)
        if pain_points:
            sb.set_pain_points(pain_points)
        if hypotheses:
            sb.set_hypotheses(hypotheses)
        if segments:
            sb.set_segments(segments)
        survey = sb.build()
        return SurveyBuilder.render_markdown(survey)

    # ── CEO 报告 / CEO Report ──
    def generate_persona(
        self,
        include_ceo_analysis: bool = False,
        total_users: int = 0,
    ) -> str:
        """生成完整的角色文档（可选 CEO 分析）。"""
        parts = [self._builder.render_all_markdown()]
        if include_ceo_analysis:
            review = self._builder.review_quality()
            parts.append(self._builder.render_review_markdown(review))
            if total_users > 0:
                parts.append(f"\n**总用户基数:** {total_users:,}")
        return "\n\n".join(parts)

    # ── 功能优先级 / Feature Prioritization ──
    def add_feature(
        self,
        name: str,
        persona_needs: Dict[str, str],
        impact: str = "高",
        effort: str = "中",
    ) -> None:
        """添加功能到优先级矩阵。"""
        self._feature.add_feature(name, persona_needs, impact, effort)

    def render_feature_matrix(self) -> str:
        """渲染功能优先级矩阵。"""
        return self._feature.render_feature_matrix_markdown()

    # ── 测试脚本 / Test Scripts ──
    def add_test_script(
        self,
        persona_name: str,
        steps: Optional[List[Dict[str, str]]] = None,
    ) -> None:
        """添加可用性测试脚本。"""
        if steps:
            self._measure.add_test_script(persona_name, steps)

    def render_test_plan(self) -> str:
        """渲染测试计划。"""
        return self._measure.render_test_plan_markdown()
