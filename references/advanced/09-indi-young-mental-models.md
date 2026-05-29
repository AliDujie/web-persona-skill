# 09 · Indi Young 心智模型与思维风格 (Mental Models & Thinking Styles)

> 来源：Indi Young《Mental Models: Aligning Design Strategy with Human Behavior》(Rosenfeld Media, 2008) +《Practical Empathy: For Collaboration and Creativity in Your Work》(Rosenfeld Media, 2015) + 后续在 indiyoung.com 发布的"Thinking Style Segments"方法。
>
> Indi Young 是 Adaptive Path 联合创始人，提出**完全脱离人口学**的用户研究范式——是对 Mulder 派"行为 + 人口学"分群的最强方法论挑战。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder | Indi Young |
|---|---|---|
| 分群依据 | 行为 + 态度 + 人口学 | **纯认知/情感/动机**——禁用人口学 |
| 数据来源 | 问卷量表 + 访谈 | Listening Sessions（深度倾听） |
| 输出 | Persona 卡片 | Mental Model Diagram + Thinking Style Segments |
| 哲学差异 | 用户是数据点 | 用户是认知主体 |
| 适合场景 | 已知人群、需要量化 | 行为差异远大于人口学差异时（多数情况） |

> 💡 **Indi Young 的根本论点**：人口学（年龄、性别、收入、地域）是**糟糕的预测变量**。两位 35 岁城市白领可能完全没有共同的产品决策逻辑。真正能预测产品行为的是**思维方式**。

---

## 2. Mental Model Diagram（心智模型图）

### 2.1 它长什么样？

一张**墙面级**的水平条形图，由数百个 task box（任务方框）堆叠成 tower（塔），多个 tower 组成 mental space（思维空间）：

```
┌─────────── Mental Space: 计划假期 ───────────┐
│                                              │
│  Tower: 决定去哪          Tower: 安排时间    │
│  ┌──────────┐             ┌──────────┐      │
│  │研究目的地│             │和家人协调│      │
│  ├──────────┤             ├──────────┤      │
│  │问朋友推荐│             │看公司假期│      │
│  ├──────────┤             ├──────────┤      │
│  │看 Ins   │              │预订机票  │      │
│  └──────────┘             └──────────┘      │
│ ─────────────── Below the Line ─────────────│
│  支持工具：Google Maps    支持工具：日历   │
│                            缺口：________   │
└──────────────────────────────────────────────┘
```

- **Task box**：用户实际在做的认知/行动单元（"研究目的地""问朋友推荐"）
- **Tower**：相关任务的纵向堆叠（"决定去哪"）
- **Mental Space**：相关 tower 的横向集合（整段思维过程）
- **Below the line**：当前服务/功能映射，识别 **gap**（缺口）和 **waste**（浪费）

### 2.2 它怎么生成？

```
Step 1: Listening Sessions（深度倾听）
   └─ 60-90 min 半结构化访谈 × 6-12 名/思维风格
   └─ 关键纪律：不引导、不追问解决方案、不打断
   └─ 全程录音转文字

Step 2: 任务提取
   └─ 从转录稿中标记每一处"用户做的事 / 想的事"
   └─ 每个 task 用动词 + 名词短语（"对比酒店价格"）
   └─ 一次访谈通常产出 100-300 个 task

Step 3: 亲和聚类
   └─ 把 tasks 贴到墙上
   └─ 相似的归为 tower（中观聚类）
   └─ 相关 tower 归为 mental space（宏观聚类）

Step 4: Below the Line 映射
   └─ 把当前产品功能映射到对应 task box 下
   └─ 没功能的 task = 机会
   └─ 没 task 的功能 = 浪费
```

### 2.3 它能回答什么 Persona 回答不了的问题？

| Persona 难解 | Mental Model 擅长 |
|---|---|
| "用户在我们之外的旅程中做了什么？" | 完整跨产品旅程 |
| "信息架构应该怎么命名？" | 用 tower 名作为 IA 顶级类目 |
| "我们的产品有哪些机会缺口？" | gap 分析直接对应未满足需求 |
| "为什么这功能没人用？" | 该功能下方没有 task box |

---

## 3. Thinking Style Segments（思维风格分群）

Indi Young 后期工作（2017+）的最大突破：**完全用思维风格做用户分群**。

### 3.1 思维风格 ≠ 人物角色

| 维度 | 传统 Persona | Thinking Style |
|---|---|---|
| 分群依据 | 行为 + 人口学 | **目的（Purpose）+ 方法（Approach）+ 偏好（Philosophy）** |
| 命名方式 | 姓名 + 头像 | 一句话描述这群人的思维方式 |
| 单位 | 个人 | 思维模式 |
| 验证方式 | 量化代表性 | 定性饱和（saturation） |

### 3.2 Thinking Style 的命名公式

不是给"小明 28 岁产品经理"，而是：

> "需要在不熟悉的领域快速做出可证明决策的人" (People who need to make defensible decisions fast in unfamiliar territory)

> "享受用大量时间研究然后只买一次的人" (People who enjoy spending massive time researching to buy once)

> "在压力下倾向用熟悉路径而非最优路径的人" (People who default to familiar paths under stress, even when not optimal)

每个风格会有完整的 Mental Model Diagram，但**没有姓名、年龄、照片**。

### 3.3 何时切换到 Thinking Style 分群

- 你的产品被多种人口学群体使用，但他们的行为模式高度重叠
- 你的人口学分群在 A/B 测试中没有显著差异
- 你的产品涉及决策、选择、判断（而非操作、执行）
- 你想做一个"对所有用户公平"的产品

---

## 4. Practical Empathy：共情作为方法论

《Practical Empathy》核心命题：共情不是软技能，是可训练的研究方法。

### 4.1 共情的两阶段

```
Empathy = Understanding + Acting
├── Cognitive Empathy（认知共情）：理解对方的想法、决策逻辑、目标
└── Emotional Empathy（情绪共情）：感受对方的情绪状态——但不带入个人判断
```

### 4.2 Listening Session 的纪律

| 禁忌 | 替代 |
|---|---|
| ❌ "你为什么不试 X？"（建议） | ✅ "当时是怎么想的？" |
| ❌ "我也遇到过……"（自我代入） | ✅ "嗯，请继续。" |
| ❌ "也就是说你……"（总结） | ✅ "你刚说……能多讲讲吗？" |
| ❌ 追问"为什么"3 次以上 | ✅ 给沉默留 5 秒 |

### 4.3 Empathy ≠ Sympathy ≠ Pity

```
Pity（怜悯）：我比你强，我同情你
Sympathy（同情）：我也感同身受
Empathy（共情）：我理解你的感受，但保持自己的判断空间
```

只有 Empathy 适合用研——前两者会扭曲数据。

---

## 5. 三类输出物对照

| 输出 | 生成方式 | 用途 |
|---|---|---|
| **Persona**（Mulder/Cooper） | 行为变量聚类 | 已知群体的代表 |
| **Mental Model**（Young 早期） | Listening + 任务亲和 | 完整旅程地图、IA、机会缺口 |
| **Thinking Style**（Young 近期） | 目的/方法/偏好聚类 | 不带人口学偏见的认知分群 |

> 💡 **三者并用建议**：用 Mental Model 找需求缺口 → 用 Thinking Style 做无偏分群 → 用 Persona 给团队一个具体的 face。

---

## 6. Indi Young 的反人口学论点

### 6.1 为什么人口学是糟糕的预测变量

1. **掩盖个体差异**：35 岁产品经理可能从极保守到极冒险，差异远大于"35 岁 vs 45 岁"的差异
2. **导致刻板印象**：人口学分群直接通向"足球妈妈""硅谷男"等刻板形象
3. **对包容性设计有害**：边缘群体被忽略
4. **不可操作**：知道用户是 35 岁不能告诉你按钮该放哪

### 6.2 人口学唯一合法的用途

- 法律合规（年龄限制、地域限制）
- 沟通渠道选择（不同群体看不同媒体）
- **不是**产品功能或交互的设计依据

---

## 7. 何时优先使用 Indi Young 框架

| 情境 | 推荐 |
|---|---|
| 产品涉及决策/判断/选择（而非纯任务执行） | ✅ Thinking Style 分群 |
| 需要全旅程 IA 设计 | ✅ Mental Model Diagram |
| 团队过度依赖人口学，需要纠偏 | ✅ 引入 Listening Session |
| 多元用户群体，难以归入 3-5 个 persona | ✅ Mental Model + Thinking Style |
| 已有产品，找改进机会 | ✅ Below-the-line gap 分析 |

---

## 8. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| Listening Session 访谈纪律 | `persona/interview.py` 新增 `listening_session_mode` 参数 |
| Mental Model 任务亲和 | `persona/segment.py` 扩展层次聚类（task → tower → space） |
| Thinking Style 命名公式 | `persona/persona_builder.py` 新增 `thinking_style` 字段类型 |
| 反人口学检查 | `persona/persona_builder.py` 的 `review_persona()` 新增 anti-demographics 项 |
| Empathy vs Sympathy 训练 | `persona/templates.py` 新增 listening session 培训模板 |

---

## 9. 关键引述

> "Demographics are how you find your users in the world. They are not how you understand your users." — Indi Young

> "A persona has a face. A thinking style has a logic. Sometimes you need both. Often you need only the logic." — Practical Empathy

> "Listening is not waiting for your turn to speak. It is a discipline." — Indi Young

---

*笔记整理完成 | 基于 Indi Young《Mental Models》《Practical Empathy》及思维风格方法 | 与 Mulder 派形成"反人口学/认知分群"互补*
