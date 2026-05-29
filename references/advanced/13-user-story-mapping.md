# 13 · Patton 用户故事地图 (User Story Mapping)

> 来源：Jeff Patton《User Story Mapping: Discover the Whole Story, Build the Right Product》(O'Reilly, 2014, 中文版《用户故事地图》)。
>
> Jeff Patton 在敏捷开发界提出"故事地图"方法，把扁平的 user story 列表转成有叙事流的二维地图。Persona 在其中是"故事的主角"，让产品规划从"功能列表"升级为"用户旅程"。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 与 Persona 的关系

| 维度 | Persona 单独 | Persona × Story Map |
|---|---|---|
| 输出 | 静态角色文档 | 动态用户旅程 |
| 团队对齐 | 共识"为谁设计" | 共识"如何为他们的旅程交付价值" |
| 与开发的衔接 | 弱（Persona 在墙上但 backlog 里没人提） | 强（每条 story 显式绑定 Persona） |
| 解决的痛点 | "用户是谁" | "MVP 切什么、V2/V3 切什么" |

> 💡 **Patton 的关键论点**：Persona 是 **noun**（名词），Story Map 是 **verb**（动词）。两者结合才完整：你为谁做（角色）+ 帮他们做什么旅程（地图）。

---

## 2. Story Map 的二维结构

```
─────────── 时间维度（用户旅程从左到右）───────────►

  Activity 1        Activity 2        Activity 3       ← 主干 (Backbone)
  ──────────        ──────────        ──────────       ← 一级活动
  Step 1.1          Step 2.1          Step 3.1         ← 用户步骤
  Step 1.2          Step 2.2          Step 3.2
  Step 1.3                            Step 3.3
  ↓ 优先级递减 ↓
  ┌─Story A1─┐    ┌─Story B1─┐    ┌─Story C1─┐       ← MVP 切片
  │Story A2  │    │Story B2  │    │Story C2  │
  │Story A3  │    └──────────┘    │Story C3  │
  └──────────┘                    └──────────┘
  ┌─Story A4─┐    ┌─Story B3─┐    ┌─Story C4─┐       ← V2 切片
  │Story A5  │    │Story B4  │    │Story C5  │
  └──────────┘    └──────────┘    └──────────┘
   ↓
  ┌─Story A6─┐                    ┌─Story C6─┐       ← V3 切片
  └──────────┘                    └──────────┘

─────────── 优先级维度（从上到下，价值递减）───────────►
```

### 2.1 三层结构
- **Backbone（骨架）**：用户活动序列（Activity 1 → 2 → 3）
- **Walking Skeleton**：每个活动下的最小用户步骤
- **Stories**：实现每个步骤的具体功能切片

### 2.2 切片逻辑
- **横切**（Slice horizontally）：每个发布版本走一条横线，覆盖完整用户旅程的最小可用版本
- **不要纵切**（Don't slice vertically）：一次只做完一个 Activity 的所有 Story，会让用户拿到"半个产品"

> 💡 这是 Patton 与传统 Scrum backlog 的根本差异——传统 backlog 是按 story 优先级排，容易做完一个孤立功能但用户用不起来；Story Map 强制按"完整旅程的最小版本"切。

---

## 3. Persona × Story Map 的整合方法

### 3.1 单角色 Story Map
适用于：单一首要角色，简单产品

```
[Persona: Alex] 的旅程
├── Activity 1
├── Activity 2
└── Activity 3
```

### 3.2 多角色叠加 Story Map
适用于：2-3 个角色并存，旅程有交叉

```
Activity 1     Activity 2     Activity 3
[Alex] ✓      [Alex] ✓       [Alex] ✓
[Beth] ✓      [Beth] ✗       [Beth] ✓        ← Beth 不参与 Activity 2
              [Cara] ✓                       ← Cara 仅在 Activity 2 出现
```

每条 story 标注：服务哪个 Persona、解决他们哪个目标。

### 3.3 角色专属泳道 (Persona Swim Lanes)
适用于：多边市场（如平台型产品）

```
─────────── Activity 1   Activity 2   Activity 3 ───►
[Buyer]:    Story B1      Story B2      Story B3
[Seller]:   Story S1      Story S2      Story S3
[Admin]:    -             Story A1      -
```

> 💡 平台型产品（如电商、招聘网站）必用泳道版。每个 Persona 一条泳道，看清楚平台两边/三边在不同活动中的协作。

---

## 4. Now Map vs Later Map

Patton 的另一关键贡献：把 Story Map 用作**当前-未来对比工具**。

### 4.1 Now Map（当前状态地图）
- 描述用户**今天**怎么做（不限于使用本产品）
- 暴露当前流程的痛点、低效点、断裂点
- 通常包含使用 Excel、邮件、电话等"非数字"步骤

### 4.2 Later Map（未来状态地图）
- 描述加入新产品/功能后的旅程
- 直观对比：哪些步骤被消除、合并、加速

### 4.3 Gap = 机会
- 在 Now Map 中存在但 Later Map 中消失的步骤 = 价值消除
- 在 Now Map 中是痛点但 Later Map 中变顺畅的步骤 = 价值改善
- 用此 Gap 论证 ROI

---

## 5. 7 个常见 Story Map 反模式

| 反模式 | 症状 | 修复 |
|---|---|---|
| 1. 纯任务列表 | 没有用户主体，全是功能 | 在每张卡片上加"为谁" |
| 2. 纵切发布 | V1 只有 Activity 1，用户用不起来 | 改横切 |
| 3. 没有时间维度 | 卡片随机摆放 | 强制从左到右按用户经历的时序 |
| 4. 缺 Persona 标记 | "用户登录"——哪个用户？ | 每条 story 必须标注 Persona |
| 5. Now/Later 混淆 | 两张地图混着画 | 明确分开两块墙 |
| 6. 一次性产物 | 画完就忘 | 每个 Sprint 用 Story Map 做规划工作坊 |
| 7. 工具至上 | 在 Jira 里画 Story Map | Patton 主张用物理墙、便利贴 |

---

## 6. Story Map 工作坊流程（半天）

```
0:00 - 0:30  目标对齐
   ├─ 明确这次 Map 的范围（一个 epic / 完整产品）
   └─ 选择 Persona 焦点

0:30 - 1:30  Now Map 共建
   ├─ 团队列出用户当前活动序列（横轴）
   └─ 每个活动下列出当前步骤、痛点

1:30 - 2:00  确认核心痛点
   └─ 投票选出 3-5 个最痛的步骤

2:00 - 3:00  Later Map 共建
   ├─ 重新设计未来旅程
   └─ 每个步骤下列出 stories

3:00 - 3:30  切片
   ├─ 横切 MVP（覆盖完整旅程的最小集）
   ├─ 横切 V2
   └─ 横切 V3+（拓展性 backlog）

3:30 - 4:00  与 Persona 校验
   └─ 检查每条 story 是否能回答"为哪个 Persona 解决哪个目标"
```

---

## 7. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| Story Map 三层结构 | `persona/strategy.py` 新增 `generate_story_map()` |
| Now/Later Map 模板 | `persona/templates.py` 新增 `now_later_map_template` |
| Persona × Story 映射 | `persona/persona_builder.py` 新增 `journey_map` 字段 |
| 多边平台泳道 | `persona/strategy.py` 新增 `multi_sided_lanes()` |
| 横切发布规划 | `persona/strategy.py` 功能优先级矩阵新增"发布切片"维度 |

---

## 8. 何时优先使用 Story Map

| 情境 | 推荐 |
|---|---|
| 多角色协作的复杂产品 | ✅ 泳道 Story Map 必备 |
| 已有 Persona 但 backlog 失控 | ✅ Story Map 重整 backlog |
| 跨团队（产品 + 设计 + 工程）共建 | ✅ Story Map 是天然工作坊工具 |
| MVP 切片决策 | ✅ 横切 vs 纵切的判断框架 |
| 单人独立做用研 | Persona 单独使用即可 |

---

## 9. 关键引述

> "Stop calling them user stories. They are journey segments. The shift in language changes the conversation." — Jeff Patton

> "Persona without a story is a portrait. Story without a persona is a procedure manual. Together, they are a play." — User Story Mapping

> "MVP is not the smallest product you can ship. It is the smallest version of the user's complete journey that delivers value." — Patton

---

*笔记整理完成 | 基于 Jeff Patton《User Story Mapping》| 与 Mulder 派形成"角色 → 旅程 → 发布切片"衔接*
