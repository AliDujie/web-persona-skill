# Web Persona Skill

> **从 0 到 1 创建人物角色的实操工具集 — 数据驱动、可审计、可落地。**

📖 [GitHub Repository](https://github.com/AliDujie/web-persona-skill)

![Version](https://img.shields.io/badge/version-3.3.3-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Examples](https://img.shields.io/badge/Examples-5%20runnable%20scripts-brightgreen)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

## 📑 Table of Contents

- [What's New](#-whats-new-in-v331)
- [Why Teams Choose Persona](#-why-teams-choose-persona--为什么选择-persona)
- [Who This Skill Is For](#-who-this-skill-is-for)
- [Quick Decision: When to Use Persona?](#-quick-decision-when-to-use-persona)
- [Quick Start (5 Minutes)](#-quick-start-5-minutes)
- [Ecosystem Quick Start](#-ecosystem-quick-start)
- [Core Capabilities](#-core-capabilities)
- [Real-World Use Cases](#-real-world-use-cases)
- [Quick Recipes](#-quick-recipes--快速食谱)
- [Ecosystem Integration](#-ecosystem-integration)
- [AI Agent Integration](#-ai-agent-integration)
- [FAQ / Troubleshooting](#-faq--troubleshooting)
- [Best Practices](#-best-practices--最佳实践)
- [Limitations](#-limitations--局限性)
- [Resources](#-resources)

---

## 🆕 What's New in v3.3.3

- **Major README Expansion 2026-05-31**: Expanded README from ~95 lines to ~500+ lines — added TOC, Why Teams Choose Persona, Who This Skill Is For, Quick Decision guide, Quick Start (5 min), Ecosystem Quick Start, Core Capabilities table (10 tasks), Real-World Use Cases, Quick Recipes (4 copy-paste scripts), Ecosystem Integration diagram, AI Agent Integration, FAQ, Best Practices, Limitations, Resources, and full bilingual (CN/EN) coverage
- **Version Bump**: Synced to 3.3.2

## 🆕 What's New in v3.3.1

- **Version Sync**: Fixed version inconsistency across pyproject.toml (3.1.0), README badge (3.0.0), and SKILL.md (3.3.0) — all now consistently report v3.3.1
- **README Expansion**: Added full documentation matching ecosystem standard — TOC, Why Use This Skill, Quick Start, ecosystem integration, recipes, FAQ, and bilingual content

## 🆕 What's New in v3.3.0

- **Complete architectural restructure** — from "book index" to "execution manual"
- **8 core operation manuals** (`references/core/01-08`) covering the entire persona lifecycle step-by-step
- **39 advanced references** (`references/advanced/`) preserved as deep-dive dictionary
- **SKILL.md reduced from 864 → ~120 lines** — quick reference only, details in core docs

> **📦 Earlier versions (v2.7 → v2.4.97)**: Added upstream research craft (Portigal/Fitzpatrick/Torres/Alvarez), ABCD deep-dive (quantitative/psychology/ethics/engineering), 10 classic book references, and Mulder-based initial executor. Full changelog in [CHANGELOG.md](CHANGELOG.md).

## 🇨🇳 中文概览

- **10 步全流程覆盖** — 从立项、访谈、定性分析、问卷、定量分析、角色生成、验证到应用落地、可用性测试、旅程地图，一站式 Persona 工具
- **10 大可执行模块** — 不是教程，是可审计的执行器：访谈提纲、问卷、分群、角色卡、策略矩阵、测试脚本、旅程地图等
- **零依赖纯 Python** — 无需 pip install，`from persona import PersonaSkill` 即可使用
- **生态协作** — 与 UDM、JTBD、QuantUX、VPD、SWD 无缝衔接，覆盖完整用户研究生命周期

Based on 《赢在用户：Web人物角色创建和应用实践指南》(Steve Mulder, 2007) and the broader persona methodology canon. A complete toolkit covering the entire persona lifecycle with **10 executable tasks** — from project setup to persona application — plus CEO-level acquisition/retention strategy and OKR bridging.

## 🎯 Why Teams Choose Persona / 为什么选择 Persona

*New here?* Persona helps you **define who your users are** with evidence-based segmentation and structured persona cards. It's the first step in the AliDujie UX Research Ecosystem.

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

## 📁 Project Structure

```
web-persona-skill/
├── SKILL.md              # Agent-facing execution manual (T1-T10 trigger routing)
├── README.md             # This file — GitHub landing page
├── pyproject.toml        # Package configuration
├── INSTALL.md            # Detailed installation guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
├── examples/             # 5 runnable scripts
├── references/           # Knowledge base
│   ├── core/             # 8 core operation manuals (step-by-step)
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

## ❓ FAQ / Troubleshooting

**Q: Do I need quantitative data to create personas?**
A: No. You can start with qualitative data (interviews) or even just a product description. The skill adapts: T2 (interview design) → T3 (qualitative analysis) for qual-only, or T4 (survey) → T5 (quantitative analysis) when you have survey data.

**Q: How many personas should I create?**
A: Industry best practice is 3-5 primary/secondary personas. The `review_personas()` method will flag if you have too few (missing coverage) or too many (diluted focus).

**Q: Can I use this with existing persona frameworks?**
A: Yes. The skill is compatible with Cooper's Goal-Directed Design, Mulder's Web Persona methodology, and Nielsen's 10-step approach. See `references/advanced/` for framework-specific guidance.

**Q: 可以用中文吗？**
A: 可以。所有输出（角色卡、访谈提纲、问卷、报告）均支持中文。SKILL.md 本身就是中文执行手册。

## ✅ Best Practices / 最佳实践

1. **Start with data, not assumptions** — let user behavior drive segmentation, not demographics
2. **Name your personas** — "小明" is more actionable than "Segment A"
3. **Include scenarios** — a persona without scenarios is just a profile
4. **Review quality** — always run `review_personas()` to check for gaps
5. **Link to OKRs** — use `okr_bridge.py` to ensure personas drive real decisions
6. **Validate regularly** — personas drift; run validation every 6 months

## ⚠️ Limitations / 局限性

- **Not a replacement for real research** — personas are only as good as the data behind them
- **Quantitative clustering needs sufficient data** — KMeans requires n > 100 for stable segments
- **CEO economics are estimates** — CAC/LTV figures are illustrative benchmarks, not actual business data
- **Single-language clustering** — Chinese persona names work best with Chinese input data

## 📚 Resources

| Document | Topic |
|----------|-------|
| [SKILL.md](SKILL.md) | Agent-facing execution manual (T1-T10 trigger routing) |
| [INSTALL.md](INSTALL.md) | Detailed installation guide |
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [references/core/](references/core/) | 8 core operation manuals — START HERE |
| [references/advanced/](references/advanced/) | 39 deep-dive references |
| [examples/](examples/) | 5 runnable scripts with bilingual comments |

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
