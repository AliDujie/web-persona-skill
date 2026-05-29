"""Persona × OKR & Roadmap Bridge（v2.6 新增）

把 Persona 的 Goals / Pain Points 自动转译为 Objectives + Key Results +
RICE/ICE 排序的路线图条目，让 Persona 从"研究产物"变成"战略投入"。

核心映射：
- Goals → Objective 文案
- Pain Points → 必要性证据
- Behavior 频率 / Cluster Size → RICE Reach
- Pain × Frequency → RICE Impact
- 数据成熟度 → RICE Confidence

参考：
- 方法论：references/30-okr-roadmap-bridge.md
- 关联：references/02-measuring-results.md, references/22-jtbd-persona-integration.md
"""

from __future__ import annotations

import datetime as _dt
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Sequence


# ---------------------------------------------------------------------------
# 数据类
# ---------------------------------------------------------------------------


@dataclass
class KeyResult:
    """OKR 中的 Key Result（结果指标）。"""

    statement: str
    metric: str
    baseline: Optional[float]
    target: float
    direction: str = "increase"  # increase | decrease | maintain
    cadence: str = "quarterly"
    persona_link: Optional[str] = None
    confidence: float = 0.7  # 0-1
    notes: List[str] = field(default_factory=list)


@dataclass
class Objective:
    """OKR 中的 Objective（目标）。"""

    id: str
    statement: str
    rationale: str
    persona_link: str
    quarter: str
    key_results: List[KeyResult] = field(default_factory=list)
    review_cadence: str = "monthly"


@dataclass
class RoadmapItem:
    """路线图候选条目。"""

    name: str
    reach: float
    impact: float
    confidence: float
    effort: float
    persona_link: Optional[str] = None
    score: float = 0.0
    model: str = "rice"
    rationale: str = ""


@dataclass
class OKRPlan:
    """OKR 计划包（一个季度的产出）。"""

    quarter: str
    product: str
    objectives: List[Objective]
    candidate_features: List[Dict[str, Any]]
    generated_at: str

    @property
    def key_results(self) -> List[KeyResult]:
        return [kr for obj in self.objectives for kr in obj.key_results]


# ---------------------------------------------------------------------------
# 主类
# ---------------------------------------------------------------------------


class OKRBridge:
    """Persona → OKR → 路线图打分桥接器。"""

    PERSONA_PRIORITY_WEIGHT = {
        "primary": 1.5,
        "secondary": 1.1,
        "supplemental": 0.9,
        "negative": 0.0,
    }

    def __init__(
        self,
        *,
        quarter: str,
        product: str,
        review_cadence: str = "monthly",
    ) -> None:
        self.quarter = quarter
        self.product = product
        self.review_cadence = review_cadence

    # ------------------------------------------------------------------
    # 公共 API
    # ------------------------------------------------------------------

    def derive_okrs(
        self,
        profiles: Sequence[Any],
        *,
        business_themes: Optional[Sequence[str]] = None,
        max_objectives: int = 5,
    ) -> OKRPlan:
        """从 Persona 列表派生 OKR 计划。

        Parameters
        ----------
        profiles : Sequence[PersonaProfile]
        business_themes : 可选业务主题（如"留存""新增""活跃"），用于命名 KR。
        max_objectives : 最多生成 N 个 Objective（默认 5）。
        """
        themes = list(business_themes or ["体验", "留存", "活跃"])
        objectives: List[Objective] = []
        candidates: List[Dict[str, Any]] = []

        # 仅对 primary / secondary 派生 Objective
        prioritized = sorted(
            profiles,
            key=lambda p: self.PERSONA_PRIORITY_WEIGHT.get(
                getattr(p, "priority", "supplemental"), 0.5
            ),
            reverse=True,
        )

        for idx, profile in enumerate(prioritized[:max_objectives]):
            priority = getattr(profile, "priority", "supplemental")
            if priority == "negative":
                continue
            obj = self._build_objective(profile, idx + 1, themes)
            objectives.append(obj)
            # 顺手生成路线图候选
            candidates.extend(self._suggest_features(profile))

        return OKRPlan(
            quarter=self.quarter,
            product=self.product,
            objectives=objectives,
            candidate_features=candidates,
            generated_at=_now_iso(),
        )

    def score_roadmap(
        self,
        items: Iterable[Dict[str, Any]],
        *,
        model: str = "rice",
        persona_priority: Optional[Dict[str, str]] = None,
    ) -> List[RoadmapItem]:
        """对路线图候选打分并排序。

        items 字段（兼容字典）：name, reach, impact, confidence, effort, persona_link, rationale。
        """
        if model not in {"rice", "ice"}:
            raise ValueError(f"unsupported model: {model}")
        priority_map = persona_priority or {}
        scored: List[RoadmapItem] = []
        for raw in items:
            persona_link = raw.get("persona_link")
            persona_weight = self.PERSONA_PRIORITY_WEIGHT.get(
                priority_map.get(persona_link or "", "secondary"), 1.0
            )
            reach = float(raw.get("reach", 0))
            impact = float(raw.get("impact", 1.0))
            confidence = max(0.0, min(1.0, float(raw.get("confidence", 0.7))))
            effort = max(0.5, float(raw.get("effort", 1)))
            if model == "rice":
                base = (reach * impact * confidence) / effort
            else:  # ice
                ease = 1.0 / effort
                base = impact * confidence * ease
            score = base * persona_weight
            scored.append(
                RoadmapItem(
                    name=str(raw.get("name", "(unnamed)")),
                    reach=reach,
                    impact=impact,
                    confidence=confidence,
                    effort=effort,
                    persona_link=persona_link,
                    score=score,
                    model=model,
                    rationale=str(raw.get("rationale", "")),
                )
            )
        scored.sort(key=lambda x: x.score, reverse=True)
        return scored

    # ------------------------------------------------------------------
    # 内部
    # ------------------------------------------------------------------

    def _build_objective(
        self, profile: Any, seq: int, themes: Sequence[str]
    ) -> Objective:
        name = getattr(profile, "name", f"Persona{seq}")
        goals = list(getattr(profile, "goals", []) or [])
        pains = list(getattr(profile, "pain_points", []) or [])
        # 兼容老结构：若无 pain_points 字段，从 attitudes 中找负向
        if not pains:
            pains = [a for a in (getattr(profile, "attitudes", []) or []) if "焦虑" in a or "怕" in a]
        top_goal = goals[0] if goals else f"提升 {name} 的核心体验"
        top_pain = pains[0] if pains else "（待补充：访谈采集主要痛点）"

        statement = f"让 {name} 在 {self.quarter} 内 {top_goal}"
        rationale = (
            f"驱动：{name}（{getattr(profile, 'priority', 'secondary')}）。"
            f"主要痛点：{top_pain}。"
            f"业务主题：{', '.join(themes[:2])}。"
        )

        krs = self._suggest_krs(profile, themes)
        return Objective(
            id=f"O{seq}-{self.quarter}-{_slug(name)}",
            statement=statement,
            rationale=rationale,
            persona_link=name,
            quarter=self.quarter,
            key_results=krs,
            review_cadence=self.review_cadence,
        )

    def _suggest_krs(self, profile: Any, themes: Sequence[str]) -> List[KeyResult]:
        name = getattr(profile, "name", "Persona")
        goals = list(getattr(profile, "goals", []) or [])
        # 4 类 KR 模板
        krs: List[KeyResult] = []

        # 1. 行为类
        krs.append(
            KeyResult(
                statement=f"{name} 周活 ≥ 3 次的比例从基线提升至 X%",
                metric="weekly_active_rate",
                baseline=None,
                target=40.0,
                direction="increase",
                persona_link=name,
                confidence=0.6,
                notes=["TODO: 用 measurement_toolkit.set_baseline 填基线"],
            )
        )
        # 2. 体验类
        krs.append(
            KeyResult(
                statement=f"{name} 主流程 NPS 提升 X 分",
                metric="persona_nps",
                baseline=None,
                target=12.0,
                direction="increase",
                persona_link=name,
                confidence=0.5,
            )
        )
        # 3. 转化类（基于 top goal）
        if goals:
            krs.append(
                KeyResult(
                    statement=f"{name} 完成「{goals[0]}」的转化率提升至 X%",
                    metric="goal_conversion",
                    baseline=None,
                    target=25.0,
                    direction="increase",
                    persona_link=name,
                    confidence=0.6,
                )
            )
        return krs

    def _suggest_features(self, profile: Any) -> List[Dict[str, Any]]:
        name = getattr(profile, "name", "Persona")
        priority = getattr(profile, "priority", "secondary")
        size_hint = self.PERSONA_PRIORITY_WEIGHT.get(priority, 1.0)
        # 简化：把每个 goal 转为 1 个候选
        out: List[Dict[str, Any]] = []
        for g in (getattr(profile, "goals", []) or [])[:3]:
            out.append(
                {
                    "name": f"为 {name} 提供「{g}」的端到端流程",
                    "reach": 1000 * size_hint,
                    "impact": 2.0 if priority == "primary" else 1.5,
                    "confidence": 0.7 if priority == "primary" else 0.5,
                    "effort": 4.0,
                    "persona_link": name,
                    "rationale": f"来自 Persona {name} 的核心目标",
                }
            )
        return out


# ---------------------------------------------------------------------------
# 工具
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def _slug(text: str) -> str:
    out = []
    for ch in text:
        if ch.isalnum():
            out.append(ch.lower())
        elif ch in "-_":
            out.append(ch)
        else:
            out.append("-")
    return "".join(out).strip("-") or "persona"


__all__ = [
    "OKRBridge",
    "OKRPlan",
    "Objective",
    "KeyResult",
    "RoadmapItem",
]
