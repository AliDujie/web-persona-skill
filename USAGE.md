# Web Persona Skill — Usage Guide

> 用户画像 · 使用指南

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

## 📚 Resources / 资源

- [README.md](README.md) — Full documentation
- [SKILL.md](SKILL.md) — Agent-facing skill definition
- [INSTALL.md](INSTALL.md) — Installation guide
- [CHANGELOG.md](CHANGELOG.md) — Version history
