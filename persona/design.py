"""Persona 信息架构与内容策略模块

对应模块 I（信息架构、内容策略、视觉策略）。
基于角色模型设计导航结构、内容规划和视觉方向。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


THREE_STEP_RULE_MAX = 3

CONTENT_FORMATS = ("文章", "视频", "教程", "FAQ", "案例", "白皮书", "信息图")

DEPTH_LEVELS = ("入门", "进阶", "专家")

CONTENT_PRIORITIES = ("高", "中", "低")


@dataclass
class NavItem:
    """导航条目"""
    label: str
    target_personas: List[str] = field(default_factory=list)
    children: List["NavItem"] = field(default_factory=list)


@dataclass
class ContentItem:
    """内容条目"""
    topic: str
    target_persona: str
    format: str
    depth: str
    tone: str
    frequency: str
    priority: str


@dataclass
class PathValidation:
    """路径验证结果"""
    persona_name: str
    task: str
    path: List[str] = field(default_factory=list)
    steps: int = 0
    passes_3step_rule: bool = True


class DesignAdvisor:
    """信息架构与内容策略顾问

    用法示例::

        advisor = DesignAdvisor("智能笔记App")
        advisor.add_nav_item("首页", ["效率达人", "学生用户"])
        advisor.add_nav_item("模板中心", ["效率达人"], children=[
            NavItem("会议纪要模板", ["效率达人"]),
            NavItem("学习笔记模板", ["学生用户"]),
        ])
        advisor.add_content("快速入门指南", "效率达人", "教程", "入门", "简洁专业", "一次性", "高")
        result = advisor.validate_path("效率达人", "创建会议纪要", ["首页", "模板中心", "会议纪要模板"])
        print(advisor.render_ia_markdown())
    """

    def __init__(self, product_name: str):
        self._product = product_name
        self._nav_items: List[NavItem] = []
        self._contents: List[ContentItem] = []
        self._validations: List[PathValidation] = []

    def add_nav_item(self, label: str,
                     target_personas: Optional[List[str]] = None,
                     children: Optional[List["NavItem"]] = None) -> NavItem:
        """添加顶层导航条目"""
        item = NavItem(
            label=label,
            target_personas=target_personas if target_personas is not None else [],
            children=children if children is not None else [],
        )
        self._nav_items.append(item)
        return item

    def add_content(self, topic: str, target_persona: str, format: str,
                    depth: str, tone: str, frequency: str,
                    priority: str) -> ContentItem:
        """添加内容规划条目"""
        item = ContentItem(
            topic=topic, target_persona=target_persona,
            format=format, depth=depth, tone=tone,
            frequency=frequency, priority=priority,
        )
        self._contents.append(item)
        return item

    def validate_path(self, persona_name: str, task: str,
                      path: List[str]) -> PathValidation:
        """验证用户路径是否满足三步规则

        三步规则：用户完成核心任务的点击步骤不超过3步。
        """
        steps = len(path)
        passes = steps <= THREE_STEP_RULE_MAX
        result = PathValidation(
            persona_name=persona_name, task=task,
            path=path, steps=steps, passes_3step_rule=passes,
        )
        self._validations.append(result)
        return result

    # ── Markdown 渲染 ──────────────────────────────────────────

    def render_ia_markdown(self) -> str:
        """渲染信息架构方案"""
        lines = [f"# 信息架构方案 — {self._product}\n"]

        if self._nav_items:
            lines.append("## 导航结构\n")
            for item in self._nav_items:
                personas_tag = f"（{', '.join(item.target_personas)}）" if item.target_personas else ""
                lines.append(f"- **{item.label}** {personas_tag}")
                for child in item.children:
                    child_tag = f"（{', '.join(child.target_personas)}）" if child.target_personas else ""
                    lines.append(f"  - {child.label} {child_tag}")
            lines.append("")

        if self._validations:
            lines.append("## 路径验证（三步规则）\n")
            lines.append("| 角色 | 任务 | 路径 | 步数 | 通过 |")
            lines.append("|------|------|------|------|------|")
            for v in self._validations:
                path_str = " → ".join(v.path)
                status = "✅" if v.passes_3step_rule else "❌"
                lines.append(f"| {v.persona_name} | {v.task} | {path_str} | {v.steps} | {status} |")
            lines.append("")

            failed = [v for v in self._validations if not v.passes_3step_rule]
            if failed:
                lines.append("### ⚠️ 需要优化的路径\n")
                for v in failed:
                    lines.append(
                        f"- **{v.persona_name}** 完成「{v.task}」需要 {v.steps} 步，"
                        f"超出三步规则，建议简化导航层级"
                    )
                lines.append("")

        return "\n".join(lines)

    def render_content_strategy_markdown(self) -> str:
        """渲染内容策略"""
        lines = [f"# 内容策略 — {self._product}\n"]

        if not self._contents:
            lines.append("*暂无内容规划*\n")
            return "\n".join(lines)

        by_persona: Dict[str, List[ContentItem]] = {}
        for c in self._contents:
            by_persona.setdefault(c.target_persona, []).append(c)

        for persona, items in by_persona.items():
            lines.append(f"## {persona}\n")
            lines.append("| 主题 | 格式 | 深度 | 语调 | 频率 | 优先级 |")
            lines.append("|------|------|------|------|------|--------|")
            sorted_items = sorted(items, key=lambda x: CONTENT_PRIORITIES.index(x.priority)
                                  if x.priority in CONTENT_PRIORITIES else 99)
            for item in sorted_items:
                lines.append(
                    f"| {item.topic} | {item.format} | {item.depth} "
                    f"| {item.tone} | {item.frequency} | {item.priority} |"
                )
            lines.append("")

        return "\n".join(lines)

    def render_visual_strategy_markdown(self, persona_expectations: Dict[str, str]) -> str:
        """渲染视觉策略

        Args:
            persona_expectations: {角色名: 视觉期望描述}
        """
        lines = [f"# 视觉策略 — {self._product}\n"]

        if not persona_expectations:
            lines.append("*暂无视觉策略数据*\n")
            return "\n".join(lines)

        lines.append("## 各角色视觉期望\n")
        for persona, expectation in persona_expectations.items():
            lines.append(f"### {persona}\n")
            lines.append(f"{expectation}\n")

        lines.append("## 视觉设计原则\n")
        lines.append("- 首要角色的视觉期望优先满足")
        lines.append("- 次要角色的期望不应与首要角色冲突")
        lines.append("- 在关键路径上保持视觉一致性")
        lines.append("- 用视觉层级引导用户完成核心任务\n")

        return "\n".join(lines)

    def render_json(self) -> Dict:
        """输出结构化 JSON"""
        return {
            "product": self._product,
            "navigation": [
                {
                    "label": item.label,
                    "target_personas": item.target_personas,
                    "children": [
                        {"label": c.label, "target_personas": c.target_personas}
                        for c in item.children
                    ],
                }
                for item in self._nav_items
            ],
            "content_strategy": [
                {
                    "topic": c.topic, "target_persona": c.target_persona,
                    "format": c.format, "depth": c.depth, "tone": c.tone,
                    "frequency": c.frequency, "priority": c.priority,
                }
                for c in self._contents
            ],
            "path_validations": [
                {
                    "persona": v.persona_name, "task": v.task,
                    "path": v.path, "steps": v.steps,
                    "passes_3step_rule": v.passes_3step_rule,
                }
                for v in self._validations
            ],
        }
