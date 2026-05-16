# Web Persona Skill

> **Evidence-Driven User Personas — Know Who You're Designing For.**

![Version](https://img.shields.io/badge/version-2.4.79-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-None-lightgrey)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

## 🇨🇳 中文概览

- **基于证据的用户画像**: 摒弃空想人物设定，用目标、行为、态度三个维度构建真实用户画像
- **11 项可执行能力**: 方法选择、访谈提纲、问卷设计、用户分群、画像生成、质量审查、商业策略、功能优先级、设计指导、测试规划、CEO 经济模型
- **零依赖纯 Python**: 无需 `pip install`，`from persona import PersonaSkill` 即可使用
- **生态起点**: 作为用户定义层，为 JTBD、UDM、QuantUX、VPD、SWD 提供用户基础数据

Based on *The User Is Always Right* by Steve Mulder & Ziv Yaar (2006). A complete toolkit for **web user persona creation and application**, with **10+ executable capabilities** covering method selection, interview guides, survey design, user segmentation, persona document creation, quality review, business strategy, feature prioritization, design guidance, test planning, and CEO-level economic modeling.

## 🌟 Why Persona?

| Challenge | Without Persona | With Persona |
|-----------|----------------|-------------|
| User Understanding | "Our users" — vague concept | Specific profiles with goals + behaviors |
| Design Decisions | "I think users want..." — subjective | "Alex needs to complete tasks fast" — evidence-driven |
| Team Alignment | Everyone imagines different users | Shared persona cards, unified decisions |
| Feature Priorities | Satisfy everyone = satisfy nobody | Prioritize by primary persona needs |
| Onboarding | "Let me tell you about users" | "Here's our persona cards" — instant understanding |

> **🏆 Proven Impact**: Teams that use evidence-driven personas report **30% fewer design rework cycles** because decisions are anchored to specific user goals and behaviors rather than assumptions.

## 💡 为什么选择 Persona？

> **Persona 是整个 AliDujie UX 研究生态的用户定义层，是所有研究的起点。** 基于 Steve Mulder《赢在用户》全书体系，摒弃拍脑袋的虚构人物，用目标、行为、态度三维度构建真实用户画像。11 项可执行能力从方法选择→访谈→问卷→分群→画像→质量评审→商业策略→功能优先级→设计指导→测试规划→CEO 经济模型全覆盖。配合 CEO 视角的用户经济模型（LTV/CAC），让人物角色直接驱动商业决策。
>
> *"创建 Persona 后，团队终于统一了'为谁设计'——功能优先级从'满足所有人'变成'先满足首要角色'。"*

## ⚡ Quick Start (5 Minutes)

### Install

```bash
cp -r web-persona-skill /your/agent/skills/
```

For detailed installation steps, configuration options, and agent integration guides, see [INSTALL.md](INSTALL.md).

### Use in Python

```python
from persona import PersonaSkill

# Initialize with your product name
skill = PersonaSkill("E-commerce Platform")

# 1. Generate interview guide
guide = skill.generate_interview("User Interview", ["goals", "behaviors", "pain_points"])
print(guide)

# 2. Design survey
survey = skill.generate_survey("Needs Survey", "needs", pain_points=["Search inaccurate", "Pricing unclear"])
print(survey)

# 3. Create personas
skill.add_persona(
    name="Xiao Ming",
    archetype="Efficiency-focused user",
    priority="primary",
    quote="I just want to get things done quickly",
    goals=["Place orders fast"],
    behaviors=["Frequent use of search"],
    attitudes=["Efficiency first"],
    bio="Xiao Ming is a busy white-collar worker..."
)
skill.add_persona(
    name="Xiao Hong",
    archetype="Explorer user",
    priority="secondary",
    quote="Discovering good products is what makes me happy",
    goals=["Discover unique products"],
    behaviors=["Careful comparison"],
    attitudes=["Values experience"],
    bio="Xiao Hong is a young designer..."
)

# 4. Output all persona documents
print(skill.render_all_personas())

# 5. Review persona quality (12-item check)
print(skill.review_personas())

# 6. Feature prioritization by persona
skill.add_feature("Quick checkout", {"Xiao Ming": "high", "Xiao Hong": "low"}, "high", "low")
print(skill.render_feature_matrix())

# 7. Bug prioritization (P0 = blocks primary persona's core task)
bug = skill.add_bug("Homepage loads slowly", "Xiao Ming", is_primary=True, blocks_core=True)
print(bug)
# → P0: Homepage loads slowly (blocks primary persona's core task — fix immediately)

# 8. Full report with CEO economic analysis
report = skill.generate_persona(include_ceo_analysis=True, total_users=100000)
print(report)
```

**Zero dependencies** — pure Python standard library. No `pip install` needed.

## 🧩 10+1 Capabilities

### Core Capabilities (10)

| # | Capability | What It Does |
|---|-----------|-------------|
| 1 | **Method Selection** | Qualitative/quantitative/hybrid path recommendation based on budget/time/team |
| 2 | **Interview Guide** | Goal/behavior/pain/expectation sections, customizable questions |
| 3 | **Survey Design** | Needs/validation/satisfaction survey types with Likert scales |
| 4 | **User Segmentation** | Goal/behavior/attitude 3-dimension, 2×2 matrix, segmentation evaluation |
| 5 | **Persona Document Creation** | Full persona cards (name/bio/goals/behaviors/scenarios), comparison tables, quality review |
| 6 | **Persona Promotion** | Promotion plans, poster/card copy, workshop facilitation |
| 7 | **Business Strategy** | Persona commercial value assessment, differentiation strategies, resource allocation |
| 8 | **Feature Prioritization** | Feature × persona needs matrix, P0-P3 ranking, competitive feature comparison |
| 9 | **Design Guidance** | Information architecture, content strategy, path validation (3-step rule) |
| 10 | **Results Measurement** | QA test scripts, metric system, bug priority auto-calculation |

### CEO Extensions

| Method | Output |
|--------|--------|
| `generate_persona_economics(total_users)` | Persona scale, CAC, LTV, LTV/CAC health |
| `generate_acquisition_strategy()` | Acquisition channels, budget allocation, ROI, timeline |
| `generate_retention_strategy()` | Retention rates, churn alerts, lifecycle management |
| `generate_persona(include_ceo_analysis=True)` | Full profile + all CEO analysis (one-click) |

## 📐 Golden Rules

1. **Never start from demographics** — focus on goals, behaviors, attitudes
2. **What users DO matters more than what they SAY**
3. **Primary persona: max 2** — ensure clear design decision priorities
4. **Total personas: 3-6** — too few to cover, too many to remember
5. **Bio should be a narrative** — not a list, tell a story people remember
6. **One-page principle** — keep persona documents to one page for sharing

## 🌐 Ecosystem Integration

Persona is the **user definition layer** at the very front of the research pipeline — it answers "who are we designing for?":

```
Persona → JTBD/UDM → QuantUX → VPD → SWD → STM
  ↑ You are here
```

| Downstream Skills | Collaboration |
|------------------|---------------|
| JTBD (need insights) | Persona segments → JTBD task clustering → persona documents |
| UDM (methodology) | UDM interviews/observation → Persona data collection → persona creation |
| QuantUX (quantitative) | Persona hypotheses → QuantUX behavior verification → persona refinement |
| VPD (value validation) | Persona goals/pains → VPD canvas → Persona validation |
| SWD (data storytelling) | Persona data → SWD chart selection → SWD story building |
| STM (strategic analysis) | STM competitive analysis → Persona market positioning |

Cross-skill example:
```python
# UDM → Persona → VPD → SWD full pipeline
from udm import UDMSkill
from persona import PersonaSkill
from vpd import VPDSkill
from swd import SWDSkill

# Step 1: UDM collects user research data
udm = UDMSkill("E-commerce")
interview = udm.generate_interview("User Interviews", "contextual")

# Step 2: Persona creates role documents
persona = PersonaSkill("E-commerce")
persona.add_persona("Xiao Ming", "Efficiency User", "primary", goals=["Fast checkout"])
persona.add_persona("Xiao Hong", "Explorer User", "secondary", goals=["Discover products"])

# Step 3: VPD maps to value proposition
vpd = VPDSkill("E-commerce", "Xiao Ming")
canvas = vpd.analyze_canvas(product_name="E-commerce", jobs=[{"description": "Fast checkout"}])

# Step 4: SWD presents to executives
swd = SWDSkill("User Report")
ctx = swd.build_context(audience="Product Team", cta="Optimize design for primary persona")
```

## 📖 Knowledge Base

| File | Core Content |
|------|-------------|
| `references/01-persona-basics.md` | Persona fundamentals, 3 creation paths, segmentation principles, persona anatomy, priority framework |
| `references/02-measuring-results.md` | Pre-launch testing, post-launch measurement, persona-based analytics, quantitative measurement system |
| `references/03-persona-best-practices.md` | Persona lifecycle management, promotion strategies, organizational adoption |
| `references/04-persona-driven-workflows.md` | Persona-driven design workflows across the product lifecycle |
| `references/05-ecosystem-collaboration.md` | Cross-skill collaboration patterns and examples |

## 📁 Project Structure

```
web-persona-skill/
├── SKILL.md              # Agent-facing skill definition
├── README.md             # This file — GitHub landing page
├── pyproject.toml        # Package configuration
├── requirements.txt      # No external dependencies
├── INSTALL.md            # Detailed installation guide
├── CHANGELOG.md          # Version history
├── LICENSE               # MIT License
├── CODE_OF_CONDUCT.md    # Community standards
├── CONTRIBUTING.md       # Contribution guidelines
├── references/           # 5 knowledge base documents
├── persona/              # Python executable toolkit
│   ├── __init__.py       # PersonaSkill unified entry point
│   ├── config.py         # Global configuration
│   ├── utils.py          # Knowledge base loading & search
│   ├── templates.py      # Template constants
│   ├── interview.py      # InterviewBuilder: 8 sections (warmup~closing)
│   ├── survey.py         # SurveyBuilder: needs/validation/satisfaction
│   ├── segment.py        # SegmentAnalyzer: user segmentation + 2×2 matrix
│   ├── persona_builder.py # PersonaBuilder: creation + review (12 items)
│   ├── strategy.py       # StrategyAnalyzer: business value + features + competitors
│   ├── design.py         # DesignAdvisor: IA + content + path validation
│   ├── measure.py        # MeasureSystem: test scripts + metrics + bug P0-P3
│   └── tests/
│       └── test_all.py   # 8 test cases
└── .github/              # CI/CD workflows & issue templates
```

## 🧪 Testing

```bash
cd web-persona-skill
python persona/tests/test_all.py
# Or with pytest:
python -m pytest persona/tests/test_all.py -v
```

## 📋 Real-World Use Cases

### 🏢 SaaS Product Segmentation
*Goal: Understand who uses your product before designing new features.*
→ Use `segment_analyzer()` with goal/behavior/attitude dimensions to create a 2×2 matrix. Generate interview guides with `generate_interview()` to validate each segment, then build persona cards with `add_persona()` for the top 3-4 segments. Run `review_personas()` to ensure quality.

### 🛒 E-commerce Persona Refresh
*Goal: Update outdated personas with fresh behavioral data.*
→ Feed analytics data into the `SegmentAnalyzer` to identify behavioral shifts. Use `generate_survey("needs")` to validate findings with a representative sample. Update persona cards with new `bio`, `goals`, and `behaviors` fields.

### 🎯 B2B Persona-Driven Roadmap
*Goal: Prioritize features by primary persona needs.*
→ After creating personas, use `add_feature()` to build a feature × persona matrix. Apply `render_feature_matrix()` to see which features serve the primary persona. Use `add_bug()` to auto-prioritize bugs that block primary persona core tasks (P0).

### 🏥 Healthcare Portal Persona Creation
*Goal: Create personas for a multi-stakeholder healthcare system.*
→ Start with `segment_analyzer()` to identify patient, provider, and admin segments. Generate contextual interview guides with `generate_interview("User Interview", ["goals", "behaviors", "pain_points"])`. Build 4-5 persona cards and run `review_personas()` for a quality score above 80/100.

## 📋 Classic Cases

| Case | Industry | Key Insight |
|------|---------|------------|
| VistaPrint | Online printing | Predictive model 70% accuracy in identifying high-value users |
| BrownCo | Financial brokerage | Used personas to subtract features rather than chase giants |
| CNN.com | News media | 6 personas rolled out company-wide, execs distributed "We're not the target user" T-shirts |
| Best Buy | Retail | Personas guided store optimization, target customer spending increased 30% |
| Sony Boom Box | Consumer electronics | Users said they wanted yellow but picked black — proved actions ≠ words |

## 📋 When NOT to Use Persona

- **Choosing research methods or designing interviews** → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods)
- **Statistical analysis or A/B testing** → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **Understanding user Jobs-to-be-Done** → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **Value proposition canvas analysis** → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)
- **Data visualization & storytelling** → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)

## 📚 References

| Book | Author | Contribution |
|------|--------|-------------|
| **The User Is Always Right** | Steve Mulder & Ziv Yaar (2006) | Foundation — persona creation and application |
| About Face | Alan Cooper (2014) | Goal-directed design methodology |
| The Inmates Are Running the Asylum | Alan Cooper (1999) | Origin of the persona concept |
| Storytelling with Data | Cole Nussbaumer Knaflic (2015) | Data visualization of research findings |

## 🔗 Extended Ecosystem

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Persona user economics → CEO resource allocation |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | Persona segments → CPO audience prioritization |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | Persona roles → CMO target audience positioning |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | Persona tech behaviors → CTO tech investment priorities |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | Persona quarterly updates → CEO plan review |

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

## ❓ FAQ / Troubleshooting

**Q: How many personas should I create?**
Aim for 3-6. Fewer than 3 means you haven't captured enough diversity. More than 6 and nobody will remember them. Max 2 should be marked as "primary" for clear prioritization.

**Q: What makes a good persona bio?**
Tell a story, not a list. "Alex is a 32-year-old project manager who juggles 5 teams and loses 2 hours daily to status meetings" is better than "Age: 32, Role: PM, Pain: Meetings". Make it memorable.

**Q: How do I know my personas are good quality?**
Use `review_personas()` — it runs a 12-item quality check covering evidence-based creation, distinctiveness, actionability, memorability, and more. Scores above 80/100 indicate strong personas.

**Q: Can I use Persona with analytics data?**
Yes. Start with behavioral data from analytics, then layer on qualitative insights from [UDM](https://github.com/AliDujie/universal-design-methods) interviews. The `SegmentAnalyzer` supports goal/behavior/attitude-based segmentation that maps directly to analytics cohorts.

**Q: What's the CEO economic model?**
Call `generate_persona(include_ceo_analysis=True, total_users=100000)` to auto-generate persona scale estimates, CAC, LTV, LTV/CAC ratio, acquisition strategy, and retention analysis — turning personas into business cases.

**Q: How does Persona connect to the rest of the AliDujie ecosystem?**
Persona is the starting point: it tells you *who* you're designing for. Then [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) discovers *what they need*, [UDM](https://github.com/AliDujie/universal-design-methods) tells you *how to research them*, [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) *validates* your hypotheses, [VPD](https://github.com/AliDujie/value-proposition-design) maps *how to deliver value*, and [SWD](https://github.com/AliDujie/storytelling-with-data) *presents* it all to stakeholders.

## 📚 Resources

- [INSTALL.md](INSTALL.md) — Detailed installation guide and agent integration
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — Community guidelines

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
