---
name: web-persona-skill
version: "2.4.25"
description: Web人物角色(Personas)创建与应用专家技能。基于《赢在用户》全书知识体系，具备完整执行能力：方法选择决策、访谈提纲生成、问卷设计、用户细分、角色文档创建、质量评审、商业策略分析、功能优先级排序、设计指导、测试计划与衡量体系，以及CEO视角经济模型与增长策略。
---

# Web Persona 人物角色创建与应用专家 Skill

基于《赢在用户：Web人物角色创建和应用实践指南》(The User Is Always Right) 全书知识体系构建。

## 一、核心方法论

| 模块 | 核心问题 | 关键行动 |
|------|---------|---------|
| A. 方法选择 | 该用定性/定量/混合路径？ | 评估预算/时间/团队 -> 推荐路径 + 执行计划 |
| B. 定性研究 | 用户真实目标和行为是什么？ | 生成访谈提纲 -> 招募方案 -> 数据分析 |
| C. 定量研究 | 如何用数据验证发现？ | 设计问卷 -> 分析方案 -> 数据洞察 |
| D. 用户细分 | 用户群体如何划分？ | 目标/行为/观点三维 -> 细分矩阵 -> 验证 |
| E. 角色创建 | 如何让角色真实可信？ | 文档生成 -> 对比表 -> 场景 -> 质量评审 |
| F. 活力维护 | 如何让角色持续被使用？ | 推广计划 -> 海报/卡片 -> 工作坊 |
| G. 商业策略 | 角色如何驱动商业决策？ | 价值评估 -> 差异化策略 -> 资源分配 |
| H. 功能优先级 | 先做什么功能？ | 需求x角色矩阵 -> P0-P3排序 -> 竞品分析 |
| I. 设计指导 | 如何用角色指导设计？ | 信息架构 -> 内容策略 -> 路径验证(3步规则) |
| J. 衡量成果 | 如何验证角色的价值？ | 测试脚本 -> 指标体系 -> Bug优先级 |

**黄金法则**：不从人口统计入手；聚焦目标/行为/观点三维度；用户"做了什么"比"说了什么"重要；首要角色最多2个；角色基于研究数据而非假设。

## 二、执行能力

1. **方法选择决策** -- 根据预算/时间/团队推荐定性/定量/混合路径，输出执行计划
2. **访谈提纲生成** -- 按目标/行为/痛点/期望等段落，生成定制化访谈问题
3. **问卷设计** -- 支持需求型/验证型/满意度型三类问卷，含筛选/量表/开放题
4. **用户细分** -- 数据管理、2x2矩阵、细分评估、Markdown输出
5. **角色文档创建** -- 完整角色卡(名称/简介/目标/行为/场景)、对比表、质量评审
6. **角色推广** -- 推广计划、海报/卡片文案、工作坊方案
7. **商业策略分析** -- 角色商业价值评估、差异化策略、资源分配建议
8. **功能优先级排序** -- 功能x角色需求矩阵、P0-P3优先级、竞品功能对比
9. **设计指导** -- 信息架构方案、内容策略、路径验证(3步规则)
10. **衡量成果** -- QA测试脚本、衡量指标体系、Bug优先级自动计算
11. **CEO视角分析** -- 用户经济模型(LTV/CAC)、获客策略、留存策略

## 三、触发条件总表

| 触发词 / 场景 | 执行能力 | 输出物 |
|---|---|---|
| 创建/生成人物角色、用户画像、persona | 全流程(A->D->E->F) | 完整角色文档集 |
| 选方法、怎么做、从哪开始 | 方法选择 | 方法选择建议书 |
| 访谈、用户研究、定性、访谈提纲 | 定性研究 | 访谈提纲、招募方案 |
| 问卷、调查、定量、问卷设计 | 问卷设计 | 完整问卷 |
| 细分、分群、聚类 | 用户细分 | 细分方案 + 矩阵 |
| 角色文档、角色卡片 | 角色创建 | 角色文档 + 对比表 |
| 推广、展示、维护 | 活力维护 | 推广计划、海报/卡片 |
| 商业策略、竞争、差异化 | 商业策略 | 策略报告 |
| 功能、优先级、排序、需求 | 功能优先级 | 功能矩阵 + 版本规划 |
| 信息架构、导航、内容、设计 | 设计指导 | IA方案 + 内容策略 |
| 测试、衡量、指标、效果 | 衡量成果 | 测试计划 + 指标体系 |
| 评审、检查、诊断现有角色 | 质量评审 | 12项评审报告 |
| 用户经济模型、LTV/CAC、增长策略 | CEO视角分析 | 经济模型 + 获客/留存策略 |

## 四、目录结构

```
web-persona-skill/
├── SKILL.md                     # 本文件
├── references/                  # 知识库文档
│   ├── 01-persona-basics.md     # 人物角色基础概念与价值
│   └── 02-measuring-results.md  # 成果衡量方法论
├── persona/                     # Python 工具包
│   ├── __init__.py              # PersonaSkill 统一入口类
│   ├── config.py                # 全局配置
│   ├── utils.py                 # 知识库加载与搜索
│   ├── templates.py             # 模板常量
│   ├── interview.py             # InterviewBuilder: 访谈提纲生成器
│   ├── survey.py                # SurveyBuilder: 问卷设计器
│   ├── segment.py               # SegmentAnalyzer: 用户细分
│   ├── persona_builder.py       # PersonaBuilder: 角色创建 + 评审
│   ├── strategy.py              # StrategyAnalyzer: 策略 + 功能 + 竞品
│   ├── design.py                # DesignAdvisor: IA + 内容 + 路径
│   ├── measure.py               # MeasureSystem: 测试 + 指标 + Bug
│   └── tests/test_all.py        # 8 个测试用例
├── pyproject.toml
└── .gitignore
```

## 五、知识库

| 文件 | 核心内容 |
|------|---------|
| `references/01-persona-basics.md` | 人物角色基础概念、三种创建路径、细分原则、角色构成要素、优先级体系 |
| `references/02-measuring-results.md` | 发布前测试、发布后衡量、按角色分析指标、定量衡量体系 |

---

## 六、Python 工具包

### 6.1 安装与依赖

纯 Python 3.8+ 实现，无外部依赖。

```python
import sys; sys.path.insert(0, "/path/to/web-persona-skill")
from persona import PersonaSkill
```

### 6.2 PersonaSkill 方法一览

`PersonaSkill` 封装全部模块，每个方法返回 Markdown 字符串。初始化: `skill = PersonaSkill("产品名")`

| 方法 | 能力 | 必填参数 | 返回 |
|------|------|---------|------|
| `generate_interview()` | 访谈提纲 | title, sections | Markdown |
| `generate_survey()` | 问卷设计 | title, survey_type | Markdown |
| `add_user()` | 添加用户数据 | user_id | -- |
| `add_segment()` | 添加细分群体 | name, description, core_goals, typical_behaviors, key_attitudes | Segment |
| `render_segments()` | 输出细分结果 | -- | Markdown |
| `add_persona()` | 创建角色 | name, short_desc, priority, quote, goals, behaviors, attitudes, bio | PersonaProfile |
| `add_scenario()` | 添加使用场景 | persona_name, title, trigger, steps, result | -- |
| `render_all_personas()` | 输出角色文档 | -- | Markdown |
| `render_persona_comparison()` | 角色对比表 | -- | Markdown |
| `review_personas()` | 质量评审(12项) | -- | Markdown |
| `add_persona_value()` | 角色商业价值 | persona_name, market_size, spending, acquisition_cost, lifetime_value, score | BusinessValue |
| `render_strategy()` | 商业策略报告 | -- | Markdown |
| `add_feature()` | 添加功能 | name, persona_needs, business_value, tech_difficulty | FeatureItem |
| `render_feature_matrix()` | 功能矩阵(P0-P3) | -- | Markdown |
| `add_competitor()` | 添加竞品 | name, features_coverage | -- |
| `render_competitor_analysis()` | 竞品分析 | -- | Markdown |
| `validate_path()` | 路径验证(3步) | persona_name, task, path | str |
| `render_ia()` | 信息架构 | -- | Markdown |
| `render_content_strategy()` | 内容策略 | -- | Markdown |
| `add_test_script()` | 测试脚本 | persona_name, steps | TestScript |
| `add_metric()` | 衡量指标 | persona_name, metric, target, source, method | MetricItem |
| `add_bug()` | Bug优先级 | description, persona, is_primary, blocks_core | str |
| `render_test_plan()` | 测试计划 | -- | Markdown |
| `render_measure_system()` | 衡量体系 | -- | Markdown |
| `search_knowledge()` | 知识库检索 | keyword | Dict |
| `generate_persona_economics()` | CEO: 经济模型 | total_users(默认100000) | Markdown |
| `generate_acquisition_strategy()` | CEO: 获客策略 | -- | Markdown |
| `generate_retention_strategy()` | CEO: 留存策略 | -- | Markdown |
| `generate_persona()` | CEO: 完整报告 | include_ceo_analysis, total_users | Markdown |

### 6.3 模块速查

| 模块文件 | 主类 | 输出类型 | 说明 |
|---------|------|---------|------|
| `interview.py` | `InterviewBuilder` -> `InterviewGuide` | Markdown / JSON | 8段落(warmup~closing)，自定义问题，研究提示 |
| `survey.py` | `SurveyBuilder` -> `Survey` | Markdown | needs/validation/satisfaction 三类问卷 |
| `segment.py` | `SegmentAnalyzer` -> `SegmentationResult` | Markdown | 用户数据+细分群体+2x2矩阵+评估 |
| `persona_builder.py` | `PersonaBuilder` -> `PersonaProfile` | Markdown | 角色文档+对比表+场景+12项质量评审 |
| `strategy.py` | `StrategyAnalyzer` -> `FeatureItem` | Markdown | 商业价值+功能矩阵(P0-P3)+竞品分析 |
| `design.py` | `DesignAdvisor` -> `PathValidation` | Markdown | 导航+内容策略+路径验证(3步规则) |
| `measure.py` | `MeasureSystem` -> `BugPriority` | Markdown | 测试脚本+指标+Bug(P0=首要角色核心阻塞) |

**角色优先级**: primary(首要) / secondary(次要) / unimportant(不重要) / negative(排斥的)

**Bug优先级**: P0=首要角色核心任务阻塞 | P1=首要角色非核心 | P2=次要角色 | P3=不影响任务

### 6.4 CEO 视角扩展分析

在角色创建完成后，可生成商业决策级分析（须先调用 `add_persona()`）:

| 方法 | 输出内容 |
|------|---------|
| `generate_persona_economics(total_users)` | 各Persona规模、CAC、LTV、LTV/CAC健康度 |
| `generate_acquisition_strategy()` | 获客渠道、预算分配、ROI、时间线 |
| `generate_retention_strategy()` | 留存率、流失预警、生命周期管理 |
| `generate_persona(include_ceo_analysis=True)` | 完整画像 + 上述全部CEO分析（一键生成） |

### 6.5 完整使用示例

```python
from persona import PersonaSkill

skill = PersonaSkill("电商平台")

# 访谈提纲
print(skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"]))

# 问卷设计
print(skill.generate_survey("需求调研", "needs", pain_points=["搜索不精准", "价格不透明"]))

# 创建角色
skill.add_persona("小明", "效率型用户", "primary", "我只想快速完成",
    goals=["快速下单"], behaviors=["频繁使用"],
    attitudes=["追求效率"], bio="小明是一位忙碌的白领...")
skill.add_persona("小红", "探索型用户", "secondary", "发现好物才开心",
    goals=["发现特色商品"], behaviors=["仔细比较"],
    attitudes=["重视体验"], bio="小红是一位年轻设计师...")
print(skill.render_all_personas())
print(skill.review_personas())

# 功能优先级
skill.add_feature("快速下单", {"小明": "高", "小红": "低"}, "高", "低")
print(skill.render_feature_matrix())

# Bug 优先级
print(skill.add_bug("首页加载慢", "小明", is_primary=True, blocks_core=True))
# -> P0: 首页加载慢 (影响首要角色的核心任务，必须立即修复)

# CEO 视角完整报告（角色文档 + 经济模型 + 获客 + 留存）
print(skill.generate_persona(include_ceo_analysis=True, total_users=100000))

# 知识库检索
print(skill.search_knowledge("细分"))
```

### 6.6 AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 始终通过 `PersonaSkill` 类调用，不直接实例化子模块 |
| 2 | **返回值** | 所有方法返回 Markdown 字符串，可直接展示给用户 |
| 3 | **触发映射** | 根据用户意图匹配触发条件总表，选择对应能力 |
| 4 | **顺序执行** | 全流程按 A->D->E->F 顺序，商业分析按 G->H 顺序 |
| 5 | **知识优先** | 方法论问题先调用 `search_knowledge()` 查询知识库 |
| 6 | **先角色后分析** | CEO视角方法须先 `add_persona()` 创建角色后才可使用 |
| 7 | **交互引导** | 执行前先收集必要信息（业务类型、目标用户、预算时间等） |
| 8 | **完整交付** | 每个任务产出完整可用的文档/方案/报告 |

### 6.7 测试说明

```bash
cd web-persona-skill && python persona/tests/test_all.py
# 或: python -m pytest persona/tests/test_all.py -v
```

| 测试用例 | 覆盖模块 | 验证内容 |
|---------|---------|---------|
| `test_knowledge_loading()` | 知识库 | 加载、搜索、关键词匹配 |
| `test_interview_builder()` | 访谈(B) | 段落选择、自定义问题、Markdown/JSON |
| `test_survey_builder()` | 问卷(C) | needs/validation/satisfaction 三类型 |
| `test_segment_analyzer()` | 细分(D) | 数据管理、细分评估、矩阵输出 |
| `test_persona_builder()` | 角色(E) | 创建、场景、对比、12项质量评审 |
| `test_strategy_analyzer()` | 策略(G/H) | 商业价值、功能矩阵、竞品分析 |
| `test_design_advisor()` | 设计(I) | 导航、内容、3步规则路径验证 |
| `test_measure_system()` | 衡量(J) | 测试脚本、指标、Bug P0-P3 |

### 6.8 与其他 Skill 的协作

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 研究结果可视化 | Storytelling with Data | Persona数据 -> SWD选图表 -> SWD构建故事 |
| 价值主张验证 | Value Proposition Design | Persona目标 -> VPD画布 -> Persona验证 |
| JTBD 研究整合 | JTBD Knowledge Skill | JTBD Jobs -> Persona细分映射 -> 角色文档 |
| 定量研究支撑 | Quantitative UX Research | UXR数据 -> Persona定量验证 -> 角色精化 |

---

## 七、最佳实践

| # | 原则 | 说明 |
|---|------|------|
| 1 | 永远基于真实数据 | 不编造角色，必须有研究数据支撑 |
| 2 | 聚焦目标而非人口统计 | 年龄/性别适合营销但不适合设计决策 |
| 3 | 角色数量控制在3-6个 | 太少覆盖不全，太多难以记忆 |
| 4 | 首要角色最多2个 | 保证设计决策有明确优先级 |
| 5 | 简介是叙述型自传 | 不用列表，讲故事才能让人记住 |
| 6 | 一页纸原则 | 角色文档控制在一页内，便于传播 |
| 7 | 持续维护角色活力 | 海报张贴、会议引用、定期数据更新 |
| 8 | 角色驱动全流程 | 从信息架构到视觉设计到测试，全程引用角色 |

## 八、经典案例

| 案例 | 行业 | 核心洞察 |
|------|------|---------|
| VistaPrint | 在线印刷 | 预言模型70%准确度识别高价值用户 |
| BrownCo | 金融经纪 | 通过角色做减法而非追赶巨头 |
| CNN.com | 新闻媒体 | 6个角色推广全公司，高层分发"我们不是目标用户"T恤 |
| Best Buy | 零售 | 角色指导零售店优化，目标客户消费额提升30% |
| Sony Boom Box | 消费电子 | 用户说想要黄色但都拿了黑色，证明言行不一 |

## 九、与其他 Skill 协作

Persona 是 AliDujie UX 研究技能生态系统的用户定义层，为其他技能提供用户视角：

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 角色数据可视化 | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Persona 数据 → SWD 选图表 → SWD 构建故事 |
| 角色到价值主张 | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Persona 目标/痛点 → VPD 画布 → Persona 验证 |
| JTBD 研究整合 | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD Jobs → Persona 细分映射 → Persona 文档 |
| 角色定量验证 | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | UXR 数据 → Persona 定量验证 → Persona 精化 |
| 角色研究方法 | [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | UDM 访谈/观察 → Persona 数据收集 → Persona 创建 |
| 角色战略分析 | [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | STM 竞争分析 → Persona 市场定位 → STM 战略建议 |

**协作示例（UDM → Persona → SWD）**：
```python
# Step 1: UDM 收集用户研究数据
# Step 2: Persona 创建角色文档
from persona import PersonaSkill
skill = PersonaSkill("电商平台")
skill.add_persona("小明", "效率型用户", "primary", goals=["快速下单"])
print(skill.render_all_personas())
# Step 3: SWD 将角色数据可视化
from swd import SWDSkill
swd = SWDSkill("用户画像汇报")
ctx = swd.build_context(audience="产品团队", cta="按首要角色优化设计")
```

## 十、参考资料

| 书名 | 作者 | 说明 |
|------|------|------|
| **赢在用户 (The User Is Always Right)** | Steve Mulder & Ziv Yaar (2006) | 本 Skill 的理论基础 |
| About Face | Alan Cooper (2014) | 目标导向设计方法 |
| The Inmates Are Running the Asylum | Alan Cooper (1999) | Persona 概念的起源 |
| Storytelling with Data | Cole Nussbaumer Knaflic (2015) | 研究结果的数据可视化与叙事 |

## 最佳实践

| # | 原则 | 说明 |
|---|------|------|
| 1 | 永远基于真实数据 | 不编造角色，必须有研究数据支撑 |
| 2 | 聚焦目标而非人口统计 | 年龄/性别适合营销但不适合设计决策 |
| 3 | 角色数量 3-6 个 | 太少覆盖不全，太多难以记忆 |
| 4 | 首要角色最多 2 个 | 保证设计决策有明确优先级 |
| 5 | 简介是叙述型自传 | 不用列表，讲故事才能让人记住 |
| 6 | 一页纸原则 | 角色文档控制在一页内，便于传播 |
| 7 | 持续维护角色活力 | 海报张贴、会议引用、定期数据更新 |

### AliDujie 技能生态

Persona 是 **AliDujie UX 研究技能生态系统** 的用户定义层，为其他技能提供用户视角：

| 技能 | 定位 | 协作模式 |
|------|------|---------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 方法论核心 | UDM 访谈/观察 → Persona 数据收集 → 角色创建 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | JTBD 任务聚类 → Persona 角色定义 |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量研究 | Persona 假设 → QuantUX 行为验证 → 角色迭代 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值验证 | Persona 目标/痛点 → VPD 画布 → Persona 验证 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | Persona 数据 → SWD 可视化汇报 |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略框架 | STM 竞争分析 → Persona 市场定位 |
