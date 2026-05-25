#!/usr/bin/env python3
"""Persona Example 02: Survey & Segmentation / 问卷与分群

Generate user research surveys and segment audiences.
生成用户调研问卷并进行用户分群。

Run: python 02_survey_and_segmentation.py
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from persona import PersonaSkill

print("=" * 60)
print("Persona Example 02: Survey & Segmentation")
print("示例 02：问卷与分群")
print("=" * 60)

skill = PersonaSkill("FreshMart 生鲜电商")

# ── Generate a needs-based survey ──
print("\n📋 Needs-Based Survey Generation / 需求型问卷生成")
print("-" * 50)
survey = skill.generate_survey(
    title="生鲜配送需求调研",
    survey_type="needs",
    pain_points=["配送太慢", "食材不新鲜", "价格偏高"]
)
print(survey[:500])
print("...\n")

# ── Add users and segment ──
skill.add_user("U01",
    goals=["快速完成购物"],
    behaviors=["每周下单3次"],
    attitudes=["注重效率"])
skill.add_user("U02",
    goals=["省钱"],
    behaviors=["比价后下单"],
    attitudes=["价格敏感"])
skill.add_user("U03",
    goals=["新鲜品质"],
    behaviors=["周末集中采购"],
    attitudes=["追求品质"])

skill.add_segment("效率型", "追求快速便捷",
    ["快速完成"], ["高频使用"], ["效率优先"], 50, users=["U01"])
skill.add_segment("经济型", "追求性价比",
    ["省钱"], ["比价"], ["价格敏感"], 30, users=["U02"])
skill.add_segment("品质型", "追求高品质",
    ["新鲜品质"], ["集中采购"], ["追求品质"], 20, users=["U03"])

print("\n📊 User Segments / 用户分群")
print("-" * 50)
segments = skill.render_segments()
print(segments[:500])
print("...\n")

print("✅ Tip: Use survey data to validate segments before creating personas.")
print("✅ 提示：在创建角色之前，使用调研数据验证分群。")
