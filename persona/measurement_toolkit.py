"""Persona × 测量工具包（v2.6 新增）

把 NPS / CES / CSAT / Goal Funnel / Activation / Retention 等核心测量
指标做成可注册、可计算、可导出的标准化数据结构，支持 Persona 切片。

设计原则：
- 与 measure.py（可用性测试）互补：本模块做长期指标体系
- 与 OKR Bridge 联动：每个 KR 可自动注册为 Metric
- 仅依赖标准库

参考：
- 方法论：references/02-measuring-results.md
- 工程：references/31-measurement-toolkit.md
"""

from __future__ import annotations

import datetime as _dt
import statistics as _stats
from dataclasses import dataclass, field
from typing import Any, Dict, Iterable, List, Optional, Sequence


METRIC_TYPES = {"nps", "ces", "csat", "goal_conversion", "activation", "retention", "custom"}


# ---------------------------------------------------------------------------
# 数据类
# ---------------------------------------------------------------------------


@dataclass
class Metric:
    """指标定义。"""

    key: str
    name: str
    type: str  # one of METRIC_TYPES
    persona: Optional[str] = None
    cadence: str = "quarterly"  # weekly | monthly | quarterly | yearly
    baseline: Optional[float] = None
    target: Optional[float] = None
    direction: str = "increase"  # increase | decrease | maintain
    unit: str = ""
    description: str = ""

    def __post_init__(self) -> None:
        if self.type not in METRIC_TYPES:
            raise ValueError(
                f"unsupported metric type: {self.type}; expected one of {sorted(METRIC_TYPES)}"
            )


@dataclass
class MetricSnapshot:
    """单期指标快照。"""

    metric_key: str
    period: str
    value: float
    sample_size: int
    breakdown: Dict[str, Any] = field(default_factory=dict)
    captured_at: str = ""
    notes: List[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# 主类
# ---------------------------------------------------------------------------


class MeasurementToolkit:
    """指标注册、计算、追踪、导出。"""

    def __init__(self, *, product: str) -> None:
        self.product = product
        self._metrics: Dict[str, Metric] = {}
        self._snapshots: Dict[str, List[MetricSnapshot]] = {}
        self._raw: Dict[str, Dict[str, List[float]]] = {}  # key → {period → values}

    # ------------------------------------------------------------------
    # 注册
    # ------------------------------------------------------------------

    def register(self, metric: Metric) -> None:
        if metric.key in self._metrics:
            raise ValueError(f"metric '{metric.key}' already registered")
        self._metrics[metric.key] = metric
        self._snapshots[metric.key] = []
        self._raw[metric.key] = {}

    def register_from_kr(self, kr: Any) -> Metric:
        """从 OKR Bridge 的 KeyResult 自动注册。

        kr 应有字段：metric, statement, baseline, target, direction, persona_link, cadence
        """
        key = f"kr_{getattr(kr, 'metric', 'unnamed')}_{_slug(getattr(kr, 'persona_link', '') or 'all')}"
        metric_type = _infer_type_from_kr(kr)
        metric = Metric(
            key=key,
            name=getattr(kr, "statement", key),
            type=metric_type,
            persona=getattr(kr, "persona_link", None),
            cadence=getattr(kr, "cadence", "quarterly"),
            baseline=getattr(kr, "baseline", None),
            target=getattr(kr, "target", None),
            direction=getattr(kr, "direction", "increase"),
        )
        self.register(metric)
        return metric

    def get(self, key: str) -> Metric:
        if key not in self._metrics:
            raise KeyError(f"metric '{key}' not registered")
        return self._metrics[key]

    def list_metrics(self) -> List[Metric]:
        return list(self._metrics.values())

    # ------------------------------------------------------------------
    # 数据上传
    # ------------------------------------------------------------------

    def ingest_nps(self, key: str, *, scores: Sequence[float], period: str) -> None:
        self._validate_type(key, "nps")
        self._raw[key].setdefault(period, []).extend(float(s) for s in scores)

    def ingest_ces(self, key: str, *, scores: Sequence[float], period: str) -> None:
        self._validate_type(key, "ces")
        self._raw[key].setdefault(period, []).extend(float(s) for s in scores)

    def ingest_csat(self, key: str, *, scores: Sequence[float], period: str) -> None:
        self._validate_type(key, "csat")
        self._raw[key].setdefault(period, []).extend(float(s) for s in scores)

    def ingest_funnel(
        self,
        key: str,
        *,
        entered: int,
        completed: int,
        period: str,
    ) -> None:
        self._validate_type(key, "goal_conversion")
        if entered < 0 or completed < 0 or completed > entered:
            raise ValueError("invalid funnel values")
        # 用两个值填进 raw（[entered, completed]）
        self._raw[key][period] = [float(entered), float(completed)]

    def ingest_activation(
        self,
        key: str,
        *,
        signups: int,
        activated: int,
        period: str,
    ) -> None:
        self._validate_type(key, "activation")
        if signups < 0 or activated < 0 or activated > signups:
            raise ValueError("invalid activation values")
        self._raw[key][period] = [float(signups), float(activated)]

    def ingest_retention(
        self,
        key: str,
        *,
        cohort: int,
        retained: int,
        period: str,
    ) -> None:
        self._validate_type(key, "retention")
        if cohort < 0 or retained < 0 or retained > cohort:
            raise ValueError("invalid retention values")
        self._raw[key][period] = [float(cohort), float(retained)]

    def ingest_custom(
        self,
        key: str,
        *,
        value: float,
        sample_size: int,
        period: str,
    ) -> None:
        self._validate_type(key, "custom")
        self._raw[key][period] = [float(value), float(sample_size)]

    # ------------------------------------------------------------------
    # 计算
    # ------------------------------------------------------------------

    def compute(self, key: str, *, period: str) -> MetricSnapshot:
        metric = self.get(key)
        raw = self._raw[key].get(period, [])
        if not raw:
            raise ValueError(f"no raw data for {key} in {period}; ingest first")

        if metric.type == "nps":
            value, breakdown = self._compute_nps(raw)
            n = len(raw)
        elif metric.type == "ces":
            value, breakdown = self._compute_ces(raw)
            n = len(raw)
        elif metric.type == "csat":
            value, breakdown = self._compute_csat(raw)
            n = len(raw)
        elif metric.type == "goal_conversion":
            entered, completed = raw[0], raw[1]
            value = (completed / entered * 100) if entered else 0.0
            breakdown = {"entered": entered, "completed": completed}
            n = int(entered)
        elif metric.type == "activation":
            signups, activated = raw[0], raw[1]
            value = (activated / signups * 100) if signups else 0.0
            breakdown = {"signups": signups, "activated": activated}
            n = int(signups)
        elif metric.type == "retention":
            cohort, retained = raw[0], raw[1]
            value = (retained / cohort * 100) if cohort else 0.0
            breakdown = {"cohort": cohort, "retained": retained}
            n = int(cohort)
        elif metric.type == "custom":
            value, n = raw[0], int(raw[1])
            breakdown = {}
        else:  # pragma: no cover
            raise RuntimeError(f"unsupported metric type: {metric.type}")

        snap = MetricSnapshot(
            metric_key=key,
            period=period,
            value=value,
            sample_size=n,
            breakdown=breakdown,
            captured_at=_now_iso(),
        )
        self._snapshots[key].append(snap)
        return snap

    def timeseries(self, key: str) -> List[MetricSnapshot]:
        return sorted(self._snapshots.get(key, []), key=lambda s: s.period)

    def report_okr_progress(self, plan: Any) -> List[Dict[str, Any]]:
        """对接 OKR Bridge：返回每条 KR 的最新进度。"""
        rows: List[Dict[str, Any]] = []
        for obj in getattr(plan, "objectives", []):
            for kr in obj.key_results:
                key = f"kr_{getattr(kr, 'metric', 'unnamed')}_{_slug(getattr(kr, 'persona_link', '') or 'all')}"
                snaps = self._snapshots.get(key, [])
                latest = snaps[-1] if snaps else None
                rows.append(
                    {
                        "objective": obj.statement,
                        "kr": kr.statement,
                        "baseline": kr.baseline,
                        "target": kr.target,
                        "current": latest.value if latest else None,
                        "progress_pct": _progress(kr, latest),
                        "period": latest.period if latest else None,
                    }
                )
        return rows

    # ------------------------------------------------------------------
    # 渲染
    # ------------------------------------------------------------------

    def render_markdown(self, *, persona: Optional[str] = None) -> str:
        lines = [f"# 测量报告：{self.product}", "", f"生成时间：{_now_iso()}", ""]
        metrics = [
            m
            for m in self._metrics.values()
            if persona is None or m.persona == persona
        ]
        if not metrics:
            lines.append("（暂无指标）")
            return "\n".join(lines)
        for m in metrics:
            lines.append(f"## {m.name} (`{m.key}`)")
            lines.append(
                f"- 类型: {m.type}  |  Persona: {m.persona or 'all'}  |  Cadence: {m.cadence}"
            )
            if m.baseline is not None or m.target is not None:
                lines.append(
                    f"- 基线: {m.baseline}  |  目标: {m.target}  |  方向: {m.direction}"
                )
            snaps = self.timeseries(m.key)
            if not snaps:
                lines.append("- 无快照（请先 ingest_*）")
            else:
                lines.append("")
                lines.append("| Period | Value | Sample | Breakdown |")
                lines.append("|---|---|---|---|")
                for s in snaps:
                    lines.append(
                        f"| {s.period} | {s.value:.2f} | {s.sample_size} | "
                        f"{', '.join(f'{k}={v}' for k, v in s.breakdown.items()) or '-'} |"
                    )
            lines.append("")
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # 内部
    # ------------------------------------------------------------------

    def _validate_type(self, key: str, expected: str) -> None:
        m = self.get(key)
        if m.type != expected:
            raise ValueError(
                f"metric '{key}' is type {m.type}, cannot ingest as {expected}"
            )

    @staticmethod
    def _compute_nps(scores: Sequence[float]) -> tuple[float, Dict[str, Any]]:
        n = len(scores)
        if n == 0:
            return 0.0, {}
        promoters = sum(1 for s in scores if s >= 9)
        detractors = sum(1 for s in scores if s <= 6)
        passives = n - promoters - detractors
        value = (promoters - detractors) / n * 100
        return value, {
            "promoters_pct": promoters / n * 100,
            "passives_pct": passives / n * 100,
            "detractors_pct": detractors / n * 100,
            "mean": _stats.mean(scores),
        }

    @staticmethod
    def _compute_ces(scores: Sequence[float]) -> tuple[float, Dict[str, Any]]:
        if not scores:
            return 0.0, {}
        mean = _stats.mean(scores)
        easy_pct = sum(1 for s in scores if s >= 6) / len(scores) * 100
        return mean, {"mean": mean, "easy_pct(>=6)": easy_pct}

    @staticmethod
    def _compute_csat(scores: Sequence[float]) -> tuple[float, Dict[str, Any]]:
        if not scores:
            return 0.0, {}
        satisfied = sum(1 for s in scores if s >= 4) / len(scores) * 100
        return satisfied, {"satisfied_pct": satisfied, "mean": _stats.mean(scores)}


# ---------------------------------------------------------------------------
# 工具
# ---------------------------------------------------------------------------


def _now_iso() -> str:
    return _dt.datetime.now(_dt.timezone.utc).isoformat(timespec="seconds")


def _slug(text: str) -> str:
    out = []
    for ch in (text or ""):
        if ch.isalnum():
            out.append(ch.lower())
        elif ch in "-_":
            out.append(ch)
        else:
            out.append("-")
    return "".join(out).strip("-") or "all"


def _infer_type_from_kr(kr: Any) -> str:
    metric_name = (getattr(kr, "metric", "") or "").lower()
    if "nps" in metric_name:
        return "nps"
    if "ces" in metric_name:
        return "ces"
    if "csat" in metric_name:
        return "csat"
    if "conversion" in metric_name or "funnel" in metric_name:
        return "goal_conversion"
    if "activation" in metric_name:
        return "activation"
    if "retention" in metric_name:
        return "retention"
    return "custom"


def _progress(kr: Any, snap: Optional[MetricSnapshot]) -> Optional[float]:
    if snap is None:
        return None
    baseline = getattr(kr, "baseline", None)
    target = getattr(kr, "target", None)
    if target is None:
        return None
    if baseline is None:
        return None
    span = target - baseline
    if span == 0:
        return 100.0
    return (snap.value - baseline) / span * 100


__all__ = ["MeasurementToolkit", "Metric", "MetricSnapshot"]
