# 08 · Goodwin 数字时代设计 (Designing for the Digital Age)

> 来源：Kim Goodwin《Designing for the Digital Age: How to Create Human-Centered Products and Services》(Wiley, 2009, 739 页)。
>
> Kim Goodwin 是 Cooper 公司前副总裁与首席设计师，本书是 Cooper 派 Goal-Directed Design 的**端到端实操手册**——从项目立项到详细设计的全流程，Persona 是其中模型化阶段的核心产物。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 与 Cooper《About Face》的关系

| 维度 | Cooper《About Face》 | Goodwin《Designing for the Digital Age》 |
|---|---|---|
| 定位 | 方法论圣经 | 实操百科 |
| 重点 | "为什么这样做" | "具体怎么做、第几天做什么" |
| 范围 | 交互设计原则 | 项目立项→交付的完整流程 |
| Persona 章节 | 1-2 章 | 6 章（建模、骨架、奠基、其他模型、场景、文档） |

> 💡 **Goodwin 的独特贡献**：把 Persona 放在"建模阶段 (Modeling Phase)"中，与 **Workflow Models（工作流模型）/ Artifact Models（工件模型）/ Mental Models（心智模型）/ Empathy Maps（共情地图）** 并列，强调"人物角色不是孤立产物，是建模阶段的一部分"。

---

## 2. 七阶段项目框架

Goodwin 把数字产品设计拆为七阶段，Persona 在第 3 阶段产出，并贯穿后续：

```
1. Project Planning      项目规划 — 目标、范围、研究计划
2. Research              研究 — 利益相关者访谈、用户访谈、专家、文献
3. Modeling              建模 — Persona + 其他四类模型
4. Requirements          需求 — 基于角色的场景与需求列表
5. Framework Definition  框架定义 — 信息架构、交互框架、视觉语言
6. Detailed Design       详细设计 — 高保真原型、规范文档
7. Implementation Support 实现支持 — 与开发协作、可用性验证
```

> Persona 的真正价值在阶段 4-7 持续兑现——而非阶段 3 完成时。

---

## 3. Persona 七步生成法（Goodwin 版）

Goodwin 把 Cooper 的七步法做了更精细的操作化定义：

### Step 1: 识别行为变量 (Behavioral Variables)
列出 4-8 类与产品相关的行为变量，每类设为一条连续轴：

```
活动 (Activities):    频率从 [低] -------- [高]
态度 (Attitudes):     对技术从 [恐惧] -------- [拥抱]
能力 (Aptitudes):     专业知识从 [新手] -------- [专家]
动机 (Motivations):   从 [外在驱动] -------- [内在驱动]
技能 (Skills):        操作技能从 [无] -------- [熟练]
```

### Step 2: 把受访者映射到变量上
- 每位访谈对象在每条轴上画一个点
- 不必精确到刻度，相对位置即可
- 用不同颜色/形状区分受访者

### Step 3: 识别显著模式
- 在多条轴上同时聚集的受访者 = 一个潜在角色
- "同时"是关键——只在 1-2 条轴上聚集不构成角色
- 至少 3 条轴上的协同聚集才被视为有效模式

### Step 4: 综合特征
| 字段 | 来源 |
|---|---|
| 行为细节 | 来自映射到该模式的所有受访者的行为 |
| 目标 | 行为背后的"为什么" |
| 环境 | 物理、社会、组织上下文 |
| 技能/能力 | 对产品域的知识水平 |
| 演示信息 | 添加照片、姓名、虚构细节让角色"活" |

### Step 5: 完整性与冗余检查
- 是否覆盖关键行为差异？
- 是否有两个角色目标几乎相同？合并
- 是否有"我们没数据但应该有"的模式？补访谈

### Step 6: 指派类型
- Primary / Secondary / Supplemental / Customer / Served / Negative
- 每条产品线只能 1 个 Primary

### Step 7: 撰写叙事
- Persona Skeleton（轻量，1-2 页）→ 用于内部沟通
- Persona Description（标准，5-10 页）→ 用于设计参考
- Foundation Document（完整，30-40 页）→ 用于深度研究和长期项目

---

## 4. Goodwin 的"五模型"建模框架

Persona 只是建模阶段的**第一个**产物。Goodwin 主张配合使用其他四类模型：

| 模型 | 内容 | 何时使用 |
|---|---|---|
| **1. Persona** | 用户原型 | 任何项目 |
| **2. Workflow Model** | 当前任务的步骤、决策点、阻塞点 | 复杂流程类产品 |
| **3. Artifact Model** | 用户当前使用的工件（表格、文档、白板） | 替代/数字化既有工具时 |
| **4. Mental Model** | 用户对系统的心理模型（与 Indi Young 互通） | 信息架构、概念命名时 |
| **5. Empathy Map** | 角色的所见/所想/所感/所行 | 推广/团队对齐时 |

> 💡 **Mulder 派的盲点**：仅有 Persona 不足以设计复杂产品。Goodwin 的"五模型并用"是对 Mulder 单一产物模式的扩展。

---

## 5. Persona Skeleton（骨架）模板

Goodwin 强力推荐先做骨架、获团队共识后再投入完整文档：

```markdown
# Persona Skeleton: [代号]

## 谁
- 一句话描述
- 关键人口学（仅当与行为相关时）

## 关键行为
- 行为 1（频率 / 上下文）
- 行为 2
- 行为 3

## 主要目标
- 目标 1
- 目标 2

## 与产品的关系
- 当前如何使用 / 为什么使用 / 痛点

## 区分性特征
- 与其他角色最不一样的 1-2 点
```

> ⏱ **生产效率**：一个骨架 1-2 小时；完整描述 1-2 天；Foundation Document 1-2 周。

---

## 6. 从 Persona 到 Requirements 的桥梁：Context Scenarios

Goodwin 把场景分为四类（比 Cooper 多两类）：

| 场景类型 | 用途 | 阶段 |
|---|---|---|
| **Context Scenario** | 描述目标和上下文，无 UI | 需求阶段 |
| **Key Path Scenario** | 关键交互路径，含 UI | 框架阶段 |
| **Validation Scenario** | 边缘和异常情况 | 详细设计阶段 |
| **Day-in-the-Life Scenario** | 全天叙事，跨多次产品使用 | 战略阶段 |

每条 Context Scenario 应能直接拆解为：
- **角色目标**：用户想完成什么
- **数据需求**：系统需要什么数据
- **功能需求**：系统需要什么功能
- **上下文需求**：环境/设备/时机约束

> 💡 这正是"为什么场景比角色重要"——场景是从角色到产品决策的转换器。

---

## 7. 实战章节速查

Goodwin 书中可直接套用的工作产物：

| 工作产物 | 章节 | 何时用 |
|---|---|---|
| Stakeholder Interview Guide | 第 4 章 | 项目立项 |
| User Interview Guide (Goal-Directed) | 第 5 章 | 用户研究 |
| Behavioral Variable Mapping Sheet | 第 7 章 | 模式识别 |
| Persona Foundation Document Template | 第 8 章 | 完整角色文档 |
| Workflow Model Notation | 第 9 章 | 流程建模 |
| Context Scenario Template | 第 10 章 | 需求生成 |
| Information Architecture Worksheet | 第 13 章 | IA 设计 |
| Design Principles Worksheet | 第 14 章 | 视觉/交互定调 |

---

## 8. 何时优先使用 Goodwin 框架

| 情境 | 推荐 |
|---|---|
| 端到端从 0 到 1 的产品设计 | ✅ Goodwin 七阶段是首选 |
| 复杂工作流类产品（CRM、ERP、医疗信息系统） | ✅ 五模型并用必备 |
| 已有 Persona 但不知如何衔接到设计 | ✅ Context Scenario 桥接器 |
| 仅做 Persona 创建（不涉及后续设计） | Mulder/Cooper 即可 |

---

## 9. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| Persona Skeleton 模板 | `persona/templates.py` 新增 `skeleton_template` |
| 行为变量映射 | `persona/segment.py` 扩展为多维（4-8 轴） |
| 五模型建模框架 | 新增 `persona/models.py`（未来扩展，含 workflow/artifact/mental） |
| Context/Key Path/Validation/Day-in-the-Life 场景 | `persona/design.py` 场景生成可分四类 |
| 七阶段项目框架 | `persona/strategy.py` 项目规划模块可对接 |

---

## 10. 关键引述

> "Personas alone are not enough. The richer your model set, the better your design decisions." — Kim Goodwin

> "Don't fall in love with your first persona draft. Skeletons exist so you can throw them away." — Designing for the Digital Age

> "If a persona doesn't change a single design decision, it's decoration, not research." — Goodwin

---

*笔记整理完成 | 基于 Goodwin《Designing for the Digital Age》核心章节 | 与 Mulder 派形成"端到端实操"互补*
