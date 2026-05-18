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


### 🔗 Cross-Skill Collaboration / 跨技能协作

| Persona 产出 → | 下游技能用它做... | 示例调用 |
|---------------|-----------------|----------|
| 角色档案 | [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 按角色做 Jobs 聚类 | `jtbd.score_opportunity()` per persona |
| 角色目标/痛点 | [VPD](https://github.com/AliDujie/value-proposition-design) 填充价值主张画布 | `vpd.analyze_canvas(jobs=persona.goals)` |
| 角色细分 | [UDM](https://github.com/AliDujie/universal-design-methods) 按角色设计研究方案 | `udm.generate_interview(persona.archetype)` |
| 角色行为数据 | [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) 定量验证假设 | `quantux.heart_framework(persona.behaviors)` |
| 角色统计数据 | [SWD](https://github.com/AliDujie/storytelling-with-data) 可视化汇报 | `swd.build_story(protagonist=persona.name)` |

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

> 💡 **Try it now / 立即尝试**:
> ```python
> from persona import PersonaSkill
> skill = PersonaSkill("你的产品")
> skill.add_persona(name="Alex", archetype="Power User", priority="primary", goals=["快速完成任务"])
> print(skill.review_personas())
> ```

## 🤖 AI Agent Integration

Persona is the **starting point** of the AliDujie ecosystem — making it an ideal first skill to integrate into any agent workflow:

```python
# Example: Persona as agent tools
from persona import PersonaSkill

persona = PersonaSkill("E-commerce Platform")

@tool
def create_user_persona(name: str, archetype: str, priority: str, goals: list, behaviors: list, attitudes: list, bio: str):
    """Create an evidence-driven user persona card."""
    return persona.add_persona(name=name, archetype=archetype, priority=priority, goals=goals, behaviors=behaviors, attitudes=attitudes, bio=bio)

@tool
def generate_user_interview(topic: str, sections: list):
    """Generate a structured user interview guide covering goals, behaviors, pain points."""
    return persona.generate_interview(topic, sections)

@tool
def prioritize_features(feature_name: str, persona_needs: dict, importance: str, effort: str):
    """Build a feature × persona priority matrix."""
    return persona.add_feature(feature_name, persona_needs, importance, effort)
```

### Agent Workflow Pattern
```
Product brief → Persona.add_persona() → Evidence-driven persona cards
     ↓
Persona review → Persona.review_personas() → Quality score + improvement suggestions
     ↓
Persona data → JTBD discovery → UDM research design → Full pipeline
```

### Prompt Engineering Tips
- **Evidence-first**: When creating personas via LLM, always reference real user data — use `review_personas()` to catch fiction masquerading as evidence
- **Golden Rules as guardrails**: Inject the 6 Persona Golden Rules into system prompts to guide LLM persona creation
- **Pipeline anchor**: Persona output feeds every downstream skill — start here for consistent research pipelines

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

```
┌─────────────────────────────────────────────────────────┐
│  PERSONA GOLDEN RULES  (6 Rules to Follow)              │
├─────────────────────────────────────────────────────────┤
│  1. Start from goals/behaviors, NOT demographics        │
│  2. What users DO > what they SAY                       │
│  3. Max 2 primary personas per product                  │
│  4. Total: 3-6 personas (enough to cover, not forget)   │
│  5. Bio = a story, not a list                           │
│  6. One-page per persona for sharing                    │
└─────────────────────────────────────────────────────────┘
```

1. **Never start from demographics** — focus on goals, behaviors, attitudes
2. **What users DO matters more than what they SAY**
3. **Primary persona: max 2** — ensure clear design decision priorities
4. **Total personas: 3-6** — too few to cover, too many to remember
5. **Bio should be a narrative** — not a list, tell a story people remember
6. **One-page principle** — keep persona documents to one page for sharing

## 🔗 生态快速开始

Persona 是研究管道最前端的用户定义层——回答"我们为谁设计？"：

```python
# Persona（谁）→ JTBD（需要什么）→ UDM（怎么研究）→ VPD（价值）→ SWD（呈现）
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from vpd import VPDSkill
from swd import SWDSkill

p = PersonaSkill("电商平台")      # 定义目标用户
j = JTBDSkill("电商平台")         # 发现用户任务
u = UDMSkill("电商平台")         # 设计研究方法
v = VPDSkill("电商平台", "用户")   # 验证价值主张
s = SWDSkill("用户报告")          # 向高管呈现
```

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
persona.add_persona(name="Xiao Ming", archetype="Efficiency User", priority="primary",
    quote="I just want to get things done fast",
    goals=["Fast checkout"], behaviors=["Uses search frequently"],
    attitudes=["Efficiency first"], bio="Busy white-collar worker")
persona.add_persona(name="Xiao Hong", archetype="Explorer User", priority="secondary",
    quote="Discovering good products makes me happy",
    goals=["Discover products"], behaviors=["Careful comparison"],
    attitudes=["Values experience"], bio="Young designer who loves finding unique items")

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

## ⚡ 30-Second Quick Start / 30秒快速开始

```python
from persona import PersonaSkill

# One-liner: create a persona and review quality
p = PersonaSkill("Your Product")
p.add_persona(name="Alex", archetype="Power User", priority="primary", goals=["Complete tasks fast"])
print(p.review_personas())
```

## 🧪 Testing

```bash
cd web-persona-skill
python persona/tests/test_all.py
# Or with pytest:
python -m pytest persona/tests/test_all.py -v
```


### ⏱️ 5-Minute Quick-Start Checklist

- [ ] **Install** — `cp -r web-persona-skill /your/agent/skills/`
- [ ] **Import** — `from persona import PersonaSkill`
- [ ] **Initialize** — `skill = PersonaSkill("Your Product")`
- [ ] **Interview guide** — `skill.generate_interview("User Interview", ["goals", "behaviors", "pain_points"])`
- [ ] **Create persona** — `skill.add_persona(name="Alex", archetype="Power User", priority="primary", ...)`
- [ ] **Quality review** — `skill.review_personas()` (12-item check)
- [ ] **Feature matrix** — `skill.render_feature_matrix()`
- [ ] **CEO analysis** — `skill.generate_persona(include_ceo_analysis=True, total_users=100000)`

### ⏱️ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r web-persona-skill /your/agent/skills/`
- [ ] **导入** — `from persona import PersonaSkill`
- [ ] **初始化** — `skill = PersonaSkill("你的产品")`
- [ ] **访谈提纲** — `skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"])`
- [ ] **创建角色** — `skill.add_persona(name="Alex", archetype="Power User", priority="primary", ...)`
- [ ] **质量评审** — `skill.review_personas()`（12 项检查）
- [ ] **功能矩阵** — `skill.render_feature_matrix()`
- [ ] **CEO 分析** — `skill.generate_persona(include_ceo_analysis=True, total_users=100000)`

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
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | Strategic business frameworks | `STMSkill` |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | CTO-level tech strategy & architecture guidance | `CTOSkill` |

### 🔗 Extended Ecosystem

Persona user definition can be combined with management skills to turn user insights into organizational decisions:

| Extended Skill | Collaboration Scenario |
|---------------|----------------------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Persona user economics → CEO resource allocation |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | Persona segments → CPO audience prioritization |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | Persona roles → CMO target audience positioning |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | Persona tech behaviors → CTO tech investment priorities |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | Persona quarterly updates → CEO plan review |

### 💡 Pro Tips / 专业技巧
- **Goals > demographics**: Never start persona creation with age/gender — start with what users are trying to accomplish
- **Max 2 primary personas**: If everyone is primary, no one is — force prioritization to drive clearer design decisions
- **Behavioral evidence wins**: What users *do* (analytics data, task flows) trumps what they *say* in surveys
- **P0 bug rule**: Any bug blocking a primary persona's core task is P0 — use this to cut through prioritization debates
- **Story bios beat bullet points**: "Alex loses 2 hours daily to status meetings" is more actionable than "Age: 32, Role: PM"
- **Use the quality review early**: Run `review_personas()` before presenting — scores below 80 mean you need more evidence
- **Chain with ecosystem**: Persona defines who → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) discovers what → [UDM](https://github.com/AliDujie/universal-design-methods) validates how → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) quantifies → [VPD](https://github.com/AliDujie/value-proposition-design) maps value → [SWD](https://github.com/AliDujie/storytelling-with-data) presents

## 🛡️ Common Pitfalls & How to Avoid Them

| Pitfall | How Persona Helps |
|---------|---------------|
| Fictional personas nobody trusts | `review_personas()` runs 12-item quality check to catch evidence gaps |
| Too many personas to remember | Enforces max 2 primary, 3-6 total — forces real prioritization |
| Personas gathering dust in a folder | `generate_acquisition_strategy()` + promotion plans keep them alive |
| Design decisions still subjective | `render_feature_matrix()` ties every feature to a specific persona need |
| Personas that don't drive decisions | `add_bug()` auto-prioritizes by persona impact — P0/P1/P2 |

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

## 🏗️ Advanced: Custom Configuration

Persona supports runtime configuration via the `AnalysisConfig` class:

```python
from persona import PersonaSkill, AnalysisConfig

config = AnalysisConfig()
config.set_max_personas(6)      # Cap total personas
config.set_primary_persona_limit(2)  # Max 2 primary personas
config.set_review_threshold(80)  # Minimum quality score to pass

skill = PersonaSkill("My Product", config=config)
```

See [INSTALL.md](INSTALL.md) for full configuration options and agent integration guides.

## 📊 Version History

See [CHANGELOG.md](CHANGELOG.md) for full release notes.

**Latest (v2.4.79)**: Added cross-skill collaboration table linking to all 5 ecosystem skills, improved Pro Tips section with persona creation guidance.

## 📚 Resources

- [SKILL.md](SKILL.md) — Agent-facing skill definition and prompt templates
- [USAGE.md](USAGE.md) — Detailed usage guide with code examples / 详细使用指南
- [INSTALL.md](INSTALL.md) — Detailed installation guide and agent integration
- [CONTRIBUTING.md](CONTRIBUTING.md) — How to contribute
- [CHANGELOG.md](CHANGELOG.md) — Version history
- [SECURITY.md](SECURITY.md) — Security policy and responsible use
- [references/](references/) — Persona template files and interview guides
- [persona/](persona/) — Core Python module source code

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**Built with ❤️ as part of the AliDujie UX Research Ecosystem**

**Persona** · [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) · [UDM](https://github.com/AliDujie/universal-design-methods) · [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) · [VPD](https://github.com/AliDujie/value-proposition-design) · [SWD](https://github.com/AliDujie/storytelling-with-data) · [STM](https://github.com/AliDujie/Structured-Thinking-Model)
