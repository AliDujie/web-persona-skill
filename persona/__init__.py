"""Web Persona 人物角色创建与应用工具包

基于《赢在用户：Web人物角色创建和应用实践指南》全书知识体系构建。
覆盖 SKILL.md 全部 A-J 模块的执行能力。

快速开始::

    from persona import PersonaSkill
    skill = PersonaSkill("飞猪旅行")

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

__version__ = "1.0.0"

from .config import AnalysisConfig, PERSONA_PRIORITIES, PRIORITY_LABELS, KNOWLEDGE_FILES
from .config import RESEARCH_METHODS, PERSONA_DIMENSIONS, INTERVIEW_SECTIONS, SURVEY_TYPES
from .utils import load_knowledge, load_all_knowledge, search_knowledge
from .templates import (
    INTERVIEW_QUESTIONS, PERSONA_DOCUMENT_TEMPLATE,
    QUALITY_CHECKLIST, REPORT_TEMPLATE,
)
from .interview import InterviewBuilder, InterviewGuide
from .survey import SurveyBuilder, Survey
from .segment import SegmentAnalyzer, Segment, SegmentationResult
from .persona_builder import PersonaBuilder, PersonaProfile, QualityReview
from .strategy import StrategyAnalyzer, FeatureItem, BusinessValue
from .design import DesignAdvisor, ContentItem, PathValidation
from .measure import MeasureSystem, TestScript, MetricItem, BugPriority

from typing import Dict, List, Optional


class PersonaSkill:
    """Web Persona 统一入口类 — 封装全部 A-J 模块执行能力

    用法::

        skill = PersonaSkill("飞猪旅行")

        # 模块B: 访谈提纲
        guide = skill.generate_interview("用户访谈", ["goals", "pain_points"])

        # 模块C: 调查问卷
        survey = skill.generate_survey("需求调研", "needs", pain_points=["找酒店耗时"])

        # 模块D: 用户细分
        skill.add_user("U01", goals=["快速预订"], behaviors=["每周使用"], attitudes=["追求效率"])
        skill.add_segment("效率型", "追求速度", ["快速完成"], ["高频使用"], ["效率优先"], 40)
        print(skill.render_segments())

        # 模块E: 创建角色
        skill.add_persona("小明", "效率型用户", "primary", "快就是好",
                          goals=["快速完成"], behaviors=["高频"], attitudes=["效率"],
                          bio="小明是...")
        print(skill.render_all_personas())

        # 模块E: 质量评审
        review = skill.review_personas()

        # 模块H: 功能优先级
        skill.add_feature("快速预订", {"小明": "高"}, "高", "低")
        print(skill.render_feature_matrix())

        # 模块J: 测试计划
        skill.add_test_script("小明", [{"action": "打开首页", "expected": "显示推荐"}])
        print(skill.render_test_plan())
    """

    def __init__(self, product_name: str, config: Optional[AnalysisConfig] = None):
        self.product = product_name
        self.config = config or AnalysisConfig()
        self.segment_analyzer = SegmentAnalyzer()
        self.persona_builder = PersonaBuilder(product_name)
        self.strategy_analyzer = StrategyAnalyzer(product_name)
        self.design_advisor = DesignAdvisor(product_name)
        self.measure_system = MeasureSystem(product_name)

    # ── 模块B: 访谈 ──
    def generate_interview(self, title: str,
                           sections: Optional[List[str]] = None,
                           context: str = "") -> str:
        builder = InterviewBuilder(title, self.config)
        if context:
            builder.set_context(context)
        if sections:
            builder.include_sections(sections)
        guide = builder.build()
        return InterviewBuilder.render_markdown(guide)

    # ── 模块C: 问卷 ──
    def generate_survey(self, title: str, survey_type: str,
                        pain_points: Optional[List[str]] = None,
                        hypotheses: Optional[List[str]] = None,
                        segments: Optional[List[str]] = None) -> str:
        builder = SurveyBuilder(title, survey_type)
        builder.set_product(self.product)
        if pain_points:
            builder.set_pain_points(pain_points)
        if hypotheses:
            builder.set_hypotheses(hypotheses)
        if segments:
            builder.set_segments(segments)
        survey = builder.build()
        return SurveyBuilder.render_markdown(survey)

    # ── 模块D: 细分 ──
    def add_user(self, user_id: str, goals: List[str] = None,
                 behaviors: List[str] = None, attitudes: List[str] = None,
                 demographics: Dict = None, quotes: List[str] = None):
        return self.segment_analyzer.add_user(
            user_id, goals or [], behaviors or [], attitudes or [],
            demographics or {}, quotes or [])

    def add_segment(self, name: str, description: str,
                    core_goals: List[str], typical_behaviors: List[str],
                    key_attitudes: List[str], percentage: int = 0,
                    users: List[str] = None):
        return self.segment_analyzer.add_segment(
            name, description, core_goals, typical_behaviors,
            key_attitudes, percentage, users or [])

    def render_segments(self) -> str:
        self.segment_analyzer.build()
        return self.segment_analyzer.render_markdown()

    # ── 模块E: 角色创建 ──
    def add_persona(self, name: str, short_desc: str, priority: str,
                    quote: str, goals: List[str], behaviors: List[str],
                    attitudes: List[str], bio: str,
                    demographics: Dict = None, tech_usage: Dict = None,
                    business_goals: List[str] = None) -> PersonaProfile:
        return self.persona_builder.add_persona(
            name, short_desc, priority, quote, goals, behaviors,
            attitudes, bio, demographics or {}, tech_usage or {},
            business_goals or [])

    def add_scenario(self, persona_name: str, title: str, trigger: str,
                     steps: List[str], result: str):
        for p in self.persona_builder.get_personas():
            if p.name == persona_name:
                self.persona_builder.add_scenario(p, title, trigger, steps, result)
                return
        raise ValueError(f"未找到角色: {persona_name}")

    def render_all_personas(self) -> str:
        return self.persona_builder.render_all_markdown()

    def render_persona_comparison(self) -> str:
        return self.persona_builder.render_comparison()

    def review_personas(self) -> str:
        review = self.persona_builder.review_quality()
        return self.persona_builder.render_review_markdown(review)

    # ── 模块G: 商业策略 ──
    def add_persona_value(self, persona_name: str, market_size: str,
                          spending: str, acquisition_cost: str,
                          lifetime_value: str, score: int):
        return self.strategy_analyzer.add_persona_value(
            persona_name, market_size, spending, acquisition_cost,
            lifetime_value, score)

    def render_strategy(self) -> str:
        return self.strategy_analyzer.render_strategy_markdown()

    # ── 模块H: 功能优先级 ──
    def add_feature(self, name: str, persona_needs: Dict[str, str],
                    business_value: str, tech_difficulty: str):
        return self.strategy_analyzer.add_feature(
            name, persona_needs, business_value, tech_difficulty)

    def render_feature_matrix(self) -> str:
        return self.strategy_analyzer.render_feature_matrix_markdown()

    def add_competitor(self, name: str, features_coverage: Dict[str, str]):
        return self.strategy_analyzer.add_competitor(name, features_coverage)

    def render_competitor_analysis(self) -> str:
        return self.strategy_analyzer.render_competitor_markdown()

    # ── 模块I: 设计 ──
    def validate_path(self, persona_name: str, task: str,
                      path: List[str]) -> str:
        v = self.design_advisor.validate_path(persona_name, task, path)
        status = "✅ 通过" if v.passes_3step_rule else "⚠️ 超过3步"
        return f"{v.persona_name} - {v.task}: {v.steps}步 {status}"

    def render_ia(self) -> str:
        return self.design_advisor.render_ia_markdown()

    def render_content_strategy(self) -> str:
        return self.design_advisor.render_content_strategy_markdown()

    # ── 模块J: 衡量 ──
    def add_test_script(self, persona_name: str, steps: List[Dict]):
        return self.measure_system.add_test_script(persona_name, steps)

    def add_metric(self, persona_name: str, metric: str, target: str,
                   source: str, method: str):
        return self.measure_system.add_metric(
            persona_name, metric, target, source, method)

    def add_bug(self, description: str, persona: str,
                is_primary: bool, blocks_core: bool) -> str:
        bug = self.measure_system.add_bug(
            description, persona, is_primary, blocks_core)
        return f"{bug.priority}: {bug.description} ({bug.rationale})"

    def render_test_plan(self) -> str:
        return self.measure_system.render_test_plan_markdown()

    def render_measure_system(self) -> str:
        return self.measure_system.render_measure_system_markdown()

    # ── 知识库 ──
    def search_knowledge(self, keyword: str) -> Dict[str, List[str]]:
        return search_knowledge(keyword)


__all__ = [
    "PersonaSkill",
    "AnalysisConfig", "PERSONA_PRIORITIES", "PRIORITY_LABELS", "KNOWLEDGE_FILES",
    "RESEARCH_METHODS", "PERSONA_DIMENSIONS", "INTERVIEW_SECTIONS", "SURVEY_TYPES",
    "load_knowledge", "load_all_knowledge", "search_knowledge",
    "INTERVIEW_QUESTIONS", "PERSONA_DOCUMENT_TEMPLATE", "QUALITY_CHECKLIST",
    "InterviewBuilder", "InterviewGuide",
    "SurveyBuilder", "Survey",
    "SegmentAnalyzer", "Segment", "SegmentationResult",
    "PersonaBuilder", "PersonaProfile", "QualityReview",
    "StrategyAnalyzer", "FeatureItem", "BusinessValue",
    "DesignAdvisor", "ContentItem", "PathValidation",
    "MeasureSystem", "TestScript", "MetricItem", "BugPriority",
]
