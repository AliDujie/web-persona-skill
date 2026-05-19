# Web Persona Skill — Usage Guide

> 用户画像 · 使用指南

## 📐 Where Persona Fits in the Pipeline

```
Persona (Who) → JTBD (What) → UDM (Research) → QuantUX (Validate) → VPD (Value) → SWD (Present)
↑
Persona sits here — the starting point
```

- **First in the pipeline** — defines who you're designing for before anything else
- **Before** JTBD discovers Jobs, UDM plans research, and all other skills
- **Persona** provides evidence-driven user profiles that anchor every downstream decision

## ⚡ 5-Minute Quick Start / 5分钟快速开始

```bash
cp -r web-persona-skill /your/agent/skills/
python -c "
from persona import PersonaSkill
skill = PersonaSkill('My Product')
skill.add_persona(name='Alex', archetype='Power User', priority='primary', goals=['Complete tasks fast'])
print(skill.review_personas())
"
```

## 🔑 Core Workflows / 核心工作流

### 1. Create Personas / 创建用户画像

```python
from persona import PersonaSkill

skill = PersonaSkill("E-commerce Platform")

skill.add_persona(
    name="Xiao Ming",
    archetype="Efficiency-focused user",
    priority="primary",
    quote="I just want to get things done quickly",
    goals=["Place orders fast", "Track delivery status"],
    behaviors=["Uses search, skips browsing"],
    attitudes=["Efficiency first"],
    bio="Xiao Ming is a busy white-collar worker who shops online during lunch breaks"
)
skill.add_persona(
    name="Xiao Hong",
    archetype="Explorer user",
    priority="secondary",
    quote="Discovering good products is what makes me happy",
    goals=["Discover unique products", "Compare options thoroughly"],
    behaviors=["Careful comparison, reads reviews"],
    attitudes=["Values experience over speed"],
    bio="Xiao Hong is a young designer who treats shopping as a hobby"
)

print(skill.render_all_personas())
```

### 2. Interview + Survey / 访谈 + 问卷

```python
# Generate interview guide
guide = skill.generate_interview("User Interview", ["goals", "behaviors", "pain_points"])

# Design survey
survey = skill.generate_survey("Needs Validation", "needs",
    pain_points=["Search inaccurate", "Pricing unclear"])
```

### 3. User Segmentation / 用户分群

```python
# 3-dimension segmentation (goals/behaviors/attitudes)
segmentation = skill.segment_analyzer(
    users=[
        {"name": "User1", "goals": "speed", "behaviors": "search-heavy", "attitudes": "efficiency"},
        {"name": "User2", "goals": "discovery", "behaviors": "browse-heavy", "attitudes": "experience"},
    ]
)
```

### 4. Quality Review / 质量评审

```python
# 12-item quality check
review = skill.review_personas()
# Checks: evidence-based, distinct, actionable, memorable, etc.
```

### 5. Feature Prioritization / 功能优先级

```python
# Build feature × persona matrix
skill.add_feature("Quick checkout", {"Xiao Ming": "high", "Xiao Hong": "low"}, "high", "low")
skill.add_feature("Product discovery", {"Xiao Ming": "low", "Xiao Hong": "high"}, "medium", "medium")
print(skill.render_feature_matrix())

# Bug prioritization (P0 = blocks primary persona's core task)
bug = skill.add_bug("Homepage loads slowly", "Xiao Ming", is_primary=True, blocks_core=True)
# → P0: Homepage loads slowly (blocks primary persona's core task — fix immediately)
```

### 6. CEO Economic Model / CEO 经济模型

```python
report = skill.generate_persona(include_ceo_analysis=True, total_users=100000)
# → Persona scale, CAC, LTV, LTV/CAC health, acquisition strategy, retention analysis
```

## 📋 Common Scenarios / 常见场景

| Scenario | Flow | APIs |
|----------|------|------|
| SaaS segmentation | Segment → Interview → Persona | `segment_analyzer()` → `generate_interview()` → `add_persona()` |
| Persona refresh | Analytics → Survey → Update | `generate_survey()` → `add_persona()` → `review_personas()` |
| Feature roadmap | Persona → Feature matrix → Priority | `add_persona()` → `add_feature()` → `render_feature_matrix()` |
| Executive buy-in | Persona → CEO economic model | `generate_persona(include_ceo_analysis=True)` |

## 🏆 Golden Rules / 黄金法则

1. **From goals/behaviors, not demographics** — 从目标/行为出发，不是人口统计
2. **What users DO > what they SAY** — 行为大于言辞
3. **Max 2 primary personas** — 首要角色不超过2个
4. **Total 3-6 personas** — 太少覆盖不足，太多记不住
5. **Bio = a story** — 讲故事，不是列清单
6. **One-page per persona** — 每页一个画像，方便分享

## 🔗 Ecosystem Integration / 生态协作

```python
# Persona (who) → JTBD (what) → UDM (how) → VPD (value) → SWD (present)
from persona import PersonaSkill
from jtbd import JTBDSkill
from vpd import VPDSkill
from swd import SWDSkill

persona = PersonaSkill("E-commerce")
persona.add_persona(name="Xiao Ming", archetype="Efficiency User", priority="primary",
    goals=["Fast checkout"], behaviors=["Uses search"],
    attitudes=["Efficiency first"], bio="Busy professional")

jtbd = JTBDSkill("E-commerce")
score = jtbd.score_opportunity("Buy quickly", struggle=4, alternative=3, market=5, budget=4)

vpd = VPDSkill("E-commerce", "Xiao Ming")
canvas = vpd.analyze_canvas(product_name="Quick Checkout",
    jobs=[{"description": "Fast checkout", "importance": 5}])

swd = SWDSkill("User Report")
story = swd.build_story(protagonist="Product Team",
    imbalance="Primary persona needs faster checkout",
    call_to_action="Invest in one-page checkout")
```

## 🧪 Testing / 测试

```bash
cd web-persona-skill
python persona/tests/test_all.py
```

## 🎯 Persona Anti-Patterns / 画像常见误区

Below are the most common persona mistakes — and what to do instead.

### ❌ Mistake 1: Demographic-Based Personas / 基于人口统计的画像

**Wrong:** "Female, 25-34, urban, college-educated, income ¥10k+"
**Right:** "Needs to compare products across 3+ stores before buying; uses mobile during commute; abandons cart if shipping > ¥15"

> **Demographics describe *who* — personas need *why* and *how*.**  Start from goals, behaviors, and attitudes. Demographics can supplement, but never lead.

### ❌ Mistake 2: Too Many Primary Personas / 首要角色过多

**Wrong:** Marking all 5 personas as "primary" because "every user matters."
**Right:** Max **2 primary personas**. If everyone is primary, no one is — you lose the ability to make clear prioritization decisions.

> **Primary personas drive design decisions.**  When trade-offs arise, ask: "What does our primary persona need?" If there's no primary, there's no answer.

### ❌ Mistake 3: Fictional Instead of Evidence-Based / 虚构而非基于证据

**Wrong:** Inventing personas from team assumptions or stakeholder guesses with no user data behind them.
**Right:** Every persona element (goals, behaviors, pain points) traces back to real evidence — interviews, analytics, survey data, or support tickets. Use `review_personas()` to catch evidence gaps (12-item quality check, scores < 80 need more data).

> **A persona without evidence is just a stereotype with a name.**  没有证据的画像只是贴了标签的刻板印象。

### ❌ Mistake 4: Personas That Gather Dust / 创建后束之高阁

**Wrong:** Creating beautiful persona cards, printing them, and never referencing them again.
**Right:** Tie every feature decision, bug priority, and design review back to personas. Use `render_feature_matrix()` to force persona-driven prioritization. Run quarterly persona refreshes with new data.

> **Personas are decision tools, not wall art.**  画像是决策工具，不是墙上的装饰画。

### ❌ Mistake 5: Bio as a Bullet List / 画像简介写成清单

**Wrong:** "Age: 32. Role: PM. Pain: Meetings. Tech: iPhone."
**Right:** "Alex is a senior PM juggling 5 teams. She loses 2 hours daily to status meetings and switches between 4 tools just to check if a feature shipped."

> **A bio should tell a story people remember.**  简介应该是一个让人记住的故事，而不是一堆干巴巴的条目。

---

### 🛡️ Quick Reference: Anti-Pattern Checklist / 速查清单

| Anti-Pattern | Red Flag | Fix |
|-------------|----------|-----|
| Demographic-led | Persona starts with age/gender/income | Start with goals, behaviors, attitudes |
| Too many primaries | > 2 personas marked "primary" | Force prioritization — pick top 1-2 |
| Fictional | No data source cited for any attribute | Run `review_personas()` — score must be ≥ 80 |
| Unused | Last referenced > 30 days ago | Embed in feature reviews, bug triage, roadmap planning |
| List-style bio | Bio reads like a résumé | Rewrite as a 2-3 sentence narrative with context |

## 🔗 Related Skills in the Ecosystem / 生态系统中的相关技能

Persona is the **user definition layer** — the starting point that anchors every downstream skill:

| Skill | Role | How It Connects with Persona |
|-------|------|----------------------------|
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | Demand insight | JTBD task clusters → Persona segment definition → evidence-driven profiles |
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | Methodology core | UDM interviews/observation → Persona data collection → persona creation |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | Quantitative validation | Persona hypotheses → QuantUX behavioral analysis → persona iteration |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Product-market fit | Persona goals/pains → VPD canvas → persona validation |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Data storytelling | Persona data → SWD chart selection → executive narrative |

> 💡 **Recommended chain:** Persona (define who) → JTBD (discover what Jobs) → UDM (research how) → QuantUX (validate) → VPD (map value) → SWD (present)

### Quick Cross-Skill Example / 跨技能示例

```python
from persona import PersonaSkill
from jtbd import JTBDSkill
from vpd import VPDSkill
from swd import SWDSkill

# Persona defines who we're designing for
persona = PersonaSkill("E-commerce Platform")
persona.add_persona(name="Alex", archetype="Efficiency Seeker", priority="primary",
    goals=["Complete purchase in under 2 minutes"],
    behaviors=["Uses search, rarely browses"],
    attitudes=["Values time over discovery"],
    bio="Alex is a busy professional who shops online during commute")

# JTBD discovers what Jobs this persona needs done
jtbd = JTBDSkill("E-commerce Platform")
score = jtbd.score_opportunity("Find and purchase quickly", struggle=4, alternative=3, market=4, budget=4)

# VPD maps persona needs to value proposition
vpd = VPDSkill("E-commerce Platform", "Efficiency Seekers")
vpd.analyze_canvas(product_name="ShopFast",
    jobs=[{"description": "Quick purchase"}],
    pains=[{"description": "Too many steps to checkout", "severity": "critical"}])

# SWD presents persona data to stakeholders
swd = SWDSkill("Persona Report")
story = swd.build_story(protagonist="Product Team",
    imbalance="Efficiency seekers abandon at checkout",
    call_to_action="Reduce checkout to 2 steps")
```

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CHANGELOG.md](CHANGELOG.md) — Version history
