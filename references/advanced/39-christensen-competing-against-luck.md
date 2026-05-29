# 39 — Clayton Christensen · Competing Against Luck: The Story of Innovation and Customer Choice (2016)

> **Tier F · JTBD 理论源头**｜关键词：Jobs to Be Done 原版、Milkshake Story、Forces of Progress、Hiring/Firing、Circumstance-Based Categorization

---

## 一、核心定位

这是 JTBD 理论的"源头活水"。现有 `references/22-jtbd-persona-integration.md` 基于 Klement 的实操集成视角，而 Christensen 本书是**理论起源**——解释"为什么人不是按人口统计做选择，而是按'要完成的任务'做选择"。理解这本书 = 理解为什么 Persona 需要从"是谁"升级到"要做什么"。

### 1.1 Christensen vs Klement 的区别

| 维度 | Christensen (本书) | Klement (Ref #22) |
|---|---|---|
| 定位 | 理论创始/战略视角 | 实操集成/设计师视角 |
| 核心概念 | Job + Circumstance + Hiring | Job Story + Switch Interview |
| 适用层级 | CEO/战略/商业模式 | PM/Designer/Sprint |
| Persona 关系 | "Persona 按人分类是错的" | "Persona + Job 可以共存互补" |
| 本 skill 用法 | 理论根基 + 战略决策 | 日常工作流集成 |

---

## 二、核心理论：Job to Be Done

### 2.1 Milkshake Story（经典案例）

> 一家快餐连锁想提高奶昔销量。按传统 Persona 做法：调研了"35岁男性通勤族"的口味偏好，改配方——没用。

**Christensen 的发现**：

| 早晨奶昔 | 下午奶昔 |
|---|---|
| Job：让长距离通勤不无聊 | Job：让孩子开心/做好爸爸 |
| 竞品：香蕉、贝果、甜甜圈、播客 | 竞品：去游乐场、买玩具 |
| 需要：浓稠（撑得久）、吸管（单手） | 需要：小杯（不想等太久） |
| 改进方向：更浓、加果粒、提前备好 | 改进方向：更小杯、更快出餐 |

**启示**：同一个人（35岁男性）在不同**Circumstance（情境）**下雇佣同一产品来做**完全不同的 Job**。人口统计 Persona 无法解释这个差异——只有 Job 能解释。

### 2.2 Job 的正式定义

> "A Job to Be Done is the progress that a person is trying to make in a particular circumstance."

三要素分解：

| 要素 | 定义 | 例 |
|---|---|---|
| Progress | 从当前状态到更好状态的移动 | "从无聊→不无聊" |
| Person | 任何人（不限于人口统计类型） | 通勤者 |
| Circumstance | 特定时间/地点/情境/约束 | "早晨7:30开车上班路上、单手" |

### 2.3 Job 三层（Functional + Emotional + Social）

| 层次 | 定义 | Milkshake 例 |
|---|---|---|
| Functional | 实际要完成的任务 | 填饱肚子 + 打发时间 |
| Emotional | 内心感受 | 不想无聊/焦虑 |
| Social | 别人怎么看我 | "我是个负责任的通勤者" |

---

## 三、Forces of Progress（进步的四种力量）

### 3.1 四力模型

```
         推向新方案                    拉回旧方案
    ┌─────────────────┐          ┌─────────────────┐
    │ Push (of the    │          │ Anxiety (of the │
    │ current situation)│         │ new solution)   │
    │ "现状太痛了"      │          │ "新东西靠谱吗？" │
    └────────┬────────┘          └────────┬────────┘
             │                             │
             ▼                             ▼
    ┌─────────────────┐          ┌─────────────────┐
    │ Pull (of the    │          │ Habit (of the   │
    │ new solution)   │          │ current way)    │
    │ "新方案好诱人"    │          │ "老办法虽然不好  │
    │                 │          │  但至少熟悉"     │
    └─────────────────┘          └─────────────────┘

切换发生条件: Push + Pull > Anxiety + Habit
```

### 3.2 四力与 Persona 的关系

| 力量 | Persona 维度映射 |
|---|---|
| Push | Pain Points（当前痛点） |
| Pull | Goals / Desired Outcome |
| Anxiety | Barriers to Adoption / Trust Issues |
| Habit | Current Solutions / Switching Cost |

### 3.3 Persona 增强：加入 Forces 字段

```yaml
persona:
  name: "效率达人小王"
  # 传统字段...
  forces_of_progress:
    push: "每次订酒店要花30分钟比价，很烦"
    pull: "如果有个工具2分钟搞定，太棒了"
    anxiety: "个性化推荐会不会暴露我的隐私？"
    habit: "虽然慢，但携程至少不会出错"
```

---

## 四、Circumstance-Based Categorization

### 4.1 核心主张

> Christensen: "The critical unit of analysis is the circumstance, not the customer."

| 传统分类（按人） | Christensen 分类（按情境） |
|---|---|
| "35岁男性白领" | "早晨独自通勤 + 需要打发30分钟" |
| 看起来精确实则无用 | 直接指向产品设计方向 |
| 一个 Persona 适用所有场景 | 同一人在不同情境有不同 Job |

### 4.2 情境变量清单

| 维度 | 例 |
|---|---|
| When（时间） | 早晨/深夜/周末/出差前 |
| Where（地点） | 通勤中/办公室/家里沙发 |
| With whom（社交） | 独处/和家人/和同事 |
| While doing what（并行任务） | 开车/等人/做饭 |
| Constraint（约束） | 单手/静音环境/弱网 |
| Emotional state（情绪） | 焦虑/无聊/兴奋 |
| Energy level（精力） | 精力充沛/疲惫 |

### 4.3 Persona × Circumstance 矩阵

```
           早晨通勤    午休碎片    出差前夜    周末闲逛
效率达人     Job A       Job B       Job C       Job D
社交推荐型   Job E       Job F       Job G       Job H
价格敏感型   Job I       Job J       Job K       Job L
```

> 每个格子是一个独立的"Job Instance"——产品设计应瞄准**格子**，而非**行**。

---

## 五、Hiring & Firing（雇佣与解雇）

### 5.1 核心隐喻

> 客户不是"购买"产品——是**雇佣**产品来帮他完成一个 Job。当产品完不成这个 Job 时，客户会**解雇**它。

### 5.2 Hiring Criteria（雇佣标准）

| 标准 | 对应 |
|---|---|
| 能完成 Functional Job | 基本功能 |
| 情感上让我舒服 | UX / Brand Feeling |
| 社交上不丢脸 | Social Proof / Brand Image |
| 比现有方案好"够多" | Push + Pull > Anxiety + Habit |
| 获取成本可接受 | Price / Learning Curve |

### 5.3 Firing Signals（解雇信号）

| 信号 | 意味着 |
|---|---|
| 使用频率下降 | Job 没被满足/换了替代品 |
| 只用部分功能 | 产品解决了一半 Job |
| 投诉/差评 | 主动解雇前奏 |
| 推荐意愿 (NPS) 为负 | 即将或已经解雇 |

---

## 六、非消费（Non-consumption）

### 6.1 定义

> 当没有任何产品被雇佣来完成某个 Job 时——那个 Job 处于"非消费"状态。这是最大的创新机会。

### 6.2 识别非消费的方法

| 信号 | 例 |
|---|---|
| Workaround 很痛苦但"凑合" | 用 Excel 管客户关系 |
| 干脆放弃不做 | "旅行比价太累了，随便订一个" |
| 委托给别人 | "让助理帮我订" |
| 等待技术/价格变化 | "等5G普及了再说" |

### 6.3 非消费 × Persona

- 非消费往往发生在**现有 Persona 未覆盖**的人群中
- 发现非消费 = 发现新 Persona 的机会
- 用 Alvarez 的 Lean CustDev 方法去验证非消费 Job 是否值得解决

---

## 七、Job Spec（任务规格书）

### 7.1 模板

```markdown
## Job Spec: [Job 名称]

**Job Statement**: 
When I [circumstance], I want to [progress], so I can [outcome].

**Functional Dimension**: [具体要完成什么]
**Emotional Dimension**: [想要什么感觉]
**Social Dimension**: [想被怎么看]

**Current Solutions Hired**:
1. [方案1] — 优点: / 缺点:
2. [方案2] — 优点: / 缺点:

**Non-consumption**: [什么情况下干脆不做]

**Forces**:
- Push: [现状之痛]
- Pull: [理想之美]
- Anxiety: [切换之虑]
- Habit: [惯性之力]

**Success Metrics**: [怎么知道 Job 被很好地完成了]
```

---

## 八、JTBD 与 Persona 的整合策略

### 8.1 三种整合模式

| 模式 | 做法 | 适合 |
|---|---|---|
| Job-first, Persona-second | 先识别 Job → 再给每个 Job 画执行者画像 | 新产品/新市场 |
| Persona-first, Job-overlay | 先有 Persona → 给每个 Persona 标记核心 Job | 已有用户基础 |
| Matrix（推荐） | Persona × Circumstance 矩阵，每格一个 Job | 复杂产品/多场景 |

### 8.2 Persona Card 增强（含 Job 字段）

```yaml
persona:
  name: "效率达人小王"
  primary_job: "在有限时间内完成旅行规划，不浪费脑力"
  circumstance: "出差前一晚/周末碎片时间"
  hired_solutions:
    - "携程App（慢但可靠）"
    - "同事推荐（社交信任）"
  firing_risk: "如果比价超过5分钟就会放弃"
  non_consumption: "有时直接让助理订/放弃比价随便选"
```

---

## 九、反模式

| # | 反模式 | Christensen 的批判 | 修复 |
|---|---|---|---|
| 1 | 按人口统计分 Segment | "相关性≠因果性" | 按 Job + Circumstance 分 |
| 2 | 问"你想要什么功能" | 用户不知道自己的 Job | 观察行为 + Switch Interview |
| 3 | Big Data 相关性分析 | 只告诉你"什么"不告诉你"为什么" | 补充定性 Job 研究 |
| 4 | 满足所有人 | 结果谁的 Job 都没做好 | 聚焦最痛的 Job |
| 5 | 只看 Functional Job | 忽略 Emotional/Social 维度 | 三层 Job 同时考虑 |
| 6 | 认为 Job 永远不变 | Circumstance 变化 → Job 变化 | 持续监测情境变量 |
| 7 | Persona 无 Job 字段 | Persona 变成人口统计收集器 | 强制添加 Job Statement |

---

## 十、与现有 references 的关系图

```
Christensen (本文 #39)         Klement (#22)
    │ JTBD 理论源头                │ 实操集成
    │                             │
    ├── Forces of Progress ──────→ Switch Interview 六问
    ├── Circumstance ────────────→ Job Story 模板
    ├── Non-consumption ─────────→ Persona 新增机会
    │                             │
    └── Hiring/Firing ───────────→ measurement_toolkit.py
                                      (NPS/Churn 即"解雇"信号)
```

---

## 本部分核心要点总结

1. **"人不按人口统计做选择——按情境下的 Job 做选择"**是 Persona 最深层的理论挑战
2. **Circumstance（情境）是因果关系的单位**：同一人在不同情境有完全不同的 Job
3. **Forces of Progress 四力模型**解释了为什么人切换/不切换产品
4. **非消费是最大的创新机会**：没有任何产品被雇佣的 Job = 蓝海
5. **Persona × Circumstance 矩阵**是 Christensen 理论与 Persona 实践的最佳整合方式
6. **本书提供"为什么"，Klement #22 提供"怎么做"**——两者互补

---

## 🔗 跨技能协作

| 场景 | 推荐协作 Skill |
|---|---|
| JTBD 实操落地 | `jtbd-knowledge-skill` + `22-jtbd-persona-integration` |
| Job 发现式访谈 | `33-fitzpatrick-mom-test` (Mom Test) |
| Forces of Progress 量化 | `web-persona-skill` → `measurement_toolkit.py` |
| Persona × Job 矩阵构建 | `web-persona-skill` 主流程 |
| 非消费市场机会分析 | `market-research` |
| Job → OKR 转化 | `web-persona-skill` → `okr_bridge.py` |
