"""Persona 商业策略与功能优先级模块

对应模块 G（商业价值评估）+ H（功能优先级矩阵与竞品分析）。
评估各角色的商业价值、规划功能优先级、进行竞品特性对比。
"""

from dataclasses import dataclass, field
from typing import Dict, List


PRIORITY_LEVELS = ("P0", "P1", "P2", "P3")

PRIORITY_DESCRIPTIONS: Dict[str, str] = {
    "P0": "必须有 — 首要角色核心任务所需",
    "P1": "应该有 — 首要角色重要但非阻塞",
    "P2": "可以有 — 次要角色需求或锦上添花",
    "P3": "暂缓 — 优先级低或投入产出比不足",
}

TECH_DIFFICULTY_LEVELS = ("低", "中", "高", "极高")

BUSINESS_VALUE_LEVELS = ("低", "中", "高", "极高")


@dataclass
class BusinessValue:
    """角色商业价值评估"""
    persona_name: str
    market_size: str
    spending_potential: str
    acquisition_cost: str
    lifetime_value: str
    score: int  # 1-10


@dataclass
class FeatureItem:
    """功能条目"""
    name: str
    persona_needs: Dict[str, str]  # {角色名: 需求描述}
    business_value: str
    tech_difficulty: str
    priority: str = ""  # P0-P3，自动计算


@dataclass
class CompetitorFeature:
    """竞品特性覆盖"""
    name: str
    description: str
    coverage: Dict[str, str] = field(default_factory=dict)  # {竞品名: "●"/"○"/""}


class StrategyAnalyzer:
    """商业策略分析器

    用法示例::

        analyzer = StrategyAnalyzer("智能笔记App")
        analyzer.add_persona_value("效率达人", "500万", "高", "中", "高", 8)
        analyzer.add_persona_value("学生用户", "2000万", "低", "低", "中", 5)
        analyzer.add_feature("AI摘要", {"效率达人": "快速提取要点", "学生用户": "辅助复习"},
                             business_value="高", tech_difficulty="高")
        analyzer.add_competitor("Notion", {"AI摘要": "●", "手写识别": "○"})
        print(analyzer.render_strategy_markdown())
    """

    def __init__(self, product_name: str):
        self._product = product_name
        self._values: List[BusinessValue] = []
        self._features: List[FeatureItem] = []
        self._competitors: Dict[str, Dict[str, str]] = {}  # {竞品名: {功能名: 覆盖}}

    def add_persona_value(self, persona_name: str, market_size: str,
                          spending_potential: str, acquisition_cost: str,
                          lifetime_value: str, score: int) -> BusinessValue:
        """添加角色商业价值评估"""
        if not 1 <= score <= 10:
            raise ValueError(f"score 必须在 1-10 之间，当前: {score}")
        bv = BusinessValue(
            persona_name=persona_name, market_size=market_size,
            spending_potential=spending_potential, acquisition_cost=acquisition_cost,
            lifetime_value=lifetime_value, score=score,
        )
        self._values.append(bv)
        return bv

    def add_feature(self, name: str, persona_needs: Dict[str, str],
                    business_value: str, tech_difficulty: str) -> FeatureItem:
        """添加功能条目，自动计算优先级"""
        feat = FeatureItem(
            name=name, persona_needs=persona_needs,
            business_value=business_value, tech_difficulty=tech_difficulty,
        )
        feat.priority = self._calculate_priority(feat)
        self._features.append(feat)
        return feat

    def add_competitor(self, name: str, features_coverage: Dict[str, str]) -> None:
        """添加竞品及其功能覆盖情况"""
        self._competitors[name] = features_coverage

    def _calculate_priority(self, feature: FeatureItem) -> str:
        """基于首要角色需求 + 商业价值自动计算优先级

        规则：
        - 首要角色（得分最高）有需求 + 商业价值高/极高 → P0
        - 首要角色有需求 + 商业价值中 → P1
        - 次要角色有需求 + 商业价值高/极高 → P1
        - 次要角色有需求 + 商业价值中 → P2
        - 其余 → P3
        """
        primary = self._get_primary_persona()
        has_primary_need = primary in feature.persona_needs if primary else False
        bv = feature.business_value

        if has_primary_need:
            if bv in ("高", "极高"):
                return "P0"
            if bv == "中":
                return "P1"
            return "P2"
        else:
            if bv in ("高", "极高"):
                return "P1"
            if bv == "中":
                return "P2"
            return "P3"

    def _get_primary_persona(self) -> str:
        """获取得分最高的首要角色名称"""
        if not self._values:
            return ""
        return max(self._values, key=lambda v: v.score).persona_name

    # ── Markdown 渲染 ──────────────────────────────────────────

    def render_strategy_markdown(self) -> str:
        """渲染商业策略报告"""
        lines = [f"# 商业策略报告 — {self._product}\n"]

        primary = self._get_primary_persona()
        if primary:
            lines.append(f"**首要角色:** {primary}\n")

        if self._values:
            lines.append("## 角色商业价值评估\n")
            lines.append("| 角色 | 市场规模 | 消费潜力 | 获客成本 | 生命周期价值 | 综合评分 |")
            lines.append("|------|---------|---------|---------|------------|---------|")
            sorted_values = sorted(self._values, key=lambda v: v.score, reverse=True)
            for v in sorted_values:
                lines.append(
                    f"| {v.persona_name} | {v.market_size} | {v.spending_potential} "
                    f"| {v.acquisition_cost} | {v.lifetime_value} | {v.score}/10 |"
                )
            lines.append("")

            lines.append("### 策略建议\n")
            if len(sorted_values) >= 2:
                top = sorted_values[0]
                second = sorted_values[1]
                lines.append(
                    f"- **优先服务 {top.persona_name}**（评分 {top.score}/10），"
                    f"其消费潜力为「{top.spending_potential}」，生命周期价值为「{top.lifetime_value}」"
                )
                lines.append(
                    f"- **次要关注 {second.persona_name}**（评分 {second.score}/10），"
                    f"作为增长储备"
                )
            elif sorted_values:
                top = sorted_values[0]
                lines.append(f"- **核心服务 {top.persona_name}**（评分 {top.score}/10）")
            lines.append("")

        return "\n".join(lines)

    def render_feature_matrix_markdown(self) -> str:
        """渲染功能优先级矩阵"""
        lines = [f"# 功能优先级矩阵 — {self._product}\n"]

        if not self._features:
            lines.append("*暂无功能数据*\n")
            return "\n".join(lines)

        for p_level in PRIORITY_LEVELS:
            feats = [f for f in self._features if f.priority == p_level]
            if not feats:
                continue
            desc = PRIORITY_DESCRIPTIONS.get(p_level, "")
            lines.append(f"## {p_level}: {desc}\n")
            for feat in feats:
                lines.append(f"### {feat.name}\n")
                lines.append(f"- **商业价值:** {feat.business_value}")
                lines.append(f"- **技术难度:** {feat.tech_difficulty}")
                if feat.persona_needs:
                    lines.append("- **角色需求:**")
                    for persona, need in feat.persona_needs.items():
                        lines.append(f"  - {persona}: {need}")
                lines.append("")

        return "\n".join(lines)

    def render_competitor_markdown(self) -> str:
        """渲染竞品功能对比"""
        lines = [f"# 竞品功能对比 — {self._product}\n"]

        if not self._competitors:
            lines.append("*暂无竞品数据*\n")
            return "\n".join(lines)

        all_features = sorted({
            feat_name
            for coverage in self._competitors.values()
            for feat_name in coverage
        })

        comp_names = sorted(self._competitors.keys())
        header = "| 功能 | " + " | ".join(comp_names) + f" | {self._product} |"
        sep = "|------|" + "|".join(["---"] * len(comp_names)) + "|---|"
        lines.append(header)
        lines.append(sep)

        for feat_name in all_features:
            cells = []
            for comp in comp_names:
                cells.append(self._competitors[comp].get(feat_name, ""))
            row = f"| {feat_name} | " + " | ".join(cells) + " | ● |"
            lines.append(row)
        lines.append("")

        lines.append("**图例:** ● 完整支持 | ○ 部分支持 | 空 不支持\n")

        return "\n".join(lines)

    def render_json(self) -> Dict:
        """输出结构化 JSON"""
        return {
            "product": self._product,
            "primary_persona": self._get_primary_persona(),
            "business_values": [
                {
                    "persona": v.persona_name, "market_size": v.market_size,
                    "spending_potential": v.spending_potential,
                    "acquisition_cost": v.acquisition_cost,
                    "lifetime_value": v.lifetime_value, "score": v.score,
                }
                for v in self._values
            ],
            "features": [
                {
                    "name": f.name, "persona_needs": f.persona_needs,
                    "business_value": f.business_value,
                    "tech_difficulty": f.tech_difficulty, "priority": f.priority,
                }
                for f in self._features
            ],
            "competitors": {
                name: coverage
                for name, coverage in self._competitors.items()
            },
        }
