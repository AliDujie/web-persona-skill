"""Web Persona Skill 测试套件

覆盖全部核心模块的 8 个测试用例。
运行方式: cd web-persona-skill && python -m pytest persona/tests/test_all.py -v
"""

import sys
from pathlib import Path

# 确保项目根目录在 sys.path 中
ROOT = Path(__file__).resolve().parent.parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


# ── 测试1: 知识库加载与搜索 ──────────────────────────────────

def test_knowledge_loading():
    """验证知识库文件能正常加载和搜索。"""
    from persona.utils import load_knowledge, search_knowledge

    # 加载指定主题
    content = load_knowledge("persona_basics")
    assert len(content) > 100, "persona_basics 内容不应为空"
    assert "人物角色" in content, "persona_basics 应包含'人物角色'关键词"

    content2 = load_knowledge("measuring_results")
    assert len(content2) > 100, "measuring_results 内容不应为空"

    # 搜索关键词
    results = search_knowledge("用户")
    assert len(results) > 0, "搜索'用户'应返回结果"


# ── 测试2: 访谈提纲生成 ──────────────────────────────────────

def test_interview_builder():
    """验证访谈提纲生成器的完整流程。"""
    from persona.interview import InterviewBuilder

    builder = InterviewBuilder("飞猪旅行用户访谈")
    builder.set_context("针对近期注册的新用户")
    builder.set_target_users("过去30天内注册的用户")
    builder.include_sections(["goals", "behaviors", "pain_points"])
    builder.add_custom_question("goals", "你最希望通过飞猪实现什么？", priority=3)
    builder.add_tip("注意观察用户提到价格时的情绪变化")

    guide = builder.build()
    assert len(guide.questions) > 3, "应生成多个问题"
    assert guide.title == "飞猪旅行用户访谈"
    assert guide.context == "针对近期注册的新用户"

    # 验证自定义问题被包含
    custom_qs = [q for q in guide.questions if q.is_custom]
    assert len(custom_qs) == 1, "应包含1个自定义问题"
    assert custom_qs[0].priority == 3

    # 验证 Markdown 输出
    md = InterviewBuilder.render_markdown(guide)
    assert "飞猪旅行用户访谈" in md
    assert len(md) > 200, "Markdown 输出不应过短"

    # 验证 JSON 输出
    data = InterviewBuilder.render_json(guide)
    assert "title" in data
    assert "questions" in data
    assert len(data["questions"]) == len(guide.questions)


# ── 测试3: 问卷设计生成 ──────────────────────────────────────

def test_survey_builder():
    """验证三种类型问卷的生成。"""
    from persona.survey import SurveyBuilder

    # 需求型问卷
    builder = SurveyBuilder("旅行需求调研", "needs")
    builder.set_product("飞猪旅行")
    builder.set_pain_points(["找酒店耗时", "价格不透明", "评价不可信"])
    survey = builder.build()
    assert len(survey.questions) >= 3, "需求型问卷应有多个问题"
    assert survey.survey_type == "needs"

    md = SurveyBuilder.render_markdown(survey)
    assert "旅行需求调研" in md
    assert "飞猪旅行" in md

    # 验证型问卷
    builder2 = SurveyBuilder("细分验证", "validation")
    builder2.set_product("飞猪旅行")
    builder2.set_hypotheses(["用户主要为商旅出行", "用户重视性价比"])
    survey2 = builder2.build()
    assert survey2.survey_type == "validation"
    assert len(survey2.questions) >= 2

    # 满意度问卷
    builder3 = SurveyBuilder("满意度调查", "satisfaction")
    builder3.set_product("飞猪旅行")
    survey3 = builder3.build()
    assert survey3.survey_type == "satisfaction"


# ── 测试4: 用户细分分析 ──────────────────────────────────────

def test_segment_analyzer():
    """验证用户细分的数据管理和评估功能。"""
    from persona.segment import SegmentAnalyzer

    analyzer = SegmentAnalyzer()

    # 添加用户数据
    analyzer.add_user("U01", goals=["快速预订"], behaviors=["每天使用"],
                      attitudes=["追求效率"], quotes=["时间就是金钱"])
    analyzer.add_user("U02", goals=["发现好物"], behaviors=["周末浏览"],
                      attitudes=["享受过程"], quotes=["旅行是一种生活方式"])

    # 添加细分群体
    s1 = analyzer.add_segment("效率型", "追求速度和效率",
                              ["快速完成"], ["高频使用"], ["效率优先"], 60, ["U01"])
    s2 = analyzer.add_segment("探索型", "享受发现的乐趣",
                              ["发现好物"], ["浏览为主"], ["好奇心强"], 40, ["U02"])

    assert len(analyzer._segments) == 2
    assert s1.estimated_percentage == 60

    # 设置维度并构建
    analyzer.set_dimensions("使用目标", "使用频率")
    result = analyzer.build()
    assert result.dimension_primary == "使用目标"
    assert len(result.segments) == 2

    # 验证 Markdown 输出
    md = analyzer.render_markdown()
    assert "效率型" in md
    assert "探索型" in md


# ── 测试5: 人物角色创建与质量评审 ─────────────────────────────

def test_persona_builder():
    """验证角色创建、对比和质量评审的完整流程。"""
    from persona.persona_builder import PersonaBuilder

    builder = PersonaBuilder("飞猪旅行")

    # 创建两个角色
    p1 = builder.add_persona(
        name="小明", short_desc="效率型商旅用户", priority="primary",
        quote="我只想快速搞定住宿，把时间花在工作上",
        goals=["快速预订", "价格合理", "位置方便"],
        behaviors=["每周出差2-3次", "只看前3个结果", "从不写评价"],
        attitudes=["追求效率", "信任品牌", "价格敏感"],
        bio="小明是一位28岁的互联网产品经理，频繁出差是他的工作常态...",
        demographics={"age": "28", "occupation": "产品经理", "income": "25-35万"},
        tech_usage={"device": "手机为主", "frequency": "每天"},
        business_goals=["提升预订转化率", "增加复购频次"]
    )

    p2 = builder.add_persona(
        name="小红", short_desc="探索型休闲用户", priority="secondary",
        quote="旅行不只是目的地，更是发现的过程",
        goals=["发现特色住宿", "获取灵感", "分享体验"],
        behaviors=["提前1个月规划", "仔细阅读评价", "拍照分享"],
        attitudes=["追求品质", "重视体验", "乐于分享"],
        bio="小红是一位24岁的设计师，热爱旅行和摄影...",
        demographics={"age": "24", "occupation": "设计师", "income": "15-20万"},
    )

    assert len(builder.get_personas()) == 2
    assert p1.priority == "primary"
    assert p2.priority == "secondary"

    # 添加场景
    builder.add_scenario(p1, "紧急出差预订",
                         "临时接到明天出差通知",
                         ["打开App", "搜索目的地酒店", "按价格排序", "选择第一个", "完成支付"],
                         "3分钟内完成预订，松了一口气")

    assert len(p1.scenarios) == 1

    # 角色文档输出
    md = builder.render_persona_markdown(p1)
    assert "小明" in md
    assert "效率型商旅用户" in md
    assert "primary" in md.lower() or "首要" in md

    # 角色对比表
    comparison = builder.render_comparison()
    assert "小明" in comparison
    assert "小红" in comparison

    # 质量评审
    review = builder.review_quality()
    assert review.total_score > 0
    assert review.max_score == 12
    assert review.grade in ("A", "B", "C", "D", "F")

    review_md = builder.render_review_markdown(review)
    assert "质量" in review_md or "评审" in review_md or "检查" in review_md


# ── 测试6: 商业策略与功能优先级 ──────────────────────────────

def test_strategy_analyzer():
    """验证商业策略、功能矩阵和竞品分析。"""
    from persona.strategy import StrategyAnalyzer

    analyzer = StrategyAnalyzer("飞猪旅行")

    # 角色商业价值评估
    analyzer.add_persona_value("小明", "大型市场", "高", "中", "高", 8)
    analyzer.add_persona_value("小红", "中型市场", "中", "低", "中", 6)

    # 功能优先级
    f1 = analyzer.add_feature("快速预订", {"小明": "高", "小红": "低"}, "高", "低")
    f2 = analyzer.add_feature("旅行灵感", {"小明": "低", "小红": "高"}, "中", "中")

    assert f1.priority in ("P0", "P1", "P2", "P3")

    # 竞品分析
    analyzer.add_competitor("携程", {"快速预订": "●", "旅行灵感": "○"})
    analyzer.add_competitor("Airbnb", {"快速预订": "○", "旅行灵感": "●"})

    # 验证输出
    strategy_md = analyzer.render_strategy_markdown()
    assert "小明" in strategy_md

    feature_md = analyzer.render_feature_matrix_markdown()
    assert "快速预订" in feature_md

    competitor_md = analyzer.render_competitor_markdown()
    assert "携程" in competitor_md


# ── 测试7: 设计指导与路径验证 ────────────────────────────────

def test_design_advisor():
    """验证信息架构、内容策略和路径验证。"""
    from persona.design import DesignAdvisor

    advisor = DesignAdvisor("飞猪旅行")

    # 导航结构
    advisor.add_nav_item("首页", ["小明", "小红"])
    advisor.add_nav_item("酒店", ["小明"])
    advisor.add_nav_item("灵感", ["小红"])

    # 内容规划
    advisor.add_content("酒店推荐", "小明", "列表", "简洁", "专业", "每日", "P0")
    advisor.add_content("旅行攻略", "小红", "图文", "详细", "亲切", "每周", "P1")

    # 路径验证（3步规则）
    v1 = advisor.validate_path("小明", "预订酒店", ["首页", "酒店列表", "预订"])
    assert v1.steps == 3
    assert v1.passes_3step_rule is True

    v2 = advisor.validate_path("小红", "浏览攻略", ["首页", "灵感", "攻略列表", "文章详情", "收藏"])
    assert v2.steps == 5
    assert v2.passes_3step_rule is False

    # 验证输出
    ia_md = advisor.render_ia_markdown()
    assert "首页" in ia_md

    content_md = advisor.render_content_strategy_markdown()
    assert "酒店推荐" in content_md


# ── 测试8: 测试计划与衡量体系 ────────────────────────────────

def test_measure_system():
    """验证测试脚本、指标体系和Bug优先级自动计算。"""
    from persona.measure import MeasureSystem

    system = MeasureSystem("飞猪旅行")

    # 测试脚本
    system.add_test_script("小明", [
        {"action": "打开App", "expected": "显示首页推荐"},
        {"action": "搜索'杭州酒店'", "expected": "显示搜索结果列表"},
        {"action": "点击第一个结果", "expected": "显示酒店详情页"},
        {"action": "点击'立即预订'", "expected": "进入支付页面"},
    ])

    # 衡量指标
    system.add_metric("小明", "预订转化率", "≥15%", "日志分析", "漏斗分析")
    system.add_metric("小明", "预订完成时间", "≤3分钟", "日志分析", "时间统计")

    # Bug优先级自动计算
    bug1 = system.add_bug("支付按钮无响应", "小明", is_primary_persona=True, blocks_core_task=True)
    assert bug1.priority == "P0", "首要角色核心任务阻塞应为P0"

    bug2 = system.add_bug("图片加载慢", "小明", is_primary_persona=True, blocks_core_task=False)
    assert bug2.priority == "P1", "首要角色非核心阻塞应为P1"

    bug3 = system.add_bug("攻略排版问题", "小红", is_primary_persona=False, blocks_core_task=False)
    assert bug3.priority == "P2", "次要角色非核心问题应为P2"

    # 验证输出
    test_md = system.render_test_plan_markdown()
    assert "小明" in test_md
    assert "打开App" in test_md

    measure_md = system.render_measure_system_markdown()
    assert "预订转化率" in measure_md


# ── 入口 ─────────────────────────────────────────────────────

if __name__ == "__main__":
    tests = [
        ("测试1: 知识库加载与搜索", test_knowledge_loading),
        ("测试2: 访谈提纲生成", test_interview_builder),
        ("测试3: 问卷设计生成", test_survey_builder),
        ("测试4: 用户细分分析", test_segment_analyzer),
        ("测试5: 人物角色创建与质量评审", test_persona_builder),
        ("测试6: 商业策略与功能优先级", test_strategy_analyzer),
        ("测试7: 设计指导与路径验证", test_design_advisor),
        ("测试8: 测试计划与衡量体系", test_measure_system),
    ]
    passed = 0
    failed = 0
    for name, fn in tests:
        try:
            fn()
            print(f"  ✅ {name}")
            passed += 1
        except Exception as e:
            print(f"  ❌ {name}: {e}")
            failed += 1
    print(f"\n结果: {passed} 通过, {failed} 失败, 共 {len(tests)} 个测试")
