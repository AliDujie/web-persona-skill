# 34 — Teresa Torres · Continuous Discovery Habits: Discover Products That Create Customer Value and Business Value (2021)

> **Tier E · 上游研究手艺 + 持续发现**｜关键词：Opportunity Solution Tree、Weekly Touchpoints、Assumption Testing、Discovery Cadence、Product Trio

---

## 一、核心定位

Torres 彻底颠覆了"一次性研究 → 交付 Persona → 封存"的传统模型。她的核心主张：**发现（Discovery）不是项目，是习惯——每周都做，像刷牙一样**。本书把 Persona 从"交付物"变成"持续校准的假设"。

### 1.1 与传统 Persona 项目制的对比

| 维度 | 传统项目制 | Continuous Discovery |
|---|---|---|
| 频率 | 年/半年一次大研究 | 每周至少 1 次客户触点 |
| 谁做 | UX Researcher 独立承担 | Product Trio（PM + Designer + Engineer） |
| 输出 | Persona Doc → 归档 | Opportunity Solution Tree → 持续更新 |
| 验证 | 上线后看数据 | 上线前多轮 Assumption Test |
| Persona 寿命 | 创建后逐渐过时 | 每周对话刷新行为变量 |

---

## 二、Opportunity Solution Tree (OST) 框架

### 2.1 核心结构

```
Desired Outcome（业务目标/OKR）
  ├── Opportunity 1（客户需求/痛点/期望）
  │     ├── Solution A
  │     │     ├── Assumption 1 → Experiment
  │     │     └── Assumption 2 → Experiment
  │     └── Solution B
  │           └── Assumption 3 → Experiment
  ├── Opportunity 2
  │     └── Solution C
  └── Opportunity 3
        └── …
```

### 2.2 OST 四层定义

| 层 | 定义 | 来源 |
|---|---|---|
| Outcome | 可量化的业务/产品目标 | OKR / Metric |
| Opportunity | 客户未满足的需求、痛点、期望 | 客户访谈/行为数据 |
| Solution | 可能解决 Opportunity 的产品方案 | 头脑风暴/竞品/技术 |
| Assumption | Solution 成立所需的前提假设 | 逻辑推演 |

### 2.3 OST 与 Persona 的关系

- **Opportunity 层就是 Persona 的 Pain Points / Goals 的动态版本**
- 每周访谈产生新 Opportunity → 回头检验"这个 Opportunity 属于哪个 Persona？" → 必要时拆分/合并 Persona
- `okr_bridge.py` 的 derive_okrs() 本质上就是 OST 的 Outcome→Opportunity 映射自动化

---

## 三、Weekly Customer Touchpoints（每周客户触点）

### 3.1 核心纪律

> "At minimum, the product trio should be talking to customers every week." — Torres

| 要素 | 规范 |
|---|---|
| 频率 | 至少每周 1 次（理想 2-3 次） |
| 时长 | 15-30 min（不是 60 min 正式访谈） |
| 谁参加 | Product Trio 至少 2 人在场 |
| 对象 | 真实用户/客户（非同事、非家人） |
| 记录 | Interview Snapshot（见下方模板） |

### 3.2 Interview Snapshot 模板

```markdown
## Interview Snapshot
**Date**: 2026-05-29 | **Participant**: [代称] | **Interviewer**: [Product Trio 谁]

### Story（一个具体经历的叙述）
> [用对方的话复述一个具体事件]

### Opportunities Identified
- Opp-1: …
- Opp-2: …

### Quotes
- "…verbatim…"

### Persona Mapping
- 最接近: Persona [X]
- 偏移点: 在 [维度] 上行为不同
```

### 3.3 自动化招募策略

| 方法 | 适合 | 如何做到"每周都有人聊" |
|---|---|---|
| 产品内触发 | B2C App | 完成某任务后弹出 "聊 15 min 送积分？" |
| Support Ticket 旁听 | B2B SaaS | CS 团队每周筛 3 张有趣 ticket 转介 |
| Calendar Block | 全部 | PM 日历固定周三下午 = Discovery Time |
| Advisory Board | Enterprise | 季度约定的 5-8 名客户顾问 |

---

## 四、Assumption Mapping & Testing

### 4.1 四类核心假设

| 假设类型 | 定义 | 验证方法 |
|---|---|---|
| Desirability | 客户想要这个吗？ | Fake Door / Painted Door Test |
| Viability | 商业上能持续吗？ | Unit Economics / Pricing Test |
| Feasibility | 技术上做得到吗？ | Spike / Prototype |
| Usability | 用户能搞明白吗？ | Usability Test / First-Click |

### 4.2 Assumption 优先级矩阵

```
        High Risk (uncertain)
             │
   ┌─────────┼─────────┐
   │  Test   │  Test   │
   │ FIRST   │  Soon   │
   │         │         │
───┼─────────┼─────────┼─── High Importance
   │  Watch  │  Skip   │     (if wrong = fail)
   │         │         │
   └─────────┼─────────┘
             │
        Low Risk (confident)
```

### 4.3 小实验菜单（从快到慢）

| 实验类型 | 时间成本 | 验证什么 |
|---|---|---|
| One-Question Survey | 1 小时 | 痛点频率 |
| Fake Door (Painted Door) | 1 天 | Desirability（点击率） |
| Concierge | 1 周 | 整体价值主张 |
| Wizard of Oz | 1-2 周 | 体验 + Desirability |
| A/B Test (Prototype) | 2 周 | Usability + Conversion |
| 真正的 MVP | 2-4 周 | 全假设综合 |

---

## 五、Compare & Contrast（对比思维）

### 5.1 核心方法

Torres 强调：**不要只评估一个方案**——永远同时比较至少 3 个 Solution。

| 原则 | 做法 |
|---|---|
| Set-based Design | 同时保留 3+ 方案直到实验否决 |
| 对比实验 | 设计 A vs B vs C 的小实验，而非只测 A |
| 避免沉没成本 | 不因"已投入"而死守一个方案 |

### 5.2 对 Persona 工作的启示

- 做 Persona 时也要"对比"：生成 3 种可能的 Persona 切分方式（按行为/按场景/按动机），用数据选最佳
- `clustering.py` 的三方法自动选择（KMeans/LCA/Factor）正是这个理念的代码化

---

## 六、Product Trio 协作模式

### 6.1 什么是 Product Trio

```
Product Manager + Product Designer + Tech Lead
       │                │                │
   商业视角          用户视角          技术视角
       └────────────────┴────────────────┘
              共同参与 Discovery
              共同拥有 OST
              共同做 Assumption Testing
```

### 6.2 协作纪律

| 活动 | 频率 | 参与者 |
|---|---|---|
| Customer Interview | 每周 | Trio 至少 2 人 |
| OST Sync | 每周 | 全 Trio |
| Assumption Mapping | 每 Sprint | 全 Trio |
| Experiment Review | 每 Sprint | 全 Trio + Stakeholder |

---

## 七、Discovery → Delivery 衔接

### 7.1 双轨制（Dual Track Agile）

```
┌──────────────────────────────────────────────────────┐
│ Discovery Track (continuous)                          │
│  Interview → OST → Assumption → Experiment → Learn  │
└──────────────────────────────┬───────────────────────┘
                               │ validated solutions
                               ▼
┌──────────────────────────────────────────────────────┐
│ Delivery Track (sprint-based)                        │
│  Story → Dev → Test → Ship → Measure                │
└──────────────────────────────────────────────────────┘
```

### 7.2 什么时候一个 Solution "毕业"进入 Delivery？

- Desirability 假设验证 ✅（客户真的想要）
- Usability 假设验证 ✅（能搞明白怎么用）
- Feasibility 确认 ✅（技术 spike 通过）
- Viability 初步验证 ✅（unit economics 可行）

---

## 八、反模式

| # | 反模式 | 表现 | Torres 的修复 |
|---|---|---|---|
| 1 | Discovery Theater | 做了访谈但不影响决策 | OST 可视化：每个决策可追溯到哪次访谈 |
| 2 | Opinion-driven Roadmap | PM 靠直觉排优先级 | Opportunity Scoring（频率×强度×广度） |
| 3 | Feature Factory | 只做 Delivery 不做 Discovery | 强制 Time-box：50% Discovery + 50% Delivery |
| 4 | Research Relay | 研究员做完丢给PM、PM丢给开发 | Product Trio 全程在场 |
| 5 | One-shot Persona | 做完 Persona 就封存 | 每周 Interview Snapshot 持续校准 |
| 6 | Solution First | 先有方案再找问题 | OST 强制先写 Opportunity 再写 Solution |
| 7 | Big Bet | 全压一个方案 | Compare & Contrast（3+ 方案并行） |

---

## 九、Persona 持续校准流程

基于 Torres 方法，Persona 不是"做一次"而是"每周微调"：

```
Week N:
  访谈 → Interview Snapshot → 发现 Opportunity
       → 检查: 这个 Opportunity 属于哪个 Persona?
       → 如果 Persona 无法解释 → 标记"Persona Tension"
       → 累积 3+ Tension → 触发 Persona Review

Persona Review (monthly/quarterly):
  收集所有 Tension 标记
  → 重新跑 clustering.py（新行为变量输入）
  → 决定: 拆分? 合并? 新增? 微调?
  → 更新 Persona Card + 通知团队
```

---

## 十、Opportunity Scoring 公式

用于在 OST 中对 Opportunity 排优先级：

```
Opportunity Score = Frequency × Intensity × Breadth

Frequency: 多少比例的用户遇到这个问题（0-1）
Intensity: 遇到时有多痛（1-5 Likert）
Breadth:   影响多少个 Persona（1-N_personas）
```

与 `okr_bridge.py` 的 RICE 模型对应关系：
- Frequency × Breadth ≈ Reach
- Intensity ≈ Impact
- Assumption 验证成本 ≈ Effort

---

## 本部分核心要点总结

1. **Discovery 是习惯，不是项目**——每周至少 1 次客户触点，Product Trio 共同参与
2. **OST 是思考工具**：Outcome→Opportunity→Solution→Assumption，层层分解
3. **永远对比 3+ 方案**：Set-based Design 避免过早锁定
4. **Assumption Testing 先于 Building**：用最小成本验证最高风险假设
5. **Persona 是持续校准的假设**：每周 Interview Snapshot 提供微调信号
6. **Opportunity Scoring 决定优先级**：Frequency × Intensity × Breadth

---

## 🔗 跨技能协作

| 场景 | 推荐协作 Skill |
|---|---|
| OST → OKR 转化 | `web-persona-skill` → `okr_bridge.py` |
| Opportunity Scoring 量化 | `web-persona-skill` → `measurement_toolkit.py` |
| 访谈设计 | `interview-kit` / `32-portigal` |
| 假设不含 pitch | `33-fitzpatrick-mom-test` |
| JTBD 视角发现 Opportunity | `jtbd-knowledge-skill` |
| Roadmap 从 OST 导出 | `roadmap-planning` |
