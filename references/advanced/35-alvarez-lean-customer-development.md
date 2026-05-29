# 35 — Cindy Alvarez · Lean Customer Development: Building Products Your Customers Will Buy (2014)

> **Tier E · 上游研究手艺 + 持续发现**｜关键词：Customer Development、Problem-Solution Fit、Pivot Signal、Early Adopter Profile、Hypothesis-Driven

---

## 一、核心定位

Alvarez 把 Steve Blank 的 Customer Development 四步法（Discovery→Validation→Creation→Building）翻译成了**产品经理/设计师可直接上手的操作手册**。与 Torres 的持续发现互补：Torres 讲"习惯系统"，Alvarez 讲"从零到一的冷启动验证"。

### 1.1 Customer Development 四步

| 步骤 | 核心问题 | Persona 关系 |
|---|---|---|
| Customer Discovery | 谁有这个问题？问题有多痛？ | 初始 Proto-Persona 假设 |
| Customer Validation | 愿意付费吗？早期采用者是谁？ | Persona 精化 + Early Adopter Profile |
| Customer Creation | 怎么规模化找到更多这样的人？ | Persona 扩展：从 Early 到 Mainstream |
| Company Building | 从产品到组织 | Persona 固化为组织共识 |

---

## 二、Problem Hypothesis Canvas

### 2.1 模板

```markdown
## Problem Hypothesis

**Target Customer**: [谁？具体到可以本周找到 5 个]
**Problem**: [一句话描述他们在做什么时遇到什么困难]
**Current Alternatives**: [他们现在怎么解决？花多少钱/时间？]
**Why Now**: [为什么这个问题现在值得解决？]

**Falsification Criteria**:
- 如果 < 3/5 人确认经历过这个问题 → 假设失败
- 如果没人花 > $X/月 解决类似问题 → 付费意愿假设失败
- 如果大家对现有方案"还行" → 痛点假设失败
```

### 2.2 与 Persona 的映射

| Canvas 字段 | Persona 对应维度 |
|---|---|
| Target Customer | Persona 的人口统计 + 行为概况 |
| Problem | Pain Points |
| Current Alternatives | Technology / Tools / Workarounds |
| Why Now | Context / Trigger Event |
| Falsification Criteria | Persona 验证门槛 |

---

## 三、Early Adopter Profile（早期采用者画像）

### 3.1 五特征识别法

| 特征 | 表现 |
|---|---|
| 1. 已经在寻找解决方案 | 主动搜索/尝试替代品 |
| 2. 拼凑了 Workaround | 用 Excel/邮件/手动流程凑合 |
| 3. 有预算/权限决定 | 能拍板付费、不需要"向上汇报" |
| 4. 对不完美有容忍度 | 能接受 Beta 版的 bug |
| 5. 愿意传播 | 会主动推荐给同行 |

### 3.2 Early Adopter ≠ Target Persona

| 维度 | Early Adopter | Target Persona（主流） |
|---|---|---|
| 痛点忍耐度 | 极低（迫切要解决） | 中等（能忍） |
| 技术能力 | 通常更高 | 平均水平 |
| 价格敏感度 | 较低（为解决问题愿意付溢价） | 较高 |
| 对UX的要求 | 能容忍粗糙 | 要求完善 |

> 陷阱：如果只基于 Early Adopter 做 Persona，后续产品可能"太极客"——需要在验证后主动扩展 Persona 覆盖主流。

---

## 四、客户对话实操

### 4.1 "问题访谈" vs "方案访谈"

| 维度 | 问题访谈（Problem Interview） | 方案访谈（Solution Interview） |
|---|---|---|
| 时机 | 还没有方案/MVP | 有了原型/MVP |
| 目标 | 验证问题存在 + 严重性 | 验证方案是否解决问题 |
| 话术 | Mom Test 式（不提产品） | 展示原型，观察行为 |
| 成功标准 | 3/5 人确认 + 有 Workaround | 能自主完成核心任务 + 表达承诺 |

### 4.2 Alvarez 的 5 条对话纪律

| # | 纪律 | 理由 |
|---|---|---|
| 1 | 开口前写下你期望听到什么 | 事后对比，防止确认偏误 |
| 2 | 每轮对话 ≤ 20 min | 短+频 > 长+稀 |
| 3 | 记录"意外" | 与假设冲突的才是真发现 |
| 4 | 每 5 次对话做一次 Synthesis | 防止信息堆积不消化 |
| 5 | 与团队分享 raw quotes，不是结论 | 让团队自己形成判断 |

---

## 五、Pivot Signal（何时转向）

### 5.1 六个 Pivot 信号

| 信号 | 表现 | 该怎么做 |
|---|---|---|
| Nobody has the problem | 0/5 确认 | Pivot Customer Segment |
| Problem exists but low intensity | "还好啦" | Pivot Problem 或加倍深挖 |
| Already solved satisfactorily | "我用 XX 挺好的" | Pivot Solution（差异化角度） |
| Won't pay | "这个该免费吧" | Pivot Business Model |
| Can't reach them | 找不到这群人 | Pivot Segment（找可触达的） |
| Wrong timing | "以后再说" | Pivot Trigger / Channel |

### 5.2 Pivot vs Persist 决策框架

```
                     ┌─ 3+ 人确认问题 ──┐
                     │                    ▼
Start ──── 问题访谈 ──┤            方案访谈 ──── 承诺？──── BUILD
                     │                    │
                     └─ 0-2 人确认 ──┐    └─ 无承诺 ──── 回到问题访谈
                                     ▼
                               PIVOT（调整假设）
```

---

## 六、MVP 类型选择矩阵

| MVP 类型 | 验证目标 | 时间成本 | 适合阶段 |
|---|---|---|---|
| Landing Page + CTA | Desirability（会点击吗） | 1-2 天 | 最早期 |
| Explainer Video | 能理解价值主张吗 | 2-3 天 | 早期 |
| Concierge | 手动交付完整体验 | 1-2 周 | 验证整体价值 |
| Wizard of Oz | 前端像真的，后端是人 | 2-3 周 | 验证交互+需求 |
| Piecemeal MVP | 用现有工具拼凑 | 1-2 周 | 验证 workflow |
| Single-feature MVP | 只做最核心一个功能 | 2-4 周 | 验证 PMF |

---

## 七、从 CustDev 到 Persona 的数据流

```
Problem Hypothesis → Problem Interview (5-10 人)
  │
  ├── 确认: 问题真实 + 有 Workaround
  │   → 提取行为变量 → Proto-Persona 升级
  │
  └── 发现: 存在 2 种截然不同的 Workaround
      → 拆分为 2 个 Persona

Solution Interview (5-10 人/Persona)
  │
  ├── Early Adopter Profile 确立
  │   → 精化 Persona 的"trigger/context"维度
  │
  └── 发现: Early Adopter 行为与假设 Persona 不符
      → 更新 Persona 或创建 "Bridge Persona"
```

---

## 八、Lean CustDev + Persona 生命周期整合

| Persona 阶段 | Lean CustDev 活动 | 输出 |
|---|---|---|
| Proto-Persona（假设） | Problem Hypothesis Canvas | 1-pager |
| Validated Problem | 5-10 次问题访谈 | 行为变量 + 痛点排序 |
| Early Adopter Persona | 5 特征识别 + Solution Interview | 精细画像 + 承诺证据 |
| Mainstream Persona | 扩大样本 + 量化验证 | 统计验证的多 Persona |
| Growth Persona | 新 segment 探索 | 下一波目标用户画像 |

---

## 九、反模式

| # | 反模式 | 后果 | 修复 |
|---|---|---|---|
| 1 | "Build it and they will come" | 产品没人用 | 先做 Problem Interview 再写一行代码 |
| 2 | 只和内部人聊 | Insider Bias | 每周至少 1 个外部客户对话 |
| 3 | 数据没有 Falsification Criteria | 永远"验证通过" | 先写失败条件再去验证 |
| 4 | Early Adopter = All Users | 产品太极客 | 区分 Early Adopter Profile 和 Target Persona |
| 5 | Pivot Too Fast | 没给假设足够样本就放弃 | 至少 5 次对话再判 |
| 6 | Pivot Too Slow | 10+ 人说不需要还在坚持 | 设定明确 Pivot 信号 |
| 7 | 无 Synthesis 纪律 | 做了 30 次对话说不清楚学到什么 | 每 5 次做一次主题归纳 |

---

## 十、工具推荐

| 阶段 | 工具 |
|---|---|
| Hypothesis Canvas | Miro / Notion / 纸笔 |
| 对话笔记 | Dovetail / Grain / 简单 Markdown |
| Persona 管理 | `web-persona-skill` persona_builder |
| 行为聚类 | `web-persona-skill` clustering.py |
| 承诺追踪 | 简单表格 (Name / Date / Commitment Type / Follow-up) |
| Pivot 决策 | Team retro meeting + 信号 checklist |

---

## 本部分核心要点总结

1. **Lean Customer Development 是"科学方法在产品中的应用"**：假设 → 实验 → 证伪/确认 → 迭代
2. **Problem Interview 先于一切**：连问题都没验证就造方案是最大的浪费
3. **Early Adopter ≠ 最终用户**：他们是验证工具，但产品最终要服务主流
4. **Falsification Criteria 是诚实的保障**：没有预设的失败条件，任何数据都能"证明"假设对
5. **Pivot 是学习的证据**：不是失败，是假设更新
6. **每 5 次对话做 Synthesis**：防止数据堆积不消化

---

## 🔗 跨技能协作

| 场景 | 推荐协作 Skill |
|---|---|
| Problem Interview 设计 | `interview-kit` + `33-fitzpatrick-mom-test` |
| Hypothesis Canvas → Persona | `web-persona-skill` 主流程 |
| CustDev 发现转 JTBD | `jtbd-knowledge-skill` |
| MVP 优先级排序 | `mvp-scoping` |
| Pivot 决策结构化分析 | `Structured-Thinking-Model` |
| 竞品替代方案分析 | `competitive-analysis` |
