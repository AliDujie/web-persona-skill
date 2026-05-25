#!/usr/bin/env python3
"""Persona Example 01: Persona Creation & Review / 角色创建与评审

Create user personas and evaluate their quality using built-in scoring.
创建用户角色并使用内置评分评估质量。

Run: python 01_persona_creation.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from persona import PersonaSkill

print("=" * 60)
print("Persona Example 01: Persona Creation & Review")
print("示例 01：角色创建与评审")
print("=" * 60)

skill = PersonaSkill("FreshMart 生鲜电商")

# ── Add user data ──
skill.add_user("U01",
    goals=["快速完成购物", "买到新鲜食材"],
    behaviors=["每周下单3次", "偏好晚间配送"],
    attitudes=["注重效率", "愿意为品质付费"],
    demographics={"age": 28, "occupation": "产品经理"}
)
skill.add_user("U02",
    goals=["省钱", "找到优惠"],
    behaviors=["比价后下单", "周末集中采购"],
    attitudes=["价格敏感", "喜欢尝试新品"],
    demographics={"age": 32, "occupation": "家庭主妇"}
)

# ── Create segments ──
skill.add_segment("效率型", "追求快速便捷",
    ["快速完成"], ["高频使用"], ["效率优先"], 60, users=["U01"])
skill.add_segment("经济型", "追求性价比",
    ["省钱"], ["周末集中采购"], ["价格敏感"], 40, users=["U02"])

# ── Create personas ──
skill.add_persona("张先生", "效率型用户", "primary",
    "快就是好",
    goals=["快速完成购物"], behaviors=["每周下单3次"],
    attitudes=["注重效率"], bio="28岁互联网产品经理，工作繁忙")

skill.add_persona("李女士", "经济型用户", "secondary",
    "省钱省心",
    goals=["找到最优惠"], behaviors=["比价后下单"],
    attitudes=["价格敏感"], bio="32岁家庭主妇，精打细算")

# ── Render ──
print("\n📋 All Personas / 所有角色")
print("-" * 50)
personas = skill.render_all_personas()
print(personas[:500])
print("...\n")

# ── Quality review ──
print("\n📊 Quality Review / 质量评审")
print("-" * 50)
review = skill.review_personas()
print(review[:400])
print("...\n")

print("✅ Tip: Run review_personas() to ensure persona quality before sharing.")
print("✅ 提示：分享前运行 review_personas() 确保角色质量。")
