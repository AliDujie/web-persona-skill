# 31 · 工程化：Persona × 测量工具包（NPS / CES / CSAT / Goal Funnel）

> 来源：Reichheld, F. *The Ultimate Question 2.0* (HBR Press, 2011)；Dixon, M. et al. *The Effortless Experience* (2013)；本技能 02 号《测量结果》方法论代码化；Pendo / Amplitude / GA4 业界实践。
>
> D 系列工程化文档第 4 篇。提供 `persona/measurement_toolkit.py` 模块，把 NPS / CES / CSAT / Persona-tagged Funnel 等核心测量指标做成可注册、可计算、可导出的标准化数据结构。

---

## 1. 模块定位

| 项 | 内容 |
|---|---|
| 模块路径 | `persona/measurement_toolkit.py` |
| 主类 | `MeasurementToolkit`、`Metric`、`MetricSnapshot` |
| 输入 | 调研/日志原始数据 + Persona 标签 |
| 输出 | 按 Persona 切片的指标快照 + 时序追踪 + 导出 |
| 依赖 | 仅标准库（可选 pandas/numpy 加速） |
| 与 measure.py 关系 | measure.py 偏可用性测试；本模块偏长期指标体系 |

---

## 2. 6 类核心指标

| 指标 | 中文 | 计算公式 | Persona 切片 |
|---|---|---|---|
| **NPS** | 净推荐值 | %推荐者 − %贬损者（0-10 量表） | 是 |
| **CES** | 费力度 | 1-7 反向加权 | 是 |
| **CSAT** | 满意度 | %满意（4-5/5）| 是 |
| **Goal Conversion** | 目标转化率 | 完成数 / 进入数 | 是（按 Persona 主目标） |
| **Activation Rate** | 激活率 | 达到激活事件人数 / 注册人数 | 是 |
| **Retention** | 留存（D7/D30） | 第 N 日仍活跃比例 | 是 |

---

## 3. 接口预览

```python
from persona.measurement_toolkit import MeasurementToolkit, Metric

kit = MeasurementToolkit(product="我的产品")

# 1. 注册 NPS 指标
kit.register(Metric(
    key="nps_persona_lin_jia",
    name="林佳 NPS",
    type="nps",
    persona="林佳",
    cadence="quarterly",
))

# 2. 上传原始打分数据
kit.ingest_nps("nps_persona_lin_jia",
               scores=[9, 10, 7, 8, 9, 6, 10, 4, 9, 8],
               period="2026Q2")

# 3. 计算 + 拿快照
snap = kit.compute("nps_persona_lin_jia", period="2026Q2")
print(snap.value, snap.sample_size)   # 30.0, 10

# 4. 时序对比
print(kit.timeseries("nps_persona_lin_jia"))

# 5. 导出 markdown 报告
print(kit.render_markdown(persona="林佳"))
```

---

## 4. 6 类指标计算公式

### 4.1 NPS
```
推荐者 = score ≥ 9
贬损者 = score ≤ 6
NPS = (推荐者数 - 贬损者数) / 总数 * 100
```

### 4.2 CES（7 点 Likert）
```
均值 = sum(scores) / n
反向：1 = 极费力，7 = 极不费力
报告：均值 + %≥6 比例
```

### 4.3 CSAT（5 点）
```
满意 = score ≥ 4
CSAT = 满意人数 / 总数 * 100
```

### 4.4 Goal Conversion（漏斗）
```
conv = completed / entered
按 Persona 切片
```

### 4.5 Activation Rate
```
activation = reached_event_in_X_days / signup
通常 X = 7
```

### 4.6 Retention（D7/D30）
```
D7 = active_on_day_7 / cohort_size
D30 = active_on_day_30 / cohort_size
```

---

## 5. 与 OKR Bridge 的协同

每个 KR 自动绑定 1 个 Metric 注册项：

```python
from persona.okr_bridge import OKRBridge
from persona.measurement_toolkit import MeasurementToolkit

bridge = OKRBridge(quarter="2026Q3", product="我的产品")
plan = bridge.derive_okrs(profiles)

kit = MeasurementToolkit(product="我的产品")
for kr in plan.key_results:
    kit.register_from_kr(kr)
```

→ 注册完成后，季度复盘时可直接 `kit.report_okr_progress(plan)` 输出每条 KR 的进度。

---

## 6. 反模式 (Anti-patterns)

| 反模式 | 症状 | 修复 |
|---|---|---|
| NPS 单数字汇报 | 只看 47 这个数字 | 必看分布 + Persona 切片 |
| 不分 cohort | 把所有用户混算 | 按注册周分队列 |
| CES 当 NPS 用 | 量表/方向混淆 | 严格遵守原始量表 |
| 不绑定 KR | 测量与 OKR 各做各的 | 用 register_from_kr 自动桥接 |
| 不留 baseline | KR 上线时无基线 | toolkit 提示 baseline 缺失 |
| 频次不一致 | 月报混合季报混合年报 | cadence 字段强制 |

---

## 7. 何时使用本模块

✅ 用：
- 已发布产品需要长期跟踪
- 多 Persona 项目，想知道每类用户体验差异
- 季度 OKR 复盘
- 与 NPS / 客服 / 调研团队协同

⛔ 不用：
- 极早期 MVP（指标定义先于数据）
- 单一指标小项目（直接 Excel 即可）

---

## 8. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| 02-measure 方法论 | 本模块为其代码实现 |
| 30-OKR Bridge | KR 自动注册指标 |
| 19-Service Design | 按 Journey 阶段切 NPS/CSAT |
| `persona/measure.py` | 互补：那是可用性测试，这是长期指标 |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| 6 类标准指标 | NPS/CES/CSAT/Goal/Activation/Retention |
| 全部支持 Persona 切片 | 每个指标必标 persona |
| 与 OKR Bridge 联动 | KR 自动注册 |
| Cadence 强制 | 防混合频次乱用 |
| Baseline 提示 | KR 上线前必填基线 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `nps-weekly-pipeline` | NPS 数据接入与周报 |
| `analytics-data-analysis` | 漏斗 / 留存 / 活跃数据计算 |
| `feedback-synthesis` | 文本反馈 → 主题贴到 NPS 分项 |
| `mindshare-88vip-analysis` | 心智测量与 Persona 切片对照 |
| `decision-tracker` | 测量异常驱动决策 |
