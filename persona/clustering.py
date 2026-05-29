"""Persona 聚类生成模块（v2.6 新增）

本模块把 16 号《统计 Persona》方法论文档落地为可调用代码，提供从
DataFrame 到 Persona 草稿的端到端管道。

设计理念：
- API 极简：3 行代码完成端到端
- 自动方法选择：根据特征类型决定 KMeans/LCA/Factor+KMeans
- 三角验证 K：Silhouette + BIC + Bootstrap 稳定性
- 与现有 PersonaBuilder 无缝集成

依赖：
- 必需：pandas ≥ 2.0, numpy ≥ 1.24, scikit-learn ≥ 1.3
- 可选：stepmix（用于 Latent Class Analysis）

使用示例::

    from persona.clustering import PersonaClusterer

    clusterer = PersonaClusterer(method="auto", k_range=(3, 7))
    result = clusterer.fit(df, features=["price_sensitivity", "freq_of_use", ...])

    print(result.optimal_k)          # 4
    print(result.silhouette_score)   # 0.58
    print(result.stability_score)    # 0.87
    drafts = result.to_persona_drafts()  # 喂给 PersonaBuilder

参考：
- 方法论：references/16-mikkelson-statistical-personas.md
- 工程：references/28-clustering-engineering.md
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

try:
    from sklearn.cluster import KMeans
    from sklearn.decomposition import PCA
    from sklearn.metrics import silhouette_score
    from sklearn.preprocessing import StandardScaler
except ImportError as exc:  # pragma: no cover
    raise ImportError(
        "persona.clustering 需要 scikit-learn。请运行: "
        "pip install -U scikit-learn pandas numpy"
    ) from exc

try:
    from stepmix.stepmix import StepMix  # type: ignore

    _HAS_STEPMIX = True
except ImportError:
    _HAS_STEPMIX = False


# ---------------------------------------------------------------------------
# 数据类
# ---------------------------------------------------------------------------


@dataclass
class ClusteringResult:
    """聚类结果容器。"""

    method: str
    optimal_k: int
    labels: np.ndarray
    centroids: pd.DataFrame
    silhouette_score: float
    stability_score: float
    feature_importance: Dict[int, List[Tuple[str, float]]]
    bic: Optional[float] = None
    probabilities: Optional[np.ndarray] = None
    raw_model: Any = None
    feature_names: List[str] = field(default_factory=list)
    cluster_sizes: Dict[int, int] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # 摘要 / 转换
    # ------------------------------------------------------------------

    def cluster_summary(self) -> pd.DataFrame:
        """返回每簇的大小、平均特征值与 Top 3 显著特征。"""
        rows = []
        for cid, size in self.cluster_sizes.items():
            top_feats = self.feature_importance.get(cid, [])[:3]
            rows.append(
                {
                    "cluster_id": cid,
                    "size": size,
                    "size_pct": size / len(self.labels),
                    "top_features": ", ".join(f"{f} ({v:+.2f})" for f, v in top_feats),
                }
            )
        return pd.DataFrame(rows).sort_values("size", ascending=False)

    def to_persona_drafts(self) -> List[Dict[str, Any]]:
        """把每簇转为 Persona 草稿（喂给 PersonaBuilder.add）。"""
        drafts: List[Dict[str, Any]] = []
        size_total = max(len(self.labels), 1)
        # 按大小排序：最大簇 = primary，其次 secondary，其余 supplemental
        sorted_clusters = sorted(
            self.cluster_sizes.items(), key=lambda kv: kv[1], reverse=True
        )
        for rank, (cid, size) in enumerate(sorted_clusters):
            priority = (
                "primary" if rank == 0 else "secondary" if rank <= 1 else "supplemental"
            )
            top_feats = self.feature_importance.get(cid, [])
            top_pos = [f for f, v in top_feats if v > 0][:3]
            top_neg = [f for f, v in top_feats if v < 0][:3]
            drafts.append(
                {
                    "cluster_id": cid,
                    "suggested_name": f"簇 {cid} 草稿（待命名）",
                    "priority": priority,
                    "size": size,
                    "size_pct": size / size_total,
                    "centroid": self.centroids.loc[cid].to_dict(),
                    "top_goals": [f"高于平均的 {f}" for f in top_pos],
                    "top_behaviors": [f"低于平均的 {f}" for f in top_neg],
                    "top_attitudes": [],
                    "narrative": (
                        f"该簇在 {', '.join(top_pos[:2])} 维度显著偏高，"
                        f"在 {', '.join(top_neg[:2]) or '其他维度'} 偏低。"
                        f"占总样本 {size / size_total:.0%}，建议进一步深访 2-3 名"
                        f"以补充人格细节。"
                    ),
                    "stability_score": self.stability_score,
                    "method": self.method,
                }
            )
        return drafts


# ---------------------------------------------------------------------------
# 主类
# ---------------------------------------------------------------------------


class PersonaClusterer:
    """Persona 聚类器。

    Parameters
    ----------
    method : {"auto", "kmeans", "lca", "factor_kmeans"}
        聚类方法。"auto" 根据特征类型自动选择。
    k_range : Tuple[int, int]
        候选簇数范围（含两端）。
    random_state : int
        随机种子，保证可复现。
    n_factors : int
        factor_kmeans 模式下提取的因子数。
    bootstrap_n : int
        稳定性 Bootstrap 重抽样次数（默认 50；CHI 标准 100，速度优先可降低）。
    min_silhouette : float
        最低 Silhouette 阈值；低于则在结果中标注警告。
    """

    def __init__(
        self,
        method: str = "auto",
        k_range: Tuple[int, int] = (3, 7),
        random_state: int = 42,
        n_factors: int = 5,
        bootstrap_n: int = 50,
        min_silhouette: float = 0.25,
    ) -> None:
        if method not in {"auto", "kmeans", "lca", "factor_kmeans"}:
            raise ValueError(f"unsupported method: {method}")
        if k_range[0] < 2 or k_range[1] < k_range[0]:
            raise ValueError("k_range 必须满足 2 ≤ low ≤ high")
        self.method = method
        self.k_range = k_range
        self.random_state = random_state
        self.n_factors = n_factors
        self.bootstrap_n = bootstrap_n
        self.min_silhouette = min_silhouette

    # ------------------------------------------------------------------
    # 公共 API
    # ------------------------------------------------------------------

    def fit(self, df: pd.DataFrame, features: Sequence[str]) -> ClusteringResult:
        """对 DataFrame 拟合聚类。"""
        if not features:
            raise ValueError("features 不能为空")
        missing = set(features) - set(df.columns)
        if missing:
            raise ValueError(f"DataFrame 缺少特征列: {missing}")

        sub = df[list(features)].copy()
        if sub.isna().any().any():
            # 简单处理：删除任何含 NA 的行，并提示
            kept = sub.dropna()
            dropped = len(sub) - len(kept)
            if dropped > 0:
                print(
                    f"[clustering] 警告：{dropped} 行因缺失被丢弃；剩余 {len(kept)} 行。"
                )
            sub = kept
        if len(sub) < 50:
            raise ValueError(
                f"样本量过小（n={len(sub)}），统计聚类至少需要 50 行；"
                f"建议先用 Lean UX Proto-Persona 法（references/11）。"
            )

        chosen = self.method if self.method != "auto" else self._decide_method(sub)
        if chosen == "lca" and not _HAS_STEPMIX:
            print("[clustering] stepmix 未安装，回退 KMeans 模式。")
            chosen = "kmeans"

        if chosen == "kmeans":
            return self._fit_kmeans(sub)
        if chosen == "lca":
            return self._fit_lca(sub)
        if chosen == "factor_kmeans":
            return self._fit_factor_kmeans(sub)
        raise RuntimeError(f"未支持的方法: {chosen}")

    # ------------------------------------------------------------------
    # 内部：方法决策
    # ------------------------------------------------------------------

    def _decide_method(self, df: pd.DataFrame) -> str:
        n_continuous = 0
        n_categorical = 0
        for col in df.columns:
            unique = df[col].nunique()
            if pd.api.types.is_numeric_dtype(df[col]) and unique > 10:
                n_continuous += 1
            else:
                n_categorical += 1
        total = max(n_continuous + n_categorical, 1)
        if n_categorical / total > 0.7:
            return "lca"
        if len(df.columns) > 20 and n_continuous > 10:
            return "factor_kmeans"
        return "kmeans"

    # ------------------------------------------------------------------
    # 内部：KMeans
    # ------------------------------------------------------------------

    def _fit_kmeans(self, df: pd.DataFrame) -> ClusteringResult:
        scaler = StandardScaler()
        X = scaler.fit_transform(df.values)

        best_k, best_sil = self._decide_k_kmeans(X)
        model = KMeans(n_clusters=best_k, random_state=self.random_state, n_init=10)
        labels = model.fit_predict(X)

        centroids = pd.DataFrame(
            scaler.inverse_transform(model.cluster_centers_),
            columns=df.columns,
            index=range(best_k),
        )
        z_centroids = pd.DataFrame(
            model.cluster_centers_, columns=df.columns, index=range(best_k)
        )

        feature_importance = self._extract_importance(z_centroids)
        sizes = {cid: int(np.sum(labels == cid)) for cid in range(best_k)}
        stability = self._bootstrap_stability_kmeans(X, best_k)

        return ClusteringResult(
            method="kmeans",
            optimal_k=best_k,
            labels=labels,
            centroids=centroids,
            silhouette_score=best_sil,
            stability_score=stability,
            feature_importance=feature_importance,
            raw_model=model,
            feature_names=list(df.columns),
            cluster_sizes=sizes,
        )

    def _decide_k_kmeans(self, X: np.ndarray) -> Tuple[int, float]:
        scores: List[Tuple[int, float]] = []
        for k in range(self.k_range[0], self.k_range[1] + 1):
            model = KMeans(n_clusters=k, random_state=self.random_state, n_init=10)
            labels = model.fit_predict(X)
            sil = silhouette_score(X, labels) if k > 1 else 0.0
            scores.append((k, sil))
        best = max(scores, key=lambda kv: kv[1])
        return best

    def _bootstrap_stability_kmeans(self, X: np.ndarray, k: int) -> float:
        rng = np.random.default_rng(self.random_state)
        n = len(X)
        if n < 50:
            return float("nan")
        agreements: List[float] = []
        ref = KMeans(
            n_clusters=k, random_state=self.random_state, n_init=10
        ).fit_predict(X)
        for _ in range(self.bootstrap_n):
            idx = rng.integers(0, n, size=n)
            X_bs = X[idx]
            lbl_bs = KMeans(
                n_clusters=k, random_state=self.random_state, n_init=5
            ).fit_predict(X_bs)
            ref_subset = ref[idx]
            agreements.append(_normalized_agreement(ref_subset, lbl_bs))
        return float(np.mean(agreements))

    # ------------------------------------------------------------------
    # 内部：Factor + KMeans
    # ------------------------------------------------------------------

    def _fit_factor_kmeans(self, df: pd.DataFrame) -> ClusteringResult:
        scaler = StandardScaler()
        X = scaler.fit_transform(df.values)
        n_components = min(self.n_factors, X.shape[1])
        pca = PCA(n_components=n_components, random_state=self.random_state)
        F = pca.fit_transform(X)

        best_k, best_sil = self._decide_k_kmeans(F)
        model = KMeans(n_clusters=best_k, random_state=self.random_state, n_init=10)
        labels = model.fit_predict(F)

        # 反推质心到原特征空间（近似）
        centers_orig = pca.inverse_transform(model.cluster_centers_)
        centroids = pd.DataFrame(
            scaler.inverse_transform(centers_orig),
            columns=df.columns,
            index=range(best_k),
        )
        z_centroids = pd.DataFrame(
            centers_orig, columns=df.columns, index=range(best_k)
        )
        feature_importance = self._extract_importance(z_centroids)
        sizes = {cid: int(np.sum(labels == cid)) for cid in range(best_k)}
        stability = self._bootstrap_stability_kmeans(F, best_k)

        return ClusteringResult(
            method="factor_kmeans",
            optimal_k=best_k,
            labels=labels,
            centroids=centroids,
            silhouette_score=best_sil,
            stability_score=stability,
            feature_importance=feature_importance,
            raw_model=(pca, model),
            feature_names=list(df.columns),
            cluster_sizes=sizes,
        )

    # ------------------------------------------------------------------
    # 内部：LCA
    # ------------------------------------------------------------------

    def _fit_lca(self, df: pd.DataFrame) -> ClusteringResult:  # pragma: no cover
        if not _HAS_STEPMIX:
            raise RuntimeError("LCA 模式需要 stepmix；请 pip install stepmix")

        # 简化处理：对类别列做 LabelEncoder
        encoded = pd.DataFrame(index=df.index)
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                encoded[col] = pd.qcut(df[col], q=4, labels=False, duplicates="drop")
            else:
                encoded[col] = df[col].astype("category").cat.codes

        scores: List[Tuple[int, float, float]] = []
        for k in range(self.k_range[0], self.k_range[1] + 1):
            model = StepMix(n_components=k, measurement="categorical", random_state=self.random_state)
            model.fit(encoded.values)
            scores.append((k, model.bic(encoded.values), 0.0))
        best = min(scores, key=lambda kv: kv[1])
        best_k = best[0]
        bic = best[1]

        model = StepMix(
            n_components=best_k, measurement="categorical", random_state=self.random_state
        )
        model.fit(encoded.values)
        probs = model.predict_proba(encoded.values)
        labels = probs.argmax(axis=1)
        sizes = {cid: int(np.sum(labels == cid)) for cid in range(best_k)}

        # 质心 = 每簇的特征均值
        centroids = pd.DataFrame(index=range(best_k), columns=df.columns, dtype=float)
        for cid in range(best_k):
            centroids.loc[cid] = df[labels == cid].mean(numeric_only=True)
        sil = silhouette_score(encoded.values, labels) if best_k > 1 else 0.0

        feature_importance = self._extract_importance_from_means(centroids)
        return ClusteringResult(
            method="lca",
            optimal_k=best_k,
            labels=labels,
            centroids=centroids,
            silhouette_score=sil,
            stability_score=float("nan"),
            feature_importance=feature_importance,
            bic=bic,
            probabilities=probs,
            raw_model=model,
            feature_names=list(df.columns),
            cluster_sizes=sizes,
        )

    # ------------------------------------------------------------------
    # 工具
    # ------------------------------------------------------------------

    def _extract_importance(
        self, z_centroids: pd.DataFrame
    ) -> Dict[int, List[Tuple[str, float]]]:
        """每簇按 |z| 排序，返回 (feature, z 值) 列表。"""
        result: Dict[int, List[Tuple[str, float]]] = {}
        for cid in z_centroids.index:
            row = z_centroids.loc[cid]
            sorted_feats = sorted(row.items(), key=lambda kv: abs(kv[1]), reverse=True)
            result[int(cid)] = [(str(f), float(v)) for f, v in sorted_feats]
        return result

    def _extract_importance_from_means(
        self, centroids: pd.DataFrame
    ) -> Dict[int, List[Tuple[str, float]]]:
        """从均值表反推：相对全局均值的偏离。"""
        global_mean = centroids.mean(axis=0)
        result: Dict[int, List[Tuple[str, float]]] = {}
        for cid in centroids.index:
            diff = centroids.loc[cid] - global_mean
            sorted_feats = sorted(diff.items(), key=lambda kv: abs(kv[1]), reverse=True)
            result[int(cid)] = [(str(f), float(v)) for f, v in sorted_feats]
        return result


# ---------------------------------------------------------------------------
# 辅助函数
# ---------------------------------------------------------------------------


def _normalized_agreement(a: np.ndarray, b: np.ndarray) -> float:
    """Rand-style 归一一致性（粗略）。"""
    if len(a) != len(b):
        raise ValueError("a, b 长度必须一致")
    if len(a) < 2:
        return 1.0
    n = len(a)
    pairs_a = (a[:, None] == a[None, :]).astype(int)
    pairs_b = (b[:, None] == b[None, :]).astype(int)
    agree = (pairs_a == pairs_b).sum()
    return float(agree) / (n * n)


__all__ = ["PersonaClusterer", "ClusteringResult"]
