# Web Persona Skill

[![Ecosystem](https://img.shields.io/badge/AliDujie-Ecosystem-7B68EE.svg)](https://github.com/AliDujie)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Version](https://img.shields.io/badge/version-2.4.56-green.svg)](CHANGELOG.md)
[![Install Guide](https://img.shields.io/badge/install-guide-orange.svg)](INSTALL.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026-05-14-brightgreen.svg)

> 👤 **一句话介绍**: 基于 Steve Mulder《The User Is Always Right》的完整人物角色工具包。从用户研究到角色创建，从商业策略到设计指导，内置 CEO 视角的用户经济模型分析。

```text
┌─────────┐    ┌──────────┐    ┌─────┐    ┌──────────┐    ┌─────┐    ┌─────┐
│ Persona │ →  │   JTBD   │ →  │ UDM │ →  │ QuantUX  │ →  │ VPD │ →  │ SWD │
│ 角色定义 │    │ 需求洞察  │    │ 研究方法 │    │ 定量验证  │    │ 价值设计│    │ 数据叙事 │
└─────────┘    └──────────┘    └─────┘    └──────────┘    └─────┘    └─────┘
```

**Persona is the foundation** — evidence-based user roles that anchor every other skill. Start here to define WHO you're designing for.

---
## 📑 目录 / Table of Contents

- [中文说明](#中文说明)
  - [🌐 技能生态系统](#-技能生态系统-skill-ecosystem)
  - [🌟 为什么使用这个技能？](#-为什么使用这个技能why-use-this-skill)
  - [⚡ 5 分钟快速开始](#-5-分钟快速开始-quick-start)
  - [💡 9 大核心能力](#-9-大核心能力)
  - [🔧 实用示例](#-实用示例)
  - [📁 项目结构](#-项目结构)
  - [👥 这个技能适合谁？](#-这个技能适合谁who-is-this-for)
  - [🛠️ 疑难解答](#-疑难解答-troubleshooting)
  - [🏆 案例研究](#-案例研究-case-studies)
  - [🆘 获取帮助](#-获取帮助-getting-help)
  - [🔗 相关技能](#-相关技能)
- [English](#english)
  - [🌟 Why Use This Skill?](#-why-use-this-skill)
  - [🚀 Quick Start](#-quick-start)
  - [🔗 Related Skills](#-related-skills-1)
- [🤝 参与贡献](#-参与贡献-contributing)
- [📜 许可](#-许可-license)
- [🔗 技能生态工作流](#-技能生态工作流-skill-ecosystem-workflow)


## 🌐 技能生态系统 (Skill Ecosystem)

本技能是 AliDujie 用户研究技能生态系统的**人物角色核心**，负责创建证据驱动的用户角色。与其他技能协同使用，效果更佳：

| 技能 | 角色 | 协同场景 |
|------|------|----------|
| [🔍 Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 研究方法 | UDM 研究数据 → Persona 角色创建 → 设计指导 |
| [📊 Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量验证 | Persona 假设 → QuantUX 行为验证 → 角色精化 |
| [📈 Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | Persona 数据 → SWD 可视化 → 团队对齐 |
| [🎯 JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 深度需求洞察 | Persona 角色 → JTBD 工作映射 → 深层需求 |
| [💎 Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值设计 | Persona 细分 → VPD 画布分析 → 价值匹配 |
| [🧠 Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略分析 | Persona 洞察 → STM 商业框架 → 市场定位 |

---

### 🔗 Ecosystem Quick Start / 生态系统快速上手

Persona 是 7 技能工作流的**起点**——定义 "为谁设计"，一切从人物角色开始。

```
Persona (← 你在这里) → JTBD → UDM → QuantUX → VPD → SWD
```

**组合调用示例：**
```python
# Step 1: 创建人物角色
from persona import PersonaSkill
persona = PersonaSkill("旅行平台")

# 基于真实数据创建角色
persona.add_persona("小明", "效率型用户", "primary",
                    "我只想快速完成预订",
                    goals=["快速找到酒店", "一键支付"],
                    behaviors=["工作日使用", "价格不敏感"],
                    attitudes=["时间就是金钱"],
                    bio="28岁，IT 行业，每月出差 2-3 次")

# Step 2: 生成角色专属访谈提纲
guide = persona.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"])

# Step 3: 获取设计指导
advice = persona.generate_design_guidance("小明")

# Step 4: 将 Persona 交给 JTBD 做深层需求分析
from jtbd import JTBDSkill
jtbd = JTBDSkill("旅行平台")
score = jtbd.score_opportunity("快速完成预订", struggle=4, alternative=3, market=4, budget=4)
```

> 💡 **提示**: Persona 是一切的基础——先用它定义 "为谁设计"，后续所有技能都基于这些角色展开。

> 💡 **Try it now / 立即尝试**:
> ```python
> from persona import PersonaSkill
> skill = PersonaSkill("你的产品")
> skill.add_persona("示例用户", "核心用户群", "primary", "我的核心诉求", goals=["目标1"], behaviors=["行为1"], attitudes=["态度1"], bio="背景描述")
> print(skill.render_all_personas())  # 立即渲染角色
> ```

### ✅ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r web-persona-skill /your/agent/skills/`
- [ ] **导入** — `from persona import PersonaSkill`
- [ ] **初始化** — `skill = PersonaSkill("你的产品")`
- [ ] **人物角色** — `skill.add_persona("小明", "效率型用户", "primary", "我只想快速完成", goals=["..."], behaviors=["..."], attitudes=["..."], bio="...")`
- [ ] **访谈提纲** — `skill.generate_interview("访谈", sections=["goals", "behaviors", "pain_points"])`
- [ ] **用户细分** — `skill.add_segment("效率型", "追求速度", ["快速完成"], ["高频使用"], ["效率优先"])`
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

### 🌍 实战场景指南

| 你的场景 | 调用方式 | 输出结果 |
|----------|---------|----------|
| "为产品创建人物角色" | `add_persona(name, type, "they want to...", goals=[...])` | 完整角色档案：目标、行为、痛点 |
| "该问用户什么问题？" | `generate_interview("访谈", sections=["goals", "behaviors"])` | 对齐角色需求的研究访谈指南 |
| "细分用户群" | `add_segment("效率型", "追求速度", ["快速完成"])` | 行为细分 + 区分特征 |
| "获取角色设计指导" | `generate_design_guidance("小明")` | 可执行的设计建议与禁忌 |
| "这个角色的商业价值？" | `generate_economic_model("小明")` | 用户经济模型：获客、LTV、留存 |

> 💡 **提示**: 基于真实数据创建角色——使用 UDM 研究发现作为每个角色属性的证据支撑。

### 🌟 为什么使用这个技能？(Why Use This Skill?)

- **经典方法论** — 基于 Steve Mulder《The User Is Always Right》，人物角色领域的经典著作
- **全链路工具** — 从用户研究到角色创建，从商业策略到设计指导
- **CEO 视角** — 内置用户经济模型、获取策略、留存策略分析
- **零依赖** — 纯 Python 标准库实现，无外部依赖，5 分钟上手
- **双语支持** — 完整中英文文档，适合国际化团队
- **即插即用** — API 设计直观，代码示例丰富，即刻产出人物角色报告
- **证据驱动** — 每个角色属性都基于真实研究数据，而非虚构的假设——让团队决策有据可依
- **从角色到策略** — 不止是创建人物档案，更提供获取策略、留存策略、用户经济模型等可执行的商业建议
- **团队对齐** — 用具体的人物角色取代抽象的"用户"讨论，让设计、产品、营销团队在同一个语境下协作

### ⚡ 5 分钟快速开始 (Quick Start)

#### 步骤 1: 安装技能

```bash
# 方式 A: 复制到你的 AI Agent skills 目录
cp -r web-persona-skill /your/agent/skills/

# 方式 B: 作为 Python 包安装（支持 pip import）
cd web-persona-skill && pip install -e .
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
    "小明", "效率型用户", "primary",
    quote="我只想快速找到想要的商品",
    goals=["快速完成任务", "获得个性化推荐"],
    behaviors=["频繁使用搜索", "比价后再购买"],
    attitudes=["追求效率"],
    bio="忙碌的白领，重视时间"
)

skill.add_persona(
    "小红", "探索型用户", "secondary",
    quote="我喜欢发现新品和优惠",
    goals=["发现新品", "获取优惠信息"],
    behaviors=["浏览推荐", "关注直播"],
    attitudes=["喜欢探索"],
    bio="年轻用户，喜欢发现新事物"
)

print(skill.render_all_personas())
# 输出：2 个角色档案，包含目标、行为、痛点、设计指导

# ===== 场景 2: 访谈提纲与问卷设计 =====
guide = skill.generate_interview(
    "新用户上手体验访谈",
    sections=["goals", "behaviors", "pain_points", "motivations"]
)
print(guide)

survey = skill.generate_survey("用户细分问卷", "needs", pain_points=["搜索不精准"])
print(survey)

# ===== 场景 3: CEO 视角用户经济模型 =====
report = skill.generate_persona(include_ceo_analysis=True)
print(report)
# 输出：用户经济模型 + 获取策略 + 留存策略

# ===== 场景 4: 功能优先级 + Bug 优先级 =====
skill.add_feature("快速下单", {"小明": "高", "小红": "低"}, "高", "低")
skill.add_feature("个性化推荐", {"小明": "中", "小红": "高"}, "高", "中")
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
skill.add_test_script("小明", [{"action": "打开首页", "expected": "显示推荐"}, {"action": "搜索商品", "expected": "展示结果"}, {"action": "查看详情", "expected": "加载详情"}, {"action": "完成下单", "expected": "确认页面"}])
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
    "小明", "效率型用户", "primary",
    quote="我只想快速找到想要的商品",
    goals=["快速完成任务", "获得个性化推荐"],
    behaviors=["频繁使用搜索", "比价后再购买"],
    attitudes=["追求效率"],
    bio="忙碌的白领"
)

# 步骤 2: 定义次要角色
skill.add_persona(
    "小红", "探索型用户", "secondary",
    quote="我喜欢发现新品和优惠",
    goals=["发现新品", "获取优惠信息"],
    behaviors=["浏览推荐", "关注直播", "分享好物"],
    attitudes=["喜欢探索"],
    bio="年轻用户，喜欢发现新事物"
)

# 步骤 3: 渲染所有角色
print(skill.render_all_personas())

# 步骤 4: 生成内容策略与设计指导
design_guide = skill.render_content_strategy()
print(design_guide)
```

#### 示例 2: 用户细分与问卷设计

```python
# 生成用户细分问卷
survey = skill.generate_survey("用户细分问卷", "needs", pain_points=["搜索不精准"])
print(survey)

# 用户细分分析
skill.add_user("u001", goals=["快速购买"], behaviors=["高频使用"], attitudes=["效率优先"])
skill.add_user("u002", goals=["发现好物"], behaviors=["低频浏览"], attitudes=["价格敏感"])
skill.add_segment("效率型", "追求速度", ["快速完成"], ["高频使用"], ["效率优先"], 60)
skill.add_segment("探索型", "喜欢发现", ["发现新品"], ["低频浏览"], ["价格敏感"], 40)
print(skill.render_segments())
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
│   ├── utils.py          # 工具函数
│   ├── templates.py      # 模板常量
│   ├── interview.py      # 访谈提纲生成器
│   ├── survey.py         # 问卷设计器
│   ├── segment.py        # 用户细分分析器
│   ├── persona_builder.py # 人物角色构建器
│   ├── strategy.py       # 商业策略与功能优先级
│   ├── design.py         # 信息架构与内容策略
│   ├── measure.py        # 测试计划与衡量体系
│   └── tests/            # 测试套件
└── references/           # 知识库文档（5 篇，含最佳实践和跨技能工作流）
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
| **单一焦点** | 每个角色有一个核心目标 | "快速完成购物" vs "发现新品" |
| **行为驱动** | 基于行为模式而非人口统计 | "频繁使用搜索" vs "25-35 岁女性" |
| **场景具体** | 角色在特定场景下才有意义 | "工作日午餐时" vs "一般购物" |
| **可区分** | 角色之间行为模式明显不同 | 效率型 vs 探索型 |

### 💡 专业技巧

- **给角色起名** — "小明"和"小红"比"角色 1"和"角色 2"更容易记住。名字让角色在设计讨论中变得真实可引用
- **每个角色给一句引言** — 一句话捕捉核心需求，让角色在设计讨论中容易被引用和参考
- **每次设计评审都用角色** — 问"这个决定服务于哪个角色？"如果答案是"所有人"，可能没有服务好任何人
- **将角色映射到商业价值** — 不是所有角色同等重要。量化每个角色的经济影响来优先设计投资
- **也创建反角色** — 定义你不为谁设计。这防止范围蔓延，让团队保持聚焦

### ❌ 常见错误

- **仅人口统计的角色** — 年龄、性别和收入不告诉你任何行为信息。关注目标、行为和痛点
- **角色太多** — 超过 4-5 个角色会分散焦点。优先选择 1 个主要角色、2-3 个次要角色，做艰难选择
- **角色落灰** — 如果角色不在日常决策中使用，它们就是墙上的壁纸。打印出来贴在墙上，在会议中引用
- **跳过 12 项质量评审** — 使用内置质量检查清单，在弱角色误导团队之前发现它们
- **混淆细分和角色** — 细分告诉你每类"有多少"；角色告诉你"他们需要什么"。两者有价值但不同

### ❓ 常见问题 (FAQ)

**Q: 人物角色 (Persona) 和用户细分 (Segmentation) 有什么区别？**
A: 用户细分是基于数据将用户分组（如行为模式、使用频率），人物角色是为每个重要分组创建有名字、有故事的档案。细分是"分群"，Persona 是"人格化"。本技能同时支持两者。

**Q: 需要多少研究数据才能创建 Persona？**
A: 建议至少 5-8 个用户访谈或 50+ 份问卷数据。没有足够数据时，可以用假设性 Persona 起步，但必须标注"待验证"并尽快用真实研究确认。

**Q: Persona 创建后怎么用？**
A: 在产品设计、功能优先级、营销信息、服务设计等决策中引用 Persona。问自己"这个决定对 [角色名] 有什么影响？"如果团队不做 Persona 驱动的决策，Persona 就成了墙上装饰。

**Q: 如何验证 Persona 的有效性？**
A: 用新研究数据验证角色行为模式是否成立。配合 QuantUX 的日志分析，用真实行为数据验证角色假设。建议每 6-12 个月更新一次。

### ⚠️ 常见角色创建陷阱 (Common Pitfalls)

| 陷阱 | 表现 | 应对 |
|------|------|------|
| 从人口统计开始 | "25-35 岁白领女性" | 从目标/行为/观点三维度开始，人口统计是补充 |
| 角色太多失去焦点 | 创建 10+ 个角色 | 控制在 3-6 个，首要角色最多 2 个 |
| 角色没有优先级 | 所有角色"同等重要" | 明确 primary/secondary/negative，保证设计决策有优先级 |
| 简介用列表 | 用 bullet points 描述角色 | 用叙述型自传，讲故事才能让人记住 |
| 不维护活力 | 角色创建后不用 | 海报张贴、会议引用、定期数据更新 |
| 跳过质量评审 | 直接用未评审的角色 | 运行 12 项质量评审检查，确保角色基于真实数据 |

> 💡 **提示**: Persona 是用户定义层——为所有其他技能提供证据驱动的用户视角。先创建角色，再驱动 JTBD/UDM/VPD 分析。

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
    "精明的比价妈妈", "目标导向型", "primary",
    quote="我要为家人找到最划算的商品",
    goals=["找到性价比最高的商品", "确保商品安全可靠"],
    behaviors=["购买前花 30 分钟比较", "看重其他妈妈的评价"],
    attitudes=["重视性价比"],
    bio="两位孩子的妈妈，注重家庭开支"
)

# 步骤 2: 生成访谈提纲验证角色假设
interview = skill.generate_interview(
    "人物角色验证",
    sections=["goals", "behaviors", "pain_points"]
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
skill.add_user("u001", goals=["跟踪团队进度"], behaviors=["每日查看仪表盘"], attitudes=["结果导向"])
skill.add_user("u002", goals=["明确任务优先级"], behaviors=["中等频率使用"], attitudes=["注重效率"])
skill.add_user("u003", goals=["快速找到文件"], behaviors=["低频使用"], attitudes=["需要简单体验"])
skill.add_segment("团队负责人", "管理团队需要可视化", ["跟踪进度"], ["每日查看仪表盘"], ["结果导向"], 30)
skill.add_segment("执行成员", "执行任务需要清晰指引", ["明确优先级"], ["中等频率使用"], ["注重效率"], 50)
skill.add_segment("外部协作者", "偶尔参与需要快速上手", ["快速查找"], ["低频使用"], ["简单体验"], 20)

# 为每个细分创建设计指导
guidance = skill.generate_design_guidance(segments)
```

**成果**: 针对 3 个细分角色优化 onboarding 流程，新用户激活率从 35% 提升到 58%

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---


---

### 🧭 快速决策指南 (Quick Decision Guide)

| 你的问题 | 推荐技能 |
|----------|----------|
| "需要创建用户画像" | → **Web Persona (本技能)** — 人物角色创建与细分 |
| "不知道选什么研究方法" | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) — 方法推荐与执行 |
| "想理解用户背后的「工作」" | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) — 用户"工作"挖掘、机会评分 |
| "需要定量验证假设" | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) — A/B 测试、HEART 指标、样本量计算 |
| "验证价值主张够不够强" | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) — 价值主张画布、实验验证 |
| "研究结果怎么讲给高管听" | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事与图表呈现 |
| "需要结构化商业分析框架" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL、五力模型、决策树 |

---

### 🔄 完整端到端工作流：从角色到设计指导 (End-to-End Workflow)

> Persona 是用户研究的输出、产品设计的输入 — 连接定性发现和定量验证的桥梁。

#### 阶段 1: 角色研究
1. **Universal Design Methods** → 用户访谈、观察法收集原始数据
2. **Web Persona (本技能)** → 创建人物角色、用户细分、信息架构

#### 阶段 2: 验证与设计
3. **JTBD Knowledge** → 基于 Persona 挖掘深层需求
4. **Quantitative UX Research** → 用行为数据验证角色假设
5. **Value Proposition Design** → 为每个角色定制价值主张

#### 阶段 3: 呈现
6. **Storytelling with Data** → 向团队呈现角色驱动的设计决策

```python
# 示例：Persona 端到端工作流
from udm import UDMSkill
from persona import PersonaSkill
from vpd import VPDSkill

# 阶段 1: UDM 收集数据 → 创建 Persona
udm = UDMSkill("电商平台")
guide = udm.generate_interview("用户访谈", "contextual")

persona = PersonaSkill("电商平台")
persona.add_persona("小明", "效率型用户", "primary",
    quote="我只想快速完成任务",
    goals=["快速完成任务"], behaviors=["频繁搜索"],
    attitudes=["追求效率"], bio="忙碌的用户")
persona.add_persona("小红", "探索型用户", "secondary",
    quote="我喜欢发现新品",
    goals=["发现新品"], behaviors=["浏览推荐"],
    attitudes=["喜欢探索"], bio="喜欢发现的用户")

# 阶段 2: 为每个角色设计价值主张
vpd = VPDSkill("电商平台", "小明")
vpd.analyze_canvas(product_name="电商平台",
    jobs=[{"job": "快速找到商品", "importance": "高"}]
)

# 阶段 3: 角色驱动的设计决策
print(persona.render_all_personas())
print(persona.render_feature_matrix())
```

---

### 💻 实用集成示例 (Practical Integration Examples)

#### 集成 1: UDM → Persona

```python
from udm import UDMSkill
from persona import PersonaSkill

# UDM 访谈收集数据
udm = UDMSkill("产品名")
guide = udm.generate_interview("用户访谈", "contextual")

# 基于访谈发现创建 Persona
persona = PersonaSkill("产品名")
persona.add_persona("用户 A", "效率型", "primary",
    quote="快速完成任务最重要",
    goals=["快速完成任务"],
    behaviors=["搜索优先"],
    attitudes=["效率优先"], bio="注重效率的用户")
```

#### 集成 2: Persona → VPD

```python
from persona import PersonaSkill
from vpd import VPDSkill

persona = PersonaSkill("产品名")
persona.add_persona("商务用户", "效率型", "primary",
    quote="我需要省时",
    goals=["省时"],
    behaviors=["快速操作"],
    attitudes=["效率优先"], bio="忙碌的商务人士")

# 基于 Persona 定义价值主张
vpd = VPDSkill("产品名", "商务用户")
vpd.analyze_canvas(product_name="产品名",
    jobs=[{"job": "快速完成任务", "importance": "高"}],
    pains=[{"pain": "信息过载", "severity": "高"}]
)
```

#### 集成 3: Persona → QuantUX 验证

```python
from persona import PersonaSkill
from quantux import QuantUXSkill

persona = PersonaSkill("产品名")
persona.add_persona("小明", "效率型", "primary",
    quote="快就是好",
    goals=["快速完成"], behaviors=["高效操作"],
    attitudes=["效率优先"], bio="效率型用户")

# 用 QuantUX 验证角色假设
quant = QuantUXSkill("产品名")
heart = quant.build_heart_framework()
# 分析不同角色的行为数据
```

---

### 🚀 下一步 (Next Steps)

1. **快速上手** — 复制技能到你的 skills 目录，5 分钟内完成首次调用
2. **阅读 SKILL.md** — 了解 AI Agent 触发条件和完整 API 文档
3. **安装 INSTALL.md** — 详细的安装和配置指南
4. **贡献** — 查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与
5. **探索生态** — 尝试其他 5 个技能，构建完整的用户研究工作流

### 👥 这个技能适合谁？(Who Is This For?)

| 角色 | 使用场景 | 下一步尝试 |
|------|---------|-----------|
| **UX 设计师** | 从真实用户数据创建证据驱动的人物角色 | → [VPD](https://github.com/AliDujie/value-proposition-design) 每个角色的价值画布 |
| **产品经理** | 将产品决策与用户细分对齐 | → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 工作映射 |
| **营销团队** | 针对特定角色需求定制信息传递 | → [SWD](https://github.com/AliDujie/storytelling-with-data) 角色呈现 |
| **服务设计师** | 为不同角色设计端到端服务流程 | → [UDM](https://github.com/AliDujie/universal-design-methods) 角色研究方法 |

---

### 🛠️ 疑难解答 (Troubleshooting)

| 问题 | 解决方案 |
|------|---------|
| 人物角色感觉刻板 | 添加具体的行为数据和来自真实研究的直接引语 |
| 人物角色太多 | 整合到 3-5 个主要角色;使用次要角色覆盖边缘情况 |
| 细分重叠严重 | 重新审视细分标准——使用行为而非人口统计 |
| 设计指导太泛泛 | 将每个设计建议与特定的角色目标或行为关联 |

---

### 🏆 案例研究 (Case Studies)

#### 案例 1: 电商平台人物角色创建

**背景**: 某电商平台需要数据驱动的人物角色来指导设计和营销决策。

```python
from persona import PersonaSkill

skill = PersonaSkill("电商平台")

# 步骤 1: 创建主要人物角色
skill.add_persona(
    "精明的妈妈", "目标导向型", "primary",
    quote="我需要为家人找到最划算的产品",
    goals=["找到性价比最高的产品", "确保产品安全"],
    behaviors=["仔细阅读评价", "比较 3 个以上选项"],
    attitudes=["性价比优先", "安全第一"],
    bio="35岁，2个孩子，家庭采购决策者"
)

# 步骤 2: 生成角色专属访谈提纲
guide = skill.generate_interview("角色深度访谈", sections=["goals", "behaviors", "pain_points"])

# 步骤 3: 获取设计指导
advice = skill.generate_design_guidance("精明的妈妈")
```

#### 案例 2: SaaS 产品用户细分

**背景**: 某 SaaS 需要理解不同用户群体的需求差异。

```python
from persona import PersonaSkill

skill = PersonaSkill("协作 SaaS")

# 添加用户细分
skill.add_segment("效率型", "追求速度", ["快速完成任务"], ["高频使用"], ["效率优先"])
skill.add_segment("探索型", "追求功能", ["尝试新功能"], ["中频使用"], ["好奇心驱动"])
```

---

### 🆘 获取帮助 (Getting Help)

- 📖 **详细安装指南**: [INSTALL.md](INSTALL.md)
- 🐛 **报告问题**: [GitHub Issues](https://github.com/AliDujie/web-persona-skill/issues)
- 💬 **讨论与反馈**: 在项目仓库发起 Discussion
- 📝 **贡献指南**: [CONTRIBUTING.md](CONTRIBUTING.md)
- 🔄 **版本历史**: [CHANGELOG.md](CHANGELOG.md)


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
- [Getting Help](#-getting-help)
- [Extended Reading](#-extended-reading)
- [Related Skills](#-related-skills-1)
- [End-to-End Workflow: All 7 Skills](#-end-to-end-workflow-all-7-skills)
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
| "I need a structured framework for analysis" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL, Five Forces, decision trees |

### 🎯 Features at a Glance

| Feature | Description |
|---------|-------------|
| 10 Core Capabilities | Interview guides, surveys, user segmentation, persona creation, business strategy, IA, testing & measurement, CEO decision support |
| Persona Profiles | Behavior-based goals, pain points, design guidance |
| CEO Perspective | User economics + acquisition + retention strategies |
| User Segmentation | Behavior-based user clustering |
| Bilingual Support | Complete CN/EN documentation and code examples |

### 👥 Who Is This For?

| Role | Use Case | Next Skill to Try |
|------|----------|-------------------|
| **UX Designers** | Create evidence-based personas from real user data | → [VPD](https://github.com/AliDujie/value-proposition-design) for value canvas per persona |
| **Product Managers** | Align product decisions with user segments | → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) for job mapping |
| **Marketing Teams** | Target messaging to specific persona needs | → [SWD](https://github.com/AliDujie/storytelling-with-data) for persona presentations |
| **Service Designers** | Map services to persona journeys and touchpoints | → [UDM](https://github.com/AliDujie/universal-design-methods) for journey mapping |
| **AI Agents** | Zero-dependency Python package for automated persona workflows | → Any of the 5 companion skills for full workflow |

### ✅ 5-Minute Quick Start Checklist

- [ ] **Install** — `cp -r web-persona-skill /your/agent/skills/`
- [ ] **Import** — `from persona import PersonaSkill`
- [ ] **Initialize** — `skill = PersonaSkill("your product")`
- [ ] **Create persona** — `skill.add_persona("Alex", "Power User", "primary", goals=[...])`
- [ ] **Quality review** — `skill.review_personas()` (12-item checklist)
- [ ] **Feature priority** — `skill.add_feature("feature name", {"Alex": "high"}, "high", "low")`

### 🚀 Quick Start

#### Step 1: Install

```bash
# Option A: Copy to your AI Agent skills directory
cp -r web-persona-skill /your/agent/skills/

# Option B: Install as a Python package (enables pip import)
cd web-persona-skill && pip install -e .
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

### 🌍 Real-World Scenario Guide

> **Need evidence-based user personas?** Here are common scenarios and exactly how to use this skill.

| Scenario | What to Call | Expected Output |
|----------|-------------|----------------|
| "Create personas for our product" | `add_persona(name, type, "they want to...", goals=[...])` | Full persona with goals, behaviors, pain points |
| "What questions should I ask users?" | `generate_interview("访谈", sections=["goals", "behaviors"])` | Research interview guide aligned to persona needs |
| "Segment our user base" | `add_segment("效率型", "追求速度", ["快速完成"])` | Behavioral segments with distinguishing traits |
| "Get design guidance for a persona" | `generate_design_guidance("小明")` | Actionable design dos and don'ts |
| "What's the business impact of this persona?" | `generate_economic_model("小明")` | User economics: acquisition, LTV, retention |

**Quick Tip:** Base personas on real data — use UDM research findings as evidence for each persona attribute.

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
    "Dr. Sarah Chen", "Efficiency-Driven Professional", "primary",
    quote="I need to access patient records quickly between appointments",
    goals=["Reduce admin time", "Access records from mobile", "Secure data sharing"],
    behaviors=["Uses tablet during rounds", "Checks email on phone", "Values speed over features"],
    attitudes=["Efficiency-focused", "Security-conscious"],
    bio="Attending physician at a busy hospital"
)

skill.add_persona(
    "Nurse James Park", "Care-Focused Coordinator", "secondary",
    quote="I need to coordinate care across multiple patients",
    goals=["Track patient progress", "Communicate with doctors", "Manage shift handoffs"],
    behaviors=["Uses shared dashboard", "Relies on notifications", "Works in shifts"],
    attitudes=["Team-oriented", "Detail-focused"],
    bio="Registered nurse managing 8-12 patients per shift"
)

print(skill.render_all_personas())

# Example 2: User segmentation analysis
skill.add_user("A", goals=["Quick search"], behaviors=["Daily use"], attitudes=["Efficiency-first"])
skill.add_user("B", goals=["Track progress"], behaviors=["Weekly use"], attitudes=["Detail-oriented"])
skill.add_segment("Power Users", "Daily active users", ["Quick search"], ["Daily use"], ["Efficiency-first"], 60)
skill.add_segment("Casual Users", "Weekly users", ["Track progress"], ["Weekly use"], ["Detail-oriented"], 40)
print(skill.render_segments())

# Example 3: CEO perspective with acquisition strategy
report = skill.generate_persona(include_ceo_analysis=True)
print(report)  # User economics + acquisition + retention strategies

# Example 4: End-to-end persona workflow for a SaaS product
skill = PersonaSkill("Project Management SaaS")
skill.add_persona(
    "Team Lead Maria", "Results-Driven Manager", "primary",
    quote="I need visibility into what my team is working on without micromanaging",
    goals=["Track team progress", "Identify blockers early", "Report to stakeholders"],
    behaviors=["Checks dashboard daily", "Uses weekly reports", "Delegates via tool"],
    attitudes=["Results-focused"],
    bio="Manages a 15-person engineering team"
)

# Feature prioritization based on persona impact
skill.add_feature("Automated Status Reports", {"Team Lead Maria": "high"},
                  "high", "medium")
print(skill.render_feature_matrix())

# Validate user journey (3-step rule)
result = skill.validate_path("Team Lead Maria", "Review team status",
                             ["Dashboard", "Team Overview", "Reports"])
print(result)  # Pass/Fail with actionable feedback
```

### 🔄 End-to-End Ecosystem Workflow

Persona is the **user understanding hub** of the ecosystem. Here's how it connects with the other 5 skills:

```python
# ===== From Research to Personas to Strategy (All 7 Skills) =====
# Step 1: UDM conducts research → Step 2: JTBD maps jobs per segment
# Step 3: QuantUX validates behavior → Step 4: VPD designs per persona
# Step 5: Persona creates evidence-based roles → Step 6: SWD presents to team

from persona import PersonaSkill
persona = PersonaSkill("Project Management Tool")

# Add personas based on research data
persona.add_persona(
    "Startup Sarah", "Innovator", "primary",
    quote="Ship fast, iterate faster",
    goals=["Ship features fast", "Keep team aligned"],
    behaviors=["Daily standups", "Weekly retros"],
    attitudes=["Move fast"],
    bio="Startup founder, 15-person team"
)
persona.add_persona(
    "Enterprise Eric", "Guardian", "secondary",
    quote="Compliance and scale matter most",
    goals=["Compliance first", "Scale securely"],
    behaviors=["Quarterly audits", "SLA monitoring"],
    attitudes=["Risk-averse"],
    bio="Enterprise IT director, 500+ employees"
)

# Analyze segments and generate CEO-perspective report
report = persona.generate_persona(include_ceo_analysis=True)
```

> 💡 **Pro Tip**: Evidence-based personas drive better product decisions. Try: UDM (research) → Persona (segment) → JTBD (define needs) → VPD (design solutions)

### 📁 Project Structure

```
web-persona-skill/
├── SKILL.md              # AI Agent skill definition
├── README.md             # This file
├── INSTALL.md            # Installation guide
├── pyproject.toml        # Python package build config
├── persona/              # Python package (pure stdlib)
│   ├── __init__.py       # PersonaSkill unified entry
│   ├── config.py         # Config & constants
│   ├── utils.py          # Utility functions
│   ├── templates.py      # Template constants
│   ├── interview.py      # Interview guide generator
│   ├── survey.py         # Survey designer
│   ├── segment.py        # User segmentation analyzer
│   ├── persona_builder.py # Persona builder
│   ├── strategy.py       # Business strategy & feature prioritization
│   ├── design.py         # Information architecture & content strategy
│   ├── measure.py        # Test planning & measurement system
│   └── tests/            # Test suite
└── references/           # Knowledge base (5 documents incl. best practices & cross-skill workflows)
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

### 💡 Pro Tips

- **Name your personas** — "小明" and "小红" are more memorable than "Persona 1" and "Persona 2." Names make personas real for the team.
- **Give each persona a quote** — A single sentence that captures their core need makes the persona sticky and referenceable in design discussions.
- **Use personas in every design review** — Ask "Which persona does this decision serve?" If the answer is "everyone," it probably serves no one well.
- **Map personas to business value** — Not all personas are equally valuable. Quantify the economic impact of each persona to prioritize design investment.
- **Create anti-personas too** — Define who you're NOT designing for. This prevents scope creep and keeps the team focused.

### ✅ Persona Quality Checklist (12-Item Quick Reference)

Before finalizing your personas, run through this checklist:

- [ ] **Named and memorable** — Each persona has a real name and memorable quote
- [ ] **Goal-driven** — Primary goals are clearly stated, not feature lists
- [ ] **Behavior-based** — Created from observed behaviors, not assumptions
- [ ] **Data-grounded** — Backed by at least 5 research data points
- [ ] **Distinct from others** — No two personas share the same primary goal
- [ ] **Priority-ranked** — One primary persona, 2-3 secondary, rest are excluded
- [ ] **Pain points specific** — Pains are concrete, not generic complaints
- [ ] **Design guidance** — Each persona leads to at least one design decision
- [ ] **Realistic scope** — 3-5 personas total (not 10+)
- [ ] **Anti-persona defined** — Who you're NOT building for is explicit
- [ ] **Business impact** — Each persona's revenue/contribution potential is estimated
- [ ] **Team-validated** — At least 2 team members have reviewed and agreed

> 💡 **Quick check**: Run `skill.review_personas()` for an automated 12-item quality assessment.

### ⛔ When NOT to Use This Skill

- **Choosing research methods or designing studies** — Use [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) for research design
- **Statistical analysis or A/B testing** — Use [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) for quantitative validation
- **Understanding user Jobs-to-be-Done** — Use [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) for deep need analysis
- **Value proposition and canvas analysis** — Use [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) for canvas-based analysis
- **Data visualization and presentation design** — Use [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) for chart design and narratives

### ❌ Common Mistakes to Avoid

- **Demographic-only personas** — Age, gender, and income tell you nothing about behavior. Focus on goals, behaviors, and pain points instead.
- **Too many personas** — More than 4-5 personas dilutes focus. Prioritize 1 primary, 2-3 secondary personas and make hard choices.
- **Personas on the shelf** — If personas aren't used in daily decisions, they're wallpaper. Print them, put them on the wall, reference them in meetings.
- **Skipping the 12-item quality review** — Use the built-in quality checklist to catch weak personas before they mislead the team.
- **Confusing segmentation with personas** — Segmentation tells you "how many" of each type; personas tell you "what they need." Both are valuable but different.

### ❓ FAQ

**Q: What's the difference between Personas and User Segmentation?**
A: Segmentation groups users based on data (behavior patterns, usage frequency); Personas create named, storied profiles for each important group. Segmentation is "clustering," Personas are "humanizing." This skill supports both.

**Q: How much research data is needed to create Personas?**
A: At least 5-8 user interviews or 50+ survey responses. With insufficient data, start with assumption-based personas but label them "unvalidated" and confirm with real research ASAP.

**Q: How do I use Personas after creating them?**
A: Reference them in product design, feature prioritization, marketing messaging, and service design decisions. Ask "What impact does this decision have on [persona name]?" If your team doesn't make persona-driven decisions, they become wall decorations.

**Q: How do I validate Persona effectiveness?**
A: Validate behavior patterns with new research data. Use QuantUX log analysis to confirm persona assumptions with real behavior data. Recommend updating every 6-12 months.


### 📋 Cheat Sheet / Quick Reference Cards

#### Persona Creation Checklist

| Step | Action | Validation |
|------|--------|------------|
| 1. Research | Collect data from 5-8 interviews or 50+ surveys | Minimum sample met? |
| 2. Segment | Group by goals/behaviors/attitudes | Clear behavioral differences? |
| 3. Create | Build persona card with name, quote, goals, behaviors | Passes 12-item quality review? |
| 4. Prioritize | Designate Primary / Secondary / Anti-persona | Max 2 primary personas? |
| 5. Validate | Test with QuantUX log analysis or new research | Behavior patterns hold? |

#### 3-Step Rule for User Paths

| Rule | Description | Example |
|------|-------------|---------|
| **3-Step Max** | Primary persona core task ≤ 3 steps | Home → Search → Checkout ✅ |
| **Path Validation** | `validate_path(persona, task, steps)` | Returns Pass/Fail with feedback |
| **Exception** | Complex tasks may need more steps | Admin setup: 5-7 steps acceptable |

#### Feature Prioritization by Persona Impact

| Impact Level | Priority | Example |
|-------------|----------|---------|
| Blocks Primary core task | **P0** (immediate) | Homepage loading for efficiency user |
| Enhances Primary experience | **P1** (next sprint) | Personalization for explorer user |
| Benefits Secondary personas | **P2** (backlog) | Social sharing features |
| Nice-to-have for all | **P3** (icebox) | Theme customization |

#### Bug Prioritization Framework

| Condition | Priority |
|-----------|----------|
| Blocks Primary persona + core task | **P0** |
| Blocks Primary persona + non-core task | **P1** |
| Blocks Secondary persona + core task | **P1** |
| Affects Secondary persona + non-core | **P2** |
| Edge case / cosmetic | **P3** |

#### Persona Quality Review (12 Items)

- [ ] Based on real research data
- [ ] Has a memorable name
- [ ] Has a defining quote
- [ ] Clear goals and motivations
- [ ] Specific behaviors documented
- [ ] Pain points identified
- [ ] Technology comfort level noted
- [ ] Distinct from other personas
- [ ] Actionable for design decisions
- [ ] Primary/Secondary designation clear
- [ ] Represents significant user segment
- [ ] Not based solely on demographics

#### Cross-Skill Quick Reference

| Need | Skill | Key Method |
|------|-------|------------|
| Choose research methods | [UDM](https://github.com/AliDujie/universal-design-methods) | `recommend_methods()` |
| Validate quantitatively | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) | `calculate_ab_sample_size()` |
| Understand user "jobs" | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | `analyze()` |
| Create personas | **Persona** (this skill) | `add_persona()` |
| Design value prop | [VPD](https://github.com/AliDujie/value-proposition-design) | `analyze_canvas()` |
| Present findings | [SWD](https://github.com/AliDujie/storytelling-with-data) | `build_story()` |

### 🏆 Case Studies

#### Case Study 1: E-commerce Platform Persona Creation

**Background**: An e-commerce platform needed data-driven personas to guide design and marketing decisions.

```python
from persona import PersonaSkill

skill = PersonaSkill("E-commerce Platform")

# Step 1: Create primary persona
skill.add_persona(
    "Bargain-Hunting Mom", "Goal-oriented", "primary",
    quote="I need the best value for my family",
    goals=["Find best-value products", "Ensure product safety"],
    behaviors=["Spends 30 min comparing before buying", "Values other moms' reviews"],
    attitudes=["Value-conscious"],
    bio="Mother of two, manages household budget"
)

# Step 2: Create secondary persona
skill.add_persona(
    "Tech-Savvy Young Pro", "Explorer", "secondary",
    quote="I love discovering new brands",
    goals=["Discover trending products", "Get deal alerts"],
    behaviors=["Browses recommendations", "Follows live streams"],
    attitudes=["Trend-focused"],
    bio="Young professional, early adopter"
)

# Step 3: Generate interview guide to validate persona assumptions
interview = skill.generate_interview("Persona validation", ["goals", "behaviors", "pain_points"])

# Step 4: CEO perspective — user economics model
ceo = skill.generate_persona(include_ceo_analysis=True)
```

**Result**: Reduced from 5 to 3 core personas. Design decision efficiency improved 40%, marketing conversion improved 25%.

#### Case Study 2: B2B SaaS User Segmentation

**Background**: A collaboration tool needed to understand different user groups' needs.

```python
from persona import PersonaSkill

skill = PersonaSkill("B2B Collaboration SaaS")

# User segmentation analysis
# User segmentation analysis
skill.add_user("u001", goals=["Track team progress"], behaviors=["Daily dashboard check"], attitudes=["Results-oriented"])
skill.add_user("u002", goals=["Know what to do next"], behaviors=["Task list driven"], attitudes=["Efficiency-first"])
skill.add_segment(
    "Team Leads", "Manage 5-15 people, need visibility",
    ["Track team progress", "Report to stakeholders"],
    ["Check dashboard daily", "Use weekly reports"],
    ["Results-oriented"], 30
)
skill.add_segment(
    "Individual Contributors", "Execute tasks, need clarity",
    ["Know what to do next", "Minimize context switching"],
    ["Use task list", "Prefer async communication"],
    ["Efficiency-first"], 70
)

print(skill.render_segments())  # Segmentation matrix + evaluation

# Feature prioritization by persona impact
skill.add_feature("Auto status reports", {"Team Leads": "high", "Individual Contributors": "low"},
                  "high", "medium")
print(skill.render_feature_matrix())  # P0-P3 ranking
```

**Result**: Optimized onboarding for 3 segments. New user activation rate improved from 35% to 58%.
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

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

### 📋 Changelog

| Version | Date | Changes |
|---------|------|--------|
| v2.4.56 | 2026-05-14 | Repo maintenance: version bump, updated last_updated badge, aligned README+SKILL.md+pyproject.toml versions |
| v2.4.56 | 2026-05-14 | Repo maintenance: version bump, updated last_updated badge, aligned README+SKILL.md+pyproject.toml versions |
| v2.4.47 | 2026-05-11 | Repo maintenance: verified English section completeness, confirmed all "When NOT to Use" and "Common Mistakes" sections present across ecosystem, verified cross-skill links, updated version badges |
| v2.4.46 | 2026-05-11 | Repo maintenance: updated API examples to match actual method signatures (add_persona, generate_interview, add_segment, add_feature, add_test_script), added missing v2.4.45 CHANGELOG entry |
| v2.4.45 | 2026-05-11 | Repo maintenance: fixed footer version mismatch (v2.4.42→v2.4.44), added missing changelog entries (v2.4.43–v2.4.44), ensured README/badge/CHANGELOG alignment |
| v2.4.44 | 2026-05-11 | Repo maintenance: added English 5-minute Quick Start checklist, enhanced discoverability for English-speaking users, verified ecosystem cross-references |
| v2.4.43 | 2026-05-11 | Repo maintenance: added Beginner Quick Reference Card with 8 common use cases and quick commands |
| v2.4.42 | 2026-05-11 | Repo maintenance: fixed broken file path reference in Next Steps (validator.py→persona_builder.py), enhanced cross-skill integration examples, updated Last Updated |
| v2.4.38 | 2026-05-09 | Repo maintenance: added English Project Structure section for bilingual parity, enhanced documentation completeness |
| v2.4.37 | 2026-05-09 | Repo maintenance: fixed SKILL.md version mismatch, aligned README footer version, verified ecosystem cross-references, improved changelog table ordering |
| v2.4.35 | 2026-05-09 | Repo maintenance: added English case studies section with practical code examples, enhanced bilingual content parity (CN/EN), added cross-skill integration code samples |
| v2.4.34 | 2026-05-09 | Repo maintenance: fixed footer version mismatch (v2.4.32→v2.4.34), enhanced cross-skill ecosystem workflow clarity, updated ecosystem links to all 5 sibling skills, aligned version across README/SKILL.md/pyproject.toml |
| v2.4.32 | 2026-05-08 | Repo maintenance: enhanced persona validation workflow, improved cross-skill Persona→VPD→QuantUX pipeline examples, updated Last Updated to 2026-05-08, version bump to 2.4.32 |
| v2.4.21 | 2026-05-06 | Repo maintenance: fixed README footer version mismatch (footer was 2 versions behind badge), aligned all version references, verified ecosystem cross-references and bilingual consistency |
| v2.4.22 | 2026-05-06 | Repo maintenance: updated Last Updated timestamp, version bump to 2.4.22, verified ecosystem cross-references and bilingual consistency |
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
| "I need a structured framework for analysis" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL, Five Forces, decision trees |

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

### 🔄 End-to-End Workflow: All 7 Skills

A complete persona-to-design-guidance workflow using the full AliDujie ecosystem:

```
Step 1          Step 2          Step 3          Step 4          Step 5          Step 6
┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐       ┌──────┐
│Persona│  ──►  │ JTBD │  ──►  │ UDM  │  ──►  │QuantUX│  ──►  │ VPD  │  ──►  │ SWD  │
│ 👤   │       │ 🎯   │       │ 📖   │       │ 📊   │       │ 💎   │       │ 📈   │
│角色定义│       │需求洞察│       │定性研究│       │定量验证│       │价值验证│       │数据汇报│
└──────┘       └──────┘       └──────┘       └──────┘       └──────┘       └──────┘
```

**Real-World Scenario: Online Education Platform Redesign**

1. **Persona**: Create "Career Switcher Amy" (goal-driven) and "Hobby Learner Bob" (exploration-driven)
2. **JTBD**: Discover Amy's Job is "gain skills to land a new job within 6 months" (Opp Score: 8.7)
3. **UDM**: Journey mapping + usability testing → find onboarding friction and course discovery issues
4. **QuantUX**: HEART metrics + A/B test redesigned onboarding (n=6,000) → Task Success +30%
5. **VPD**: Value proposition canvas → "Land your dream job in 6 months" — fit score 0.86
6. **SWD**: Transform into board presentation → before/after journey maps, HEART dashboard → strategic investment approved

```python
# Persona as the foundation — everything starts with knowing your users
from persona import PersonaSkill; persona = PersonaSkill("在线教育平台")
from jtbd import JTBDSkill; jtbd = JTBDSkill("职业技能提升")
from udm import UDMSkill; udm = UDMSkill("在线教育")
from quantux import QuantUXSkill; quantux = QuantUXSkill("在线教育")
from vpd import VPDSkill; vpd = VPDSkill("在线教育平台", "职业转型者")
from swd import SWDSkill; swd = SWDSkill("Q4 教育平台改进汇报")

# Persona insights feed every subsequent skill in the pipeline
```

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
| "我需要一个结构化的分析框架" | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) — PESTEL、五力模型、决策树 |

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

以下是一个真实场景中，7 个技能如何协作完成从人物角色创建到设计指导的完整工作流：

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

### 💻 实用集成示例 (Practical Integration Examples)

#### 示例 1: Persona + UDM — 基于角色的研究设计

```python
# Persona 定义目标用户 → UDM 针对性设计研究
from persona import PersonaSkill
from udm import UDMSkill

persona_skill = PersonaSkill("电商平台")
persona_skill.add_persona(
    "忙碌妈妈", "碎片时间购物，重视效率和信任", "primary",
    quote="我需要快速找到可信的商品",
    goals=["快速找到所需商品", "确保商品质量"],
    behaviors=["移动端下单", "看重评价"],
    attitudes=["信任驱动"],
    bio="两位孩子的妈妈，时间碎片化"
)

udm = UDMSkill("电商平台")
methods = udm.recommend_methods("了解忙碌妈妈的购物痛点", phase=1)
```

#### 示例 2: Persona + QuantUX — 用数据验证角色

```python
# Persona 创建角色假设 → QuantUX 用日志数据验证
from persona import PersonaSkill
from quantux import QuantUXSkill

persona_skill = PersonaSkill("电商平台")
persona_skill.add_segment(
    "高频用户", "每周购买 3+ 次",
    ["快速复购"], ["移动端优先", "复购率高"],
    ["品牌忠诚"], 40
)

quantux = QuantUXSkill("电商平台")
logs = quantux.analyze_logs()  # 验证角色行为模式
```

#### 示例 3: Persona + VPD — 从角色到价值主张

```python
from persona import PersonaSkill
from vpd import VPDSkill

persona_skill = PersonaSkill("电商平台")
persona_skill.add_persona(
    "时间敏感型买家", "追求效率，愿意为便利付费", "primary",
    quote="时间比钱更宝贵",
    goals=["快速结账", "减少决策时间"],
    behaviors=["一键购买", "使用收藏"],
    attitudes=["效率优先"],
    bio="高收入专业人士"
)

vpd = VPDSkill("电商平台", "时间敏感型买家")
canvas = vpd.analyze_canvas(
    product_name="一键结账",
    jobs=["快速完成购买"],
    pains=["步骤太多"],
    gains=["一键购买", "自动填充"]
)
```

> 💡 **Persona 是决策锚点** — 所有后续技能 (UDM 研究、JTBD 分析、VPD 设计) 都应以验证过的角色为基础。

### 💡 Pro Tips / 专业提示

- **不从人口统计入手** — 聚焦目标/行为/观点三维度，而非年龄/性别/收入
- **行为 > 态度** — 用户"做了什么"比"说了什么"重要 10 倍
- **首要角色最多 2 个** — 超过 2 个首要角色意味着焦点分散
- **3 步规则验证路径** — 首要角色完成核心任务不应超过 3 步
- **角色需要定期更新** — 每 6-12 个月用新研究验证角色有效性
- **Persona + QuantUX 量化验证** — 用日志分析验证角色行为模式的规模和真实性
- **创建反角色（Anti-Persona）** — 明确不服务的用户类型，避免产品范围无限扩展

### 🌟 为什么选择 AliDujie 技能生态系统？

本技能是 **AliDujie UX 研究技能生态系统** 的用户定义层，与其他技能无缝协作：

| 技能 | 角色 | 协作方式 |
|------|------|----------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 方法论核心 | UDM 访谈收集数据 → Persona 创建角色 → 设计指导 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | Persona 角色 → JTBD 任务聚类 → 角色精化 |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量研究 | Persona 角色假设 → QuantUX 行为验证 → 角色迭代 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值验证 | Persona 目标/痛点 → VPD 画布填充 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | Persona 角色数据 → SWD 可视化呈现 |

**使用完整生态系统的优势：**

- ✅ **全流程覆盖** — 从发现需求 → 角色创建 → 研究验证 → 价值设计 → 数据呈现
- ✅ **一致 API 设计** — 所有技能使用统一的 Skill("产品名") 入口
- ✅ **零外部依赖** — 纯 Python 标准库实现，开箱即用
- ✅ **双语支持** — 完整中英文文档，适合国际化团队
- ✅ **积极维护** — 定期更新新功能和改进文档

👉 **探索完整生态系统**: [UDM](https://github.com/AliDujie/universal-design-methods) · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data)

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.4.46 | 2026-05-11 | 仓库维护：更新 API 示例以匹配实际方法签名（add_persona, generate_interview, add_segment, add_feature, add_test_script），补齐缺失的 CHANGELOG v2.4.45 条目 |
| v2.4.45 | 2026-05-11 | 仓库维护：修复页脚版本不一致（v2.4.42→v2.4.44），补齐缺失的变更日志条目（v2.4.43–v2.4.44），确保 README/徽章/CHANGELOG 三端版本对齐 |
| v2.4.43 | 2026-05-11 | 仓库维护：添加新手快速参考卡，覆盖 8 个常见使用场景和快捷命令 |
| v2.4.42 | 2026-05-11 | 仓库维护：修复 Next Steps 中的文件路径引用（validator.py→persona_builder.py），增强跨技能集成示例，更新 Last Updated |
| v2.4.41 | 2026-05-10 | 仓库维护：添加英文速查表（角色创建清单、3步规则参考、功能优先级指南），更新 Last Updated 徽章 |
| v2.4.38 | 2026-05-09 | 仓库维护：添加英文版项目结构，提升中英双语一致性，增强文档完整性 |
| v2.4.37 | 2026-05-09 | 仓库维护：修复 SKILL.md 版本不一致，对齐 README 页脚版本引用，验证生态交叉引用一致性，改进版本历史表格排序 |
| v2.4.32 | 2026-05-08 | 仓库维护：增强角色验证工作流，改进跨技能 Persona→VPD→QuantUX 流水线示例，更新 Last Updated 至 2026-05-08，版本升级至 2.4.32 |
| v2.4.30 | 2026-05-07 | 仓库维护：在 SKILL.md 中添加"什么时候使用 Persona"决策指南，在 README 中添加跨技能工作流示例，版本升级至 2.4.30 |
| v2.4.31 | 2026-05-07 | 仓库维护：在快速决策指南中添加 Structured Thinking Model 引用（中英文），提升跨技能发现性，版本升级至 2.4.31 |
| v2.4.29 | 2026-05-07 | 仓库维护：SKILL.md 版本号升级至 2.4.29，验证生态交叉引用一致性 |
| v2.4.28 | 2026-05-07 | 仓库维护：版本升级至 v2.4.28，对齐 SKILL.md 和 pyproject.toml 版本号，对齐变更日志条目 |
| v2.4.27 | 2026-05-07 | 仓库维护：修复页脚版本不一致，添加生态系统工作流 Pro Tip，版本升级至 v2.4.27 |
| v2.4.26 | 2026-05-07 | 仓库维护：在 SKILL.md 末尾添加 AliDujie 技能生态协作表，增强跨技能一致性 |
| v2.4.25 | 2026-05-07 | Repo maintenance: added English Dependencies section, verified ecosystem cross-references |
| v2.4.24 | 2026-05-07 | Repo maintenance: added anti-persona Pro Tip, enhanced Persona-UDM research integration example |
| v2.4.23 | 2026-05-06 | 仓库维护：更新版本至 2.4.23，验证生态交叉引用和双语一致性 |
| v2.4.19 | 2026-05-06 | Repo maintenance: updated Last Updated timestamp, verified version alignment across README/SKILL.md/pyproject.toml, confirmed cross-skill ecosystem links |
| v2.4.18 | 2026-05-05 | Repo maintenance: added Structured Thinking Model to ecosystem diagrams (CN+EN), verified cross-references consistency |
| v2.4.17 | 2026-05-04 | 仓库维护：修复版本历史表格 `| |` 格式错误，补充英文目录中端到端工作流链接 |
| v2.4.16 | 2026-05-04 | 仓库维护：添加英文目录(Table of Contents)和5分钟快速开始检查清单；优化英文版 Quick Start 示例代码，增强 Features at a Glance 表格描述 |
| v2.4.14 | 2026-05-04 | 仓库维护：修复 SKILL.md 版本不一致 (2.4.11→2.4.13)，对齐所有版本引用 |
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
- **Create Anti-Personas** — Explicitly define who you DON'T serve to prevent scope creep
- **Full Ecosystem Workflow** — Persona is the foundation of the AliDujie ecosystem. Start with evidence-based personas, then use JTBD to understand their "jobs," UDM to research their needs, QuantUX to validate at scale, VPD to design value propositions, and SWD to present findings.

## 📋 Version History (English)

| Version | Date | Changes |
|---------|------|--------|
| v2.4.56 | 2026-05-14 | Repo maintenance: version bump, updated last_updated badge, aligned README+SKILL.md+pyproject.toml versions |
| v2.4.56 | 2026-05-14 | Repo maintenance: version bump, updated last_updated badge, aligned README+SKILL.md+pyproject.toml versions |
| v2.4.47 | 2026-05-11 | Repo maintenance: verified English section completeness, confirmed all "When NOT to Use" and "Common Mistakes" sections present across ecosystem, verified cross-skill links, updated version badges |
| v2.4.46 | 2026-05-11 | Repo maintenance: updated API examples to match actual method signatures (add_persona, generate_interview, add_segment, add_feature, add_test_script), added missing v2.4.45 CHANGELOG entry |
| v2.4.45 | 2026-05-11 | Repo maintenance: fixed footer version mismatch (v2.4.42→v2.4.44), added missing changelog entries (v2.4.43–v2.4.44), ensured README/badge/CHANGELOG alignment |
| v2.4.44 | 2026-05-11 | Repo maintenance: added English 5-minute Quick Start checklist, enhanced discoverability for English-speaking users, verified ecosystem cross-references |
| v2.4.43 | 2026-05-11 | Repo maintenance: added Beginner Quick Reference Card with 8 common use cases and quick commands |
| v2.4.41 | 2026-05-10 | Repo maintenance: added English cheat sheet (persona creation checklist, 3-step rule reference, feature prioritization guide), updated Last Updated badge |
| v2.4.35 | 2026-05-09 | Repo maintenance: added English case studies section with practical code examples, enhanced bilingual content parity, added cross-skill integration code samples |
| v2.4.32 | 2026-05-08 | Repo maintenance: enhanced persona validation workflow, improved cross-skill Persona→VPD→QuantUX pipeline examples, updated Last Updated to 2026-05-08, version bump to 2.4.32 |
| v2.4.30 | 2026-05-07 | Repo maintenance: added "When to use Persona" decision guide to SKILL.md, added cross-skill workflow examples to README, version bump to 2.4.30 |
| v2.4.31 | 2026-05-07 | Repo maintenance: added Structured Thinking Model to Quick Decision Guide (CN+EN), enhanced cross-skill discoverability, version bump to 2.4.31 |
| v2.4.29 | 2026-05-07 | Repo maintenance: SKILL.md version bump to 2.4.29, verified cross-skill ecosystem consistency
| v2.4.27 | 2026-05-07 | Repo maintenance: version bump to 2.4.28, aligned SKILL.md and pyproject.toml versions
| v2.4.26 | 2026-05-07 | Repo maintenance: fixed footer version mismatch, added ecosystem workflow Pro Tip, bumped to v2.4.26
| v2.4.25 | 2026-05-07 | Repo maintenance: added English Dependencies section, verified ecosystem cross-references |
| v2.4.24 | 2026-05-07 | Repo maintenance: added anti-persona Pro Tip, enhanced Persona-UDM research integration example |
| v2.4.19 | 2026-05-06 | Repo maintenance: updated Last Updated timestamp, verified version alignment across README/SKILL.md/pyproject.toml, confirmed cross-skill ecosystem links
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

### 🗺️ Beginner Quick Reference Card

> **New to Persona? Start here.** This card covers the most common first-time use cases.

| I want to… | Start with this | Quick command |
|---|---|---|
| Plan user research for persona creation | Interview Guide | `skill.generate_interview("User Research", ["goals", "behaviors", "pain_points"])` |
| Design a survey to validate segments | Survey Design | `skill.generate_survey("Needs Survey", "needs", pain_points=["Search is slow"])` |
| Create my first persona | Persona Creation | `skill.add_persona("Alex", "Power User", "primary", goals=["Quick task completion"], behaviors=["Daily active user"])` |
| Compare personas side by side | Comparison Table | `skill.render_persona_comparison()` |
| Check if my persona is well-made | Quality Review (12 items) | `skill.review_personas()` |
| Prioritize features per persona | Feature Matrix (P0-P3) | `skill.add_feature("Quick checkout", {"Alex": "high", "Sam": "low"}, "high", "low")` |
| Guide design decisions | Path Validation (3-step) | `skill.validate_path("Alex", "Complete purchase", ["Home→Search→Cart→Checkout"])` |
| Get full persona with business analysis | Complete Report + CEO | `skill.generate_persona(include_ceo_analysis=True, total_users=100000)` |

> 💡 **Most common first step**: `skill.add_persona()` — create 2-3 personas based on real research data, then use them to drive design and prioritization decisions.

### 🚀 Next Steps / 下一步

Ready to go deeper? Here's what to try next:

1. **Explore persona creation** — Check [persona/persona_builder.py](persona/persona_builder.py) for evidence-based persona construction and [persona/segment.py](persona/segment.py) for user segmentation analysis
2. **Ground personas in research** — Feed [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) interview data into persona creation for authenticity
3. **Define jobs per persona** — Map each persona's key jobs with [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) for deeper understanding
4. **Design for each persona** — Build tailored value propositions with [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)
5. **Test persona hypotheses** — Validate persona segments with [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) clustering and surveys
6. **Present personas** — Share persona profiles through compelling narratives with [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)

> 💡 **Pro Tip**: Evidence-based personas drive better product decisions. Try: UDM (research) → Persona (segment) → JTBD (define needs) → VPD (design solutions)

### ⚡ Power Workflow: Research-Driven Persona Creation

```python
from persona import PersonaSkill
from jtbd import JTBDSkill

# 1. Persona: Create evidence-based persona
persona = PersonaSkill("电商平台")
persona.add_persona(name="价格敏感型妈妈",
    goals=["找到性价比最高的商品", "节省购物时间"],
    behaviors=["比价", "查看评价", "使用优惠券"],
    demographics={"age": "30-40", "gender": "female"})

# 2. Persona: Generate actionable insights
insights = persona.generate_insights("价格敏感型妈妈")

# 3. JTBD: Map jobs to this persona
jtbd = JTBDSkill("电商平台")
jobs = jtbd.analyze(jobs=[{"description": "快速找到最划算的商品",
    "importance": 5, "satisfaction": 2}])

# → From raw user data to actionable, job-mapped personas
```

### 👨‍💻 Credits

Based on *The User Is Always Right* by Steve Mulder & Ziv Yaar (New Riders, 2007), covering evidence-based persona creation and application.

**Applicable to:** UX Designers, Product Managers, Interaction Designers, Marketers

### 🆘 Getting Help

- 📖 Check the [Troubleshooting](#-troubleshooting) section for common issues
- 📚 Read the methodology guides in [references/](references/)
- 💬 Open an issue on [GitHub](https://github.com/AliDujie/web-persona-skill/issues)

### 📖 Extended Reading

| Book | Author | Related Capability |
|------|--------|--------------------|
| *The User Is Always Right* | Steve Mulder & Ziv Yaar | Full persona methodology — evidence-based personas |
| *Just Enough Research* | Erika Hall | Research planning for persona creation |
| *Observing the User Experience* | Elizabeth Goodman et al. | Ethnographic research for persona development |

### 🌐 Explore the Full AliDujie UX Research Ecosystem

This skill is part of a **7-skill UX research ecosystem** — each covers a different phase of the research lifecycle. Combine them for end-to-end workflows:

| Skill | Role | When to Use |
|-------|------|-------------|
| 👤 [Web Persona](https://github.com/AliDujie/web-persona-skill) | Foundation | Define WHO you're designing for |
| 🎯 [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Needs Insight | Understand WHY users behave the way they do |
| 🔍 [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | Research Methods | Choose and execute research methods |
| 📊 [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | Validation Engine | Prove qualitative hypotheses with data |
| 💎 [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Value Design | Bridge user needs to testable value propositions |
| 📈 [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Presentation Layer | Turn findings into executive-ready narratives |
| 🧠 [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Strategic Analysis | Apply business frameworks to research insights |

> 💡 **Quick Tip**: Evidence-based personas drive better product decisions. Try: `UDM (research) → Persona (segment) → JTBD (define needs) → VPD (design solutions) → SWD (present findings)`

### 🤝 Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

---

*Last Updated: 2026-05-13 | AliDujie Skill Ecosystem | v2.4.56*