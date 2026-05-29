# 12 · Erika Hall 实用主义研究 (Just Enough Research)

> 来源：Erika Hall《Just Enough Research》第 2 版 (A Book Apart, 2019)。
>
> Erika Hall 是 Mule Design 联合创始人。本书在 UX 研究界以"反研究剧场化"著称——主张做"刚好够用"的研究而非完美研究。Persona 在该框架中是研究问题的产物，而非自带光环的产物。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 与 Mulder/Cooper/Lean UX 的关系

| 维度 | Mulder/Cooper | Lean UX | Erika Hall |
|---|---|---|---|
| 启动逻辑 | 项目立项就做 | 假设驱动 | **问题驱动** |
| 研究产出 | Persona 是核心交付物 | Proto-Persona 假设 | Persona 是次级产物（如有需要） |
| 哲学立场 | "我们要了解用户" | "我们要快速学习" | "我们要回答某个具体问题" |
| 输出形态 | 重 | 轻 | "刚好够" |

> 💡 **Erika Hall 的核心命题**：研究不是 ritual（仪式），是工具。任何研究开始前必须问：**"这次研究要回答什么决策？"** 没有决策就别启动研究。

---

## 2. 五类研究问题 (Five Types of Research)

每类回答不同问题，需要不同方法：

| 类型 | 问什么 | 典型方法 | Persona 用途 |
|---|---|---|---|
| **Generative**（生成式） | "存在什么需求？我们没看到什么？" | 民族志、深访 | 形成原始 Persona 假设 |
| **Descriptive**（描述式） | "用户当前如何做事？" | 现场观察、日记研究 | Persona 中"行为"段填充 |
| **Evaluative**（评估式） | "我们的方案能用吗？" | 可用性测试 | 用 Persona 招募代表性测试者 |
| **Causal**（因果式） | "X 改变会导致 Y 吗？" | A/B 测试 | 按 Persona 分组分析 |
| **Strategic / Process**（战略式） | "我们应该往哪个方向？" | 工作坊、SWOT、五力 | Persona 作为战略决策依据 |

> 💡 **Persona 不是 Generative 研究的产物**——它是 Descriptive 研究的综合输出。这是 Hall 与传统派的关键差异：传统派把"创建 Persona"作为研究目标；Hall 把"回答问题"作为研究目标，Persona 只是中间产物。

---

## 3. "Just Enough" 的判断标准

什么时候研究"够了"？Hall 给出三条判断：

### 3.1 Saturation（饱和）
- 连续 3 名受访者没有提供新信息 → 该方向饱和
- 不必追求"代表性"，只需到饱和

### 3.2 Confidence（信心）
- 决策者愿意基于现有数据做决定 → 信心达到
- 此时再做研究 = 浪费

### 3.3 Time Box（时间盒）
- 预设研究时间（如 2 周），到点交付现有发现
- 即使不饱和，也要把"知道什么 / 不知道什么"明确列出

> ⚠️ 反模式："Research Theater"（研究剧场）——做研究是为了让自己看起来严谨，而非为决策服务。Hall 在书中点名批评的最严重病症。

---

## 4. 轻量 Persona（Hall 版）

Hall 不反对 Persona，但反对 Persona 的"过度装饰"：

### 4.1 必要字段（仅 5 项）

```markdown
# Persona: [代号]

## 一句话身份
[他/她是谁，与产品什么关系]

## 想完成的事
- [Job 1]
- [Job 2]

## 当前怎么做
- [现状方法]
- [当前痛点]

## 决策标准
- [选择产品时关心什么]

## 我们假设但还没验证的
- [ ] [假设 1]
- [ ] [假设 2]
```

### 4.2 不要的字段

| 不要 | 原因 |
|---|---|
| 假名（如"Alex"） | 不必要的虚构 |
| 照片 | 容易引入刻板印象 |
| 详细人口学 | 与决策无关时只是噪音 |
| 爱好/喜爱品牌 | 99% 与产品决策无关 |
| "幽默风趣"形容词 | 不可观察、不可验证 |

> 💡 **核心纪律**：每个字段都要能回答"这影响哪个产品决策？"。不能就删掉。

---

## 5. 研究问题清单（Hall 版工作坊）

启动任何研究前，团队共同填写：

```
1. 我们要做什么决策？
   ____________________________________

2. 决策的截止时间是？
   ____________________________________

3. 我们目前知道什么？
   ____________________________________

4. 我们不知道但需要知道什么？
   ____________________________________

5. 哪种研究类型最匹配这个问题？
   [ ] Generative   [ ] Descriptive   [ ] Evaluative
   [ ] Causal       [ ] Strategic

6. 我们能投入多少时间和预算？
   ____________________________________

7. 谁会用这个研究结果？
   ____________________________________

8. 什么样的发现会真正改变决策？
   ____________________________________
```

> 💡 第 8 题是核心：如果"任何发现都不会改变决策"，那这个研究本身就不该启动。

---

## 6. Hall 反"Persona 万能论"的论点

Hall 列出 Persona **不**能解决的问题：

| Persona 不能告诉你 | 应该用什么 |
|---|---|
| 用户的实际工作流 | Workflow Model（Goodwin） |
| 用户的心智模型 | Mental Model Diagram（Indi Young） |
| 用户的具体任务结构 | Jobs-To-Be-Done 框架 |
| 量化偏好与权重 | Conjoint / MaxDiff（QuantUX） |
| 是否会买单 | Smoke Test / Concierge MVP（Lean UX） |
| 长期使用模式 | 数据分析、留存队列 |

> 💡 **Persona 的合法用途**：让团队对"我们在为谁设计"达成共识。仅此而已。其他问题用其他工具。

---

## 7. 何时优先使用 Hall 框架

| 情境 | 推荐 |
|---|---|
| 团队过度依赖 Persona，研究偏离决策 | ✅ Hall 框架纠偏 |
| 时间预算极紧（<2 周内出答案） | ✅ Just Enough Research 优先 |
| 已有研究但没人用 | ✅ 用研究问题清单倒逼 |
| 学术/方法论严谨度审查 | ❌ 用 Lene Nielsen |
| 大型组织、跨部门协作 | ❌ 用 Pruitt-Adlin |

---

## 8. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| 五类研究问题 | `persona/interview.py` 新增 `research_type` 参数 |
| 研究问题清单（8 题） | `persona/templates.py` 新增 `research_brief_template` |
| 轻量 Persona 5 字段 | `persona/templates.py` 新增 `minimal_persona_template` |
| Saturation/Confidence/TimeBox 判断 | `persona/measure.py` 新增 `research_completion_check()` |
| 反 Research Theater 检查 | `persona/persona_builder.py` 的 `review_persona()` 新增"决策关联度"项 |

---

## 9. 关键引述

> "Doing research is not a virtue. Answering questions is. If your research doesn't answer a question, it doesn't matter how rigorous it is." — Erika Hall

> "Personas are not the goal of research. They are sometimes a useful side effect of research." — Just Enough Research

> "The right amount of research is the amount that lets you make the next decision with confidence. Not more, not less." — Erika Hall

---

*笔记整理完成 | 基于 Erika Hall《Just Enough Research》第 2 版 | 与 Mulder 派形成"决策驱动/反过度研究"互补*
