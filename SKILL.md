---
name: web-persona-skill
version: "3.0.0"
description: "从0到1创建 Persona 的实操工具集。8篇核心操作手册（立项→定性/定量/混合→分析→塑造→验证→应用）+ 39篇进阶参考 + 4个Python工具模块（clustering / llm_prompts / okr_bridge / measurement_toolkit）。融合 Cooper / Mulder / NNGroup / Portigal / Kahneman 等 30+ 经典方法论，按实操阶段组织而非按书籍罗列。"
author: "渡劫"
---

# Web Persona Skill — 从 0 到 1 创建人物角色

## 该不该建 Persona？

| 信号 | 该建 | 不该建 |
|------|------|--------|
| 用户差异 | 行为/目标差异大 | 用户高度同质 |
| 团队争论 | 频繁争论"用户要什么" | 已有清晰共识 |
| 项目阶段 | 新产品/新市场/重大改版 | 短期活动/纯技术重构 |

两个以上信号指向"该建"→ 开始。

## 选方法

```
├── 团队小 / 预算有限 / 时间 <4周
│   └─► 定性路径 → core/02
│
├── 大组织 / 需说服高管 / 需量化市场份额
│   └─► 定量路径 → core/03
│
├── 资源充足 + 决策权重高
│   └─► 混合路径 → core/04
│
└── 完全没有用户认知
    └─► 先做 Proto-Persona 工作坊（2h）→ core/01 §2.3
```

## 8 步执行

| 步骤 | 做什么 | 操作手册 |
|------|--------|---------|
| 1 | 立项规划：确认目标、选方法、组团队 | `references/core/01-project-setup.md` |
| 2 | 定性采集：深度访谈 + 现场观察 | `references/core/02-qualitative-research.md` |
| 3 | 定量采集：问卷设计 + 大样本采集 | `references/core/03-quantitative-research.md` |
| 4 | 混合衔接：定性→定量→定性深化 | `references/core/04-mixed-method.md` |
| 5 | 分析聚类：行为变量 + 亲和图/统计聚类 | `references/core/05-analysis-clustering.md` |
| 6 | 角色塑造：命名 + 叙事 + 优先级 | `references/core/06-persona-creation.md` |
| 7 | 验证精化：内部审视 + 外部验证 + 持续追踪 | `references/core/07-validation.md` |
| 8 | 应用推广：嵌入流程 + 度量效果 + 保鲜 | `references/core/08-application.md` |

## Python 工具速查

```python
# 统计聚类
from persona.clustering import PersonaClusterer
result = PersonaClusterer(method="auto").fit(df, n_clusters_range=(3, 7))

# LLM 辅助（模拟访谈/文案评估/魔鬼代言人/多角色锦标赛）
from persona.llm_prompts import PersonaPromptLibrary
prompt = PersonaPromptLibrary.simulated_interview(profile, task="...", questions=[...])

# Persona → OKR → 路线图
from persona.okr_bridge import OKRBridge
plan = OKRBridge().derive_okrs(persona_profiles)

# 效果度量（NPS/CES/CSAT/漏斗/激活/留存）
from persona.measurement_toolkit import MeasurementToolkit
toolkit = MeasurementToolkit()
toolkit.ingest_nps(persona="...", score=42, n=150)
```

## 核心原则

1. **全员参与** — 不是研究员的独角戏，核心成员必须在关键节点参与
2. **行为分群 > 人口统计** — 用"做什么"而非"是谁"定义 Persona
3. **3-5 个就够** — 宁少不多，深度 > 数量
4. **叙事让 Persona 活** — 一个具体场景 > 一页性格描述
5. **做完才是开始** — 嵌入决策流程才有价值，否则束之高阁

## 目录结构

```
web-persona-skill/
├── SKILL.md              ← 你在这里
├── references/
│   ├── core/             ← 8篇核心操作手册（从0到1的完整指南）
│   │   ├── 01-project-setup.md
│   │   ├── 02-qualitative-research.md
│   │   ├── 03-quantitative-research.md
│   │   ├── 04-mixed-method.md
│   │   ├── 05-analysis-clustering.md
│   │   ├── 06-persona-creation.md
│   │   ├── 07-validation.md
│   │   └── 08-application.md
│   ├── advanced/         ← 39篇进阶参考（按需查阅的方法论字典）
│   │   ├── 01-05: Mulder《赢在用户》系列
│   │   ├── 06-15: 经典书系（Cooper/Lifecycle/Goodwin/Young/Nielsen/LeanUX/...）
│   │   ├── 16-27: ABCD深化（量化/心理学/伦理）
│   │   ├── 28-31: 工程化配套文档
│   │   └── 32-39: 上游研究手艺+体验地图+叙事+JTBD
│   └── README.md
├── persona/              ← Python工具包
│   ├── __init__.py       ← PersonaSkill 主类
│   ├── clustering.py     ← 统计聚类（KMeans/LCA/Factor）
│   ├── llm_prompts.py   ← LLM Prompt 模板库
│   ├── okr_bridge.py    ← Persona→OKR→Roadmap
│   ├── measurement_toolkit.py ← 效果度量
│   └── ...（其他辅助模块）
├── README.md
├── CHANGELOG.md
└── pyproject.toml
```

## 触发条件

| 用户说 | 使用 |
|--------|------|
| "帮我做/创建 Persona" | 按 8 步执行 |
| "用户是谁？用户有哪几类？" | 从 core/01 开始引导 |
| "怎么做用户访谈" | core/02 + advanced/32 |
| "怎么做用户分群/聚类" | core/05 + persona/clustering.py |
| "Persona 做完怎么用" | core/08 |
| "验证 Persona 是否准确" | core/07 |
| "生成 Persona 的 Prompt" | persona/llm_prompts.py |
| "Persona 对应什么 OKR" | persona/okr_bridge.py |
| 需要 NPS/留存等度量 | persona/measurement_toolkit.py |

## 与其他 Skill 协作

| 协作 Skill | 协作方式 |
|-----------|---------|
| JTBD Knowledge | Persona 明确"为谁"，JTBD 明确"要完成什么任务" |
| Universal Design Methods | UDM 提供 100 种研究方法，Persona 是其中的产出物之一 |
| Value Proposition Design | Persona 作为 VPD 画布的"客户画像"输入 |
| Storytelling with Data | 将 Persona 洞察转化为数据可视化汇报 |

## 何时不使用本 Skill

- 只需要市场细分数据（无需完整 Persona）→ 用 analytics
- 只需要一次性的用户画像描述 → 直接写，不需要 skill
- 需要实时 A/B 测试设计 → Quantitative UX Research
- 需要竞品分析框架 → Competitive Analysis
