# Web Persona Skill — Runnable Examples

Zero-dependency Python examples demonstrating Persona creation and application capabilities. Each script is standalone.

## Quick Start

```bash
PYTHONPATH=. python examples/01_persona_creation.py
PYTHONPATH=. python examples/02_segmentation.py
PYTHONPATH=. python examples/03_feature_prioritization.py
```

## Examples

| Script | What It Shows |
|--------|--------------|
| `01_persona_creation.py` | Creating data-driven personas from interview data |
| `02_segmentation.py` | 3-step user segmentation with behavioral clustering |
| `03_feature_prioritization.py` | Prioritizing features based on primary persona's core tasks |

## Try Before You Decide

```bash
PYTHONPATH=. python -c "
from persona import PersonaSkill
skill = PersonaSkill('My Product')
guide = skill.generate_interview('User Research', 'contextual')
print(guide)
"
```
