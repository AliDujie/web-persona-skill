#!/usr/bin/env python3
"""Example: User Segmentation with Behavioral Clustering.

Scenario: Segmenting users of a fitness app into 3 distinct groups.
"""
from persona import PersonaSkill

persona = PersonaSkill("Fitness App")

print("=" * 60)
print("3-Step Segmentation: Fitness App Users")
print("=" * 60)

segmentation = persona.quick_segment(
    behaviors=[
        {"user": 1, "workouts_per_week": 5, "features_used": ["plan", "track", "social"]},
        {"user": 2, "workouts_per_week": 2, "features_used": ["plan"]},
        {"user": 3, "workouts_per_week": 7, "features_used": ["plan", "track", "social", "nutrition"]},
        {"user": 4, "workouts_per_week": 1, "features_used": ["track"]},
    ]
)
print(segmentation)

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
