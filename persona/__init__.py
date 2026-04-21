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

    # ── CEO 视角扩展分析 ──
    def generate_persona_economics(self, total_users: int = 100000) -> str:
        """
        生成用户经济模型（CEO 视角）

        基于用户画像，估算各 Persona 的规模、获客成本、生命周期价值。

        Args:
            total_users: 总用户数基准（默认 10 万）
        """
        personas = self.persona_builder.get_personas()
        if not personas:
            return "## 用户经济模型\n\n⚠️ 请先创建人物角色（使用 add_persona 方法）"

        # 基于已创建的 persona 生成经济模型
        persona_count = len(personas)
        base_percentage = 100 // persona_count

        result = f"""## 用户经济模型

**总用户基准**: {total_users:,} 人

---

### 各 Persona 规模估算

| Persona | 占比 | 用户数 | 优先级 | 特征描述 |
|---------|------|--------|--------|---------|
"""
        for i, p in enumerate(personas):
            percentage = base_percentage if i < persona_count - 1 else 100 - (base_percentage * (persona_count - 1))
            user_count = int(total_users * percentage / 100)
            priority_label = PRIORITY_LABELS.get(p.priority, p.priority)
            result += f"| {p.name} | {percentage}% | {user_count:,} | {priority_label} | {p.short_desc} |\n"

        result += f"""
---

### 获客成本估算 (CAC)

| Persona | 主要渠道 | 渠道成本 | 转化率 | 预计 CAC |
|---------|---------|---------|--------|---------|
"""
        for p in personas:
            # 根据优先级估算 CAC
            if p.priority == "primary":
                cac = "150 元"
                channel = "内容营销"
                conversion = "3.5%"
            elif p.priority == "secondary":
                cac = "100 元"
                channel = "社交媒体"
                conversion = "2.8%"
            else:
                cac = "50 元"
                channel = "自然流量"
                conversion = "1.5%"
            result += f"| {p.name} | {channel} | 5 元/点击 | {conversion} | {cac} |\n"

        result += f"""
---

### 生命周期价值 (LTV)

| Persona | 平均客单价 | 年消费频次 | 平均留存 | LTV |
|---------|-----------|-----------|---------|-----|
"""
        for p in personas:
            # 根据优先级估算 LTV
            if p.priority == "primary":
                ltv = "1,200 元"
                avg_order = "200 元"
                frequency = "6 次"
                retention = "18 个月"
            elif p.priority == "secondary":
                ltv = "600 元"
                avg_order = "150 元"
                frequency = "4 次"
                retention = "12 个月"
            else:
                ltv = "200 元"
                avg_order = "100 元"
                frequency = "2 次"
                retention = "6 个月"
            result += f"| {p.name} | {avg_order} | {frequency} | {retention} | {ltv} |\n"

        result += f"""
---

### LTV/CAC 健康度分析

| Persona | LTV | CAC | LTV/CAC | 健康标准 | 评估 |
|---------|-----|-----|---------|---------|------|
"""
        for p in personas:
            if p.priority == "primary":
                ltv_num = 1200
                cac_num = 150
            elif p.priority == "secondary":
                ltv_num = 600
                cac_num = 100
            else:
                ltv_num = 200
                cac_num = 50
            ratio = ltv_num / cac_num
            status = "🟢" if ratio > 3 else "🟡" if ratio > 2 else "🔴"
            result += f"| {p.name} | {ltv_num} 元 | {cac_num} 元 | {ratio:.1f} | > 3 | {status} |\n"

        result += """
---

### 战略建议

#### 重点投入 Persona
"""
        primary_personas = [p for p in personas if p.priority == "primary"]
        if primary_personas:
            result += f"**推荐**: {', '.join([p.name for p in primary_personas])}\n\n"
            result += "**理由**:\n"
            result += "1. LTV/CAC > 3（健康）\n"
            result += "2. 留存率高\n"
            result += "3. 增长潜力大\n\n"

        result += """#### 谨慎投入 Persona
"""
        low_priority = [p for p in personas if p.priority in ("unimportant", "negative")]
        if low_priority:
            result += f"**推荐**: {', '.join([p.name for p in low_priority])}\n\n"
            result += "**理由**:\n"
            result += "1. LTV/CAC < 3（需优化）\n"
            result += "2. 价格敏感，忠诚度低\n"
            result += "3. 建议优化定价策略\n"

        return result

    def generate_acquisition_strategy(self) -> str:
        """
        生成用户获取策略（基于 Persona 经济模型）

        为各 Persona 设计针对性的获客策略和预算分配。
        """
        personas = self.persona_builder.get_personas()
        if not personas:
            return "## 用户获取策略\n\n⚠️ 请先创建人物角色（使用 add_persona 方法）"

        result = """## 用户获取策略

---

### 各 Persona 获客策略

"""
        for p in personas:
            if p.priority == "primary":
                target_users = "35%"
                channels = [
                    {"name": "内容营销", "budget": "50 万", "users": "3,333 人", "cac": "150 元", "roi": "200%"},
                    {"name": "KOL 合作", "budget": "30 万", "users": "2,000 人", "cac": "150 元", "roi": "180%"},
                ]
                key_message = "强调品质、体验、口碑"
            elif p.priority == "secondary":
                target_users = "40%"
                channels = [
                    {"name": "社交媒体广告", "budget": "40 万", "users": "4,000 人", "cac": "100 元", "roi": "150%"},
                    {"name": "促销活动", "budget": "20 万", "users": "2,000 人", "cac": "100 元", "roi": "120%"},
                ]
                key_message = "强调优惠、折扣、性价比"
            else:
                target_users = "25%"
                channels = [
                    {"name": "搜索广告", "budget": "15 万", "users": "3,000 人", "cac": "50 元", "roi": "100%"},
                    {"name": "应用商店", "budget": "5 万", "users": "1,000 人", "cac": "50 元", "roi": "80%"},
                ]
                key_message = "强调快速、简单、省时"

            result += f"""#### {p.name}
**目标**: 获取 {target_users} 用户

**核心渠道**:
| 渠道 | 预算 (万) | 预计获客 | CAC | ROI |
|------|----------|---------|-----|-----|
"""
            for ch in channels:
                result += f"| {ch['name']} | {ch['budget']} | {ch['users']} | {ch['cac']} | {ch['roi']} |\n"

            result += f"""
**关键信息**: {key_message}

---

"""

        result += """### 总预算分配

| Persona | 预算 (万) | 占比 | 预计获客 | 加权 CAC |
|---------|----------|------|---------|---------|
"""
        total_budget = 0
        total_users = 0
        for p in personas:
            if p.priority == "primary":
                budget = 80
                users = 5333
                cac = 150
            elif p.priority == "secondary":
                budget = 60
                users = 6000
                cac = 100
            else:
                budget = 20
                users = 4000
                cac = 50
            total_budget += budget
            total_users += users
            result += f"| {p.name} | {budget} | {int(budget/total_budget*100)}% | {users:,} 人 | {cac} 元 |\n"

        result += f"""| **总计** | **{total_budget}** | **100%** | **{total_users:,} 人** | **{int(total_budget/total_users*10000)} 元** |

---

### 获客时间线

| 阶段 | 时间 | 目标 | 预算 | 关键指标 |
|------|------|------|------|---------|
| Phase 1 | 0-4 周 | 验证渠道 | {int(total_budget*0.2)} 万 | CAC < 150 元 |
| Phase 2 | 4-12 周 | 规模化 | {int(total_budget*0.5)} 万 | 获客 {int(total_users*0.6):,} 人 |
| Phase 3 | 12-24 周 | 优化 ROI | {int(total_budget*0.3)} 万 | LTV/CAC > 3 |
"""

        return result

    def generate_retention_strategy(self) -> str:
        """
        生成用户留存策略（基于 Persona 特征）

        为各 Persona 设计针对性的留存策略和生命周期管理。
        """
        personas = self.persona_builder.get_personas()
        if not personas:
            return "## 用户留存策略\n\n⚠️ 请先创建人物角色（使用 add_persona 方法）"

        result = """## 用户留存策略

---

### 各 Persona 留存分析

| Persona | 次日留存 | 7 日留存 | 30 日留存 | 90 日留存 | 行业基准 |
|---------|---------|---------|---------|---------|---------|
"""
        for p in personas:
            if p.priority == "primary":
                retention = {"次日": "45%", "7日": "35%", "30日": "25%", "90日": "18%", "基准": "15%"}
                status = "🟢"
            elif p.priority == "secondary":
                retention = {"次日": "40%", "7日": "28%", "30日": "18%", "90日": "12%", "基准": "12%"}
                status = "🟡"
            else:
                retention = {"次日": "35%", "7日": "22%", "30日": "12%", "90日": "8%", "基准": "10%"}
                status = "🟡"
            result += f"| {p.name} | {retention['次日']} | {retention['7日']} | {retention['30日']} | {retention['90日']} | {retention['基准']} {status} |\n"

        result += """
---

### 留存驱动因素

"""
        for p in personas:
            if p.priority == "primary":
                drivers = ["服务质量（影响权重 40%）", "个性化体验（影响权重 35%）", "会员权益（影响权重 25%）"]
                signals = ["满意度评分下降", "投诉次数增加", "会员续费率下降"]
                intervention = "客服主动关怀"
            elif p.priority == "secondary":
                drivers = ["优惠活动频率（影响权重 50%）", "价格竞争力（影响权重 30%）", "积分奖励（影响权重 20%）"]
                signals = ["连续 7 天未访问", "优惠券未使用", "比价行为增加"]
                intervention = "发送专属优惠"
            else:
                drivers = ["操作便捷性（影响权重 60%）", "加载速度（影响权重 40%）"]
                signals = ["连续 14 天未访问", "跳出率增加", "停留时间缩短"]
                intervention = "简化流程引导"

            result += f"""#### {p.name}
**关键驱动因素**:
"""
            for i, driver in enumerate(drivers, 1):
                result += f"{i}. {driver}\n"

            result += """
**流失预警信号**:
"""
            for i, signal in enumerate(signals, 1):
                result += f"- 信号 {i}: {signal}\n"

            result += f"""
**干预策略**: {intervention}

---

"""

        result += """### 生命周期管理

| 阶段 | """
        result += " | ".join([p.name for p in personas])
        result += " |\n|------|" + "|".join(["--------" for _ in personas]) + "|\n"

        stages = [
            ("新用户 (0-7 天)", ["首单优惠", "品质展示", "快速引导"]),
            ("活跃用户 (7-30 天)", ["复购优惠", "会员权益", "快捷功能"]),
            ("成熟用户 (30-90 天)", ["积分奖励", "专属服务", "自动化"]),
            ("衰退用户 (90 天+)", ["召回优惠", "关怀回访", "简化流程"]),
        ]

        for stage_name, strategies in stages:
            result += f"| {stage_name} | " + " | ".join(strategies) + " |\n"

        result += """
---

### 留存提升计划

| 举措 | 投入 | 预期效果 | 时间周期 | 优先级 |
|------|------|---------|---------|--------|
| 会员体系 | 50 万 | 留存提升 15% | 8 周 | P0 |
| 个性化推荐 | 30 万 | 留存提升 10% | 6 周 | P1 |
| 客服优化 | 20 万 | 留存提升 8% | 4 周 | P1 |

**总投入**: 100 万
**预期 ROI**: 250%
"""

        return result

    def generate_persona(self, include_ceo_analysis: bool = True, total_users: int = 100000) -> str:
        """
        生成用户画像报告（含 CEO 决策模块）

        Args:
            include_ceo_analysis: 是否包含 CEO 视角扩展分析（默认 True）
            total_users: 总用户数基准（默认 10 万）
        """
        # 生成基础用户画像
        personas = self.persona_builder.get_personas()
        if not personas:
            return "⚠️ 请先创建人物角色（使用 add_persona 方法）"

        base_report = self.render_all_personas()

        if include_ceo_analysis:
            economics = self.generate_persona_economics(total_users)
            acquisition = self.generate_acquisition_strategy()
            retention = self.generate_retention_strategy()
            return f"""{base_report}

---

## CEO 视角扩展分析

{economics}

---

{acquisition}

---

{retention}
"""
        else:
            return base_report


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
