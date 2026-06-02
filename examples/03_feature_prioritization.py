#!/usr/bin/env python3
"""Example: Feature Prioritization by Persona Impact.

Scenario: Deciding which features to build next based on persona needs.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from persona import PersonaSkill

persona = PersonaSkill("Productivity App")

print("=" * 60)
print("Feature Prioritization: Productivity App")
print("=" * 60)

# Add personas first
persona.add_persona(
    "Busy Manager Mike", "效率型管理者", "primary", "快就是好",
    goals=["快速完成每日任务规划"],
    behaviors=["高频使用任务列表"],
    attitudes=["追求效率", "讨厌浪费时间"],
    bio="Mike是一位忙碌的部门经理，需要快速管理每日任务。"
)
persona.add_persona(
    "实习生小美", "学习型用户", "secondary", "需要指导",
    goals=["学习任务管理方法"],
    behaviors=["浏览模板库"],
    attitudes=["好学", "需要结构化引导"],
    bio="小美是刚入职的实习生，想学习如何高效管理工作。"
)

# Add features with persona needs + business value + tech difficulty
persona.add_feature("AI meeting summaries", persona_needs={
    "Busy Manager Mike": "primary", "实习生小美": "secondary"
}, business_value="high", tech_difficulty="medium")
persona.add_feature("Calendar integration", persona_needs={
    "Busy Manager Mike": "primary"
}, business_value="high", tech_difficulty="low")
persona.add_feature("Team dashboard", persona_needs={
    "Busy Manager Mike": "secondary", "实习生小美": "primary"
}, business_value="medium", tech_difficulty="medium")
persona.add_feature("Focus mode timer", persona_needs={
    "Busy Manager Mike": "primary", "实习生小美": "secondary"
}, business_value="medium", tech_difficulty="low")

# Render the feature matrix
matrix = persona.render_feature_matrix()
print(matrix)

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
