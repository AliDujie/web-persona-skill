# 07 · Pruitt & Adlin 人物角色生命周期 (The Persona Lifecycle)

> 来源：John Pruitt & Tamara Adlin《The Persona Lifecycle: Keeping People in Mind Throughout Product Design》(Morgan Kaufmann, 2006, 700+ 页) +《The Essential Persona Lifecycle》(2010, 简化实战版)。
>
> 两位作者来自微软用户体验团队，本书是迄今为止最完整的人物角色组织治理手册。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder | Pruitt & Adlin |
|---|---|---|
| 关注重心 | **创建**人物角色（前端） | **运营**人物角色（全周期）|
| 输出形态 | 角色文档 | 治理流程 + 文档 + 工具包 |
| 时间跨度 | 项目立项期 | 项目前→中→后→退役 |
| 组织视角 | 设计/产品团队 | 跨部门（含管理层、销售、客服） |
| 弱点补盲 | Mulder 几乎不讲"角色发布后如何被持续使用" | Pruitt-Adlin 的核心战场 |

> 💡 **核心命题**：人物角色失败的原因 80% 不在创建质量，而在"创建后无人使用"。Lifecycle 解决的就是这个问题。

---

## 2. 五阶段生命周期

Pruitt & Adlin 把人物角色比作一个"虚拟员工"，有完整的生命周期：

```
Family Planning  →  Conception & Gestation  →  Birth & Maturation  →  Adulthood  →  Lifetime Achievement & Retirement
   计划生育          受孕与孕育               诞生与成长             成熟期         功成身退
   (规划阶段)        (创建阶段)               (推广阶段)            (使用阶段)     (退役阶段)
```

### 2.1 Family Planning（规划阶段）— "我们真的需要 Persona 吗？"

| 任务 | 关键产出 |
|---|---|
| 评估组织成熟度 | 决策风格 / 用户研究文化 / 高管 buy-in |
| ROI 论证 | 预估节省的返工成本 vs Persona 创建成本 |
| 干系人映射 | 谁会用 / 谁会反对 / 谁需要培训 |
| 资源规划 | 时间（通常 6-12 周）、预算、团队配置 |

> ⚠️ **关键预警**：如果组织文化是"高管直觉决策、不重视用户研究"，先做小规模 Lean UX proto-persona（见 `11-lean-ux-proto-personas.md`），用胜利证明价值再上完整方法。

### 2.2 Conception & Gestation（受孕与孕育）— 创建阶段

Pruitt & Adlin 把角色构造拆成"骨骼-血肉"两步法：

#### Step 1: Persona Skeleton（角色骨架）— 1 周内
- 列出可能的 7-10 个候选角色
- 每个角色用 5-10 条 bullet 描述：群体名 + 关键行为 + 核心目标 + 区分性特征
- **此时不要写故事/不要起名字**——避免过早爱上某个角色
- 用骨架做团队投票，决定哪些值得"完整孕育"为正式 persona

#### Step 2: Foundation Document（奠基文档）— 4-8 周
对入选角色做完整数据填充：
- **Factoid pile**（事实卡片堆）：从访谈/数据中摘录 50-200 条事实片段，用墙面贴卡分类
- 把 factoids 归到角色骨架的各个段落下
- 为每条角色描述附带 **数据来源标记**（哪条访谈、哪份报告）
- 形成 30-50 页的 Foundation Document

> 💡 **Pruitt 招牌方法**："Factoid → Foundation"。每条角色描述都能追溯到原始数据，这是抵御"角色是编出来的"质疑的最强护甲。

### 2.3 Birth & Maturation（诞生与成长）— 推广阶段

```
Birth Day（发布日）：举办 Persona Launch 活动，1-2 小时全员参与
├── 海报上墙（每个工位都能看见）
├── 角色卡片（钱包大小，方便随身携带）
├── 角色名牌（会议室门口标"今天在为 Alex 设计"）
├── Persona Buddies（每位角色配一个团队大使）
└── 培训工作坊（每个部门 1 场，重点讲"如何在我的工作中使用"）
```

**首月跟踪指标**：
- 团队中能说出 Primary 角色姓名的比例
- 设计评审中引用 Persona 的次数
- 决策会议中"这是为谁做的"问题的频次

### 2.4 Adulthood（成熟期）— 使用阶段

人物角色应该被"嵌入"到现有工作流中，而非作为独立产物存在：

| 工作流 | Persona 的嵌入方式 |
|---|---|
| 需求评审 | 每个需求必须标注 Primary 角色 + 解决该角色哪个目标 |
| 设计评审 | 设计师以"Alex 视角"过 walkthrough |
| Bug 分类 | Bug 优先级按"影响哪个 Primary 角色"加权 |
| 销售/市场 | 销售话术按角色定制；广告投放按角色定向 |
| 客服 | 工单按角色归类，反馈回流到 Foundation Document |
| 招聘 | JD 中描述"需要为 Alex 这样的用户负责" |

### 2.5 Lifetime Achievement & Retirement（功成身退）— 退役阶段

Persona 不应永生。**触发退役的信号**：
- 业务方向转型，目标人群变化（如 B2C → B2B）
- 数据表明现有角色已不能解释 30% 以上的用户行为
- 新的研究方法（如 JTBD、Mental Models）显示更优分群
- 团队已内化角色思维，不再需要外显文档

**退役仪式**：
- 写一份 Lifetime Achievement 报告：这套角色驱动了哪些决策、产生了哪些 ROI
- 归档 Foundation Document 到知识库（不删除）
- 启动新一轮 Family Planning

> ⚠️ **常见错误：Zombie Personas（僵尸角色）**——已经过时却仍在引用。退役比创建更难，因为没人愿意承认"我们曾经依赖的角色已经失效"。设定 12-18 个月的强制复审制度。

---

## 3. 核心工具：Foundation Document 详细模板

```
[Persona Name] - Foundation Document v[X.X] / [Date]

§ 1. 角色摘要
   - 一句话定位
   - 关键引语（来自真实受访者）
   - 角色照片
   - 类型：Primary / Secondary / Supplemental / Negative

§ 2. 个人画像
   - 人口学（仅作为颜色，不作为分群依据）
   - 教育与职业背景
   - 家庭与生活方式
   - 技术熟练度

§ 3. 目标（Experience / End / Life 三层）
   - 与产品相关的目标
   - 与产品无关但驱动决策的人生目标

§ 4. 行为模式
   - 与产品相关的关键行为
   - 频率、时长、触发场景
   - 信息消费习惯

§ 5. 痛点与动机
   - 当前未被满足的需求
   - 已使用的替代方案
   - 切换成本

§ 6. 与产品的关系
   - 当前阶段（Awareness / Consider / Use / Advocate）
   - 增长路径
   - 流失风险

§ 7. 一日叙事 (Day in the Life)
   - 1500-3000 字的真实场景叙事
   - 必须包含：上下文、决策点、情绪曲线

§ 8. 引用与数据来源
   - 每条事实标注来源 (Interview-3, Survey-Q12, Analytics-Q1)
   - 至少 50 条 factoids

§ 9. 与其他角色的关系
   - 对比矩阵
   - 角色间互动（如有）

§ 10. 版本历史
   - v1.0 创建日期 / 数据来源
   - 每次修订的依据
```

---

## 4. Pruitt & Adlin 提出的 7 类常见 Persona 反模式

| 反模式 | 症状 | 修复 |
|---|---|---|
| 1. Stereotype Persona | 名字 + 照片 + 一堆人口学数据 | 加入行为变量、目标层次 |
| 2. Wishful Persona | "完美用户"投射，没有缺点 | 必须包含痛点、能力局限、负面动机 |
| 3. Self-portrait Persona | 团队成员的自画像 | 必须基于团队外部数据 |
| 4. Generic Persona | "30 岁城市白领"——没有任何区分性 | 找到该角色独特的行为/态度组合 |
| 5. Buzzword Persona | 全是"高效""智能""注重品质" | 用具体行为代替形容词 |
| 6. Snapshot Persona | 一次性创建，永不更新 | 设定季度复审机制 |
| 7. Solo Persona | 单独存在，不进入工作流 | 嵌入需求/设计/Bug/客服流程 |

---

## 5. 何时优先使用 Lifecycle 框架

| 情境 | 推荐 |
|---|---|
| 大型企业、跨部门协作复杂 | ✅ Lifecycle 不可省 |
| 第一次引入 Persona、面临质疑 | ✅ Family Planning 阶段尤为关键 |
| 已有 Persona 但"没人用" | ✅ 直接补 Birth & Maturation 推广 |
| 创业团队 < 10 人 | 简化版即可，无需完整生命周期 |
| 一次性研究项目（如学位论文） | 跳过 Adulthood/Retirement |

---

## 6. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| Persona Skeleton（骨架） | `persona/persona_builder.py` 新增 `create_skeleton()` 轻量方法 |
| Foundation Document 模板 | `persona/templates.py` 新增 `foundation_doc_template` |
| 推广方案（海报/卡片/工作坊） | `persona/templates.py` 已有 `promotion_plan` 可对齐扩展 |
| 7 类反模式检查清单 | `persona/persona_builder.py` 的 `review_persona()` 12 项可补充至 19 项 |
| 退役评估 | 新增 `persona/lifecycle.py` 模块（未来扩展） |

---

## 7. 关键引述

> "Personas don't fail because they are poorly created. They fail because no one uses them." — Pruitt & Adlin

> "If you cannot trace every claim in your persona back to a piece of data, your persona is fiction, not research." — The Persona Lifecycle

> "Personas are virtual employees. They need to be hired, trained, given a job, evaluated, and—when their job is done—retired with dignity." — Adlin & Pruitt

---

*笔记整理完成 | 基于 Pruitt & Adlin《The Persona Lifecycle》核心章节 | 与 Mulder 派形成"全周期治理"互补*
