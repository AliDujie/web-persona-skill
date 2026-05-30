# Web Persona Skill

> **从 0 到 1 创建人物角色的实操工具集**

📖 [GitHub Repository](https://github.com/AliDujie/web-persona-skill)

![Version](https://img.shields.io/badge/version-3.3.1-blue)
![Python](https://img.shields.io/badge/Python-3.8%2B-green)
![License](https://img.shields.io/badge/License-MIT-orange)
![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

---

## What's New

### v3.3.1 - Version sync and consistency fix
- Fixed version inconsistency across pyproject.toml (3.1.0), README badge (3.0.0), and SKILL.md (3.3.0)
- All files now consistently report v3.3.1


**Complete architectural restructure — from "book index" to "execution manual".**

v3.0 fundamentally reorganizes how this skill delivers knowledge. Instead of 39 reference files organized by book/author, there are now:

- **8 core operation manuals** (`references/core/01-08`) that walk you through the entire persona process step-by-step, from project setup to ongoing application
- **39 advanced references** (`references/advanced/`) preserved as a deep-dive dictionary for when you need to go deeper on specific topics

### Why this matters

Previous versions (v2.5–v2.7) kept adding references, growing from 5 to 39 files. The result was comprehensive but hard to navigate — users had to know *which book* to look up rather than *what step they were at*. v3.0 solves this by organizing around the execution lifecycle.

### Structure

```
references/
├── core/                     ← START HERE: 8 step-by-step guides
│   ├── 01-project-setup.md       立项：该不该做？选什么方法？组什么团队？
│   ├── 02-qualitative-research.md 定性路径全流程
│   ├── 03-quantitative-research.md 定量路径全流程
│   ├── 04-mixed-method.md         混合路径
│   ├── 05-analysis-clustering.md  从数据到分群
│   ├── 06-persona-creation.md     角色塑造+叙事技巧
│   ├── 07-validation.md           验证精化
│   └── 08-application.md          应用落地+维护
├── advanced/                 ← DEEP DIVE: 39 method references
│   ├── 01-05: Mulder系列
│   ├── 06-15: 经典书系
│   ├── 16-27: ABCD深化
│   ├── 28-31: 工程化配套
│   └── 32-39: 上游研究+体验地图
└── README.md
```

### Key design decisions

1. **Organized by execution stage, not by book** — find what you need based on where you are in the process
2. **Each core doc is self-contained** — includes steps, templates, checklists, and common mistakes
3. **Cross-references to advanced/** — when you want to go deeper, each core doc points you to the relevant advanced reference
4. **SKILL.md reduced from 864 → ~120 lines** — quick reference only, details live in core docs

---

## Quick Start

```python
from persona import PersonaSkill

skill = PersonaSkill("你的产品")
skill.add_persona(name="Alex", archetype="Power User", priority="primary",
                  goals=["快速完成任务"])
print(skill.render_all_personas())
```

## Python Modules

| Module | Purpose |
|--------|---------|
| `persona/clustering.py` | Statistical clustering (KMeans/LCA/Factor) |
| `persona/llm_prompts.py` | LLM prompt templates (interview/evaluation/debate) |
| `persona/okr_bridge.py` | Persona → OKR → Roadmap bridge |
| `persona/measurement_toolkit.py` | NPS/CES/CSAT/funnel measurement |

## Earlier Releases

- **v2.7.0** (2026-05-29): Added upstream research craft (Portigal/Fitzpatrick/Torres/Alvarez) + experience mapping & narrative (Kalbach/Quesenbery/Kuniavsky/Christensen)
- **v2.6.0** (2026-05-29): ABCD deep-dive — quantitative/psychology/ethics/engineering + 4 Python modules
- **v2.5.0** (2026-05-29): 10 classic book references, multi-perspective meta-decider upgrade
- **v2.4.97**: Initial Mulder-based single-method executor

## License

MIT
