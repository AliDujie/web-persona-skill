# 22 · JTBD × Persona：Job 与角色的整合方法

> 来源：Christensen, C. M., Hall, T., Dillon, K. & Duncan, D. S. *Competing Against Luck: The Story of Innovation and Customer Choice* (HarperBusiness, 2016)；Klement, A. *When Coffee and Kale Compete* (NYC Publishing, 2016)；Wunker, S., Wattman, J. & Farber, D. *Jobs to be Done: A Roadmap for Customer-Centered Innovation* (AMACOM, 2017)；Spiek, C. & Moesta, B. *The Re-Wired Group* internal materials；Ulwick, T. *Jobs to be Done: Theory to Practice* (2016)。
>
> JTBD 与 Persona 长期被对立："JTBD 派"觉得 Persona 是花哨的人口学；"Persona 派"觉得 JTBD 缺少人性温度。本笔记主张：**Job 是动词，Persona 是名词，二者必须同时存在，互不替代**。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | JTBD 视角（本笔记） |
|---|---|---|
| 关注核心 | 用户是谁 | 用户在何情境下试图取得何进展 |
| 单位 | 角色 | 工作 (Job) |
| 工具 | 卡片 | Job Story、4 Forces、Switch Interview |
| 适合场景 | 设计语境 | 创新、定位、市场进入 |
| 失败诊断 | 角色定义不清 | Job 没找对、Forces 不平衡 |

> 💡 **整合立场**：**Persona 描绘"谁"** + **JTBD 描绘"在追求什么进展"** = 完整人物。两者解决不同问题，不应互相替代。

---

## 2. Job 的三层结构 (Christensen)

| 层级 | 含义 | 示例（咖啡馆） |
|---|---|---|
| **Functional** | 功能层 | 咖啡因、解渴 |
| **Emotional (Personal)** | 情感层 | 自我犒赏、放松 |
| **Social** | 社交层 | 显得有格调、约见朋友 |

> 一个看似简单的 Job 通常三层都有；忽略情感和社交 = 输给情绪型对手。

### 2.1 Job 的特征
- **持久** — Job 不变，方案变（人类一直需要"通勤途中觉得不那么无聊"，方案从纸质书 → 收音机 → Walkman → iPod → Spotify → 播客）
- **情境化** — 同一用户在不同情境有不同 Job
- **以进展为单位** — Job = "make progress"，不是"做任务"

---

## 3. Job Story 句式（Klement, 2016）

```
When [情境],
I want to [动机/动作],
So I can [预期结果].
```

对比 Persona 的 User Story：
```
As a [角色],
I want to [功能],
So that [收益].
```

| 维度 | Job Story | User Story |
|---|---|---|
| 起点 | 情境 (When) | 角色 (As a) |
| 焦点 | 进展 | 功能 |
| 风险 | 漏掉角色 | 漏掉情境 |
| 推荐 | **同时使用** | **同时使用** |

> 💎 **关键**：把 Job Story 与 Persona 卡片绑定 = 既知道情境，也知道是谁。

---

## 4. Switch Interview（4 Forces 模型）

任何人换方案的瞬间，4 力同时作用：

```
推动 Push        ↗  ↘  Habit 习惯
                      已有方案的惯性
                ↗  ↘
新方案 → 选择 ←
                ↘  ↗
拉动 Pull        ↘  ↗  Anxiety 焦虑
                      新方案的不确定
```

| 力 | 中文 | 含义 |
|---|---|---|
| **Push** | 推动 | 现状的痛 |
| **Pull** | 拉动 | 新方案的吸引 |
| **Habit** | 惯性 | 已习惯的旧方案 |
| **Anxiety** | 焦虑 | 切换的恐惧 |

> 公式：**Switch 发生 ⇔ Push + Pull > Habit + Anxiety**

### 4.1 Switch Interview 6 大问题
1. 您**第一次**意识到需要新方案是什么时候？
2. 您之前用什么？为什么不够？
3. 您评估了哪些候选？
4. 您**犹豫了什么**？担心什么？
5. 最终促使您下决定的事是什么？
6. 用了之后，是否实现了当初的进展？

> 与 Revella Win/Loss（17 号）几乎同源——B2B 与 B2C 的同构方法。

---

## 5. JTBD × Persona 整合模型

### 5.1 一个 Persona 可对应多个 Job

```
Persona: 林佳, 34, 二孩妈妈
├── Job 1: When 早高峰送娃路上, I want 单手快速购物, so 减少负担
├── Job 2: When 半夜娃发烧, I want 快速判断要不要去医院, so 减少焦虑
└── Job 3: When 周末一家四口, I want 找一个所有人都满意的活动, so 享受家庭时间
```

### 5.2 一个 Job 可被多个 Persona 完成

```
Job: When 通勤途中, I want 觉得时间过得快, so 不那么累

Persona A: 高强（工程师）→ 用方案: 听播客
Persona B: 林佳（妈妈）→ 用方案: 打电话给家人
Persona C: 老周（退休）→ 用方案: 看新闻 App
```

> 💎 **设计含义**：同一个产品功能可服务多 Persona 的同一 Job——这是市场扩张机会。

### 5.3 整合模板

```
Persona 卡片新增 jobs 字段：

jobs:
  - id: job_1
    when: "周末晚上孩子睡着后"
    i_want_to: "快速找到 30 分钟内能做完的辅食"
    so_i_can: "明天早上少手忙脚乱"
    forces:
      push: "工作日总是手忙脚乱"
      pull: "看到朋友圈晒辅食"
      habit: "用现成超市冷冻品"
      anxiety: "怕做出来娃不吃"
    progress_metric: "周末备餐时间从 90 分钟降到 30 分钟"
```

---

## 6. Outcome-Driven Innovation (Ulwick)

Ulwick 的 ODI 法把 Job 进一步拆解为 Outcomes（期望结果）：

| 项 | 含义 |
|---|---|
| Job | "通勤途中，觉得时间过得快" |
| Outcome 1 | 减少"在路上无聊"的频率 |
| Outcome 2 | 增加"获取信息"的可能 |
| Outcome 3 | 减少"被打扰"的频率 |

每个 Outcome 用 **重要性 × 满足度** 打分（1-10）：
- 重要性高 + 满足度低 = 机会缺口（Opportunity）
- 公式：**Opportunity = Importance + max(Importance - Satisfaction, 0)**

> ODI 提供量化框架，与统计 Persona（16 号）天然合体。

---

## 7. Persona × JTBD × Forces 决策流程

```
1. Persona 卡片已有
2. 列该 Persona 的 3-5 个核心 Jobs（覆盖关键情境）
3. 每个 Job 写 Job Story
4. 关键 Job 做 Switch Interview（10-15 名）
5. 4 Forces 量化（每力 1-10 打分）
6. 算 Switch Score = (Push + Pull) − (Habit + Anxiety)
7. 决定打那个 Job：分数 ≥ +3 = 可推；< 0 = 还需打磨
8. ODI 给 Job 拆 Outcomes，找机会缺口
9. 落入 PRD / 路线图
```

---

## 8. 反模式 (Anti-patterns)

| 反模式 | 症状 | 后果 |
|---|---|---|
| **Job 即功能** | "他想用搜索框" | 把方案当 Job，永远输给变化 |
| **没情境** | "想买东西" | Job 失去具体性，无法验证 |
| **三层只剩 Functional** | 只问功能 | 输给情绪型对手 |
| **JTBD 取代 Persona** | "我们 JTBD 了，不需要 Persona" | 失去人格、文化、伦理维度 |
| **Switch 不诊断 4 力** | 只看 Push + Pull | 不知道为什么用户最终没切 |
| **Forces 拍脑袋打分** | 没访谈支撑 | ODI 数字虚高 |
| **不更新 Job** | Job 一年不变 | Job 也会演化（疫情/AI 等） |

---

## 9. 何时使用 JTBD 视角

✅ 用：
- 寻找新机会、市场进入
- 跨品类竞争分析（"我们的对手不是 X，而是用户用来填补这个进展的任何方案"）
- 创新立项、PRD 早期
- 切换型产品（替代现有方案）
- 与 Persona 配套使用，做"角色 × 情境 × 进展"完整视角

⛔ 不用：
- UI 微调（不需要 Job 视角）
- 单一任务工具（Job 简单显然）
- 已经聚焦极小细分场景
- 想完全替代 Persona（错误立场）

---

## 10. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/persona_builder.py` | 增加 `jobs[]` 字段（Job Story + Forces） |
| `persona/jobs.py`（v2.6 新增） | Job/Outcome/Forces 数据模型 |
| 17-Buyer Persona | 5 Rings 与 4 Forces 互通 |
| 20-Kahneman | Anxiety 力的本质是 Loss Aversion |
| 21-Fogg | Job 触发瞬间映射 Trigger |
| 30-OKR-Bridge | Job Outcomes → 业务 KR |

> 项目已有 `jtbd-knowledge-skill` 技能，本笔记与其互补：jtbd-knowledge-skill 负责 JTBD 全流程实施，本笔记聚焦"如何与 Persona 整合"。

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| Job 与 Persona 互补 | 动词 vs 名词，必须同时存在 |
| Job 三层 | Functional + Emotional + Social |
| Job Story 与 User Story 并用 | 一个补情境，一个补角色 |
| 4 Forces 决定切换 | (Push+Pull) > (Habit+Anxiety) |
| ODI 量化机会 | Importance + max(I-S, 0) |
| Switch Interview 是核心引擎 | 真实切换瞬间访谈 |
| Persona × Jobs 多对多 | 一人多 Job，一 Job 多人 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `jtbd-knowledge-skill` | JTBD 主技能；本笔记 = 与 Persona 整合视角 |
| `value-proposition-design` | VPC 与 Job/Pain/Gain 同源 |
| `prd-writing` | PRD 增加 Job Story + Forces 段 |
| `competitive-analysis` | 跨品类竞争 = 同 Job 不同方案 |
| `mvp-scoping` | ODI 机会缺口 → MVP 切片 |
| `roadmap-planning` | Job 群构建 1-3 年路线图 |

---

> 📚 **延伸阅读**：
> - Christensen et al. (2016). *Competing Against Luck*. 全书。
> - Klement (2016). *When Coffee and Kale Compete*。Job Story 经典。
> - Wunker, Wattman & Farber (2017). *Jobs to be Done*. 实操路线图。
> - Ulwick (2016). *Jobs to be Done: Theory to Practice*. ODI。
> - Spiek & Moesta. *The Jobs To Be Done Handbook* (Re-Wired Group)。
> - 中国情境：可结合飞猪 *目的地决策旅程* 内部研究读 4 Forces 模型。
