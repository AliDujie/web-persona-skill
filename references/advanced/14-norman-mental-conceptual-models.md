# 14 · Norman 心智模型与概念模型 (Mental Models & Conceptual Models)

> 来源：Don Norman《The Design of Everyday Things》(原版 1988《POET》, 修订版 2013《DOET》) +《The Design of Future Things》(2007) + 多篇 NN/g 文章。
>
> Don Norman 是认知科学家，"用户体验 (User Experience)" 一词的发明者。本书提供了 Persona 方法论的**理论根基**——为什么"以用户为中心"是必要的、设计师与用户的认知差距来自哪里。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 与 Persona 方法的关系

| 维度 | Norman | Persona 方法 |
|---|---|---|
| 学科 | 认知科学 | 设计实践 |
| 角色 | 提供"为什么"的理论根基 | 提供"怎么做"的工具 |
| 核心概念 | 心智模型 / 概念模型 / 系统映像 | 角色档案 / 场景 |
| 输出 | 设计原则 | 设计规范 |

> 💡 **Norman 的核心命题**："设计师不是用户"——这句话是所有 Persona 方法的认知科学基础。Cooper、Mulder、Goodwin 都隐含引用 Norman 的理论。

---

## 2. 三模型框架 (The Three Models)

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   设计师                                       用户     │
│     │                                            │      │
│     ▼                                            ▼      │
│  ┌────────────┐    生成      ┌────────────┐            │
│  │ Designer's │  ─────────►  │  System    │  ◄───────  │
│  │   Model    │              │   Image    │   感知    │
│  │ (概念模型) │              │ (系统映像) │            │
│  └────────────┘              └────────────┘            │
│         │                          │                    │
│         │ 应该等于                 │ 应该让             │
│         ▼                          ▼                    │
│  ┌────────────────────────────────────┐                │
│  │      User's Mental Model           │                │
│  │         (用户心智模型)             │                │
│  └────────────────────────────────────┘                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 2.1 Conceptual Model（概念模型 / 设计师模型）
- 设计师对系统**应该如何工作**的理解
- 写在文档里、白板上、设计师脑中
- 用户**永远看不到**这个模型

### 2.2 Mental Model（心智模型 / 用户模型）
- 用户对系统**实际如何工作**的猜测
- 来自先前经验、直觉、试错
- 通常是不完整、不准确的
- 但**用户的所有操作都基于此模型**

### 2.3 System Image（系统映像）
- 用户能实际感知到的所有东西：界面、文档、错误信息、外观
- 是设计师与用户唯一的沟通桥梁
- **设计的本质 = 通过 System Image 把 Conceptual Model 传递给用户的 Mental Model**

> 💡 **Persona 的认知作用**：迫使设计师显式描述"目标用户的 Mental Model 是什么"，从而判断 System Image 是否能正确传达 Conceptual Model。没有 Persona，设计师默认假设"用户的 Mental Model = 我的 Conceptual Model"，这是最常见的设计错误。

---

## 3. 七步行动模型 (Seven Stages of Action)

用户使用产品时的认知-行动循环：

```
1. Goal             我想做什么？
   ↓
2. Plan             我打算怎么做？
   ↓
3. Specify          我具体执行什么动作？
   ↓
4. Perform          执行动作
   ↓
5. Perceive         我看到了什么变化？
   ↓
6. Interpret        这意味着什么？
   ↓
7. Compare          这是我想要的结果吗？
   ↓ （回到 Goal 或调整 Plan）
```

### 3.1 两类设计鸿沟

| 鸿沟 | 出现位置 | 设计应对 |
|---|---|---|
| **Gulf of Execution**（执行鸿沟） | Step 2-4：用户不知道**该怎么做** | 提供清晰可见的功能、合理的默认值 |
| **Gulf of Evaluation**（评估鸿沟） | Step 5-7：用户不知道**结果是什么** | 即时反馈、明确状态、可解释错误 |

> 💡 **Persona 的设计应用**：每个角色的"技能水平"和"心智模型成熟度"决定了他们更容易遭遇哪个鸿沟。新手用户主要受执行鸿沟困扰；专家用户主要受评估鸿沟困扰。

---

## 4. Affordances & Signifiers（可供性与符号）

### 4.1 Affordance（可供性）
- 物体**实际**能被怎么使用（如把手"可以被握住"）
- 是物理属性 + 用户能力的组合
- 用户不一定能**察觉**到 affordance

### 4.2 Signifier（符号）
- **告诉用户** affordance 存在的视觉/听觉/触觉提示
- "推"字标签、按钮形状、悬停效果都是 signifier
- 设计师真正能控制的是 signifier，不是 affordance

### 4.3 与 Persona 的关联
- **新手 Persona** 严重依赖 signifier（按钮必须看起来像按钮）
- **专家 Persona** 可识别隐藏的 affordance（可接受简洁界面）
- 不区分 Persona 时，设计师常陷入两难——简洁 vs 易学
- Persona 的存在让"为谁优化"明确化

---

## 5. Norman 关于 Persona 的批评与建议

Norman 多次在文章中讨论 Persona：

### 5.1 他赞同的部分
- Persona 帮助团队避免"为自己设计"
- Persona 是从认知科学到设计实践的好桥梁
- 多元 Persona 提醒包容性

### 5.2 他批评的部分
- 静态 Persona 容易固化偏见
- 单数 Persona（特别是 Cooper 的 Primary）可能导致"为想象中的人设计而非真人"
- Persona 不能替代**直接观察用户行为**

### 5.3 他建议的整合
- Persona + **Activity-Centered Design**（活动中心设计）
- 不是"为人设计"，而是"为人的活动设计"
- 每个 Persona 应配 Activity Map（活动地图）

> 💡 **Activity-Centered Design** 与 Patton 的 Story Map、Goodwin 的 Workflow Model 思路一致：Persona 是名词，活动是动词，光有名词无法设计。

---

## 6. 七大设计原则 (Seven Fundamental Principles)

Norman 提炼的设计七原则，可作为 Persona 场景验证的检查清单：

| 原则 | 含义 | Persona 应用 |
|---|---|---|
| 1. **Discoverability**（可发现性） | 用户能找到功能 | 按 Persona 技能水平验证 |
| 2. **Feedback**（反馈） | 每个动作有响应 | 按 Persona 焦虑水平定制 |
| 3. **Conceptual Model**（概念模型） | 系统映像清晰传达模型 | 按 Persona 心智模型差异调整 |
| 4. **Affordances**（可供性） | 物体暗示用法 | 按 Persona 经验丰富度优化 |
| 5. **Signifiers**（符号） | 提示存在哪些动作 | 按 Persona 视觉素养调整 |
| 6. **Mappings**（映射） | 控制与结果对应 | 按 Persona 文化背景验证 |
| 7. **Constraints**（约束） | 限制错误动作 | 按 Persona 错误容忍度配置 |

---

## 7. 何时优先引用 Norman 框架

| 情境 | 推荐 |
|---|---|
| 团队需要理论根基（如向高管解释为何要做 Persona） | ✅ Norman 三模型最有说服力 |
| 设计评审时分析"为什么用户不会用" | ✅ 七步行动 + 两鸿沟分析 |
| 制定通用设计原则 | ✅ 七大原则作为检查清单 |
| 需要直接的产品决策工具 | ❌ Norman 偏理论，需要其他派别落地 |

---

## 8. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| 三模型框架 | `persona/persona_builder.py` 新增 `mental_model` 字段（描述该角色对产品域的认知） |
| 七步行动模型 | `persona/design.py` 路径验证可分七步 |
| 两鸿沟检查 | `persona/measure.py` Bug 优先级新增"鸿沟类型"维度 |
| Affordance/Signifier 检查 | `persona/design.py` 视觉/交互建议可对照 |
| 七大设计原则 | `persona/persona_builder.py` 的 `review_persona()` 可扩展验证维度 |

---

## 9. 关键引述

> "The designer does not communicate directly with the user. All communication takes place through the system image. The designer is not the user." — Don Norman, DOET

> "It is not enough that we build products that function, that are understandable and usable. We also need to build products that bring joy and excitement, pleasure and fun, and yes, beauty to people's lives." — Norman

> "Personas are valuable as long as they remind us of the gap between our understanding of the system and the user's. The moment they make us forget that gap, they have failed." — Norman, on Persona limits

---

*笔记整理完成 | 基于 Norman《DOET》核心章节及多篇文章 | 提供 Persona 方法的认知科学根基*
