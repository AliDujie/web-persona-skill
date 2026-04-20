"""人物角色文档生成器

对应模块E：基于细分结果构建完整的 Persona 文档，
包含角色画像、场景叙事、对比分析和质量评审。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


QUALITY_ITEMS: List[Dict[str, str]] = [
    {"id": "Q01", "category": "基础信息", "item": "角色有明确的姓名和简短描述"},
    {"id": "Q02", "category": "基础信息", "item": "包含代表性引言（Quote）"},
    {"id": "Q03", "category": "目标与动机", "item": "列出了至少 2 个核心目标"},
    {"id": "Q04", "category": "目标与动机", "item": "目标之间有层次区分（功能/情感/社会）"},
    {"id": "Q05", "category": "行为模式", "item": "描述了至少 2 个典型行为"},
    {"id": "Q06", "category": "行为模式", "item": "行为描述基于观察而非假设"},
    {"id": "Q07", "category": "态度与价值观", "item": "列出了关键态度和价值取向"},
    {"id": "Q08", "category": "场景叙事", "item": "至少包含 1 个使用场景"},
    {"id": "Q09", "category": "场景叙事", "item": "场景包含触发条件、步骤和结果"},
    {"id": "Q10", "category": "人口统计", "item": "包含必要的人口统计信息"},
    {"id": "Q11", "category": "差异化", "item": "与其他角色有明确区分"},
    {"id": "Q12", "category": "可操作性", "item": "角色信息能直接指导设计决策"},
]


@dataclass
class PersonaProfile:
    """单个人物角色画像"""

    name: str
    short_desc: str
    priority: str = "primary"
    quote: str = ""
    goals: List[str] = field(default_factory=list)
    behaviors: List[str] = field(default_factory=list)
    attitudes: List[str] = field(default_factory=list)
    bio: str = ""
    demographics: Dict[str, str] = field(default_factory=dict)
    tech_usage: Dict[str, str] = field(default_factory=dict)
    business_goals: List[str] = field(default_factory=list)
    scenarios: List[Dict[str, str]] = field(default_factory=list)


@dataclass
class PersonaComparison:
    """多角色对比结果"""

    personas: List[PersonaProfile] = field(default_factory=list)
    conflicts: List[Dict[str, str]] = field(default_factory=list)
    design_insights: Dict[str, str] = field(default_factory=dict)


@dataclass
class QualityReview:
    """质量评审结果"""

    checklist: List[Dict[str, object]] = field(default_factory=list)
    total_score: int = 0
    max_score: int = 0
    grade: str = ""


class PersonaBuilder:
    """人物角色文档生成器

    提供角色创建、场景添加、对比分析、质量评审和报告输出的完整 API。

    用法示例::

        builder = PersonaBuilder("旅行预订平台")
        p = builder.add_persona("小王", "效率型商旅用户", priority="primary",
                                quote="我只想用最短时间搞定住宿",
                                goals=["快速预订", "价格透明"],
                                behaviors=["使用筛选功能", "对比多个平台"],
                                attitudes=["效率至上", "价格敏感"],
                                bio="28岁，互联网公司产品经理，每月出差2-3次",
                                demographics={"age": "28", "role": "产品经理"},
                                tech_usage={"mobile": "重度", "desktop": "中度"},
                                business_goals=["降低差旅时间成本"])
        builder.add_scenario(p, "紧急出差预订", "临时接到出差通知",
                             ["打开APP", "筛选目的地酒店", "按价格排序", "一键预订"],
                             "5分钟内完成预订")
        print(builder.render_all_markdown())
    """

    def __init__(self, product_name: str) -> None:
        self.product_name = product_name
        self._personas: List[PersonaProfile] = []

    def add_persona(
        self,
        name: str,
        short_desc: str,
        priority: str = "primary",
        quote: str = "",
        goals: Optional[List[str]] = None,
        behaviors: Optional[List[str]] = None,
        attitudes: Optional[List[str]] = None,
        bio: str = "",
        demographics: Optional[Dict[str, str]] = None,
        tech_usage: Optional[Dict[str, str]] = None,
        business_goals: Optional[List[str]] = None,
    ) -> PersonaProfile:
        """添加一个人物角色"""
        valid_priorities = ("primary", "secondary", "unimportant", "negative")
        if priority not in valid_priorities:
            raise ValueError(
                f"优先级 '{priority}' 无效，可选: {valid_priorities}"
            )
        persona = PersonaProfile(
            name=name,
            short_desc=short_desc,
            priority=priority,
            quote=quote,
            goals=goals or [],
            behaviors=behaviors or [],
            attitudes=attitudes or [],
            bio=bio,
            demographics=demographics or {},
            tech_usage=tech_usage or {},
            business_goals=business_goals or [],
        )
        self._personas.append(persona)
        return persona

    def add_scenario(
        self,
        persona: PersonaProfile,
        title: str,
        trigger: str,
        steps: List[str],
        result: str,
    ) -> None:
        """为角色添加使用场景"""
        persona.scenarios.append({
            "title": title,
            "trigger": trigger,
            "steps": " → ".join(steps),
            "result": result,
        })

    def get_personas(self) -> List[PersonaProfile]:
        """获取所有已定义的角色"""
        return list(self._personas)

    def render_persona_markdown(self, persona: PersonaProfile) -> str:
        """输出单个角色的 Markdown 文档"""
        priority_labels = {
            "primary": "🔴 首要角色",
            "secondary": "🟡 次要角色",
            "unimportant": "🔵 不重要角色",
            "negative": "⚫ 排斥角色",
        }
        lines = [f"# {persona.name}\n"]
        lines.append(f"**{persona.short_desc}**\n")
        lines.append(f"**优先级:** {priority_labels.get(persona.priority, persona.priority)}\n")

        if persona.quote:
            lines.append(f"> \"{persona.quote}\"\n")

        if persona.bio:
            lines.append(f"## 个人简介\n\n{persona.bio}\n")

        # 人口统计
        if persona.demographics:
            lines.append("## 人口统计\n")
            for key, val in persona.demographics.items():
                lines.append(f"- **{key}:** {val}")
            lines.append("")

        # 技术使用
        if persona.tech_usage:
            lines.append("## 技术使用\n")
            for key, val in persona.tech_usage.items():
                lines.append(f"- **{key}:** {val}")
            lines.append("")

        # 目标
        if persona.goals:
            lines.append("## 目标\n")
            for g in persona.goals:
                lines.append(f"- {g}")
            lines.append("")

        # 行为
        if persona.behaviors:
            lines.append("## 行为模式\n")
            for b in persona.behaviors:
                lines.append(f"- {b}")
            lines.append("")

        # 态度
        if persona.attitudes:
            lines.append("## 态度与价值观\n")
            for a in persona.attitudes:
                lines.append(f"- {a}")
            lines.append("")

        # 业务目标
        if persona.business_goals:
            lines.append("## 业务目标\n")
            for bg in persona.business_goals:
                lines.append(f"- {bg}")
            lines.append("")

        # 场景
        if persona.scenarios:
            lines.append("## 使用场景\n")
            for idx, sc in enumerate(persona.scenarios, 1):
                lines.append(f"### 场景{idx}: {sc['title']}\n")
                lines.append(f"- **触发条件:** {sc['trigger']}")
                lines.append(f"- **步骤:** {sc['steps']}")
                lines.append(f"- **结果:** {sc['result']}")
                lines.append("")

        return "\n".join(lines)

    def render_all_markdown(self) -> str:
        """输出所有角色的完整 Markdown 文档"""
        lines = [f"# {self.product_name} — 用户角色文档\n"]
        lines.append(f"共定义 {len(self._personas)} 个角色\n")

        # 角色总览
        lines.append("## 角色总览\n")
        lines.append("| 角色 | 描述 | 优先级 |")
        lines.append("|------|------|--------|")
        for p in self._personas:
            lines.append(f"| {p.name} | {p.short_desc} | {p.priority} |")
        lines.append("")

        lines.append("---\n")

        # 各角色详情
        for p in self._personas:
            lines.append(self.render_persona_markdown(p))
            lines.append("---\n")

        return "\n".join(lines)

    def render_comparison(self) -> str:
        """输出角色对比表"""
        if len(self._personas) < 2:
            return "（需要至少 2 个角色才能生成对比表）"

        lines = ["# 角色对比分析\n"]

        headers = ["维度"] + [p.name for p in self._personas]
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("|" + "|".join(["------"] * len(headers)) + "|")

        # 描述
        desc_row = ["简短描述"] + [p.short_desc for p in self._personas]
        lines.append("| " + " | ".join(desc_row) + " |")

        # 优先级
        pri_row = ["优先级"] + [p.priority for p in self._personas]
        lines.append("| " + " | ".join(pri_row) + " |")

        # 核心目标
        goal_row = ["核心目标"] + [
            "、".join(p.goals[:2]) if p.goals else "—"
            for p in self._personas
        ]
        lines.append("| " + " | ".join(goal_row) + " |")

        # 典型行为
        beh_row = ["典型行为"] + [
            "、".join(p.behaviors[:2]) if p.behaviors else "—"
            for p in self._personas
        ]
        lines.append("| " + " | ".join(beh_row) + " |")

        # 关键态度
        att_row = ["关键态度"] + [
            "、".join(p.attitudes[:2]) if p.attitudes else "—"
            for p in self._personas
        ]
        lines.append("| " + " | ".join(att_row) + " |")

        # 场景数
        sc_row = ["场景数"] + [str(len(p.scenarios)) for p in self._personas]
        lines.append("| " + " | ".join(sc_row) + " |")
        lines.append("")

        return "\n".join(lines)

    def review_quality(self) -> QualityReview:
        """对所有角色执行质量评审"""
        checklist: List[Dict[str, object]] = []
        passed = 0

        for item in QUALITY_ITEMS:
            result = self._check_quality_item(item["id"])
            entry: Dict[str, object] = {
                "id": item["id"],
                "category": item["category"],
                "item": item["item"],
                "passed": result,
            }
            checklist.append(entry)
            if result:
                passed += 1

        max_score = len(QUALITY_ITEMS)
        ratio = passed / max_score if max_score else 0

        if ratio >= 0.9:
            grade = "A"
        elif ratio >= 0.75:
            grade = "B"
        elif ratio >= 0.6:
            grade = "C"
        elif ratio >= 0.4:
            grade = "D"
        else:
            grade = "F"

        return QualityReview(
            checklist=checklist,
            total_score=passed,
            max_score=max_score,
            grade=grade,
        )

    def _check_quality_item(self, item_id: str) -> bool:
        """检查单个质量项是否通过"""
        if not self._personas:
            return False

        if item_id == "Q01":
            return all(p.name and p.short_desc for p in self._personas)
        elif item_id == "Q02":
            return all(bool(p.quote) for p in self._personas)
        elif item_id == "Q03":
            return all(len(p.goals) >= 2 for p in self._personas)
        elif item_id == "Q04":
            return all(len(p.goals) >= 3 for p in self._personas)
        elif item_id == "Q05":
            return all(len(p.behaviors) >= 2 for p in self._personas)
        elif item_id == "Q06":
            return all(len(p.behaviors) >= 1 for p in self._personas)
        elif item_id == "Q07":
            return all(bool(p.attitudes) for p in self._personas)
        elif item_id == "Q08":
            return all(len(p.scenarios) >= 1 for p in self._personas)
        elif item_id == "Q09":
            return all(
                all("trigger" in sc and "steps" in sc and "result" in sc
                    for sc in p.scenarios)
                for p in self._personas
                if p.scenarios
            )
        elif item_id == "Q10":
            return all(bool(p.demographics) for p in self._personas)
        elif item_id == "Q11":
            if len(self._personas) < 2:
                return True
            descs = [p.short_desc for p in self._personas]
            return len(descs) == len(set(descs))
        elif item_id == "Q12":
            return all(
                p.goals and p.behaviors and p.attitudes
                for p in self._personas
            )
        return False

    def render_review_markdown(self, review: QualityReview) -> str:
        """输出质量评审的 Markdown 报告"""
        lines = ["# 角色质量评审报告\n"]
        lines.append(f"**总分:** {review.total_score}/{review.max_score}")
        lines.append(f"**等级:** {review.grade}\n")

        # 按类别分组
        categories: Dict[str, List[Dict[str, object]]] = {}
        for entry in review.checklist:
            cat = str(entry["category"])
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(entry)

        for cat, items in categories.items():
            lines.append(f"## {cat}\n")
            for entry in items:
                status = "✅" if entry["passed"] else "❌"
                lines.append(f"- {status} {entry['item']}")
            lines.append("")

        # 改进建议
        failed = [e for e in review.checklist if not e["passed"]]
        if failed:
            lines.append("## 改进建议\n")
            for entry in failed:
                lines.append(f"- **{entry['id']}:** 需要补充 — {entry['item']}")
            lines.append("")

        return "\n".join(lines)

    def render_json(self) -> Dict:
        """输出 JSON 格式的角色数据"""
        return {
            "product_name": self.product_name,
            "personas": [
                {
                    "name": p.name,
                    "short_desc": p.short_desc,
                    "priority": p.priority,
                    "quote": p.quote,
                    "goals": p.goals,
                    "behaviors": p.behaviors,
                    "attitudes": p.attitudes,
                    "bio": p.bio,
                    "demographics": p.demographics,
                    "tech_usage": p.tech_usage,
                    "business_goals": p.business_goals,
                    "scenarios": p.scenarios,
                }
                for p in self._personas
            ],
            "persona_count": len(self._personas),
        }
