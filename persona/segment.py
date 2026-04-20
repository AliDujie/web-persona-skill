"""用户细分分析器

对应模块D：基于用户研究数据进行行为/态度细分，
生成可操作的用户群体划分与评估报告。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


EVALUATION_DIMENSIONS = ("differentiation", "actionability", "coverage")

EVALUATION_LABELS: Dict[str, str] = {
    "differentiation": "差异性",
    "actionability": "可操作性",
    "coverage": "覆盖性",
}

EVALUATION_RUBRICS: Dict[str, Dict[int, str]] = {
    "differentiation": {
        5: "各细分群体在目标、行为、态度上有本质差异，几乎无重叠",
        4: "群体间差异明显，少量边缘用户可能跨群",
        3: "群体间有可辨识的差异，但部分维度重叠",
        2: "群体间差异较小，主要靠单一维度区分",
        1: "群体间几乎无差异，细分缺乏意义",
    },
    "actionability": {
        5: "每个细分群体都能直接指导产品设计和营销策略",
        4: "大部分群体能指导具体决策",
        3: "部分群体有可操作性，部分过于笼统",
        2: "细分结果难以转化为具体行动",
        1: "细分结果完全无法指导实际工作",
    },
    "coverage": {
        5: "细分覆盖了 95% 以上的目标用户",
        4: "细分覆盖了 80%-95% 的目标用户",
        3: "细分覆盖了 60%-80% 的目标用户",
        2: "细分覆盖了 40%-60% 的目标用户",
        1: "细分覆盖不足 40% 的目标用户",
    },
}


@dataclass
class UserDataPoint:
    """单个用户的研究数据"""

    user_id: str
    goals: List[str] = field(default_factory=list)
    behaviors: List[str] = field(default_factory=list)
    attitudes: List[str] = field(default_factory=list)
    demographics: Dict[str, str] = field(default_factory=dict)
    quotes: List[str] = field(default_factory=list)


@dataclass
class Segment:
    """一个用户细分群体"""

    name: str
    description: str
    core_goals: List[str] = field(default_factory=list)
    typical_behaviors: List[str] = field(default_factory=list)
    key_attitudes: List[str] = field(default_factory=list)
    estimated_percentage: float = 0.0
    representative_users: List[str] = field(default_factory=list)


@dataclass
class SegmentationResult:
    """完整的细分分析结果"""

    dimension_primary: str = ""
    dimension_secondary: str = ""
    segments: List[Segment] = field(default_factory=list)
    evaluation: Dict[str, int] = field(default_factory=dict)

    @property
    def total_percentage(self) -> float:
        return sum(s.estimated_percentage for s in self.segments)

    @property
    def evaluation_avg(self) -> float:
        if not self.evaluation:
            return 0.0
        return round(sum(self.evaluation.values()) / len(self.evaluation), 2)


class SegmentAnalyzer:
    """用户细分分析器

    提供用户数据录入、细分群体定义、质量评估和报告输出的完整 API。

    用法示例::

        analyzer = SegmentAnalyzer()
        analyzer.add_user("U01", goals=["快速完成任务"], behaviors=["高频使用搜索"],
                          attitudes=["效率至上"], demographics={"age": "25-35"})
        analyzer.add_segment("效率型", "追求速度和效率的用户",
                             core_goals=["快速完成任务"], typical_behaviors=["高频使用搜索"],
                             key_attitudes=["效率至上"], percentage=40.0, users=["U01"])
        analyzer.set_dimensions("行为频率", "使用动机")
        result = analyzer.build()
        print(analyzer.render_markdown())
    """

    def __init__(self) -> None:
        self._users: List[UserDataPoint] = []
        self._segments: List[Segment] = []
        self._evaluation: Dict[str, int] = {}
        self._dim_primary: str = ""
        self._dim_secondary: str = ""

    def add_user(
        self,
        user_id: str,
        goals: Optional[List[str]] = None,
        behaviors: Optional[List[str]] = None,
        attitudes: Optional[List[str]] = None,
        demographics: Optional[Dict[str, str]] = None,
        quotes: Optional[List[str]] = None,
    ) -> UserDataPoint:
        """录入单个用户的研究数据"""
        user = UserDataPoint(
            user_id=user_id,
            goals=goals or [],
            behaviors=behaviors or [],
            attitudes=attitudes or [],
            demographics=demographics or {},
            quotes=quotes or [],
        )
        self._users.append(user)
        return user

    def add_segment(
        self,
        name: str,
        description: str,
        core_goals: Optional[List[str]] = None,
        typical_behaviors: Optional[List[str]] = None,
        key_attitudes: Optional[List[str]] = None,
        percentage: float = 0.0,
        users: Optional[List[str]] = None,
    ) -> Segment:
        """定义一个用户细分群体"""
        segment = Segment(
            name=name,
            description=description,
            core_goals=core_goals or [],
            typical_behaviors=typical_behaviors or [],
            key_attitudes=key_attitudes or [],
            estimated_percentage=percentage,
            representative_users=users or [],
        )
        self._segments.append(segment)
        return segment

    def evaluate_segmentation(self) -> Dict[str, int]:
        """评估细分质量：差异性、可操作性、覆盖性各 1-5 分"""
        evaluation: Dict[str, int] = {}
        for dim in EVALUATION_DIMENSIONS:
            evaluation[dim] = self._evaluate_dimension(dim)
        self._evaluation = evaluation
        return evaluation

    def _evaluate_dimension(self, dimension: str) -> int:
        """根据细分数据自动评估单个维度的分数"""
        if not self._segments:
            return 1

        if dimension == "differentiation":
            return self._evaluate_differentiation()
        elif dimension == "actionability":
            return self._evaluate_actionability()
        elif dimension == "coverage":
            return self._evaluate_coverage()
        return 1

    def _evaluate_differentiation(self) -> int:
        """评估各群体之间的差异程度"""
        if len(self._segments) < 2:
            return 1
        all_goals = [set(s.core_goals) for s in self._segments]
        overlap_count = 0
        pair_count = 0
        for i in range(len(all_goals)):
            for j in range(i + 1, len(all_goals)):
                pair_count += 1
                if all_goals[i] & all_goals[j]:
                    overlap_count += 1
        if pair_count == 0:
            return 3
        overlap_ratio = overlap_count / pair_count
        if overlap_ratio == 0:
            return 5
        elif overlap_ratio < 0.3:
            return 4
        elif overlap_ratio < 0.6:
            return 3
        elif overlap_ratio < 0.8:
            return 2
        return 1

    def _evaluate_actionability(self) -> int:
        """评估细分结果的可操作性"""
        if not self._segments:
            return 1
        detailed = sum(
            1 for s in self._segments
            if s.core_goals and s.typical_behaviors and s.key_attitudes
        )
        ratio = detailed / len(self._segments)
        if ratio >= 0.9:
            return 5
        elif ratio >= 0.7:
            return 4
        elif ratio >= 0.5:
            return 3
        elif ratio >= 0.3:
            return 2
        return 1

    def _evaluate_coverage(self) -> int:
        """评估细分对目标用户的覆盖程度"""
        total = sum(s.estimated_percentage for s in self._segments)
        if total >= 95:
            return 5
        elif total >= 80:
            return 4
        elif total >= 60:
            return 3
        elif total >= 40:
            return 2
        return 1

    def set_dimensions(self, primary: str, secondary: str) -> None:
        """设置细分的主轴和副轴维度"""
        self._dim_primary = primary
        self._dim_secondary = secondary

    def build(self) -> SegmentationResult:
        """构建完整的细分分析结果"""
        if not self._evaluation:
            self.evaluate_segmentation()
        return SegmentationResult(
            dimension_primary=self._dim_primary,
            dimension_secondary=self._dim_secondary,
            segments=list(self._segments),
            evaluation=dict(self._evaluation),
        )

    def render_markdown(self) -> str:
        """输出完整的细分分析 Markdown 报告"""
        result = self.build()
        lines = ["# 用户细分分析报告\n"]

        # 细分矩阵
        lines.append("## 细分矩阵\n")
        if result.dimension_primary or result.dimension_secondary:
            lines.append(f"- **主轴维度:** {result.dimension_primary or '（未设置）'}")
            lines.append(f"- **副轴维度:** {result.dimension_secondary or '（未设置）'}")
            lines.append("")

        lines.append("| 群体 | 占比 | 核心目标 | 关键行为 |")
        lines.append("|------|------|----------|----------|")
        for seg in result.segments:
            goals = "、".join(seg.core_goals[:2]) if seg.core_goals else "—"
            behaviors = "、".join(seg.typical_behaviors[:2]) if seg.typical_behaviors else "—"
            lines.append(f"| {seg.name} | {seg.estimated_percentage:.0f}% | {goals} | {behaviors} |")
        lines.append("")

        # 各群体画像
        for i, seg in enumerate(result.segments, 1):
            lines.append(f"## 群体{i}: {seg.name}\n")
            lines.append(f"**描述:** {seg.description}\n")
            lines.append(f"**估计占比:** {seg.estimated_percentage:.0f}%\n")

            if seg.core_goals:
                lines.append("**核心目标:**")
                for g in seg.core_goals:
                    lines.append(f"- {g}")
                lines.append("")

            if seg.typical_behaviors:
                lines.append("**典型行为:**")
                for b in seg.typical_behaviors:
                    lines.append(f"- {b}")
                lines.append("")

            if seg.key_attitudes:
                lines.append("**关键态度:**")
                for a in seg.key_attitudes:
                    lines.append(f"- {a}")
                lines.append("")

            if seg.representative_users:
                lines.append(f"**代表用户:** {', '.join(seg.representative_users)}\n")

        # 对比表
        if len(result.segments) >= 2:
            lines.append("## 群体对比表\n")
            headers = ["维度"] + [s.name for s in result.segments]
            lines.append("| " + " | ".join(headers) + " |")
            lines.append("|" + "|".join(["------"] * len(headers)) + "|")

            goal_row = ["核心目标"] + [
                "、".join(s.core_goals[:2]) if s.core_goals else "—"
                for s in result.segments
            ]
            lines.append("| " + " | ".join(goal_row) + " |")

            behavior_row = ["典型行为"] + [
                "、".join(s.typical_behaviors[:2]) if s.typical_behaviors else "—"
                for s in result.segments
            ]
            lines.append("| " + " | ".join(behavior_row) + " |")

            attitude_row = ["关键态度"] + [
                "、".join(s.key_attitudes[:2]) if s.key_attitudes else "—"
                for s in result.segments
            ]
            lines.append("| " + " | ".join(attitude_row) + " |")

            pct_row = ["估计占比"] + [
                f"{s.estimated_percentage:.0f}%" for s in result.segments
            ]
            lines.append("| " + " | ".join(pct_row) + " |")
            lines.append("")

        # 评估
        lines.append("## 细分质量评估\n")
        if result.evaluation:
            for dim in EVALUATION_DIMENSIONS:
                if dim in result.evaluation:
                    label = EVALUATION_LABELS[dim]
                    score = result.evaluation[dim]
                    rubric = EVALUATION_RUBRICS.get(dim, {}).get(score, "")
                    lines.append(f"- **{label}:** {score}/5 — {rubric}")
            lines.append(f"\n**综合均分:** {result.evaluation_avg}/5")
        else:
            lines.append("（尚未评估）")
        lines.append("")

        return "\n".join(lines)

    def render_json(self) -> Dict:
        """输出 JSON 格式的细分分析结果"""
        result = self.build()
        return {
            "dimension_primary": result.dimension_primary,
            "dimension_secondary": result.dimension_secondary,
            "segments": [
                {
                    "name": s.name,
                    "description": s.description,
                    "core_goals": s.core_goals,
                    "typical_behaviors": s.typical_behaviors,
                    "key_attitudes": s.key_attitudes,
                    "estimated_percentage": s.estimated_percentage,
                    "representative_users": s.representative_users,
                }
                for s in result.segments
            ],
            "evaluation": result.evaluation,
            "evaluation_avg": result.evaluation_avg,
            "total_percentage": result.total_percentage,
        }
