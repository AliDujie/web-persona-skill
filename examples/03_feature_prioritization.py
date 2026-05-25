#!/usr/bin/env python3
"""Example: Feature Prioritization by Persona Impact.

Scenario: Deciding which features to build next based on persona needs.
"""
from persona import PersonaSkill

persona = PersonaSkill("Productivity App")

print("=" * 60)
print("Feature Prioritization: Productivity App")
print("=" * 60)

priority = persona.feature_priority(
    features=[
        "AI meeting summaries",
        "Calendar integration",
        "Team dashboard",
        "Focus mode timer"
    ],
    primary_persona="Busy Manager Mike"
)
print(priority)

print("\n" + "=" * 60)
print("Bug Prioritization: P0 blocks primary persona's core task")
print("=" * 60)
print("""
  P0 (Fix immediately): Homepage loads slowly
    → Blocks primary persona's core task (check daily priorities)

  P1 (Fix this sprint): Search doesn't find archived tasks
    → Impairs secondary persona's occasional workflow

  P2 (Fix when convenient): Export formatting is ugly
    → Nice-to-have, doesn't block any core task
""")
