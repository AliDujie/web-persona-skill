# 28 · 工程化：Persona × Clustering（聚类生成）

> 来源：scikit-learn 官方文档；Salminen et al. *Persona Clustering in Practice* (2024)；本技能 16 号《统计 Persona》方法论笔记的代码化实现。
>
> 这是 D 系列工程化文档第 1 篇。把 16 号方法论变成可调用的 `persona/clustering.py` 模块，实现"输入 DataFrame → 输出簇质心 + Persona 草稿"的端到端管道。

---

## 1. 模块定位

| 项 | 内容 |
|---|---|
| 模块路径 | `persona/clustering.py` |
| 主类 | `PersonaClusterer` |
| 输入 | `pandas.DataFrame`（特征矩阵） + 可选元数据 |
| 输出 | `ClusteringResult` 含质心、标签、稳定性、Persona 骨架 |
| 依赖 | `pandas`, `numpy`, `scikit-learn`（required）；`stepmix`（可选，用于 LCA） |
| 兼容范围 | sklearn ≥ 1.3, pandas ≥ 2.0, Python ≥ 3.10 |

---

## 2. 接口快速预览

```python
from persona.clustering import PersonaClusterer

# 1. 初始化
clusterer = PersonaClusterer(
    method="auto",        # auto / kmeans / lca / factor_kmeans
    k_range=(3, 7),       # 候选簇数
    random_state=42,
)

# 2. 拟合数据
result = clusterer.fit(df, features=["price_sensitivity", "freq_of_use", ...])

# 3. 检查输出
print(result.optimal_k)           # 4
print(result.silhouette_score)    # 0.58
print(result.stability_score)     # 0.87 (bootstrap 100x)
print(result.cluster_summary())   # 每簇大小、质心、Top 特征
print(result.to_persona_drafts()) # 4 张 Persona 骨架字典

# 4. 给原 DataFrame 打标签
df["cluster_id"] = result.labels
df["cluster_prob"] = result.probabilities  # LCA 才有
```

---

## 3. 完整代码（生产级）

详见仓库 `persona/clustering.py`，本节摘录关键设计：

### 3.1 数据类
```python
@dataclass
class ClusteringResult:
    method: str
    optimal_k: int
    labels: np.ndarray
    probabilities: Optional[np.ndarray]  # LCA 才有
    centroids: pd.DataFrame              # K x feature
    silhouette_score: float
    bic: Optional[float]
    stability_score: float               # bootstrap
    feature_importance: Dict[int, List[Tuple[str, float]]]
    raw_model: Any                       # 底层 sklearn / stepmix
```

### 3.2 主类
```python
class PersonaClusterer:
    def __init__(self, method="auto", k_range=(3, 7), random_state=42, ...): ...
    def fit(self, df, features) -> ClusteringResult: ...
    def _decide_method(self, df, features) -> str: ...    # 自动选 KMeans/LCA/Factor+KMeans
    def _decide_k(self, X) -> int: ...                    # Elbow + Silhouette + BIC 三角
    def _bootstrap_stability(self, X, k, n_iter=100) -> float: ...
    def _extract_top_features(self, centroids) -> Dict: ...
```

### 3.3 决策方法的内部逻辑
```python
def _decide_method(self, df, features):
    n_continuous = sum(pd.api.types.is_numeric_dtype(df[f]) and df[f].nunique() > 10
                       for f in features)
    n_categorical = len(features) - n_continuous
    if n_categorical / len(features) > 0.7:
        return "lca"
    if len(features) > 20 and n_continuous > 10:
        return "factor_kmeans"
    return "kmeans"
```

---

## 4. 使用流程（端到端 6 步）

| 步 | 命令 |
|---|---|
| 1 | `pip install -U scikit-learn pandas numpy stepmix` |
| 2 | 准备 DataFrame：去缺失 > 30% 行，编码类别变量 |
| 3 | `clusterer = PersonaClusterer(method="auto")` |
| 4 | `result = clusterer.fit(df, features=[...])` |
| 5 | 检查 `result.stability_score >= 0.8`；不达标增加样本/换 K |
| 6 | `drafts = result.to_persona_drafts()` → 喂给 `PersonaBuilder` |

---

## 5. 与现有 PersonaBuilder 的衔接

```python
from persona import PersonaBuilder
from persona.clustering import PersonaClusterer

# 1. 先聚类
clusterer = PersonaClusterer()
result = clusterer.fit(df, features=FEATURES)

# 2. 把每个簇骨架转为 PersonaProfile
builder = PersonaBuilder("我的产品")
for draft in result.to_persona_drafts():
    builder.add(
        name=draft["suggested_name"],
        priority=draft["priority"],     # 簇大小 → primary/secondary
        quote=draft.get("quote", ""),
        goals=draft["top_goals"],
        behaviors=draft["top_behaviors"],
        attitudes=draft["top_attitudes"],
        bio=draft["narrative"],
        cluster_meta={                  # v2.6 新增字段
            "method": result.method,
            "centroid": draft["centroid"],
            "size": draft["size"],
            "stability": result.stability_score,
        },
    )

print(builder.render_all())
```

---

## 6. 评估指标的解读

| 指标 | 阈值 | 解读 |
|---|---|---|
| Silhouette | ≥ 0.5 | 良好；0.25-0.5 一般；< 0.25 差 |
| BIC | 越低越好 | 与候选 K 比较，最低者 |
| Stability (Bootstrap) | ≥ 0.80 | 80% 用户簇标签稳定；< 0.7 重做 |
| 簇大小比例 | 各簇 ≥ 5% | 过小簇 = 噪声 |
| 解释方差（Factor 法） | ≥ 60% | 因子提取的总方差 |

---

## 7. 反模式（与代码层）

| 反模式 | 症状 | 修复 |
|---|---|---|
| 不标准化 | KMeans 偏向高方差变量 | 强制 z-score |
| 把 ID/时间戳当特征 | 算法错乱 | features 白名单严格 |
| K 直接拍 | "我们就要 5 个" | 用 fit 自动 + 业务复核 |
| Bootstrap 跳过 | 速度优先 | 强制至少 30 次重抽样 |
| 中文标签直接喂 | 模型炸 | 类别变量先 OneHot/LabelEncoder |

---

## 8. 何时使用本模块

✅ 用：
- 大样本（n ≥ 200）问卷/行为数据
- 想给团队一套数据驱动 Persona 草稿
- 重做老 Persona 时验证现有分群是否合理
- 与 `mindshare-88vip-analysis` 等数据型技能联动

⛔ 不用：
- n < 100（统计意义不足）
- 完全无结构化数据（先访谈）
- 团队未理解聚类原理（先读 16 号文档）

---

## 9. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| 16-Statistical 方法论 | 本模块即其代码实现 |
| `persona/segment.py` | 老的 segment 法可保留；clustering 为新版 |
| 27-bias-audit | 聚类后必跑偏差审计（簇是否系统性偏少数群体） |
| 30-okr-bridge | 簇 → 业务指标的对接 |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| API 简洁 | 3 行代码完成端到端 |
| 自动方法选择 | 根据特征类型自动选 KMeans/LCA/Factor |
| 三角验证 K | Silhouette + BIC + 稳定性 |
| 与 PersonaBuilder 无缝集成 | 输出可直喂构建器 |
| 偏差审计强制 | 聚类后必查公平性 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `analytics-data-analysis` | 跑聚类、可视化质心 |
| `mindshare-88vip-analysis` | ODPS 大样本数据接入 |
| `feedback-synthesis` | 文本反馈 → 嵌入 → 聚类 |
| `decision-tracker` | 簇选择决策记录 |
