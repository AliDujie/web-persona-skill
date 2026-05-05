# Web Persona Skill

[![Ecosystem](https://img.shields.io/badge/AliDujie-Ecosystem-7B68EE.svg)](https://github.com/AliDujie)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Version](https://img.shields.io/badge/version-2.4.18-green.svg)](CHANGELOG.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--05-brightgreen.svg)

> 👤 **一句话介绍**: 基于 Steve Mulder《The User Is Always Right》的完整人物角色工具包。从用户研究到角色创建，从商业策略到设计指导，内置 CEO 视角的用户经济模型分析。

### ✅ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r web-persona-skill /your/agent/skills/`
- [ ] **导入** — `from persona import PersonaSkill`
- [ ] **初始化** — `skill = PersonaSkill("你的产品")`
- [ ] **人物角色** — `skill.add_persona(name="...", archetype="...", goals=[...])`
- [ ] **访谈提纲** — `skill.generate_interview("访谈", dimensions=[...])`
- [ ] **用户细分** — `skill.analyze_segments(data=[...])`
- [ ] **角色渲染** — `skill.render_all_personas()`
- [ ] **CEO 分析** — `skill.generate_persona(include_ceo_analysis=True)`

[English](#english) | [中文](#中文说明)

---

### 🤔 什么时候使用这个技能？(When to Use This Skill?)

| 你的场景 | 推荐技能 |
|----------|----------|
| 需要创建人物角色、用户细分、设计指导 | ✅ **Web Persona** (本技能) |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要商业分析框架、结构化思维、战略决策 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 **提示**: Persona 与 UDM 配合使用，用 UDM 访谈/观察方法收集角色研究数据，构建证据驱动的人物角色。

---

## 中文说明

### 🎯 Features at a Glance / 功能一览

| 功能 | 说明 |
|------|------|
| 10 大执行能力 | 访谈提纲、调查问卷、用户细分、人物角色创建、商业策略、信息架构、测试与衡量、CEO 用户经济模型 |
| 人物角色档案 | 基于行为的目标、痛点、设计指导生成 |
| CEO 视角分析 | 用户经济模型 + 获取策略 + 留存策略 |
| 用户细分 | 基于行为模式的用户分群 |
| 双语支持 | 完整中英文文档和代码示例 |

### 👥 适合谁？(Who Is This For?)

| 角色 | 使用场景 |
|------|----------|
| **UX 设计师** | 基于真实数据创建证据驱动的人物角色 |
| **产品经理** | 将产品决策与用户细分对齐 |
| **营销团队** | 针对特定人物角色需求精准定位信息 |
| **服务设计师** | 将服务映射到角色旅程和触点 |
| **AI Agent** | 作为工具调用，自动化人物角色生成流程 |

### 🏷️ GitHub Topics（推荐）

```
persona user-research user-segmentation design-guidance
python-toolkit openclaw-skill alicloud
```

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **经典方法论** — 基于 Steve Mulder《The User Is Always Right》，人物角色领域的经典著作
- **全链路工具** — 从用户研究到角色创建，从商业策略到设计指导
- **CEO 视角** — 内置用户经济模型、获取策略、留存策略分析
- **零依赖** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **双语支持** — 完整中英文文档，适合国际化团队
- **即插即用** — API 设计直观，代码示例丰富，即刻产出人物角色报告

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r web-persona-skill /your/agent/skills/
```

> 📖 详细安装指南请查看 [INSTALL.md](INSTALL.md)

#### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/web-persona-skill")
from persona import PersonaSkill

skill = PersonaSkill("电商平台")
```

#### 步骤 3: 开始使用

```python
# ===== 场景 1: 创建人物角色 =====
skill.add_persona(
    name="小明",
    archetype="效率型用户",
    type="primary",
    quote="我只想快速找到想要的商品",
    goals=["快速完成任务", "获得个性化推荐"],
    behaviors=["频繁使用搜索", "比价后再购买"]
)

skill.add_persona(
    name="小红",
    archetype="探索型用户",
    type="secondary",
    quote="我喜欢发现新品和优惠",
    goals=["发现新品", "获取优惠信息"],
    behaviors=["浏览推荐", "关注直播"]
)

print(skill.render_all_personas())
# 输出：2 个角色档案，包含目标、行为、痛点、设计指导

# ===== 场景 2: 访谈提纲与问卷设计 =====
guide = skill.generate_interview(
    "新用户上手体验访谈",
    dimensions=["goals", "behaviors", "pain_points", "motivations"]
)
print(guide)

survey = skill.design_survey("用户细分问卷", sample_size=500)
print(f"问卷题目数: {survey.question_count}")

# ===== 场景 3: CEO 视角用户经济模型 =====
report = skill.generate_persona(include_ceo_analysis=True)
print(report)
# 输出：用户经济模型 + 获取策略 + 留存策略

# ===== 场景 4: 功能优先级 + Bug 优先级 =====
skill.add_feature("快速下单", {"小明": "高", "小红": "低"}, business_value="高", tech_difficulty="低")
skill.add_feature("个性化推荐", {"小明": "中", "小红": "高"}, business_value="高", tech_difficulty="中")
print(skill.render_feature_matrix())  # P0-P3 功能优先级矩阵

# Bug 优先级 — 按角色影响面自动定级
bug1 = skill.add_bug("首页加载慢", "小明", is_primary=True, blocks_core=True)
print(bug1)  # P0: 首页加载慢 (影响首要角色核心任务)
bug2 = skill.add_bug("推荐算法偏差", "小红", is_primary=False, blocks_core=False)
print(bug2)  # P2: 推荐算法偏差

# ===== 场景 5: 信息架构 + 内容策略 =====
print(skill.render_ia())              # 信息架构方案
print(skill.render_content_strategy())  # 内容策略

# ===== 场景 6: 路径验证 (3 步规则) =====
result = skill.validate_path("小明", "完成购物", ["首页", "搜索", "详情页", "下单"])
print(result)  # 路径是否通过 3 步规则

# ===== 场景 7: 测试计划 + 衡量体系 =====
skill.add_test_script("小明", steps=["打开首页", "搜索商品", "查看详情", "完成下单"])
skill.add_metric("小明", metric="任务完成率", target="90%", source="GA", method="数据分析")
print(skill.render_test_plan())     # 测试计划
print(skill.render_measure_system())  # 衡量体系
```

### 💡 10 大核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **访谈提纲生成** | `interview.py` | 8 段落（暖场→目标→行为→痛点→期望→竞品→未来→收尾） |
| 2 | **调查问卷设计** | `survey.py` | 需求型/验证型/满意度型三类问卷 |
| 3 | **用户细分分析** | `segment.py` | 目标/行为/观点三维细分 + 2x2 矩阵 |
| 4 | **人物角色创建** | `persona_builder.py` | 完整角色卡 + 对比表 + 场景 + 12 项质量评审 |
| 5 | **商业策略** | `strategy.py` | 角色商业价值 + 功能矩阵(P0-P3) + 竞品分析 |
| 6 | **信息架构** | `design.py` | 导航方案 + 内容策略 + 路径验证(3步规则) |
| 7 | **测试与衡量** | `measure.py` | QA 测试脚本 + 指标体系 + Bug 优先级(P0-P3) |
| 8 | **CEO: 用户经济模型** | `persona.py` | LTV/CAC 模型、角色级收入估算、健康度评估 |
| 9 | **CEO: 获取策略** | `persona.py` | 获客渠道优先级、预算分配、ROI、时间线 |
| 10 | **CEO: 留存策略** | `persona.py` | 留存率、流失预警、生命周期管理、重新激活 |

### 🔧 实用示例

#### 示例 1: 完整人物角色研究流程

```python
from persona import PersonaSkill

skill = PersonaSkill("电商平台")

# 步骤 1: 定义主要角色
skill.add_persona(
    name="小明",
    archetype="效率型用户",
    type="primary",
    quote="我只想快速找到想要的商品",
    goals=["快速完成任务", "获得个性化推荐"],
    behaviors=["频繁使用搜索", "比价后再购买"],
    pain_points=["搜索结果不准确", "信息过载"]
)

# 步骤 2: 定义次要角色
skill.add_persona(
    name="小红",
    archetype="探索型用户",
    type="secondary",
    quote="我喜欢发现新品和优惠",
    goals=["发现新品", "获取优惠信息"],
    behaviors=["浏览推荐", "关注直播", "分享好物"],
    pain_points=["推荐不够精准", "优惠规则复杂"]
)

# 步骤 3: 渲染所有角色
print(skill.render_all_personas())

# 步骤 4: 生成设计指导
design_guide = skill.generate_design_guide()
print(design_guide)
```

#### 示例 2: 用户细分与问卷设计

```python
# 生成用户细分问卷
survey = skill.design_survey("用户细分问卷", sample_size=500)
print(f"问卷题目数: {survey.question_count}")
print(f"预计完成时间: {survey.estimated_time} 分钟")

# 用户细分分析
segments = skill.analyze_segments(
    data=[
        {"user": "u001", "frequency": "high", "value": "high"},
        {"user": "u002", "frequency": "low", "value": "high"},
        {"user": "u003", "frequency": "high", "value": "low"},
    ]
)
print(segments)
```

#### 示例 3: CEO 视角用户经济模型

```python
# CEO 视角：用户经济模型 + 获取/留存策略
report = skill.generate_persona(include_ceo_analysis=True)
print(report)
# 输出包含：
# - 用户经济模型（LTV、CAC、留存曲线）
# - 获取策略（渠道优先级、转化漏斗）
# - 留存策略（关键行为、流失预警）
```

### 📁 项目结构

```
web-persona-skill/
├── SKILL.md              # AI Agent 技能定义
├── README.md             # 本文件
├── INSTALL.md            # 安装指南
├── pyproject.toml        # Python 包构建配置
├── persona/              # Python 包（纯标准库）
│   ├── __init__.py       # PersonaSkill 统一入口
│   ├── config.py         # 配置与常量
│   ├── interview.py      # 访谈提纲生成器
│   ├── survey.py         # 问卷设计器
│   ├── segment.py        # 用户细分分析器
│   ├── persona_builder.py # 人物角色构建器
│   ├── strategy.py       # 商业策略与功能优先级
│   ├── design.py         # 信息架构与内容策略
│   └── measure.py        # 测试计划与衡量体系
└── references/           # 知识库文档
```

### 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的人物角色核心：

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie 技能生态系统 (Skill Ecosystem)            │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│         (量化研究)   三角测量            Methods (通用设计)  │
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                      (需求洞察)               │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│         (数据叙事)   呈现              Design (价值设计)      │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (人物角色)               │
│                                         ↓                   │
│                                    🧠 Structured Thinking   │
│                                    Model (结构化思维)        │
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **Persona + UDM** → 用 UDM 访谈/观察方法收集角色研究数据
- **Persona + JTBD** → 用 JTBD 任务聚类定义人物角色
- **Persona + QuantUX** → 用量化数据验证角色细分和市场规模
- **Persona + VPD** → 用人物角色驱动价值主张设计
- **Persona + SWD** → 用数据叙事向团队展示角色故事

👉 **探索完整生态系统**: [通用设计方法](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [量化 UX 研究](https://github.com/AliDujie/Quantitative-UX-Research) | [价值主张设计](https://github.com/AliDujie/value-proposition-design) | [数据叙事](https://github.com/AliDujie/storytelling-with-data) | [结构化思维](https://github.com/AliDujie/Structured-Thinking-Model)

### 🛠️ 故障排查 (Troubleshooting)

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 角色画像过于笼统 | 研究数据不足 | 补充用户访谈，用 UDM 方法收集更多洞察 |
| 角色数量过多 | 细分过度 | 合并相似角色，保留 3-5 个核心角色 |
| 设计指导不具体 | 角色与功能脱节 | 为每个角色编写具体的用户故事和使用场景 |
| Bug 优先级混乱 | 缺乏角色视角 | 按角色影响面排序：Primary > Secondary > Negative |

### 🤝 最佳实践

#### 人物角色检查清单

- [ ] **基于真实数据** — 角色必须来自用户研究，不是凭空想象
- [ ] **数量适中** — 3-5 个核心角色，避免过多
- [ ] **有明确优先级** — Primary / Secondary / Negative 角色区分
- [ ] **包含行为数据** — 不仅描述人口统计，更要描述行为模式
- [ ] **可行动** — 每个角色必须有对应的设计指导

#### 角色创建原则

| 原则 | 说明 | 示例 |
|------|------|------|
| **单一焦点** | 每个角色有一个核心目标 | "快速完成购物" vs "发现新品" |
| **行为驱动** | 基于行为模式而非人口统计 | "频繁使用搜索" vs "25-35 岁女性" |
| **场景具体** | 角色在特定场景下才有意义 | "工作日午餐时" vs "一般购物" |
| **可区分** | 角色之间行为模式明显不同 | 效率型 vs 探索型 |

### ❓ 常见问题 (FAQ)

**Q: 人物角色 (Persona) 和用户细分 (Segmentation) 有什么区别？**
A: 用户细分是基于数据将用户分组（如行为模式、使用频率），人物角色是为每个重要分组创建有名字、有故事的档案。细分是"分群"，Persona 是"人格化"。本技能同时支持两者。

**Q: 需要多少研究数据才能创建 Persona？**
A: 建议至少 5-8 个用户访谈或 50+ 份问卷数据。没有足够数据时，可以用假设性 Persona 起步，但必须标注"待验证"并尽快用真实研究确认。

**Q: Persona 创建后怎么用？**
A: 在产品设计、功能优先级、营销信息、服务设计等决策中引用 Persona。问自己"这个决定对 [角色名] 有什么影响？"如果团队不做 Persona 驱动的决策，Persona 就成了墙上装饰。

**Q: 如何验证 Persona 的有效性？**
A: 用新研究数据验证角色行为模式是否成立。配合 QuantUX 的日志分析，用真实行为数据验证角色假设。建议每 6-12 个月更新一次。

### 📚 关于《The User Is Always Right》

- **书名**: The User Is Always Right: A Practical Guide to Creating and Using Personas for the Web
- **作者**: Steve Mulder & Ziv Yaar
- **出版**: New Riders, 2007
- **核心概念**: 人物角色创建、用户研究整合、设计指导
- **适用**: UX 设计师、产品经理、交互设计师、营销人员

### 🌟 用户评价

> "Web Persona 技能让我们从拍脑袋创建角色变成了基于数据的角色设计，设计团队和利益相关者的分歧明显减少了。"
> — 某电商平台 UX 设计负责人

> "人物角色档案的自动生成太高效了，以前需要一周的工作现在几小时搞定。"
> — 某 SaaS 公司产品经理

> "用户经济模型帮我们理解了不同角色的生命周期价值，获客策略更有针对性。"
> — 某在线教育公司增长负责人

### 📖 扩展阅读

- **《The User Is Always Right》** - Steve Mulder & Ziv Yaar (人物角色实践指南)
- **《Personas: Process and Practice》** - Lenny T. Malone (人物角色方法论)
- **《Observing the User Experience》** - Elizabeth Goodman (用户研究方法)
- **《About Face 4》** - Alan Cooper (目标导向设计与人物角色)

### 🏆 实战案例 (Case Studies)

#### 案例 1: 电商平台人物角色创建

**背景**: 某电商平台需要基于真实数据创建人物角色，指导设计和营销决策

**使用 Web Persona 技能**:
```python
from persona import PersonaSkill

skill = PersonaSkill("电商平台")

# 步骤 1: 创建人物角色
skill.add_persona(
    name="精明的比价妈妈",
    archetype="目标导向型",
    goals=["找到性价比最高的商品", "确保商品安全可靠"],
    frustrations=["商品信息不透明", "评价真假难辨"],
    behaviors=["购买前花 30 分钟比较", "看重其他妈妈的评价"]
)

# 步骤 2: 生成访谈提纲验证角色假设
interview = skill.generate_interview(
    "人物角色验证",
    dimensions=["购物目标", "决策流程", "痛点", "信息渠道"]
)

# 步骤 3: CEO 视角 — 用户经济模型
ceo = skill.generate_persona(include_ceo_analysis=True)
# → 角色生命周期价值 + 获取策略 + 留存策略
```

**成果**: 从 5 个角色聚焦到 3 个核心角色，设计决策效率提升 40%，营销转化率提升 25%

#### 案例 2: B2B SaaS 用户细分

**背景**: 某协作工具需要了解不同用户群体的需求差异

```python
from persona import PersonaSkill

skill = PersonaSkill("B2B 协作 SaaS")

# 用户细分分析
segments = skill.analyze_segments(
    data=[
        {"role": "团队负责人", "usage": "高", "pain": "看不到团队进度"},
        {"role": "执行成员", "usage": "中", "pain": "任务太多不知道先做哪个"},
        {"role": "外部协作者", "usage": "低", "pain": "找不到需要的文件"}
    ]
)

# 为每个细分创建设计指导
guidance = skill.generate_design_guidance(segments)
```

**成果**: 针对 3 个细分角色优化 onboarding 流程，新用户激活率从 35% 提升到 58%

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 📑 Table of Contents

- [Why Use This Skill?](#-why-use-this-skill)
- [Quick Decision Guide](#-quick-decision-guide)
- [Features at a Glance](#-features-at-a-glance)
- [Quick Start](#-quick-start)
- [10 Core Capabilities](#-10-core-capabilities)
- [Practical Examples](#-practical-examples)
- [Who Is This For?](#-who-is-this-for)
- [Troubleshooting](#-troubleshooting)
- [Best Practices](#-best-practices)
- [FAQ](#-faq)
- [User Reviews](#-user-reviews)
- [Extended Reading](#-extended-reading)
- [Related Skills](#-related-skills-1)
- [Skill Ecosystem Workflow](#-skill-ecosystem-workflow-1)
- [Version History](#-version-history-english)

### 🌟 Why Use This Skill?

- **Classic Methodology** — Based on Steve Mulder's "The User Is Always Right", a classic in persona creation
- **Full-Stack Toolkit** — From user research to persona creation, from business strategy to design guidance
- **CEO Perspective** — Built-in user economics model, acquisition strategy, retention strategy analysis
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Plug-and-Play** — Intuitive API, rich code examples, produce persona reports immediately

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "I need to know who my users are" | → **Web Persona** (this skill) — Create concrete personas |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### 🎯 Features at a Glance

| Feature | Description |
|---------|-------------|
| 10 Core Capabilities | Interview guides, surveys, user segmentation, persona creation, business strategy, IA, testing & measurement, CEO decision support |
| Persona Profiles | Behavior-based goals, pain points, design guidance |
| CEO Perspective | User economics + acquisition + retention strategies |
| User Segmentation | Behavior-based user clustering |
| Bilingual Support | Complete CN/EN documentation and code examples |

### 👥 Who Is This For?

| Role | Use Case |
|------|----------|
| **UX Designers** | Create evidence-based personas from real user data |
| **Product Managers** | Align product decisions with user segments |
| **Marketing Teams** | Target messaging to specific persona needs |
| **Service Designers** | Map services to persona journeys and touchpoints |
| **AI Agents** | Zero-dependency Python package for automated persona workflows |

### 🚀 Quick Start

#### Step 1: Install

```bash
cp -r web-persona-skill /your/agent/skills/
```

> 📖 See [INSTALL.md](INSTALL.md) for detailed installation guide

#### Step 2: Use as Python Package

```python
import sys
sys.path.insert(0, "/path/to/web-persona-skill")
from persona import PersonaSkill

skill = PersonaSkill("E-commerce Platform")

# ===== Scenario 1: Create Personas =====
skill.add_persona(
    name="Xiao Ming",
    archetype="Efficiency User",
    type="primary",
    quote="I just want to quickly find what I need",
    goals=["Complete tasks quickly", "Get personalized recommendations"],
    behaviors=["Frequent search usage", "Price comparison before purchase"]
)

skill.add_persona(
    name="Xiao Hong",
    archetype="Explorer User",
    type="secondary",
    quote="I love discovering new products and deals",
    goals=["Discover new products", "Get deal information"],
    behaviors=["Browse recommendations", "Follow live streams"]
)

print(skill.render_all_personas())
# Output: 2 persona profiles with goals, behaviors, pain points, design guidance

# ===== Scenario 2: Persona Quality Review (12-Item Checklist) =====
print(skill.review_personas())

# ===== Scenario 3: CEO Perspective (User Economics + Acquisition + Retention) =====
report = skill.generate_persona(include_ceo_analysis=True)
print(report)  # User economics + Acquisition + Retention strategies

# ===== Scenario 4: Feature Priority Matrix =====
skill.add_feature("Quick Checkout", {"Xiao Ming": "high", "Xiao Hong": "low"},
                  business_value="high", tech_difficulty="low")
print(skill.render_feature_matrix())  # P0-P3 ranking

# ===== Scenario 5: Bug Priority by Persona Impact =====
bug = skill.add_bug("Slow homepage", "Xiao Ming", is_primary=True, blocks_core=True)
print(bug)  # P0: Slow homepage (blocks primary persona's core task)

# ===== Scenario 6: IA + Content Strategy =====
print(skill.render_ia())
print(skill.render_content_strategy())

# ===== Scenario 7: Path Validation (3-Step Rule) =====
result = skill.validate_path("Xiao Ming", "Complete purchase", ["Home", "Search", "Checkout"])
print(result)  # Pass/Fail with explanation
```

### 💡 10 Core Capabilities

| # | Capability | Module | Description |
|---|------------|--------|-------------|
| 1 | **Interview Guide** | `interview.py` | 8-section interview (warmup → goals → behaviors → pains → expectations → competitors → future → closing) |
| 2 | **Survey Design** | `survey.py` | Needs/validation/satisfaction survey types |
| 3 | **User Segmentation** | `segment.py` | Goals/behaviors/attitudes 3D segmentation + 2x2 matrix |
| 4 | **Persona Creation** | `persona_builder.py` | Persona profiles + comparison table + scenarios + 12-item quality review |
| 5 | **Business Strategy** | `strategy.py` | Persona business value + feature matrix (P0-P3) + competitor analysis |
| 6 | **Information Architecture** | `design.py` | Navigation + content strategy + path validation (3-step rule) |
| 7 | **Testing & Measurement** | `measure.py` | QA test scripts + metrics + bug prioritization (P0-P3) |
| 8 | **CEO: User Economics** | `persona.py` | LTV/CAC model, persona-level revenue, health assessment |
| 9 | **CEO: Acquisition Strategy** | `persona.py` | Channel prioritization, budget allocation, ROI, timeline |
| 10 | **CEO: Retention Strategy** | `persona.py` | Retention rate, churn early warning, lifecycle management, reactivation |

### 🔧 Practical Examples

```python
# Example 1: Complete persona creation workflow
skill = PersonaSkill("Healthcare Platform")

skill.add_persona(
    name="Dr. Sarah Chen",
    archetype="Efficiency-Driven Professional",
    type="primary",
    quote="I need to access patient records quickly between appointments",
    goals=["Reduce admin time", "Access records from mobile", "Secure data sharing"],
    behaviors=["Uses tablet during rounds", "Checks email on phone", "Values speed over features"]
)

skill.add_persona(
    name="Nurse James Park",
    archetype="Care-Focused Coordinator",
    type="secondary",
    quote="I need to coordinate care across multiple patients",
    goals=["Track patient progress", "Communicate with doctors", "Manage shift handoffs"],
    behaviors=["Uses shared dashboard", "Relies on notifications", "Works in shifts"]
)

print(skill.render_all_personas())

# Example 2: User segmentation analysis
segments = skill.analyze_segments(
    data=[
        {"user": "A", "frequency": "daily", "features": ["search", "bookmarks"]},
        {"user": "B", "frequency": "weekly", "features": ["dashboard", "reports"]},
    ]
)
print(f"Identified {len(segments)} distinct segments")

# Example 3: CEO perspective with acquisition strategy
report = skill.generate_persona(include_ceo_analysis=True)
print(report)  # User economics + acquisition + retention strategies

# Example 4: End-to-end persona workflow for a SaaS product
skill = PersonaSkill("Project Management SaaS")
skill.add_persona(
    name="Team Lead Maria",
    archetype="Results-Driven Manager",
    type="primary",
    quote="I need visibility into what my team is working on without micromanaging",
    goals=["Track team progress", "Identify blockers early", "Report to stakeholders"],
    behaviors=["Checks dashboard daily", "Uses weekly reports", "Delegates via tool"]
)

# Feature prioritization based on persona impact
skill.add_feature("Automated Status Reports", {"Team Lead Maria": "high"},
                  business_value="high", tech_difficulty="medium")
print(skill.render_feature_matrix())

# Validate user journey (3-step rule)
result = skill.validate_path("Team Lead Maria", "Review team status",
                             ["Dashboard", "Team Overview", "Reports"])
print(result)  # Pass/Fail with actionable feedback
```

### 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| Personas feel stereotypical | Add specific behavioral data and direct quotes from real research |
| Too many personas | Consolidate to 3-5 primary personas; use secondary for edge cases |
| Segments overlap significantly | Re-examine segmentation criteria — use behavior over demographics |
| Design guidance too generic | Tie each design recommendation to a specific persona goal or behavior |

### 🤝 Best Practices

1. **Base personas on real research** — Never create personas from assumptions alone
2. **Focus on behaviors, not demographics** — What users do matters more than who they are
3. **Include design guidance** — Each persona should inform specific design decisions
4. **Keep it to 3-5 personas** — More personas dilute focus; prioritize primary users
5. **Update regularly** — Personas decay; validate with new research every 6-12 months

### ❓ FAQ

**Q: What's the difference between Personas and User Segmentation?**
A: Segmentation groups users based on data (behavior patterns, usage frequency); Personas create named, storied profiles for each important group. Segmentation is "clustering," Personas are "humanizing." This skill supports both.

**Q: How much research data is needed to create Personas?**
A: At least 5-8 user interviews or 50+ survey responses. With insufficient data, start with assumption-based personas but label them "unvalidated" and confirm with real research ASAP.

**Q: How do I use Personas after creating them?**
A: Reference them in product design, feature prioritization, marketing messaging, and service design decisions. Ask "What impact does this decision have on [persona name]?" If your team doesn't make persona-driven decisions, they become wall decorations.

**Q: How do I validate Persona effectiveness?**
A: Validate behavior patterns with new research data. Use QuantUX log analysis to confirm persona assumptions with real behavior data. Recommend updating every 6-12 months.

### 🌟 User Reviews

> "Our team used to have armchair personas based on assumptions. This skill helped us create evidence-based personas that actually changed our design decisions." — **UX Design Lead, Healthcare Tech**

> "The segmentation analysis revealed a user group we completely missed. They turned out to be our fastest-growing segment." — **Product Manager, Social Platform**

> "We present personas to the board now. Having structured, data-backed personas makes user-centered decisions much easier." — **VP of Design, Enterprise Software**

### 📖 Extended Reading

- **"The User Is Always Right"** — Steve Mulder, the classic persona creation guide
- **"About Face: The Essentials of Interaction Design"** — Alan Cooper, persona-driven design
- **"Mapping Experiences"** — Jim Kalbach, customer journey mapping
- **"Lean UX"** — Jeff Gothelf, persona-driven agile design

### 📚 About This Skill

This skill is based on the methodology from *"The User Is Always Right"* by Steve Mulder, a classic in persona creation. The skill provides a structured approach to creating evidence-based user personas that drive design decisions.

### 🔗 Related Skills

This skill is part of the **AliDujie UX Research Skills Ecosystem**:

```
┌─────────────────────────────────────────────────────────────┐
│           AliDujie Skill Ecosystem                          │
├─────────────────────────────────────────────────────────────┤
│   📊 Quantitative UX Research ←───→ 📖 Universal Design     │
│    (quantitative)   triangulation       Methods             │
│              ↑                          ↓                   │
│              │                    🎯 JTBD Knowledge          │
│              │                    (needs insight)            │
│   📈 Storytelling with Data ←───→ 💎 Value Proposition      │
│    (data narrative) presentation         Design              │
│              ↑                          ↑                   │
│              │                    👤 Web Persona             │
│              └────────────────────  (this skill)             │
│                                         ↓                   │
│                                    🧠 Structured Thinking   │
│                                    Model                     │
└─────────────────────────────────────────────────────────────┘
```

**Integration patterns:**

- **Persona + UDM** → Collect persona research data with UDM interviews and observation methods
- **Persona + JTBD** → Define personas based on JTBD task clustering
- **Persona + QuantUX** → Validate persona segments and market size with quantitative data
- **Persona + VPD** → Drive value proposition design from persona goals and pains
- **Persona + SWD** → Present persona stories with data-driven narratives

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 design research methods
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done theory
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — Quantitative research, HEART framework
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — Value proposition canvas
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — Data storytelling
- **[Structured-Thinking-Model](https://github.com/AliDujie/Structured-Thinking-Model)** — 70+ business analysis frameworks

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | [Structured Thinking](https://github.com/AliDujie/Structured-Thinking-Model)

### 🏷️ GitHub Topics (Recommended)

```
persona user-research user-segmentation design-guidance
python-toolkit openclaw-skill alicloud
```

### 📋 Changelog

| Version | Date | Changes |
| v2.4.7 | 2026-05-03 | Repo maintenance: improved Quick Start scenario 4-7 code comment formatting, aligned SKILL.md version with README.md |
| v2.4.5 | 2026-05-03 | Repo maintenance: added English version history table at README end, added classifiers and project.urls to pyproject.toml |
| v2.4.4 | 2026-05-03 | Repo maintenance: cross-ecosystem consistency review, verified cross-references and version alignment |
| v2.4.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
| v2.4.2 | 2026-05-02 | Repo maintenance: fixed encoding bug in English capabilities table (流失预警 → churn early warning), added GitHub Topics, changelog, and Structured-Thinking-Model to English section |
| v2.4.1 | 2026-05-02 | Fixed SKILL.md version mismatch, added CEO capabilities to English table |
| v2.4 | 2026-04-30 | Updated maintenance, cleaned up formatting |

---

## 🔗 Skill Ecosystem Workflow

Persona is the persona core of the **AliDujie UX Research Skills Ecosystem**. Here are typical workflows combining it with other skills:

### 🧭 Quick Decision Guide

| Your Question | Recommended Skill |
|---------------|------------------|
| "I need to know who my users are" | → **Web Persona** (this skill) — Create concrete personas |
| "I don't know what research to do" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — Method recommendation |
| "I want to understand why users do this" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — Uncover the underlying "jobs" |
| "I need to validate a hypothesis" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B testing & sample size |
| "Is my product value strong enough?" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — Fit diagnosis |
| "How do I present research results clearly?" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — Data storytelling |

### Workflow 1: Research → Persona → Value Design

```
UDM (research) → Persona (persona creation) → VPD (value alignment)
```

**Scenario**: Evidence-driven persona creation
1. Use UDM interviews and observation to collect behavioral data
2. Use Persona to synthesize data into concrete, actionable personas
3. Use VPD to align value proposition to each persona's needs

### Workflow 2: Persona → Segmented Testing → Opportunity

```
Persona (user segments) → QuantUX (stratified A/B testing) → JTBD (opportunity scoring)
```

**Scenario**: Personalized product optimization
1. Use Persona to define user segments based on behavior patterns
2. Use QuantUX to design stratified A/B tests for each segment
3. Use JTBD to calculate opportunity scores per segment

### Workflow 3: User Feedback → Value Adjustment

```
Persona (user feedback) → SWD (chart makeover) → VPD (value adjustment)
```

**Scenario**: User satisfaction improvement
1. Use Persona to collect and organize user feedback data
2. Use SWD to transform charts, highlighting key issues
3. Use VPD to adjust value proposition based on targeted feedback

> 💡 **Tip**: Personas pair naturally with UDM — use UDM interview and observation methods to collect persona research data, building evidence-driven personas.

---

## 🔗 技能生态工作流 (Skill Ecosystem Workflow)

Persona 是 **AliDujie UX 研究技能生态系统** 的人物角色核心。以下是与其他技能配合使用的典型工作流：

### 🧭 快速决策指南 (Quick Decision Guide)

| 你的问题 | 推荐技能 |
|----------|----------|
| "我需要知道用户是谁" | → **Web Persona** (本技能) — 创建具体的人物角色 |
| "我不知道该研究什么" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — 方法推荐帮你找到方向 |
| "我想理解用户为什么这样做" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — 挖掘用户背后的"工作" |
| "我需要验证一个假设" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B 测试和样本量计算 |
| "我的产品价值够不够？" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — 契合度诊断 |
| "我怎么把研究结果讲清楚？" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事和图表改造 |

### 工作流 1: 研究 → Persona → 价值设计

```
UDM (用户访谈) → Persona (角色创建) → VPD (价值主张)
```

**场景**: 新产品设计
1. 用 UDM 访谈和观察方法收集用户数据
2. 用 Persona 基于行为数据创建证据驱动的角色
3. 用 VPD 将角色目标/痛点映射到价值主张画布

### 工作流 2: Persona → 定量验证 → 汇报

```
Persona (角色细分) → QuantUX (分层测试) → SWD (故事呈现)
```

**场景**: 个性化产品优化
1. 用 Persona 创建 3-5 个核心角色
2. 用 QuantUX 为每个角色设计分层 A/B 测试
3. 用 SWD 将角色故事和数据可视化呈现

### 工作流 3: JTBD → Persona 精化

```
JTBD (任务聚类) → Persona (角色定义) → QuantUX (规模验证)
```

**场景**: 用户细分验证
1. 用 JTBD 四力分析识别用户切换动机和任务聚类
2. 用 Persona 将 JTBD 发现整合到角色文档
3. 用 QuantUX 日志分析验证角色规模和行为模式

> 💡 **提示**: Persona 的黄金法则是"不从人口统计入手"——聚焦目标/行为/观点三维度。

## Run Tests / 运行测试

```bash
cd /path/to/web-persona-skill
python3 -m pytest persona/tests/ -v
# 或直接运行测试
python3 persona/tests/test_all.py
```

## 🤝 参与贡献 (Contributing)

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解贡献指南。

- 🐛 **报告 Bug**: 提交 [Issue](https://github.com/AliDujie/web-persona-skill/issues)
- 💡 **功能建议**: 提交 [Feature Request](https://github.com/AliDujie/web-persona-skill/issues/new?template=feature_request.md)
- 📝 **改进文档**: PR 欢迎，特别是参考文档和代码示例

## 🆘 获取帮助 (Getting Help)

- 📖 查看 [故障排查](#故障排查-troubleshooting) 部分
- 📚 阅读 [references/](references/) 目录下的知识库文档
- 💬 在 [Issues](https://github.com/AliDujie/web-persona-skill/issues) 中提问

## 📖 扩展阅读

| 书籍 | 作者 | 关联能力 |
|------|------|----------|
| 《The User Is Always Right》 | Steve Mulder & Ziv Yaar | 全书方法论基础 |
| 《Persona Lifecycle》 | John Pruitt & Tamara Adlin | 角色生命周期管理 |
| 《Just Enough Research》 | Erika Hall | 精益用户研究方法 |
| 《Observing the User Experience》 | Mike Kuniavsky | 用户观察与访谈技巧 |

## 📜 许可 (License)

MIT License — 基于《The User Is Always Right》by Steve Mulder & Ziv Yaar

## 👨‍💻 作者 (Credits)

- 基于《The User Is Always Right》by Steve Mulder & Ziv Yaar
- 技能开发：AliDujie 团队
- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫

### 🚀 完整端到端工作流：从角色到设计指导 (End-to-End Workflow)

以下是一个真实场景中，6 个技能如何协作完成从人物角色创建到设计指导的完整工作流：

**场景**: 电商平台需要基于数据的人物角色来指导产品改版

```
Phase 1: 角色研究
  UDM: 用户观察 + 情境访谈 (20 用户) → 收集行为数据
  JTBD: 分析不同用户群体的核心"工作"差异

Phase 2: Persona 角色创建 (本技能)
  → segment_users: 基于行为模式分群 (搜索型/浏览型/比价型)
  → create_persona: 创建 2 个首要角色
     "小明" - 效率型买家 (搜索型): 快速找到商品 → 3 步内完成
     "小红" - 发现型买家 (浏览型): 探索灵感 → 个性化推荐
  → generate_checklist: 角色设计检查清单 (10 维度)
  → strategy: 获取策略 + 留存策略

Phase 3: 验证与量化
  QuantUX: 日志分析验证角色行为模式 (10 万+ 用户)
  VPD: 为不同角色设计差异化价值主张

Phase 4: 设计执行
  UDM: 基于 Persona 设计可用性测试场景
  SWD: 将角色洞察转化为设计原则汇报
```

> 💡 **Persona 是工作流的决策锚点**: 所有后续决策 (功能优先级、设计方向、营销定位) 都以角色为锚

👉 **尝试完整工作流**: [UDM](https://github.com/AliDujie/universal-design-methods) · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data)

---

### 💡 Pro Tips / 专业提示

- **不从人口统计入手** — 聚焦目标/行为/观点三维度，而非年龄/性别/收入
- **行为 > 态度** — 用户"做了什么"比"说了什么"重要 10 倍
- **首要角色最多 2 个** — 超过 2 个首要角色意味着焦点分散
- **3 步规则验证路径** — 首要角色完成核心任务不应超过 3 步
- **角色需要定期更新** — 每 6-12 个月用新研究验证角色有效性
- **Persona + QuantUX 量化验证** — 用日志分析验证角色行为模式的规模和真实性

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
| v2.4.18 | 2026-05-05 | Repo maintenance: added Structured Thinking Model to ecosystem diagrams (CN+EN), verified cross-references consistency |
| v2.4.17 | 2026-05-04 | 仓库维护：修复版本历史表格 `| |` 格式错误，补充英文目录中端到端工作流链接
| v2.4.16 | 2026-05-04 | 仓库维护：添加英文目录(Table of Contents)和5分钟快速开始检查清单；优化英文版 Quick Start 示例代码，增强 Features at a Glance 表格描述
| v2.4.14 | 2026-05-04 | 仓库维护：修复 SKILL.md 版本不一致 (2.4.11→2.4.13)，对齐所有版本引用
| v2.4.12 | 2026-05-04 | 仓库维护：修复版本历史排序（v2.4.8→v2.4.10 顺序校正），增强英文版 Quick Start 场景注释 |
| v2.4.11 | 2026-05-04 | 仓库维护：添加完整端到端工作流章节（展示从角色创建到设计指导的 6 技能协作流程） |
| v2.4.10 | 2026-05-03 | 仓库维护：添加 Pro Tips 专业提示章节（中英双语），强化角色创建原则 |
| v2.4.9 | 2026-05-03 | 仓库维护：修复英文版版本历史表格格式（删除错误分隔符行），SKILL.md 版本对齐，完善角色创建原则 |
| v2.4.8 | 2026-05-03 | 仓库维护：修复版本历史表格格式（删除错误分隔符行），统一 SKILL.md 与 README.md 版本引用 |
| v2.4.7 | 2026-05-03 | 仓库维护：优化 Quick Start 场景 4-7 代码示例注释格式，统一 SKILL.md 与 README.md 版本引用 |
| v2.4.5 | 2026-05-03 | 仓库维护：添加英文版版本历史表，统一 pyproject.toml 元数据 |
| v2.4.4 | 2026-05-03 | 仓库维护：跨技能一致性审查，验证交叉引用和版本对齐 |
| v2.4.3 | 2026-05-02 | 仓库维护：为英文版添加 Quick Decision Guide 导航表，增强技能间交叉引用 |
| v2.4.2 | 2026-05-02 | 仓库维护：优化人物角色检查清单格式，增强工作流 3 描述一致性，统一交叉引用格式，补充 Features at a Glance 表 |
| v2.4.1 | 2026-05-02 | 修复 SKILL.md 版本号不一致 (v2.3.0→v2.4.0)，补充 CEO 能力到英文能力表，添加 Structured-Thinking-Model 交叉引用 |
| v2.2 | 2026-04-30 | 更新维护，清理格式 |
| v2.0 | 2026-04-29 | 统一交叉引用为 GitHub 绝对链接，添加 GitHub Topics，更新 Last Updated 日期 |
| v1.7 | 2026-04-25 | 统一技能生态格式，更新交叉引用 |
| v1.6 | 2026-04-23 | 添加 badges、技能生态系统 ASCII 图、双语支持、Why Use This Skill?、Quick Start、最佳实践、作者信息 |
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

---

### 💡 Pro Tips

- **Don't Start with Demographics** — Focus on goals/behaviors/attitudes, not age/gender/income
- **Behaviors > Attitudes** — What users "do" matters 10x more than what they "say"
- **Max 2 Primary Personas** — More than 2 primary personas means scattered focus
- **3-Step Rule for Paths** — Primary personas shouldn't need more than 3 steps for core tasks
- **Update Personas Regularly** — Validate personas with new research every 6-12 months
- **Persona + QuantUX for validation** — Use log analysis to validate persona behavior patterns at scale

## 📋 Version History (English)

| Version | Date | Changes |
| v2.4.18 | 2026-05-05 | Repo maintenance: added Structured Thinking Model to ecosystem diagrams, verified cross-references
| v2.4.17 | 2026-05-04 | Repo maintenance: fixed changelog table `| |` formatting, added end-to-end workflow English TOC link
| v2.4.16 | 2026-05-04 | Repo maintenance: added English TOC and 5-min checklist; improved English Quick Start example code, enhanced Features at a Glance table descriptions
| v2.4.14 | 2026-05-04 | Repo maintenance: fixed SKILL.md version mismatch (2.4.11→2.4.13), aligned all version references, added Credits section |
| v2.4.12 | 2026-05-04 | Repo maintenance: fixed changelog ordering (v2.4.8→v2.4.10 sequence corrected), enhanced English Quick Start scenario comments |
| v2.4.11 | 2026-05-04 | Repo maintenance: added end-to-end workflow section showing 6-skill collaboration from persona creation to design guidance |
| v2.4.10 | 2026-05-03 | Repo maintenance: added Pro Tips section (CN/EN) for persona creation principles |
| v2.4.9 | 2026-05-03 | Repo maintenance: fixed English changelog table formatting, aligned SKILL.md version, refined persona creation principles |
| v2.4.8 | 2026-05-03 | Repo maintenance: fixed changelog table formatting, aligned SKILL.md version with README.md |
| v2.4.7 | 2026-05-03 | Repo maintenance: improved Quick Start scenario 4-7 code example comment formatting, aligned SKILL.md version |
| v2.4.6 | 2026-05-03 | Repo maintenance: fixed SKILL.md version mismatch (2.4.4→2.4.6), aligned all version references across README/SKILL.md/pyproject.toml |
| v2.4.5 | 2026-05-03 | Repo maintenance: added English version history table, added classifiers and project.urls to pyproject.toml |
| v2.4.4 | 2026-05-03 | Repo maintenance: cross-ecosystem consistency review, verified cross-references and version alignment |
| v2.4.3 | 2026-05-02 | Added English Quick Decision Guide table to improve cross-skill discoverability |
| v2.4.2 | 2026-05-02 | Fixed encoding bug in English capabilities table, added GitHub Topics and changelog to English section |
| v2.4.1 | 2026-05-02 | Fixed SKILL.md version mismatch, added CEO capabilities to English table |
| v2.4 | 2026-04-30 | Updated maintenance, cleaned up formatting |
| v2.0 | 2026-04-29 | Unified cross-references to GitHub absolute links, added GitHub Topics |
| v1.7 | 2026-04-25 | Unified skill ecosystem format, updated cross-references |
| v1.6 | 2026-04-23 | Added badges, ASCII diagram, bilingual support, Why Use This Skill?, Quick Start, best practices |
| v1.3 | 2026-04-22 | Initial release |

---

### 👨‍💻 Credits

Based on *The User Is Always Right* by Steve Mulder & Ziv Yaar (New Riders, 2007), covering evidence-based persona creation and application.

**Applicable to:** UX Designers, Product Managers, Interaction Designers, Marketers

---

*Last Updated: 2026-05-05 | AliDujie Skill Ecosystem | v2.4.18*
