#!/usr/bin/env python3
"""Example: User Segmentation with Behavioral Data.

Scenario: Segmenting users of a fitness app into distinct groups.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from persona import PersonaSkill

persona = PersonaSkill("Fitness App")

print("=" * 60)
print("User Segmentation: Fitness App")
print("=" * 60)

# Add behavioral segments (required: name, description, core_goals, typical_behaviors, key_attitudes)
persona.add_segment(
    "Dedicated Athletes",
    "High-frequency users who use all features",
    core_goals=["Hit weekly fitness targets", "Share achievements"],
    typical_behaviors=["Workout 5-7 days/week", "Use plan+track+social features"],
    key_attitudes=["Health is a priority", "Social motivation"],
    percentage=30
)
persona.add_segment(
    "Casual Movers",
    "Low-frequency users who need engagement nudges",
    core_goals=["Stay generally active"],
    typical_behaviors=["Workout 1-2 days/week", "Only use plan feature"],
    key_attitudes=["Want to be healthier", "Low commitment"],
    percentage=50
)
persona.add_segment(
    "Trackers Only",
    "Minimal engagement, high churn risk",
    core_goals=["Remember what they did"],
    typical_behaviors=["Occasional logging", "No planning"],
    key_attitudes=["Low motivation", "Forgetful"],
    percentage=20
)

# Render segments
print(persona.render_segments())

print("\n" + "=" * 60)
print("Segmentation Interpretation")
print("=" * 60)
print("""
  Segment 1: "Dedicated Athletes" (high frequency, full features)
  → 30% of users, 60% of revenue → Target for premium upgrades

  Segment 2: "Casual Movers" (low frequency, basic features)
  → 50% of users, 20% of revenue → Need engagement nudges

  Segment 3: "Trackers Only" (minimal engagement)
  → 20% of users, 5% of revenue → Risk of churn → re-engagement campaigns
""")
