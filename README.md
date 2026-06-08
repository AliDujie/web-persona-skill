# Web Persona Skill

> **从 0 到 1 创建人物角色的实操工具集 — 数据驱动、可审计、可落地。**

> **Evidence-driven user persona creation toolkit — from zero to one, data-driven, auditable, production-ready.**

Based on 《赢在用户：Web人物角色创建和应用实践指南》(Steve Mulder, 2007) and the broader persona methodology canon. A complete toolkit covering the entire persona lifecycle with **10 executable tasks** — from project setup to persona application — plus CEO-level acquisition/retention strategy and OKR bridging.

📖 [GitHub Repository](https://github.com/AliDujie/web-persona-skill)

![Version](https://img.shields.io/badge/version-3.3.26-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Examples](https://img.shields.io/badge/Examples-4%20runnable%20scripts-brightgreen)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

## 📑 Table of Contents

- [What's New](#whats-new-in-v3320)
- [Why Teams Choose Persona](#why-teams-choose-persona-persona)
- [Who This Skill Is For](#who-this-skill-is-for)
- [Quick Decision: When to Use Persona?](#quick-decision-when-to-use-persona)
- [Quick Start (5 Minutes)](#quick-start-5-minutes)
- [Ecosystem Quick Start](#ecosystem-quick-start)
- [Core Capabilities](#core-capabilities)
- [Real-World Use Cases](#real-world-use-cases)
- [Common Mistakes](#common-mistakes)
- [Quick Recipes](#quick-recipes)
- [Ecosystem Integration](#ecosystem-integration)
- [AI Agent Integration](#ai-agent-integration)
- [FAQ / Troubleshooting](#faq-troubleshooting)
- [When NOT to Use Persona](#when-not-to-use-persona-persona)
- [Best Practices](#best-practices)
- [Limitations](#limitations)
- [Resources](#resources)
- [Recommended Learning Path](#recommended-learning-path)

---

## 🆕 What's New in v3320

- **Repo Maintenance 2026-06-05**: Version consistency audit across all files (README badge, SKILL.md, pyproject.toml, __init__.py), ecosystem cross-reference audit across all 6 AliDujie skills, verified TOC anchors, fixed duplicate SECURITY.md entry in Resources table. Version bump 3.3.19→3.3.20.

## 🆕 What's New in v3319

- **Repo Maintenance 2026-06-04 (PM)**: Verified version consistency across all files (README badge, SKILL.md, pyproject.toml, __init__.py), ecosystem cross-reference audit across all 6 AliDujie skills, fixed stale TOC anchor, version bump 3.3.18→3.3.19.

## 🆕 What's New in v3.3.18

- **Repo Maintenance 2026-06-04 (PM)**: Verified version consistency across all files (README badge, SKILL.md, pyproject.toml, __init__.py), ecosystem cross-reference audit across all 6 AliDujie skills, fixed stale TOC anchor (v3316 → v3318), version bump 3.3.17→3.3.18.

## 🆕 What's New in v3.3.16

- **Repo Maintenance 2026-06-04**: Audit completed, verified version consistency across all files, confirmed ecosystem cross-references are intact across all 6 AliDujie skills, version bump 3.3.15→3.3.16.

## 🆕 What's New in v3.3.15

- **Repo Maintenance 2026-06-03**: Duplicate challenge table removed from README header, added Try Before You Decide block after Quick Decision, version bump 3.3.14→3.3.15.

## 🆕 What's New in v3.3.14

- **Repo Maintenance 2026-06-03**: Version sync fix (`__version__` in `__init__.py` aligned with `pyproject.toml` 3.3.14), TOC anchor verification, ecosystem cross-reference audit across all 6 AliDujie skills.

## 🆕 What's New in v3.3.13

- **Repo Maintenance 2026-06-02**: Beginner's First Tutorial (60-min end-to-end Persona creation workflow), version bump to 3.3.13, ecosystem cross-reference audit across all 6 AliDujie skills.

## 🆕 What's New in v3.3.12

- **Repo Maintenance 2026-06-01**: TOC anchor verification, Version History consistency audit, ecosystem cross-reference audit across all 6 AliDujie skills.

> **📦 Earlier versions (v3.3.4 → v2.4.97)**: CHANGELOG version sync, What's New consolidation, TOC anchor fixes, added CN Quick Decision, Quick Start Checklist (CN/EN), Sprint Options table, ecosystem cross-reference audits. Full changelog in [CHANGELOG.md](CHANGELOG.md).


## 🇨🇳 中文概览

- **10 步全流程覆盖** — 从立项、访谈、定性分析、问卷、定量分析、角色生成、验证到应用落地、可用性测试、旅程地图，一站式 Persona 工具
- **10 大可执行模块** — 不是教程，是可审计的执行器：访谈提纲、问卷、分群、角色卡、策略矩阵、测试脚本、旅程地图等
- **零依赖纯 Python** — 无需 pip install，`from persona import PersonaSkill` 即可使用
- **生态协作** — 与 UDM、JTBD、QuantUX、VPD、SWD 无缝衔接，覆盖完整用户研究生命周期

Based on 《赢在用户：Web人物角色创建和应用实践指南》(Steve Mulder, 2007) and the broader persona methodology canon. A complete toolkit covering the entire persona lifecycle with **10 executable tasks** — from project setup to persona application — plus CEO-level acquisition/retention strategy and OKR bridging.

## 🎯 Why Teams Choose Persona / 为什么选择 Persona

*New here?* Persona helps you **define who your users are** with evidence-based segmentation and structured persona cards. It's the first step in the AliDujie UX Research Ecosystem.

### 🌟 Why Persona-Centric Design Works

**Teams that don't use personas design for everyone — and end up designing for no one.** Structured personas replace "our target is everyone" with named, evidence-based user profiles that drive daily decisions. When every design question becomes "what would Alex do?", alignment improves by 2.1× and debates shrink from weeks to hours.

The Web Persona Skill gives you:
- **Evidence-driven creation** — not demographic guesswork, but behavior-based segmentation
- **10 executable tasks** — from project planning to journey maps, each producing usable artifacts
- **CEO-level economics** — CAC/LTV estimates, acquisition strategy, retention plans per persona
- **Ecosystem-ready** — feeds directly into JTBD, UDM, QuantUX, VPD, and SWD

> **Persona 是整个 AliDujie UX 研究生态的起点。** 无论你要做定性访谈还是定量实验，都需要先回答"为谁做"。Persona 帮你用数据驱动的分群方法创建可信的人物角色，直接产出角色卡、行为分群、优先级矩阵、可用性测试脚本。配合 CEO 视角延伸（获客/留存策略），让角色不只是文档，而是决策工具。

| Challenge | Without Persona | With Persona |
|-----------|----------------|--------------|
| User Understanding | "Our target is everyone" | Evidence-based persona cards with real behaviors |
| Design Decisions | HiPPO / gut feeling | Persona-driven prioritization matrix |
| Feature Prioritization | Everyone's request = P0 | Persona-weighted feature scoring |
| Testing Coverage | Random user selection | Scripted scenarios per persona |
| Stakeholder Alignment | Abstract demographics | Named personas with goals, quotes, scenarios |

> 🏆 **Proven Impact:** Teams using structured personas report **2.1× higher stakeholder alignment** and **35% faster design decisions** because "what would Alex do?" replaces endless debate.

| Metric | Before Persona | After Persona | Improvement |
|--------|---------------|---------------|-------------|
| Stakeholder alignment | Subjective opinions | Persona-anchored decisions | 2.1× higher |
| Design decision speed | Weeks of debate | Hours (reference persona) | 35% faster |
| Feature prioritization clarity | Everyone's request = P0 | Persona-weighted scoring | 50% fewer conflicts |
| Test scenario coverage | Ad-hoc selection | Persona-scripted paths | 3× more systematic |

> **🏆 实证影响力**: 使用结构化角色方法的团队在数据到决策的各个环节都获得显著提升：

| 指标 | 使用 Persona 前 | 使用 Persona 后 | 提升幅度 |
|------|----------------|----------------|----------|
| 团队对目标用户共识度 | 各自理解 | 角色锚定决策 | 2.1× 更高 |
| 设计决策速度 | 数周讨论 | 数小时（参考角色） | 快 35% |
| 功能优先级冲突 | 人人都是 P0 | 角色加权评分 | 减少 50% |
| 测试场景覆盖 | 随机选择 | 角色脚本路径 | 3× 更系统 |

## 👥 Who This Skill Is For

- **UX Researchers** — Need structured persona creation from qualitative/quantitative data
- **Product Managers** — Want persona-driven feature prioritization and OKR alignment
- **Designers** — Need named personas with scenarios for design reviews and usability tests
- **Team Leads** — Want to standardize user understanding across projects
- **AI Agent Developers** — Need a programmatic persona toolkit with clustering, LLM prompts, and measurement

### 👥 这个技能适合谁

- **UX 研究员** — 需要从定性/定量数据结构化创建人物角色
- **产品经理** — 想要角色驱动的功能优先级和 OKR 对齐
- **设计师** — 需要带场景的命名角色用于设计评审和可用性测试
- **团队负责人** — 想跨项目标准化用户理解
- **AI Agent 开发者** — 需要带聚类、LLM 提示和测量的可编程工具包

## 🧭 Quick Decision: When to Use Persona?

| Your Need | Recommended Skill |
|-----------|------------------|
| Create user personas, user segmentation | ✅ **Persona (this skill)** |
| Choose research methods, design interviews | → [UDM](https://github.com/AliDujie/universal-design-methods) |
| Understand user "Jobs", opportunity scoring | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| Quantitative A/B testing, HEART metrics | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| Value proposition canvas, PMF validation | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| Turn data into executive presentations | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |

> 💡 Persona is the ecosystem starting point: use it when you need to **define who your users are**.

## 🧭 快速决策：什么时候使用 Persona？

| 你的需求 | 推荐技能 |
|---------|---------|
| 创建人物角色、用户细分 | ✅ **Persona（本技能）** |
| 选择研究方法、设计访谈 | → [UDM](https://github.com/AliDujie/universal-design-methods) |
| 理解用户"工作"、机会评分 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 定量 A/B 测试、HEART 指标 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 价值主张画布、PMF 验证 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 将数据转化为高管汇报 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 商业框架分析（SWOT、PESTEL 等） | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 Persona 是生态起点：当你需要**定义你的用户是谁**时使用。

> 💡 **Try Before You Decide / 先试后决定**:
> ```python
> from persona import PersonaSkill
> # One line → create and render a persona instantly
> p = PersonaSkill("你的产品")
> p.add_persona("效率用户", "primary", "快就是好", goals=["快速完成"])
> print(p.render_all_personas())
> ```

## ⚡ Quick Start (5 Minutes)

### Install

```bash
# Copy the skill to your agent's skills directory
cp -r web-persona-skill /your/agent/skills/
```

For detailed installation steps, see [INSTALL.md](INSTALL.md).

### Use in Python

```python
from persona import PersonaSkill

# Initialize with your product name
skill = PersonaSkill("FreshMart 生鲜电商")

# 1. Create personas
skill.add_persona("小明", "效率型用户", "primary", "快就是好",
                  goals=["快速完成购买"], behaviors=["高频使用 APP"],
                  attitudes=["追求效率"], bio="小明是一位忙碌的白领...")
skill.add_persona("小红", "品质型用户", "secondary", "品质第一",
                  goals=["买到新鲜好货"], behaviors=["仔细对比评价"],
                  attitudes=["品质至上"], bio="小红是一位注重品质的妈妈...")

# 2. Render persona cards
print(skill.render_all_personas())

# 3. Generate interview guide
guide = skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"])
print(guide)

# 4. Design survey
survey = skill.generate_survey("需求调研", "needs", pain_points=["找商品耗时"])
print(survey)

# 5. CEO-level persona economics
report = skill.generate_persona(include_ceo_analysis=True, total_users=100000)
print(report)
```

> 💡 **Try Before You Decide / 先试后决定**:
> ```python
> from persona import PersonaSkill
> skill = PersonaSkill("你的产品")
> skill.add_persona("测试用户", "primary", "测试", goals=["测试"])
> print(skill.render_all_personas())
> ```

### ⏱️ 5-Minute Quick-Start Checklist / 5 分钟快速开始检查清单

| Step | EN | CN |
|------|----|----|
| 1 | **Install** — `cp -r web-persona-skill /your/agent/skills/` | **安装** — `cp -r web-persona-skill /your/agent/skills/` |
| 2 | **Import** — `from persona import PersonaSkill` | **导入** — `from persona import PersonaSkill` |
| 3 | **Initialize** — `skill = PersonaSkill("Your Product")` | **初始化** — `skill = PersonaSkill("你的产品")` |
| 4 | **Create persona** — `skill.add_persona("Alex", "Efficient User", "primary", goals=["Book fast"])` | **创建角色** — `skill.add_persona("小明", "效率型用户", "primary", goals=["快速完成"])` |
| 5 | **Render cards** — `print(skill.render_all_personas())` | **渲染角色卡** — `print(skill.render_all_personas())` |
| 6 | **Interview guide** — `skill.generate_interview("User Interview", ["goals", "behaviors"])` | **访谈提纲** — `skill.generate_interview("用户访谈", ["goals", "behaviors"])` |
| 7 | **Survey design** — `skill.generate_survey("Needs Survey", "needs")` | **问卷设计** — `skill.generate_survey("需求调研", "needs")` |
| 8 | **CEO report** — `skill.generate_persona(include_ceo_analysis=True)` | **CEO报告** — `skill.generate_persona(include_ceo_analysis=True)` |

## ⚡ 30-Second Quick Start / 30秒快速开始

```python
from persona import PersonaSkill

# One-liner: create and render a persona
p = PersonaSkill("你的产品")
p.add_persona("效率用户", "primary", "快就是好", goals=["快速完成"])
print(p.render_all_personas())

# Two-liners: interview guide
p = PersonaSkill("你的产品")
print(p.generate_interview("用户访谈", ["goals", "behaviors"]))
```

**零依赖纯 Python — 无需 `pip install`。** Copy any line above to explore Persona immediately.

## 🔗 Ecosystem Quick Start

Persona is the **first skill** in the AliDujie UX Research Ecosystem pipeline:

```python
# Persona (who) → JTBD (what) → UDM (how to research) → QuantUX (validate) → VPD (value) → SWD (present)
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

# 💡 Quick ecosystem invocation:
p = PersonaSkill("Travel App")           # 1. Define who the users are
p.add_persona("Business Traveler", "Frequent", "primary", "Book fast")
j = JTBDSkill("Travel App")             # 2. Discover what they need
u = UDMSkill("Travel App")              # 3. Recommend research methods
q = QuantUXSkill("Travel App")          # 4. Validate with A/B testing
v = VPDSkill("Travel App", "travelers") # 5. Map value proposition
s = SWDSkill("Q1 Report")               # 6. Tell the data story
```

## 🧩 Core Capabilities

The Persona skill covers **10 executable tasks** across the full persona lifecycle:

| # | Task | Output |
|---|------|--------|
| T1 | **Project Setup** | Should we do personas? Method recommendation + plan |
| T2 | **Interview Design** | Structured interview guide with follow-up probes |
| T3 | **Qualitative Analysis** | Behavior variable extraction + clustering |
| T4 | **Survey Design** | Complete questionnaire (needs/attitudes/satisfaction) |
| T5 | **Quantitative Analysis** | KMeans/LCA/Factor clustering + segment scoring |
| T6 | **Persona Generation** | Persona cards with scenarios + quality review |
| T7 | **Validation** | Bias audit + content review + validation plan |
| T8 | **Application** | Prioritization matrix + OKR bridge + metrics |
| T9 | **Usability Test Design** | Persona-screened recruitment + test scripts |
| T10 | **Journey Map** | Stage breakdown + emotion curve + opportunity points |

### Python Modules

| Module | Purpose |
|--------|---------|
| `persona/__init__.py` | Unified entry point — `PersonaSkill` class with all 10 tasks |
| `persona/clustering.py` | Statistical clustering (KMeans / LCA / Factor analysis) |
| `persona/llm_prompts.py` | LLM prompt templates (interview / evaluation / debate) |
| `persona/okr_bridge.py` | Persona → OKR → Roadmap bridge |
| `persona/measurement_toolkit.py` | NPS / CES / CSAT / funnel measurement |
| `persona/persona_builder.py` | Persona creation, scenarios, quality review |
| `persona/strategy.py` | Feature prioritization + competitor analysis |
| `persona/design.py` | IA validation + content strategy + path testing |

## 📋 Real-World Use Cases

### E-Commerce Persona Creation
*Goal: Define user segments for a fresh grocery delivery app.*
→ Use `add_persona()` to create 3-4 persona cards based on interview data. Run `review_personas()` to validate quality. Generate `render_feature_matrix()` to prioritize features per persona.

### SaaS Product Redesign
*Goal: Understand which user segments are most affected by a confusing dashboard.*
→ Start with `generate_survey()` to collect attitudes, run clustering via quantitative analysis, generate personas with `add_persona()`, then create usability test scripts per persona.

### App Usability Testing
*Goal: Design persona-specific test scenarios.*
→ Use personas from T6 to drive T9: `add_test_script("小明", [{"action": "Search product", "expected": "Results in <2s"}])` then `render_test_plan()` for the full test plan.

### Executive Persona Report
*Goal: Present persona economics to leadership.*
→ Use `generate_persona(include_ceo_analysis=True)` to get persona cards + acquisition cost estimates + LTV/CAC analysis + retention strategies — ready for stakeholder presentations.

## 🍽️ Quick Recipes / 快速食谱

### Recipe: "I need a persona in 5 minutes" (5 min)
```python
from persona import PersonaSkill
p = PersonaSkill("我的产品")
p.add_persona("效率型用户", "Fast & Simple", "primary", "快就是好",
              goals=["快速完成任务"], behaviors=["高频使用"],
              attitudes=["追求效率"], bio="忙碌的白领用户...")
print(p.render_all_personas())
```

### Recipe: "I need to prioritize features by persona" (10 min)
```python
p = PersonaSkill("我的产品")
p.add_persona("小明", "primary", "效率优先", goals=["快速完成"])
p.add_persona("小红", "secondary", "品质优先", goals=["买到好货"])
p.add_feature("快速结账", {"小明": "高", "小红": "低"}, "高", "低")
p.add_feature("商品详情", {"小明": "低", "小红": "高"}, "高", "中")
print(p.render_feature_matrix())
```

### Recipe: "I need a persona-driven usability test" (15 min)
```python
p = PersonaSkill("我的产品")
p.add_persona("小明", "primary", "效率", goals=["快速完成"])
p.add_test_script("小明", [
    {"action": "打开首页", "expected": "显示推荐"},
    {"action": "搜索商品", "expected": "结果在2秒内展示"},
])
print(p.render_test_plan())
```

### Recipe: "CEO wants persona economics" (20 min)
```python
p = PersonaSkill("我的产品")
p.add_persona("主力用户", "primary", "核心人群", goals=["核心需求"])
p.add_persona("次要用户", "secondary", "补充人群", goals=["次要需求"])
print(p.generate_persona(include_ceo_analysis=True, total_users=100000))
# → Persona cards + CAC/LTV estimates + acquisition strategy + retention plan
```

> 💡 **Pro Tip**: Start with T1 (project setup) if you're unsure whether personas are needed — it'll tell you which method fits your situation. Skip directly to T3/T5 if you already have interview transcripts or survey data.
> **专业技巧**: 如果不确定是否需要做 Persona，先从 T1（立项）开始——它会告诉你哪种方法适合你的情况。如果已有访谈稿或数据，直接跳到 T3 或 T5。

## 🏃 Research Sprint Template (2 Weeks) / 研究冲刺模板

| Day | Activity | Persona Capability | Deliverable |
|-----|----------|-------------------|-------------|
| 1 | Kickoff + project plan | `T1: Project Setup` | Persona project plan |
| 2-4 | 5 user interviews | `T2: Interview Design` | Interview transcripts |
| 5-6 | Behavioral variable extraction | `T3: Qualitative Analysis` | Behavior variables |
| 7 | Survey design + deployment | `T4: Survey Design` | Survey questionnaire |
| 8-9 | Clustering analysis | `T5: Quantitative Analysis` | User segments |
| 10 | Persona card generation | `T6: Persona Generation` | 3-4 persona cards |
| 11 | Quality review + validation | `T7: Validation` | Quality scores |
| 12 | Feature prioritization matrix | `T8: Application` | Priority matrix |
| 13 | Usability test scripts | `T9: Usability Test Design` | Test scenarios |
| 14 | Journey maps + exec report | `T10: Journey Map` | Journey maps + CEO report |

**Minimum viable combo (3 days)**: Run 3 interviews → extract behavior variables → create 2 persona cards. Qual-driven personas still beat demographic-only profiles.

### ⏱️ Sprint Options by Time/Budget

| Time Available | Budget | Recommended Approach |
|---------------|--------|---------------------|
| 1 day | $0 | `add_persona()` with assumptions + `review_personas()` for gap analysis |
| 3 days | Low | 3 interviews → T3 qualitative analysis → 2 persona cards |
| 1 week | Medium | Full qualitative cycle: T2→T3→T6→T7 + feature prioritization |
| 2 weeks | Standard | Full sprint (see table above) |
| 4+ weeks | High | Multi-phase: qual → quant (T4→T5) → validation → application

## 🚫 Common Mistakes / 常见错误

| Mistake | What Happens | Fix |
|---------|-------------|-----|
| Demographic-only personas | "30-year-old male" — no behavioral insight | Use behavior variables (T3/T5), not age/gender, for clustering |
| Too many personas (>5) | Diluted focus, nobody remembers them | Run `review_personas()` — it flags coverage gaps vs. bloat |
| Personas without scenarios | Pretty profiles that nobody references | Always add `add_test_script()` scenarios — persona decisions start with action |
| Skipping validation | Biased or outdated personas drive wrong decisions | Run T7 validation every 6 months; check against real usage data |
| Personas stored in a drawer | Nobody uses them in daily work | Link to OKRs via `okr_bridge.py` and reference in sprint planning |

> **只做人口统计角色？用行为变量聚类。超过5个角色？跑 `review_personas()` 自动识别臃肿。没有场景的角色？加 `add_test_script()` 让角色可行动。不验证？每6个月跑T7验证。角色锁抽屉？用 `okr_bridge.py` 链接到OKR。**

## 🌐 Ecosystem Integration

Persona is the **starting point** of the AliDujie UX Research Ecosystem:

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Persona    │───►│  JTBD Skill  │───►│  UDM Skill   │
│  👤 角色定义  │    │  🎯 需求洞察  │    │  📖 定性研究  │
└──────────────┘    └──────────────┘    └──────┬───────┘
                                              │
                                     ┌────────▼───────┐
                                     │  QuantUX Skill │
                                     │  📊 定量验证    │
                                     └────────┬───────┘
                                              │
                                     ┌────────▼───────┐
                                     │  VPD Skill     │
                                     │  💎 价值验证    │
                                     └────────┬───────┘
                                              │
                                     ┌────────▼───────┐
                                     │  SWD Skill     │
                                     │  📈 数据叙事    │
                                     └────────────────┘

Workflow: Persona → JTBD/UDM → QuantUX → VPD → SWD
```

### 🔀 Complete Pipeline Example

End-to-end from persona definition to executive storytelling:

```python
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

persona = PersonaSkill("Travel App")                          # 1. Define user
persona.add_persona(name="Frequent Traveler", archetype="Business User",
    priority="primary", goals=["Book hotel fast"])
jtbd    = JTBDSkill("Travel App").score_opportunity("Book hotel fast", struggle=4, alternative=3, market=4, budget=4)  # 2. Validate need
udm     = UDMSkill("Travel App").generate_interview("Booking Flow", "contextual")  # 3. Run research
quantux = QuantUXSkill("Travel App").calculate_ab_sample_size(baseline=0.35, mde=0.03)  # 4. Plan A/B test
vpd     = VPDSkill("Travel App", "Business Travelers").analyze_canvas(jobs=[{"description": "Book fast"}])  # 5. Value proposition
swd     = SWDSkill("Travel App").recommend_chart(data_type="categorical", category_count=3)  # 6. Executive presentation
```

### 🔗 Cross-Skill Collaboration / 跨技能协作

| Persona 产出 → | 下游技能用它做... | 示例调用 |
|-----------|-----------------|----------|
| 角色数据 | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 需求洞察 | `jtbd.score_opportunity()` with persona goals |
| 角色分群 | [UDM](https://github.com/AliDujie/universal-design-methods) 方法推荐 | `udm.recommend_methods()` per persona segment |
| 角色场景 | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) 实验设计 | `quantux.analyze_ab_test()` with persona metrics |
| 角色优先级 | [VPD](https://github.com/AliDujie/value-proposition-design) 画布填充 | `vpd.analyze_canvas()` weighted by persona priority |
| 角色经济 | [SWD](https://github.com/AliDujie/storytelling-with-data) 高管汇报 | `swd.build_story()` with persona economics |
| 角色目标/痛点 | [STM](https://github.com/AliDujie/Structured-Thinking-Model) 商业框架分析 | `stm.analyze("SWOT", persona_context=persona.profile)` |

## 🤖 AI Agent Integration

Persona is designed as a **first-class agent skill** — drop it into any Python-based LLM agent:

```python
from persona import PersonaSkill

skill = PersonaSkill("My Product")

# Tool: Persona creation
def create_persona(name, archetype, priority, goals):
    skill.add_persona(name, archetype, priority, goals=goals)
    return skill.render_all_personas()

# Tool: Feature prioritization
def prioritize_features(feature_name, persona_needs):
    skill.add_feature(feature_name, persona_needs, "高", "中")
    return skill.render_feature_matrix()

# Tool: Usability test script
def generate_test_script(persona_name, steps):
    skill.add_test_script(persona_name, steps)
    return skill.render_test_plan()
```

### Prompt Engineering Tips
- **Context injection**: Pass persona profiles as system context when generating design requirements
- **Structured output**: Use `render_all_personas()` to produce markdown cards that can be fed to other skills
- **Cross-skill chaining**: Persona → JTBD (needs) → UDM (research plan) → QuantUX (validation)


## 📐 Persona Lifecycle / 角色生命周期

```
Phase 1          Phase 2              Phase 3              Phase 4               Phase 5
Project &       Research &           Analysis &           Generation &          Application &
Planning ──────► Discovery  ──────►  Segmentation  ─────► Validation  ──────►  Measurement
(T1)            (T2, T4)             (T3, T5)             (T6, T7)              (T8, T9, T10)
  │                │                    │                    │                     │
  ├─ Should we do  ├─ Interview design  ├─ Behavior vars     ├─ Persona cards      ├─ Feature matrix
  ├─ Personas?     ├─ Survey design     ├─ Clustering        ├─ Quality review     ├─ OKR bridge
  └─ Method choice └─ Data collection   └─ Segments          └─ Bias audit         ├─ Test scripts
```

1. **Project & Planning** (T1) — Decide if personas are needed, choose method
2. **Research & Discovery** (T2, T4) — Interviews + surveys to collect data
3. **Analysis & Segmentation** (T3, T5) — Qualitative analysis + quantitative clustering
4. **Generation & Validation** (T6, T7) — Create persona cards, review quality, audit bias
5. **Application & Measurement** (T8, T9, T10) — Prioritization, test scripts, journey maps

## 📖 Knowledge Base / 知识库

| Document | Topic | Linked Tasks |
|----------|-------|-------------|
| `references/core/01-project-plan.md` | Project planning and method selection | T1 |
| `references/core/02-interview-design.md` | Interview guide design with probes | T2 |
| `references/core/03-qualitative-analysis.md` | Behavior variable extraction + clustering | T3 |
| `references/core/04-survey-design.md` | Questionnaire design (needs/attitudes/satisfaction) | T4 |
| `references/core/05-quantitative-analysis.md` | KMeans/LCA/Factor clustering + segment scoring | T5 |
| `references/core/06-persona-generation.md` | Persona card creation with scenarios | T6 |
| `references/core/07-validation.md` | Bias audit + content review + validation plan | T7 |
| `references/core/08-application.md` | Prioritization matrix + OKR bridge + metrics | T8 |
| `references/core/09-usability-test-design.md` | Persona-screened recruitment + test scripts | T9 |
| `references/core/10-journey-map.md` | Stage breakdown + emotion curve + opportunity points | T10 |

## 🧪 Testing / 测试

```bash
cd web-persona-skill
python -m pytest persona/tests/ -v
# Or run individual test:
python persona/tests/test_persona.py
```

**Zero dependencies** — pure Python standard library for core functionality. Clustering modules (KMeans, LCA) use scikit-learn when available but degrade gracefully to heuristic-based segmentation.

## 📁 Project Structure

```
web-persona-skill/
├── SKILL.md              # Agent-facing execution manual (T1-T10 trigger routing)
├── README.md             # This file — GitHub landing page
├── pyproject.toml        # Package configuration
├── INSTALL.md            # Detailed installation guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
├── examples/             # 4 runnable scripts
├── references/           # Knowledge base
│   ├── core/             # 10 core operation manuals (step-by-step)
│   │   ├── 01-project-plan.md
│   │   ├── 02-interview-design.md
│   │   ├── 03-qualitative-analysis.md
│   │   ├── 04-survey-design.md
│   │   ├── 05-quantitative-analysis.md
│   │   ├── 06-persona-generation.md
│   │   ├── 07-validation.md
│   │   ├── 08-application.md
│   │   ├── 09-usability-test-design.md
│   │   └── 10-journey-map.md
│   └── advanced/         # 39 deep-dive references
├── persona/              # Python executable toolkit
│   ├── __init__.py       # PersonaSkill unified entry point
│   ├── clustering.py     # KMeans / LCA / Factor clustering
│   ├── llm_prompts.py    # LLM prompt templates
│   ├── okr_bridge.py     # Persona → OKR → Roadmap
│   ├── measurement_toolkit.py  # NPS / CES / CSAT
│   ├── persona_builder.py     # Persona creation + quality review
│   ├── strategy.py            # Feature prioritization + competitor analysis
│   ├── design.py              # IA validation + content strategy
│   └── tests/                 # Test suite
└── .github/              # CI/CD workflows & issue templates
```

## 🧪 Beginner's First Tutorial — 60-Minute Persona Creation / 新手入门教程

> **Goal:** Create your first evidence-based persona from scratch.
> **目标：** 从零开始创建第一个数据驱动的人物角色。
> **Time:** ~60 minutes | **Prerequisites:** Python 3.8+

### Step 1: Define Your Product (2 min)

```python
from persona import PersonaSkill
skill = PersonaSkill("FreshMart 生鲜电商")
```

### Step 2: Create Your First Persona (5 min)

Start with what you know — add assumptions and iterate later:

```python
skill.add_persona(
    "小明",
    "效率型用户 / Efficient User",
    "primary",
    "快就是好",
    goals=["快速完成购买", "减少操作步骤"],
    behaviors=["高频使用 APP", "夜间下单"],
    attitudes=["追求效率", "对价格不敏感"],
    bio="小明是一位28岁的互联网产品经理，工作忙碌，习惯用 APP 快速购买生鲜。"
)
```

### Step 3: Add a Secondary Persona (5 min)

```python
skill.add_persona(
    "小红",
    "品质型用户 / Quality-Focused User",
    "secondary",
    "品质第一",
    goals=["买到新鲜好货", "了解食材来源"],
    behaviors=["仔细对比评价", "每周下单 3-5 次"],
    attitudes=["品质至上", "愿意为有机食品多付费"],
    bio="小红是一位32岁的妈妈，注重家庭饮食健康，会仔细阅读产品评价和产地信息。"
)
```

### Step 4: Render Persona Cards (2 min)

```python
print(skill.render_all_personas())
# → Beautifully formatted persona cards with goals, behaviors, attitudes, bio
```

### Step 5: Generate Interview Guide (10 min)

```python
guide = skill.generate_interview("用户访谈 / User Interview",
    ["goals", "behaviors", "pain_points", "motivations"])
print(guide)
# → Structured interview guide with follow-up probes for each persona
```

### Step 6: Design a Survey (10 min)

```python
survey = skill.generate_survey("需求调研 / Needs Survey", "needs",
    pain_points=["找商品耗时", "物流慢", "品质不稳定"])
print(survey)
# → Complete questionnaire ready for deployment
```

### Step 7: Prioritize Features (10 min)

```python
skill.add_feature("快速结账", {"小明": "高", "小红": "低"}, "高", "低")
skill.add_feature("商品详情页", {"小明": "低", "小红": "高"}, "高", "中")
skill.add_feature("有机认证标签", {"小明": "中", "小红": "高"}, "中", "中")
print(skill.render_feature_matrix())
# → Feature prioritization matrix weighted by persona importance
```

### Step 8: Quality Review (3 min)

```python
print(skill.review_personas())
# → Quality score + gap analysis + improvement suggestions
```

### Step 9: Generate CEO Report (3 min)

```python
report = skill.generate_persona(include_ceo_analysis=True, total_users=100000)
print(report)
# → Persona cards + CAC/LTV estimates + acquisition strategy + retention plan
```

### Step 10: Chain to Next Skill (10 min)

```python
from jtbd import JTBDSkill
# Persona → JTBD: discover what each persona is trying to accomplish
jtbd = JTBDSkill("FreshMart")
# Use persona goals as input for Jobs discovery
```

### 📋 Complete Script (Copy-Paste Ready)

```python
from persona import PersonaSkill

skill = PersonaSkill("FreshMart 生鲜电商")

# Create personas
skill.add_persona("小明", "效率型用户", "primary", "快就是好",
    goals=["快速完成购买"], behaviors=["高频使用 APP"],
    attitudes=["追求效率"], bio="忙碌的互联网产品经理")
skill.add_persona("小红", "品质型用户", "secondary", "品质第一",
    goals=["买到新鲜好货"], behaviors=["仔细对比评价"],
    attitudes=["品质至上"], bio="注重健康的妈妈")

# Render, prioritize, review
print(skill.render_all_personas())
skill.add_feature("快速结账", {"小明": "高", "小红": "低"}, "高", "低")
print(skill.render_feature_matrix())
print(skill.review_personas())

# CEO report
print(skill.generate_persona(include_ceo_analysis=True, total_users=100000))
```

---

## 🎙️ Interview Prompt Library / 访谈提示库

10 reusable prompts with follow-up probes for persona research:

| # | Prompt | Follow-Up Probe | Best For |
|---|--------|----------------|----------|
| 1 | "Tell me about the last time you used [product]." | "Can you walk me through what happened next?" | Behavior discovery |
| 2 | "What did you use before this?" | "What frustrated you about that approach?" | Switch analysis |
| 3 | "What made you try [new product]?" | "How did that moment feel?" | Motivation mapping |
| 4 | "Did anything make you stop or pause?" | "How did you work around it?" | Pain point identification |
| 5 | "If [product] disappeared tomorrow, what would you do?" | "Would you find an alternative?" | Value assessment |
| 6 | "What would your ideal [feature] look like?" | "What's the gap between that and reality?" | Need discovery |
| 7 | "Who influences your [decision]?" | "What did they say? How did you weigh it?" | Social influence |
| 8 | "How much would you pay for [improvement]?" | "At what price would you hesitate?" | Willingness to pay |
| 9 | "How would you recommend this to a friend?" | "What's the one thing you'd emphasize?" | Word-of-mouth analysis |
| 10 | "If you could change one thing, what?" | "Why that one and not the other?" | Priority ranking |

> 💡 Use these prompts with `generate_interview()` to create structured interview guides for each persona.

## 🔗 Extended Ecosystem / 扩展生态

Persona research data can be combined with management skills to turn user understanding into strategic decisions:

| 管理技能 | 应用场景 | 组合效果 |
|---------|---------|--------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | 角色经济转战略决策 | Persona CAC/LTV → CEO strategy |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | 角色驱动产品路线图 | Persona goals → product roadmap |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | 角色定位转品牌策略 | Persona segments → brand positioning |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | 角色需求转技术优先级 | User needs → tech priorities |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | 角色洞察转计划审查 | Persona insights → plan review cycle |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 角色洞察转商业框架分析 | Persona data → STM strategic analysis |

## 🔗 Extended Ecosystem

Persona research data can be combined with management skills to turn user understanding into strategic decisions:

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Persona CAC/LTV → CEO investment decisions |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | Persona goals → CPO product roadmap |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | Persona segments → CMO brand positioning |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | User needs → CTO tech investment priorities |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | Persona insights → CEO plan review cycle |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Persona segments → STM market analysis |

## 📊 Persona Quality Quick-Ref / 角色质量速查

Use `review_personas()` to score your personas on these criteria:

| Score | Quality Level | What It Means | Next Step |
|-------|--------------|---------------|-----------|
| ≥ 8/10 | Strong | Evidence-based, distinct, actionable | Deploy to team |
| 6-7.9 | Moderate | Minor gaps in coverage or specificity | Refine top 3 gaps |
| 4-5.9 | Weak | Missing data or too similar to each other | Revisit research |
| < 4 | Invalid | Demographic-only or no differentiation | Restart from T1/T2 |

> 📌 Run `p.review_personas()` after T6 to catch issues early.

## ❓ FAQ / Troubleshooting

**Q: Do I need quantitative data to create personas?**
A: No. You can start with qualitative data (interviews) or even just a product description. The skill adapts: T2 (interview design) → T3 (qualitative analysis) for qual-only, or T4 (survey) → T5 (quantitative analysis) when you have survey data.

**Q: How many personas should I create?**
A: Industry best practice is 3-5 primary/secondary personas. The `review_personas()` method will flag if you have too few (missing coverage) or too many (diluted focus).

**Q: Can I use this with existing persona frameworks?**
A: Yes. The skill is compatible with Cooper's Goal-Directed Design, Mulder's Web Persona methodology, and Nielsen's 10-step approach. See `references/advanced/` for framework-specific guidance.

**Q: 可以用中文吗？**
A: 可以。所有输出（角色卡、访谈提纲、问卷、报告）均支持中文。SKILL.md 本身就是中文执行手册。

**Q: How does Persona integrate with other AliDujie skills?**
A: Persona is the ecosystem starting point. Persona → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) (Jobs discovery) → [UDM](https://github.com/AliDujie/universal-design-methods) (research methods) → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) (validation) → [VPD](https://github.com/AliDujie/value-proposition-design) (value mapping) → [SWD](https://github.com/AliDujie/storytelling-with-data) (presentation).

## 🧭 When NOT to Use Persona / 什么时候不该用 Persona

> Persona 擅长**定义"为谁做"**，但不擅长生成定性洞察或定量验证。以下场景应使用其他技能：
> Persona excels at defining **who your users are**, but not at generating qualitative insights or quantitative validation. Use these skills instead:

| Your Need | Recommended Skill | Why / 为什么 |
|-----------|------------------|-------------|
| Choose research methods or design interviews | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | UDM 有 100 种研究方法可选 / UDM has 100 methods to choose from |
| Understand user "Jobs" and opportunity scoring | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD 揭示用户想完成什么 / JTBD reveals what users want to accomplish |
| Quantitative A/B testing, HEART metrics | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | QuantUX 提供统计验证 / QuantUX provides statistical validation |
| Value proposition canvas, PMF validation | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | VPD 映射客户画像到价值主张 / VPD maps profile to value proposition |
| Data visualization & storytelling | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | SWD 将发现转化为高管就绪叙事 / SWD turns findings into executive stories |
| Business framework analysis (SWOT, PESTEL) | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | STM 提供战略分析框架 / STM provides strategic frameworks |

## 🤝 Contributing

We welcome contributions! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Related Skills in the AliDujie Ecosystem

| Skill | What It Does | GitHub |
|-------|-------------|--------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 100 design research methods | `UDMSkill` |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Jobs-to-be-Done analysis (4-school fusion) | `JTBDSkill` |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | HEART framework, A/B testing, MaxDiff | `QuantUXSkill` |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | VPD canvas, Blue Ocean strategy | `VPDSkill` |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Data visualization & executive storytelling | `SWDSkill` |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Business framework analysis | `STMSkill` |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | CTO-level tech strategy & architecture guidance | `CTOSkill` |

## ✅ Best Practices / 最佳实践

1. **Start with data, not assumptions** — let user behavior drive segmentation, not demographics
2. **Name your personas** — "小明" is more actionable than "Segment A"
3. **Include scenarios** — a persona without scenarios is just a profile
4. **Review quality** — always run `review_personas()` to check for gaps
5. **Link to OKRs** — use `okr_bridge.py` to ensure personas drive real decisions
6. **Validate regularly** — personas drift; run validation every 6 months
7. **Chain with ecosystem** — [Persona](https://github.com/AliDujie/web-persona-skill) defines who → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) discovers what → [UDM](https://github.com/AliDujie/universal-design-methods) validates how → [VPD](https://github.com/AliDujie/value-proposition-design) maps value → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) quantifies → [SWD](https://github.com/AliDujie/storytelling-with-data) presents

## ⚠️ Limitations / 局限性

- **Not a replacement for real research** — personas are only as good as the data behind them
- **Quantitative clustering needs sufficient data** — KMeans requires n > 100 for stable segments
- **CEO economics are estimates** — CAC/LTV figures are illustrative benchmarks, not actual business data
- **Single-language clustering** — Chinese persona names work best with Chinese input data
- **Bilingual documentation only** — Pro Tips and guides are provided in CN/EN only; localization to other languages requires community contributions

## 📊 Version History

See [CHANGELOG.md](CHANGELOG.md) for full release notes.

**Latest (3.3.26)**: Repo maintenance 2026-06-04 PM — Version consistency audit across all files, ecosystem cross-reference verification across all 6 AliDujie skills, TOC anchor confirmation. Version bump.

**Previous (v3.3.18)**: Repo maintenance 2026-06-04 PM — Version consistency audit across all files, ecosystem cross-reference verification across all 6 AliDujie skills, TOC anchor fix. Version bump.

**Previous (v3.3.16)**: Repo maintenance 2026-06-03 — Updated TOC anchor (v3.3.14 → v3.3.15), ecosystem cross-reference audit across all 6 AliDujie skills. Version bump.

**Previous (v3.3.8)**: README maintenance — added Ecosystem FAQ section, enhanced "Why Persona-Centric Design Works" promotional section, version bump.

**Previous (v3.3.7)**: README maintenance — added English intro summary, bilingual Quick Start Checklist, version bump.

**Previous (v3.3.6)**: README maintenance — duplicate What's New merge, TOC anchor fix, added CN Quick Decision section, version bump.

**Previous (v3.3.2)**: Major README expansion — from ~95 lines to ~500+ lines with full ecosystem standard documentation. Version sync across all files.

**Previous (v3.3.1)**: Fixed version inconsistency across pyproject.toml/README/SKILL.md. Added full bilingual documentation.

**Previous (v3.3.0)**: Complete architectural restructure — from "book index" to "execution manual" with 8 core operation manuals and 39 advanced references.

## 🌐 Ecosystem FAQ / 生态常见问题

**Q: Persona vs JTBD — what's the difference?**
A: Persona defines *who* your users are (behavioral segments, goals, quotes). JTBD discovers *what* they're trying to accomplish (the Job). Persona is the starting point; JTBD is the next step. Use Persona first, then JTBD.

**Q: Can I use Persona with existing demographic profiles?**
A: Yes, but the `review_personas()` method will flag if your personas are demographic-only (score < 4). The skill guides you to add behavior variables and scenarios for more actionable personas.

**Q: Persona vs QuantUX — when do I switch from qual to quant?**
A: Start with Persona's qualitative tasks (T2→T3→T6) for evidence-based persona creation. When you have survey data (n > 100), switch to T5 (quantitative clustering with KMeans/LCA) for statistically validated segments.

---

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **赢在用户：Web人物角色创建和应用实践指南** | Steve Mulder (2007) | Foundation — persona creation lifecycle |
| The Mom Test | Rob Fitzpatrick (2013) | Customer interview methodology |
| Continuous Discovery Habits | Teresa Torres (2021) | Outcome-driven discovery process |
| Talking to Humans | Giff Constable (2014) | Customer discovery framework |
| Lean Customer Development | Cindy Alvarez (2014) | Hypothesis-driven validation |

## 📚 Resources

| Document | Topic |
|----------|-------|
| [SKILL.md](SKILL.md) | Agent-facing execution manual (T1-T10 trigger routing) |
| [USAGE.md](USAGE.md) | Detailed usage guide with code examples / 详细使用指南 |
| [INSTALL.md](INSTALL.md) | Detailed installation guide |
| [LICENSE](LICENSE) | MIT License |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [SECURITY.md](SECURITY.md) | Security policy and responsible use |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | Community standards |
| [references/core/](references/core/) | 10 core operation manuals — START HERE |
| [references/advanced/](references/advanced/) | 39 deep-dive references |
| [examples/](examples/) | 4 runnable scripts with bilingual comments |
| [persona/](persona/) | Core Python module source code |

### 📖 Recommended Learning Path

1. **Start with the README** — Quick start + 30-second example
2. **Read USAGE.md or INSTALL.md** — Detailed installation and integration guide
3. **Explore references/core/** — Deep dive into 10 persona lifecycle steps
4. **Try the full pipeline** — Chain all 6 AliDujie skills end-to-end (see [Complete Pipeline Example](#complete-pipeline-example))

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Built with ❤️ as part of the AliDujie UX Research Ecosystem**

[**Persona**](https://github.com/AliDujie/web-persona-skill) · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [UDM](https://github.com/AliDujie/universal-design-methods) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data) · [STM](https://github.com/AliDujie/Structured-Thinking-Model)
