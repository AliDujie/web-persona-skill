"""Persona 测试计划与衡量体系模块

对应模块 J（可用性测试计划与衡量体系）。
基于角色模型制定测试脚本、定义衡量指标、划分 Bug 优先级。
"""

from dataclasses import dataclass, field
from typing import Dict, List


TEST_STEP_STATUSES = ("未执行", "通过", "失败", "阻塞")

BUG_PRIORITY_RULES: Dict[str, str] = {
    "P0": "影响首要角色的核心任务，必须立即修复",
    "P1": "影响首要角色的非核心任务，或阻塞次要角色的核心任务",
    "P2": "影响次要角色的非核心任务，或轻微体验问题",
    "P3": "视觉微调、边缘场景，可排入后续迭代",
}

METRIC_CATEGORIES = ("效率", "满意度", "转化", "留存", "错误率")


@dataclass
class TestScript:
    """可用性测试脚本"""
    persona_name: str
    steps: List[Dict] = field(default_factory=list)
    # 每步结构: {action: str, expected: str, actual: str, status: str}


@dataclass
class MetricItem:
    """衡量指标条目"""
    persona_name: str
    metric: str
    target_value: str
    data_source: str
    collection_method: str


@dataclass
class BugPriority:
    """Bug 优先级"""
    description: str
    affected_persona: str
    priority: str  # P0-P3
    rationale: str = ""


class MeasureSystem:
    """测试计划与衡量体系

    用法示例::

        system = MeasureSystem("智能笔记App")
        system.add_test_script("效率达人", [
            {"action": "点击新建笔记", "expected": "打开编辑器", "actual": "", "status": "未执行"},
            {"action": "输入标题", "expected": "标题显示", "actual": "", "status": "未执行"},
        ])
        system.add_metric("效率达人", "任务完成时间", "< 30秒", "埋点", "自动采集")
        system.add_bug("编辑器加载超过5秒", "效率达人",
                       is_primary_persona=True, blocks_core_task=True)
        print(system.render_test_plan_markdown())
    """

    def __init__(self, product_name: str):
        self._product = product_name
        self._scripts: List[TestScript] = []
        self._metrics: List[MetricItem] = []
        self._bugs: List[BugPriority] = []

    def add_test_script(self, persona_name: str,
                        steps: List[Dict]) -> TestScript:
        """添加可用性测试脚本

        Args:
            persona_name: 角色名称
            steps: 测试步骤列表，每步包含 action/expected/actual/status
        """
        validated_steps = []
        for step in steps:
            validated_steps.append({
                "action": step.get("action", ""),
                "expected": step.get("expected", ""),
                "actual": step.get("actual", ""),
                "status": step.get("status", "未执行"),
            })
        script = TestScript(persona_name=persona_name, steps=validated_steps)
        self._scripts.append(script)
        return script

    def add_metric(self, persona_name: str, metric: str,
                   target: str, source: str, method: str) -> MetricItem:
        """添加衡量指标"""
        item = MetricItem(
            persona_name=persona_name, metric=metric,
            target_value=target, data_source=source,
            collection_method=method,
        )
        self._metrics.append(item)
        return item

    def add_bug(self, description: str, affected_persona: str,
                is_primary_persona: bool = False,
                blocks_core_task: bool = False) -> BugPriority:
        """添加 Bug 并自动计算优先级

        规则：
        - 首要角色 + 阻塞核心任务 → P0
        - 首要角色 + 不阻塞核心任务 → P1
        - 非首要角色 + 阻塞核心任务 → P1
        - 非首要角色 + 不阻塞核心任务 → P2
        """
        if is_primary_persona and blocks_core_task:
            priority = "P0"
        elif is_primary_persona or blocks_core_task:
            priority = "P1"
        else:
            priority = "P2"

        rationale = BUG_PRIORITY_RULES.get(priority, "")
        bug = BugPriority(
            description=description, affected_persona=affected_persona,
            priority=priority, rationale=rationale,
        )
        self._bugs.append(bug)
        return bug

    # ── Markdown 渲染 ──────────────────────────────────────────

    def render_test_plan_markdown(self) -> str:
        """渲染可用性测试计划"""
        lines = [f"# 可用性测试计划 — {self._product}\n"]

        if not self._scripts:
            lines.append("*暂无测试脚本*\n")
            return "\n".join(lines)

        for script in self._scripts:
            lines.append(f"## 测试脚本: {script.persona_name}\n")
            lines.append("| # | 操作 | 预期结果 | 实际结果 | 状态 |")
            lines.append("|---|------|---------|---------|------|")
            for i, step in enumerate(script.steps, 1):
                lines.append(
                    f"| {i} | {step['action']} | {step['expected']} "
                    f"| {step['actual'] or '-'} | {step['status']} |"
                )
            lines.append("")

            total = len(script.steps)
            passed = sum(1 for s in script.steps if s["status"] == "通过")
            failed = sum(1 for s in script.steps if s["status"] == "失败")
            lines.append(f"**统计:** 共 {total} 步 | 通过 {passed} | 失败 {failed}\n")

        if self._bugs:
            lines.append("## Bug 优先级\n")
            lines.append("| 描述 | 影响角色 | 优先级 | 判定依据 |")
            lines.append("|------|---------|--------|---------|")
            sorted_bugs = sorted(self._bugs, key=lambda b: b.priority)
            for bug in sorted_bugs:
                lines.append(
                    f"| {bug.description} | {bug.affected_persona} "
                    f"| {bug.priority} | {bug.rationale} |"
                )
            lines.append("")

            lines.append("### 优先级规则\n")
            for level, rule in BUG_PRIORITY_RULES.items():
                lines.append(f"- **{level}:** {rule}")
            lines.append("")

        return "\n".join(lines)

    def render_measure_system_markdown(self) -> str:
        """渲染衡量体系"""
        lines = [f"# 衡量体系 — {self._product}\n"]

        if not self._metrics:
            lines.append("*暂无衡量指标*\n")
            return "\n".join(lines)

        by_persona: Dict[str, List[MetricItem]] = {}
        for m in self._metrics:
            by_persona.setdefault(m.persona_name, []).append(m)

        for persona, items in by_persona.items():
            lines.append(f"## {persona}\n")
            lines.append("| 指标 | 目标值 | 数据来源 | 采集方式 |")
            lines.append("|------|--------|---------|---------|")
            for item in items:
                lines.append(
                    f"| {item.metric} | {item.target_value} "
                    f"| {item.data_source} | {item.collection_method} |"
                )
            lines.append("")

        return "\n".join(lines)

    def render_json(self) -> Dict:
        """输出结构化 JSON"""
        return {
            "product": self._product,
            "test_scripts": [
                {
                    "persona": s.persona_name,
                    "steps": s.steps,
                }
                for s in self._scripts
            ],
            "metrics": [
                {
                    "persona": m.persona_name, "metric": m.metric,
                    "target": m.target_value, "source": m.data_source,
                    "method": m.collection_method,
                }
                for m in self._metrics
            ],
            "bugs": [
                {
                    "description": b.description,
                    "affected_persona": b.affected_persona,
                    "priority": b.priority, "rationale": b.rationale,
                }
                for b in self._bugs
            ],
        }
