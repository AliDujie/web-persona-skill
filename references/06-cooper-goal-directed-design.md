# 06 · Cooper 目标导向设计 (Goal-Directed Design)

> 来源：Alan Cooper《The Inmates Are Running the Asylum》(1999/2004) +《About Face: The Essentials of Interaction Design》第4版 (Cooper, Reimann, Cronin, Noessel, 2014)。
>
> Alan Cooper 是人物角色 (Persona) 方法的发明人——1983 年为 Sage 软件设计 SuperProject 时首次使用，1998 年正式定型并写入《Inmates》。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | Cooper（本笔记） |
|---|---|---|
| 数据来源 | 定量问卷 + 定性访谈 | 纯定性深度访谈（每角色 8-12 名受访者） |
| 角色数量 | 3-5 个并列 | 严格 1 个首要角色 + 若干次要角色 |
| 角色单位 | 用户群体的定量代表 | 复合的"原型 (archetype)" |
| 输出 | 卡片 + 对比表 | Foundation Document（30+ 页叙事文档）|
| 适合场景 | Web 站点、消费级、有调研预算 | 复杂软件、企业级、设计驱动 |

> 💡 **互补立场**：Cooper 提供"如何让单个角色深刻可信"的极致工艺；Mulder 提供"如何让一组角色有统计代表性"的工程化路径。两者结合即"深 × 广"。

---

## 2. 目标导向设计：核心信念

设计的目的不是满足"任务"，而是支撑用户的**目标 (Goal)**。任务可被替代、目标恒定。

### 三层目标模型 (Three Goal Layers)

| 层级 | 含义 | 示例（旅行 App） |
|---|---|---|
| **Experience Goals**（体验目标） | "我希望感觉……" | 不焦虑、被掌控、有成就感 |
| **End Goals**（终极目标） | "我希望完成……" | 顺利到达目的地、控制预算 |
| **Life Goals**（人生目标） | "我希望成为……" | 成为周到的家人、世界公民 |

> **设计含义**：交互层服务 End Goals；视觉/动效层服务 Experience Goals；品牌叙事层服务 Life Goals。Mulder 主要覆盖 End Goals，Cooper 让 Experience/Life 也进入决策视野。

---

## 3. 六类角色 (Six Persona Types)

Cooper 的角色不是平等并列，而是有严格的优先级层级：

| 类型 | 定义 | 设计权重 |
|---|---|---|
| **Primary（首要）** | 设计的核心驱动者；为该角色无法妥协的角色 | 100% |
| **Secondary（次要）** | 满足 Primary 后还需照顾；不破坏 Primary 体验 | 60% |
| **Supplemental（补充）** | 需求被 Primary+Secondary 覆盖即可 | 20% |
| **Customer（客户）** | 不是使用者，是采购决策者（B2B 场景） | 独立维度 |
| **Served（被服务）** | 不直接使用产品但受影响（如外科病人对手术系统） | 伦理维度 |
| **Negative（反角色）** | **明确不为之设计**的人群（防止迁就） | -100% |

> **关键纪律**：一个产品只能有 **1 个**首要角色（特殊情况下每条独立产品线 1 个）。多个首要角色 = 没有首要角色。这与 Mulder 允许多首要角色的立场不同，是 Cooper 派最强的纪律点。

---

## 4. 七步生成法 (Seven-Step Persona Process)

| 步骤 | 关键动作 | 产出物 |
|---|---|---|
| 1. 识别行为变量 | 列出 4-6 类变量：活动 (Activities)、态度 (Attitudes)、能力 (Aptitudes)、动机 (Motivations)、技能 (Skills) | 变量轴清单 |
| 2. 受访者-变量映射 | 把每位访谈对象在每条轴上画点 | 变量空间散点图 |
| 3. 识别显著模式 | 在多条轴上同时聚集的受访者 = 一个潜在角色 | 模式列表 |
| 4. 综合特征与目标 | 合成姓名、目标、行为细节、生活背景 | 角色草图 |
| 5. 完整性与冗余检查 | 是否覆盖关键差异？是否有重复角色合并？ | 角色清单 |
| 6. 指派类型 | 谁是 Primary / Secondary / Supplemental / Negative | 角色优先级图 |
| 7. 撰写叙事 | 写成 Foundation Document（含一日叙事） | 完整文档 |

> 💡 **Cooper vs Mulder 的根本差异**：Cooper 从行为变量出发"自下而上"聚类；Mulder 从问卷数据出发"自上而下"分群。两者都强调"不从人口学入手"。

---

## 5. 场景三联式 (Scenario Triad)

人物角色不是终点，**场景**才是。Cooper 提出三种场景，分阶段使用：

### 5.1 Context Scenario（情境场景，第一手）
- 写在设计开始前
- 高层叙事："Alex 周二早上 7:25 在地铁里打开 App，他想要……"
- **不涉及具体 UI**，只描述目标与上下文
- 用途：揭示设计应支持哪些核心流程

### 5.2 Key Path Scenario（关键路径场景，设计中）
- 在 Context Scenario 基础上展开关键交互
- 包含具体动作和系统响应
- 是 wireframe / prototype 的脚本
- 用途：检验信息架构能否承载主流程

### 5.3 Validation Scenario（验证场景，设计后）
- 边缘场景、错误恢复场景、必备使用场景 (Must-Use)
- 测试设计的鲁棒性
- 用途：发现"99% 顺利但 1% 崩溃"的体验断点

---

## 6. Foundation Document 结构（首要角色）

Cooper 派的角色文档不是 1 页卡片，而是 **20-40 页的奠基文档**：

```
Foundation Document
├── 1. 角色照片 + 一句话定位 + 关键引语
├── 2. 三层目标（Experience / End / Life）
├── 3. 行为变量地图（在 4-6 条轴上的位置）
├── 4. 一日叙事（A Day in the Life，1500 字 +）
├── 5. 与产品的关系（频率、动机、阻碍）
├── 6. 技能与心智模型
├── 7. 环境（物理、组织、社会）
├── 8. 引用与证据（访谈片段、行为证据）
└── 9. 角色间关系图（与 Secondary/Negative 的对比）
```

> 💡 **取舍建议**：在 Web/消费级项目使用 Mulder 1 页卡片即可；在企业软件/B2B SaaS/医疗/航空等高复杂度领域，Cooper Foundation Document 不可省略。

---

## 7. 高级概念

### 7.1 Ergonomic vs Cognitive Friction
- **Ergonomic friction**（人体工程摩擦）：物理点击、滑动、寻找
- **Cognitive friction**（认知摩擦）：理解系统状态、记忆操作、推理结果
- 现代软件的痛点 90% 是认知摩擦——Persona 的"心智模型"段必须显式描述

### 7.2 Personas vs Stereotypes vs Archetypes
- Stereotype（刻板印象）：基于群体偏见，**禁用**
- Archetype（原型）：跨文化的角色模式（《英雄之旅》），是构造工具
- Persona（人物角色）：基于研究的、有具体细节的、可挑战的——**禁止**用 stereotype 代替 persona

### 7.3 Anti-pattern: "Elastic User"
- "用户希望简单也希望强大；想要快也想要全面"——这是没有角色的征兆
- Persona 的核心价值：**强迫做出取舍**，把"用户"从一个可塑性无限的橡皮人，变成有固定目标的真人

---

## 8. 何时优先使用 Cooper 派 vs Mulder 派

| 情境 | 推荐 |
|---|---|
| Web 站点、内容平台、电商主站 | **Mulder 派**（量化代表性优先） |
| 复杂企业软件、SaaS 控制台、设计工具 | **Cooper 派**（深度叙事优先） |
| 医疗、航空、金融、安全领域 | **Cooper 派**（Validation Scenario 不可省） |
| 创业早期、无调研预算 | → 见 `11-lean-ux-proto-personas.md` |
| 需要思维风格分群（去人口学） | → 见 `09-indi-young-mental-models.md` |
| 学术/方法论严谨度审查 | → 见 `10-lene-nielsen-10steps.md` |

---

## 9. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| Experience/End/Life 三层目标 | `persona/persona_builder.py` 的 `goals` 字段可扩展为分层结构 |
| 六类角色优先级 | `persona/persona_builder.py` 的 `priority` 枚举（建议补 supplemental/served/negative） |
| 行为变量地图 | `persona/segment.py` 的二维矩阵可扩展为 4-6 维 |
| 三联场景 | `persona/design.py` 路径验证可分 Context/Key Path/Validation 三段 |
| Foundation Document | `persona/templates.py` 新增 `foundation_doc_template` 长版模板 |

---

## 10. 关键引述（用于团队推广）

> "If we want successful, pleasurable products, we have to design for the people who will actually use them. We must learn to discriminate among users." — Alan Cooper

> "When you try to please everyone, you please no one." — Alan Cooper, on the elastic user anti-pattern

> "The single most important thing about a persona is that it represents a *type* of user, but feels like a single person." — About Face 4

---

*笔记整理完成 | 基于 Cooper《Inmates》《About Face 4》核心章节 | 与 Mulder 派形成"深叙事"互补*
