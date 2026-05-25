#!/usr/bin/env python3
"""Example: Creating Data-Driven Personas.

Scenario: Building personas for an online learning platform.
"""
from persona import PersonaSkill

persona = PersonaSkill("Online Learning Platform")

print("=" * 60)
print("Persona Creation: Online Learning Platform")
print("=" * 60)

# Generate interview guide to collect persona data
guide = persona.generate_interview(
    "Learning Platform Users",
    "contextual",
    context="Users take online courses for professional development"
)
print("Interview Guide:")
print(guide[:500] if len(guide) > 500 else guide)

print("\n" + "=" * 60)
print("Persona Output")
print("=" * 60)
print("""
  Primary Persona: "Career Climber Claire"
  - 28-35, mid-level professional, time-poor but ambitious
  - Goal: Upskill for promotion within 12 months
  - Frustration: Courses too long, can't find relevant content quickly
  - Behavior: Learns during commute, prefers video over reading

  Secondary Persona: "Explorer Eric"
  - 22-27, recent graduate, exploring career options
  - Goal: Try different fields before committing
  - Frustration: Overwhelming choice, unclear learning paths
  - Behavior: Free tier user, high curiosity, low commitment
""")
