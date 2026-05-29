# 30 · 工程化：Persona × OKR & Roadmap Bridge

> 来源：Doerr, J. *Measure What Matters* (Portfolio, 2018)；Wodtke, C. *Radical Focus* (2nd ed., 2021)；本技能 02 号《测量结果》方法论扩展；Cagan, M. *Inspired* (2nd ed.) Outcome-Driven Roadmaps。
>
> D 系列工程化文档第 3 篇。把 Persona 的 Goals / Jobs / Forces 自动转译成 Objectives + Key Results + 路线图优先级，让 Persona 不只是"研究产物"而是"战略投入"。

---

## 1. 模块定位

| 项 | 内容 |
|---|---|
| 模块路径 | `persona/okr_bridge.py` |
| 主类 | `OKRBridge`、`Objective`、`KeyResult`、`RoadmapItem` |
| 输入 | `PersonaProfile` 列表 + 业务期望 |
| 输出 | 推荐 Objectives + KRs + RICE/ICE 排序的路线图条目 |
| 依赖 | 仅标准库 |

---

## 2. 核心映射规则

| Persona 元素 | 自动映射到 |
|---|---|
| Goals (Mulder) | Objective 文案 |
| Pain Points | Objective 必要性证据 |
| JTBD Outcome | Key Result 数字目标 |
| Job Forces (Push/Pull) | RICE Reach + Impact |
| Job Forces (Habit/Anxiety) | RICE Confidence 风险扣减 |
| Behavior 频率 | RICE Reach |
| Cluster Size | RICE Reach（多 Persona 时） |

---

## 3. RICE 优先级模型

| 项 | 含义 | 来自 Persona |
|---|---|---|
| **R**each | 多少人/期 | 簇大小 / 占比 |
| **I**mpact | 影响程度 0.25-3.0 | Pain × Frequency |
| **C**onfidence | 把握度 0.0-1.0 | 数据成熟度 + 验证次数 |
| **E**ffort | 人月 | 工程估算 |
| **Score** | (R × I × C) / E | 自动计算 |

### 3.1 ICE 简化版（早期项目）
**Score = Impact × Confidence × Ease**（Effort 倒数）

---

## 4. 接口预览

```python
from persona import PersonaBuilder
from persona.okr_bridge import OKRBridge

builder = PersonaBuilder("我的产品")
builder.add(name="林佳", priority="primary",
            goals=["快速搞定辅食", "晚 22:00 前完成一天家务"],
            behaviors=["晚 21:00-22:00 集中用 App"],
            ...)

bridge = OKRBridge(quarter="2026Q3", product="我的产品")
plan = bridge.derive_okrs(builder.profiles, business_themes=["留存", "活跃"])

print(plan.objectives)          # [Objective(...), ...]
for kr in plan.key_results:
    print(kr.statement, kr.target, kr.baseline)

roadmap = bridge.score_roadmap(plan.candidate_features, model="rice")
for item in roadmap[:10]:
    print(f"{item.score:.2f}  {item.name}")
```

---

## 5. 自动 Objective 生成模板

每个 primary Persona 至少产出 1 条 Objective：

```
Objective <自动生成 ID>
驱动: <Persona name>
目标: 让 <Persona name> 在 <场景> 中 <达到结果>
理由: 来自痛点：<top pain>；机会规模：<reach>
```

---

## 6. KR 自动生成 4 类模板

| 类 | 模板 | 例 |
|---|---|---|
| 行为类 | "周活 / 完成率 / 频次 提升 X%" | "林佳 周活 ≥ 3 次率 25% → 40%" |
| 体验类 | "NPS / CSAT / CES 提升 X 分" | "辅食流程 NPS +12" |
| 转化类 | "漏斗 X→Y 转化 Z%" | "辅食推荐 → 收藏 12% → 25%" |
| 时长类 | "完成时长缩短 / 增长 X%" | "Tiny Habit ABC 命中 ≥ 70%" |

---

## 7. 路线图打分流程

```python
candidates = [
    {"name": "周末备餐推荐", "reach": 8000, "impact": 2.0,
     "confidence": 0.7, "effort": 4, "persona_link": "林佳"},
    {"name": "夜间深色模式", "reach": 12000, "impact": 1.0,
     "confidence": 0.9, "effort": 1, "persona_link": "林佳"},
    ...
]

scored = bridge.score_roadmap(candidates, model="rice")
# 自动按分数排序；考虑 Persona priority 加权
```

---

## 8. 反模式 (Anti-patterns)

| 反模式 | 症状 | 修复 |
|---|---|---|
| Output→KR | 拿"上线 X 功能"当 KR | KR 必须是结果指标 |
| 把 Persona 当 KR | "服务好林佳" | 改为可量化结果 |
| 忽略 Confidence | RICE 只看 R×I/E | 加 C 抑制不确定项目 |
| 不挂钩 Persona | OKR 与 Persona 脱钩 | 每条 Objective 必有 persona_link |
| 季度无对账 | 一季度后不复盘 | 模块输出含 review_cadence |

---

## 9. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| 02-measure 方法论 | 本模块对接现有 measure 体系 |
| 22-JTBD | Outcomes / Forces 直接映射 KR / RICE |
| 31-measurement | 测量数据 → KR 进度回灌 |
| `persona/measure.py` | 复用现有 metric 注册 |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| Persona → OKR → 路线图 | 一条工程化链路 |
| RICE 自动计算 | 输入 4 字段，自动评分 |
| KR 必为结果 | 拒绝 output 类伪 KR |
| 季度复盘 | 自带 cadence 字段 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `roadmap-planning` | RICE 直喂路线图工作坊 |
| `prd-writing` | PRD 关键章节自动生成 |
| `decision-tracker` | OKR 决策记录联动 |
| `mvp-scoping` | RICE Top N → MVP 切片 |
