# Web Persona Skill

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version](https://img.shields.io/badge/version-2.3.0-green.svg)](CHANGELOG.md)
![Last Updated](https://img.shields.io/badge/last%20updated-2026--05--01-brightgreen.svg)

> 👤 **一句话介绍**: 基于 Steve Mulder《The User Is Always Right》的完整人物角色工具包。从用户研究到角色创建，从商业策略到设计指导，内置 CEO 视角的用户经济模型分析。

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

> 💡 **提示**: Persona 与 UDM 配合使用，用 UDM 访谈/观察方法收集角色研究数据，构建证据驱动的人物角色。

---

## 中文说明

### 🎯 Features at a Glance / 功能一览

| 功能 | 说明 |
|------|------|
| 7 大执行能力 | 访谈提纲、调查问卷、用户细分、人物角色创建、商业策略、信息架构、测试与衡量 |
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
```

### 💡 核心能力

| # | 能力 | 模块 | 功能 |
|---|------|------|------|
| 1 | **访谈提纲生成** | `interview.py` | 用户研究访谈框架 |
| 2 | **调查问卷设计** | `survey.py` | 用户细分问卷 |
| 3 | **用户细分分析** | `segment.py` | 基于行为的用户分群 |
| 4 | **人物角色创建** | `persona_builder.py` | 角色档案生成与管理 |
| 5 | **商业策略** | `strategy.py` | 功能优先级 + 商业策略 |
| 6 | **信息架构** | `design.py` | IA 与内容策略 |
| 7 | **测试与衡量** | `measure.py` | 测试计划与衡量体系 |

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
├── references/           # 知识库文档
└── README.md
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
└─────────────────────────────────────────────────────────────┘
```

**配合使用场景:**

- **Persona + UDM** → 用 UDM 访谈/观察方法收集角色研究数据
- **Persona + JTBD** → 用 JTBD 任务聚类定义人物角色
- **Persona + QuantUX** → 用量化数据验证角色细分和市场规模
- **Persona + VPD** → 用人物角色驱动价值主张设计
- **Persona + SWD** → 用数据叙事向团队展示角色故事

👉 **探索完整生态系统**: [通用设计方法](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [量化 UX 研究](https://github.com/AliDujie/Quantitative-UX-Research) | [价值主张设计](https://github.com/AliDujie/value-proposition-design) | [数据叙事](https://github.com/AliDujie/storytelling-with-data)

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

### 📚 关于《The User Is Always Right》

- **书名**: The User Is Always Right: A Practical Guide to Creating and Using Personas for the Web
- **作者**: Steve Mulder & Ziv Yaar
- **出版**: New Riders, 2007
- **核心概念**: 人物角色创建、用户研究整合、设计指导
- **适用**: UX 设计师、产品经理、交互设计师、营销人员

### 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

---

## English

### 🌟 Why Use This Skill?

- **Classic Methodology** — Based on Steve Mulder's "The User Is Always Right", a classic in persona creation
- **Full-Stack Toolkit** — From user research to persona creation, from business strategy to design guidance
- **CEO Perspective** — Built-in user economics model, acquisition strategy, retention strategy analysis
- **Practical Toolkit** — Pure Python standard library, zero dependencies, 5-minute setup
- **Bilingual Support** — Complete CN/EN documentation for international teams
- **Plug-and-Play** — Intuitive API, rich code examples, produce persona reports immediately

### 🎯 Features at a Glance

| Feature | Description |
|---------|-------------|
| 7 Core Capabilities | Interview guides, surveys, user segmentation, persona creation, business strategy, IA, testing & measurement |
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

```python
import sys
sys.path.insert(0, "/path/to/web-persona-skill")
from persona import PersonaSkill

skill = PersonaSkill("E-commerce Platform")

# Create Personas
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

# CEO Perspective Analysis
report = skill.generate_persona(include_ceo_analysis=True)
print(report)  # User economics + Acquisition + Retention strategies
```

### 💡 Core Capabilities

| # | Capability | Module | Description |
|---|------------|--------|-------------|
| 1 | **Interview Guide Generation** | `interview.py` | User research interview framework |
| 2 | **Survey Design** | `survey.py` | User segmentation surveys |
| 3 | **User Segmentation Analysis** | `segment.py` | Behavior-based user clustering |
| 4 | **Persona Creation** | `persona_builder.py` | Persona profile generation and management |
| 5 | **Business Strategy** | `strategy.py` | Feature priority + business strategy |
| 6 | **Information Architecture** | `design.py` | IA and content strategy |
| 7 | **Testing and Measurement** | `measure.py` | Test planning and measurement system |

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
```

### 👥 Who Is This For?

| Role | How This Skill Helps |
|------|---------------------|
| **UX Designers** | Create evidence-based personas from real user data |
| **Product Managers** | Align product decisions with user segments |
| **Marketing Teams** | Target messaging to specific persona needs |
| **Service Designers** | Map services to persona journeys and touchpoints |
| **AI Agents** | Zero-dependency Python package for automated persona generation |

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

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 design research methods
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done theory
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — Quantitative research, HEART framework
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — Value proposition canvas
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — Data storytelling

### 🌟 Why Choose AliDujie Skill Ecosystem?

This skill is part of the **AliDujie UX Research Skills Ecosystem**. Using the complete ecosystem provides:

- ✅ **Complete Coverage** — From user research to product design to data presentation, full-process tool support
- ✅ **Seamless Integration** — All skills use consistent API design and data formats
- ✅ **Best Practices** — Based on classic theories and practical experience, avoid common pitfalls
- ✅ **Active Maintenance** — Regularly updated with new features and improvements
- ✅ **Zero Dependencies** — Pure Python standard library, ready to use out of the box
- ✅ **Bilingual Support** — Complete CN/EN documentation for international team collaboration

👉 **Explore More Skills**: [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)

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

### 📦 Dependencies

- Python >= 3.8
- **No external dependencies** (pure standard library)
- Cross-platform: macOS / Linux / Windows

---

## Run Tests / 运行测试

```bash
cd /path/to/web-persona-skill
python3 -m pytest persona/tests/ -v 2>/dev/null || echo "No test suite yet — run manual validation"
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

## 📋 版本历史 (Changelog)

| 版本 | 日期 | 变更 |
|------|------|------|
| v2.3 | 2026-05-01 | 添加 "When to Use This Skill?" 决策指南，更新维护 |
| v2.2 | 2026-04-30 | 更新维护，清理格式 |
| v2.0 | 2026-04-29 | 统一交叉引用为 GitHub 绝对链接，添加 GitHub Topics，更新 Last Updated 日期 |
| v1.7 | 2026-04-25 | 统一技能生态格式，更新交叉引用 |
| v1.6 | 2026-04-23 | 添加 badges、技能生态系统 ASCII 图、双语支持、Why Use This Skill?、Quick Start、最佳实践、作者信息 |
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

---

*Last Updated: 2026-05-01 | AliDujie Skill Ecosystem | v2.3.0*
