---
name: web-persona-skill
version: "2.7.0"
description: Web人物角色(Personas)创建与应用专家技能。融合《赢在用户》《About Face》《Persona Lifecycle》《Designing for the Digital Age》《Mental Models》《Lean UX》《Buyer Personas》《Mismatch》《Interviewing Users》《The Mom Test》《Continuous Discovery Habits》《Mapping Experiences》《Competing Against Luck》等 30+ 经典著作的多书系方法论体系。v2.7.0 新增"上游研究手艺+持续发现+体验地图+叙事+JTBD理论源头"——Portigal 深度访谈 / Fitzpatrick Mom Test 客户验证 / Torres 持续发现 / Alvarez 精益客户开发 / Kalbach 体验地图 / Quesenbery UX 叙事 / Kuniavsky 观察方法 / Christensen JTBD 原版。含 4 个 Python 模块：clustering / llm_prompts / okr_bridge / measurement_toolkit。
author: "渡劫"
---

![Part of AliDujie Skills](https://img.shields.io/badge/AliDujie-UX%20Research%20Ecosystem-purple)

# Web Persona 人物角色创建与应用专家 Skill

融合 30+ 经典著作的多视角元决策器 + 量化引擎 + 心理学解释力 + 上游研究手艺 + 工程化代码。以 Steve Mulder《赢在用户》(The User Is Always Right) 为执行主轴，整合 Cooper 目标导向、Pruitt-Adlin 生命周期、Goodwin 端到端框架、Indi Young 心智模型、Lean UX Proto-Persona、Lene Nielsen 十步法等基础书系（v2.5.0），叠加 v2.6.0 四大维度（量化/心理学/伦理/工程化），再于 v2.7.0 补全上游研究手艺与持续发现：

- **量化与现代化（A 档）**：Mikkelson 统计 Persona / Revella Buyer Personas (B2B) / 合成 AI Personas / Stickdorn 服务设计
- **心理学与行为科学（B 档）**：Kahneman 双系统 / Fogg 行为模型 / JTBD-Persona 整合 / Wang 厚数据
- **伦理与多元（C 档）**：Holmes Mismatch 包容设计 / Cababa 二阶后果 / Hofstede 跨文化 / 偏差审计
- **工程化执行（D 档）**：4 个配套 Python 模块 — `persona/clustering.py` · `persona/llm_prompts.py` · `persona/okr_bridge.py` · `persona/measurement_toolkit.py`
- **上游研究手艺（E 档）**：Portigal 深度访谈 / Fitzpatrick Mom Test / Torres 持续发现 / Alvarez 精益客户开发
- **体验地图与叙事（F 档）**：Kalbach 体验地图 / Quesenbery UX 叙事 / Kuniavsky 观察方法 / Christensen JTBD 原版

> 📚 **方法论谱系（Methodology Lineage）** — 详见 `references/06-15`（v2.5）+ `references/16-31`（v2.6）+ `references/32-39`（v2.7），决策树见下文"§ 一、核心方法论"。

## 🧭 快速决策：什么时候使用 Persona？

| 你的需求 | 推荐技能 |
|---------|---------|
| 需要创建人物角色、用户细分、设计指导 | ✅ **Persona（本技能）** |
| 需要选择研究方法、设计访谈、执行可用性测试 | → [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) |
| 需要理解用户"工作"、机会评分、竞争分析 | → [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) |
| 需要定量验证假设、设计 A/B 测试、计算样本量 | → [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) |
| 需要价值主张画布、实验验证、优先级排序 | → [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) |
| 需要将研究结果转化为数据叙事、图表呈现 | → [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) |
| 需要结构化商业分析框架 | → [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) |

> 💡 Persona 是用户定义层：为所有其他技能提供证据驱动的用户视角。

### 💼 为什么团队选择 Persona

| 挑战 | 没有 Persona | 使用 Persona |
|------|----------|----------|
| 用户理解 | "我们的用户"——模糊概念 | 具体角色档案+目标+行为 |
| 设计决策 | "我觉得用户想要..."——主观 | "Alex 需要快速完成任务"——证据驱动 |
| 团队对齐 | 各想各的用户 | 共享角色档案，统一决策 |
| 功能优先级 | 满足所有人=没人满意 | 按首要角色需求排序 |
| 新人入职 | "让我告诉你用户是谁" | "这是我们的角色卡片"——秒懂 |

### 🔗 Ecosystem Quick Start / 生态系统快速上手

Persona 是 7 技能工作流的**用户定义层**——在所有研究之前使用，先明确"为谁设计"。

```python
# Step 1: 创建人物角色
from persona import PersonaSkill
persona = PersonaSkill("电商平台")
persona.add_persona(name="小明", archetype="效率型用户", priority="primary",
    quote="我只想快速完成", goals=["快速完成任务"],
    behaviors=["频繁搜索"], attitudes=["效率优先"], bio="忙碌的白领")

# Step 2: 质量评审
review = persona.review_persona("小明")  # 12 项质量检查

# Step 3: 为角色生成功能优先级
persona.add_feature("快速下单", {"小明": "高"}, "高", "低")
print(persona.render_feature_matrix())

# Step 4: CEO 视角用户经济模型
report = persona.generate_persona(include_ceo_analysis=True)
```

> 💡 **Try it now / 立即尝试**:
> ```python
> from persona import PersonaSkill
> skill = PersonaSkill("你的产品")
> skill.add_persona(name="Alex", archetype="Power User", priority="primary", goals=["快速完成任务"])
> print(skill.render_all_personas())
> ```

### ✅ 5 分钟快速开始检查清单

- [ ] **安装** — `cp -r web-persona-skill /your/agent/skills/`
- [ ] **导入** — `from persona import PersonaSkill`
- [ ] **初始化** — `skill = PersonaSkill("你的产品")`
- [ ] **创建角色** — `skill.add_persona(name="...", archetype="...", priority="primary", goals=[...])`
- [ ] **质量评审** — `skill.review_personas()`
- [ ] **功能优先级** — `skill.add_feature("功能名", {"角色": "高"}, "高", "低")`
- [ ] **完整报告** — `skill.generate_persona(include_ceo_analysis=True)`

[English](README.md#quick-start-5-minutes) | [中文](#中文说明)

## 🌐 AliDujie 技能生态系统

Persona 是 **用户定义层**，在研究流程最前端，为所有其他技能提供用户视角：

```
┌─────────────────────────────────────────────────────────────┐
│                    AliDujie UX Research Ecosystem            │
│                                                             │
│   ┌──────────────┐                                          │
│   │Persona 本技能│ 👤 用户定义层 — 创建证据驱动的人物角色      │
│   └──────┬───────┘                                          │
│          │ 研究数据                                           │
│   ┌──────▼───────┐    ┌──────────────┐                      │
│   │  JTBD Skill  │◄──►│  UDM Skill   │ 📖 方法论核心 — 100种 │
│   └──────┬───────┘    └──────┬───────┘    设计研究方法       │
│          │ 需求洞察           │ 定性发现                      │
│   ┌──────▼───────┐    ┌──────▼───────┐                      │
│   │  VPD Skill   │◄──►│  QuantUX     │ 📊 定量研究 — HEART/  │
│   └──────┬───────┘    └──────┬───────┘    A-B/MaxDiff        │
│          │ 价值主张           │ 定量验证                      │
│          └──────────┬────────┘                               │
│                     │ 研究发现                                │
│              ┌──────▼───────┐                                │
│              │  SWD Skill   │ 📈 数据叙事 — 数据可视化与汇报    │
│              └──────┬───────┘                                │
│                     │ 数据洞察                                │
│              ┌──────▼───────┐                                │
│              │  STM Skill   │ 🧠 战略分析 — 商业框架与决策      │
│              └──────────────┘                                │
│                                                             │
│  工作流: Persona → JTBD/UDM → QuantUX → VPD → SWD → STM    │
└─────────────────────────────────────────────────────────────┘
```

**Persona 的典型协作**：UDM 访谈收集数据 → Persona 创建角色 → JTBD 任务聚类 → VPD 画布填充 → QuantUX 验证 → SWD 汇报 → STM 战略决策

## 🌟 为什么选择 Persona？

- **经典方法论** — 基于 Steve Mulder《The User Is Always Right》，人物角色领域的经典著作，证据驱动的角色创建
- **全链路工具** — 从用户研究到角色创建，从商业策略到设计指导，10 大执行能力覆盖完整工作流
- **CEO 视角** — 内置用户经济模型、获取策略、留存策略，让角色数据直接与商业决策挂钩
- **零学习成本** — 纯 Python 标准库，无外部依赖，`from persona import PersonaSkill` 即可使用
- **12 项质量评审** — 自动化角色质量检查，确保角色基于真实数据而非虚构假设
- **生态前端** — 为所有其他技能提供证据驱动的用户视角，是研究流程的起点

## ⚡ 快速上手 (Quick Start)

```python
from persona import PersonaSkill

persona = PersonaSkill("你的产品名")

# 创建人物角色
persona.add_persona(
    name="效率型用户",
    short_desc="碎片时间工作，重视效率",
    priority="primary",
    quote="我只想快速完成",
    goals=["快速完成任务"],
    behaviors=["高频使用"],
    attitudes=["效率优先"],
    bio="忙碌的职场人"
)

# 质量评审
review = persona.review_persona("效率型用户")

# 角色卡片
profile = persona.profile_persona("效率型用户")
```

> 💡 **5 分钟上手**: `from persona import PersonaSkill` → 纯标准库，零依赖，开箱即用。

## 一、核心方法论

### 1.1 方法论谱系（Methodology Lineage）— v2.5.0+ 新增

本技能融合的 5 大方法论流派与 12+ 经典著作：

| 流派 | 代表著作 | 核心贡献 | 参考文档 |
|---|---|---|---|
| 🟦 **定量分群派** (Mulder/IBM) | 《The User Is Always Right》(2007) | 调研驱动 + 角色卡片 + 衡量体系 | `01-05`（默认主轴） |
| 🟥 **目标导向派** (Cooper) | 《About Face 4》《Inmates》 | Goal-Directed Design / 六类角色 / 三联场景 | `06-cooper-goal-directed-design` |
| 🟨 **生命周期派** (Pruitt & Adlin) | 《The Persona Lifecycle》(2006) | 五阶段治理 / Foundation Document | `07-persona-lifecycle` |
| 🟩 **端到端实操派** (Goodwin) | 《Designing for the Digital Age》(2009) | 七阶段框架 / 五模型并用 / Skeleton 优先 | `08-goodwin-digital-age` |
| 🟪 **认知/思维派** (Young/Norman) | 《Mental Models》《DOET》 | 反人口学 / Mental Model Diagram / 三模型框架 | `09-indi-young` `14-norman` |
| 🟫 **学术系统派** (Nielsen) | 《Personas - User Focused Design》(2019) | 四视角分类 / 十步法 / 包容性设计 | `10-lene-nielsen-10steps` |
| ⬜ **轻量假设派** (Gothelf/Hall) | 《Lean UX》《Just Enough Research》 | Proto-Persona / 假设清单 / Saturation 判断 | `11-lean-ux` `12-just-enough` |
| 🟧 **旅程衔接派** (Patton) | 《User Story Mapping》(2014) | 角色 × 故事地图 / 横切发布 | `13-user-story-mapping` |
| 🔴 **批判防御派** (Chapman & Microsoft) | 《Personas' New Clothes》《Inclusive Design》 | 五大批评 / 19 项防御评审 / Persona Spectrum | `15-personas-critique-and-defense` |

### 1.2 方法选择决策树

```
你的情境是？
│
├── 创业 < 18 个月 / 调研预算 = 0
│   └─► 🔘 Lean UX Proto-Persona（11-lean-ux）
│        └─► 6 个月后升级 → Mulder 主轴
│
├── 时间紧 (< 2 周) / 决策驱动
│   └─► 🔘 Just Enough Research（12-just-enough）
│        └─► 用 5 字段轻量 Persona
│
├── Web/电商/消费级 / 有调研预算
│   └─► 🔘 Mulder 主轴（01-05，本技能默认）
│        └─► 加 Lifecycle 治理（07-persona-lifecycle）
│
├── 复杂企业软件 / SaaS / 设计驱动
│   └─► 🔘 Cooper + Goodwin（06+08）
│        └─► Foundation Document + 五模型并用
│
├── 多边平台 / 多角色协作复杂
│   └─► 🔘 Patton Story Map 泳道（13-user-story-mapping）
│        └─► 加 Persona × Story Map 整合
│
├── 决策驱动 / 行为差异 >> 人口差异
│   └─► 🔘 Indi Young Mental Model + Thinking Style（09-indi-young）
│
├── 学术研究 / 伦理敏感 / 包容性要求高
│   └─► 🔘 Lene Nielsen 十步法（10-lene-nielsen）
│        └─► 加 Persona Spectrum（15-critique-and-defense）
│
├── 团队需要理论根基（向高管/质疑者解释）
│   └─► 🔘 Norman 三模型 + 七步行动（14-norman）
│
└── 已有 Persona 但效果不佳 / 反模式诊断
    └─► 🔘 Chapman 批判 + 19 项防御评审（15-critique-and-defense）
```

#### v2.6.0 深化决策树（量化 / 心理学 / 伦理 / 工程化）

```
你的进阶诉求是？
│
├── 大样本数据驱动 / 防御统计严谨度
│   └─► 🔘 Mikkelson 统计 Persona（16-statistical）
│        └─► KMeans / LCA / 因子+聚类 + 三角 K 决策
│        └─► 配套代码：persona/clustering.py（PersonaClusterer 一行 fit）
│
├── B2B / SaaS / 高客单 / 销售&市场协同
│   └─► 🔘 Revella Buyer Personas（17-revella）
│        └─► 5 Rings of Buying Insight + Win/Loss
│
├── 早期低预算 / 想用 LLM 生成 Persona
│   └─► 🔘 合成 AI Personas（18-synthetic-ai）
│        └─► 三范式（Augment/Simulate/Generate）+ 4 验证关卡
│        └─► 配套代码：persona/llm_prompts.py（4 类 Prompt 模板）
│
├── 服务型 / 跨触点 / 跨部门协同
│   └─► 🔘 Stickdorn 服务设计（19-service-design）
│        └─► Big Four + Service Blueprint
│
├── 决策型/金融/健康/教育 / 想做 Nudge
│   └─► 🔘 Kahneman 双系统（20-dual-system）
│        └─► System 1/2 + 11 偏差 + NUDGES
│
├── 习惯/留存/行为改变型产品
│   └─► 🔘 Fogg + Hooked（21-fogg）
│        └─► B=MAT + Tiny Habits + Hooked 4 步
│
├── 创新机会发掘 / 跨品类竞争视角
│   └─► 🔘 JTBD-Persona 整合（22-jtbd-integration）
│        └─► Job 三层 + 4 Forces + ODI
│        └─► 与 jtbd-knowledge-skill 互补，不替代
│
├── 新文化/新地域 / 大数据失效 / 创新探索
│   └─► 🔘 Wang 厚数据（23-thick-data）
│        └─► 民族志 5 件套 + Big+Thick 4 协同
│
├── 残障 / 老年 / 公共服务 / 包容性合规
│   └─► 🔘 Holmes Mismatch（24-kat-holmes）
│        └─► Mismatch 公式 + Spectrum 三类
│
├── 平台型 / AI / 监管敏感 / 二阶后果担忧
│   └─► 🔘 Cababa 系统二阶（25-cababa）
│        └─► Stakeholder 6 类 + Causal Loop + Anti-Persona
│
├── 出海 / 入华 / 跨文化品牌
│   └─► 🔘 Hofstede + Meyer Culture Map（26-hofstede）
│        └─► 6 维度 + Localization Audit 9 步
│
├── 任何对外发布的 Persona / 公平性合规
│   └─► 🔘 Bias Audit（27-bias-audit）
│        └─► 6 维 43 项 audit + 5 人多元 review
│
├── 想用代码做 OKR 衔接 / Roadmap 优先级
│   └─► 🔘 OKR Bridge（30-okr-roadmap-bridge）
│        └─► persona/okr_bridge.py（RICE/ICE 评分）
│
└── 想用代码做长期指标体系 / NPS/CES/留存
    └─► 🔘 Measurement Toolkit（31-measurement-toolkit）
         └─► persona/measurement_toolkit.py（6 类指标 + OKR 联动）
```

#### v2.7.0 研究手艺与发现决策树（上游采集 / 持续发现 / 体验地图 / JTBD 源头）

```
你的上游/表达诉求是？
│
├── 要做深度用户访谈 / 提问技巧 / Rapport 建立
│   └─► 🔘 Portigal 访谈方法论（32-portigal）
│        └─► 六阶段模型 + 6 大提问类型 + 3 层追问
│
├── 客户验证对话 / 防止恭维陷阱 / 承诺信号
│   └─► 🔘 Fitzpatrick Mom Test（33-fitzpatrick）
│        └─► 三铁律 + 过去行为 + 承诺三类（Time/Reputation/Money）
│
├── 建立持续发现习惯 / OST / 假设检验
│   └─► 🔘 Torres 持续发现（34-torres）
│        └─► Opportunity Solution Tree + Weekly Touchpoints + Assumption 4 类
│
├── 冷启动验证 / Early Adopter 画像 / Pivot 决策
│   └─► 🔘 Alvarez 精益客户开发（35-alvarez）
│        └─► Problem Hypothesis Canvas + Pivot 6 信号 + MVP 菜单
│
├── 旅程地图 / Journey Map / Service Blueprint 制图
│   └─► 🔘 Kalbach 体验地图（36-kalbach）
│        └─► 10 种图型 + 五行 Journey Map + Persona×Journey 闭环
│
├── Persona 叙事化 / 让 Persona 被记住 / 利益相关者沟通
│   └─► 🔘 Quesenbery UX 叙事（37-quesenbery）
│        └─► 五种故事类型 + 30 秒电梯版 + 故事验证
│
├── 研究方法选择 / CI / Diary Study / 多方法组合
│   └─► 🔘 Kuniavsky 观察方法（38-kuniavsky）
│        └─► 四象限方法选择 + Contextual Inquiry + 三阶段组合
│
└── JTBD 原版理论 / 情境分类 / Forces / 非消费
    └─► 🔘 Christensen Competing Against Luck（39-christensen）
         └─► Milkshake Story + 四力模型 + Circumstance-Based 分类
```

### 1.3 默认执行模块

| 模块 | 核心问题 | 关键行动 |
|------|---------|---------|
| A. 方法选择 | 该用定性/定量/混合路径？ | 评估预算/时间/团队 -> 推荐路径 + 执行计划 |
| B. 定性研究 | 用户真实目标和行为是什么？ | 生成访谈提纲 -> 招募方案 -> 数据分析 |
| C. 定量研究 | 如何用数据验证发现？ | 设计问卷 -> 分析方案 -> 数据洞察 |
| D. 用户细分 | 用户群体如何划分？ | 目标/行为/观点三维 -> 细分矩阵 -> 验证 |
| E. 角色创建 | 如何让角色真实可信？ | 文档生成 -> 对比表 -> 场景 -> 质量评审 |
| F. 活力维护 | 如何让角色持续被使用？ | 推广计划 -> 海报/卡片 -> 工作坊 |
| G. 商业策略 | 角色如何驱动商业决策？ | 价值评估 -> 差异化策略 -> 资源分配 |
| H. 功能优先级 | 先做什么功能？ | 需求x角色矩阵 -> P0-P3排序 -> 竞品分析 |
| I. 设计指导 | 如何用角色指导设计？ | 信息架构 -> 内容策略 -> 路径验证(3步规则) |
| J. 衡量成果 | 如何验证角色的价值？ | 测试脚本 -> 指标体系 -> Bug优先级 |

**黄金法则**：不从人口统计入手；聚焦目标/行为/观点三维度；用户"做了什么"比"说了什么"重要；首要角色最多2个；角色基于研究数据而非假设。

## 二、执行能力

1. **方法选择决策** -- 根据预算/时间/团队推荐定性/定量/混合路径，输出执行计划
2. **访谈提纲生成** -- 按目标/行为/痛点/期望等段落，生成定制化访谈问题
3. **问卷设计** -- 支持需求型/验证型/满意度型三类问卷，含筛选/量表/开放题
4. **用户细分** -- 数据管理、2x2矩阵、细分评估、Markdown输出
5. **角色文档创建** -- 完整角色卡(名称/简介/目标/行为/场景)、对比表、质量评审
6. **角色推广** -- 推广计划、海报/卡片文案、工作坊方案
7. **商业策略分析** -- 角色商业价值评估、差异化策略、资源分配建议
8. **功能优先级排序** -- 功能x角色需求矩阵、P0-P3优先级、竞品功能对比
9. **设计指导** -- 信息架构方案、内容策略、路径验证(3步规则)
10. **衡量成果** -- QA测试脚本、衡量指标体系、Bug优先级自动计算
11. **CEO视角分析** -- 用户经济模型(LTV/CAC)、获客策略、留存策略

## 三、触发条件总表

| 触发词 / 场景 | 执行能力 | 输出物 |
|---|---|---|
| 创建/生成人物角色、用户画像、persona | 全流程(A->D->E->F) | 完整角色文档集 |
| 选方法、怎么做、从哪开始 | 方法选择 | 方法选择建议书 |
| 访谈、用户研究、定性、访谈提纲 | 定性研究 | 访谈提纲、招募方案 |
| 问卷、调查、定量、问卷设计 | 问卷设计 | 完整问卷 |
| 细分、分群、聚类 | 用户细分 | 细分方案 + 矩阵 |
| 角色文档、角色卡片 | 角色创建 | 角色文档 + 对比表 |
| 推广、展示、维护 | 活力维护 | 推广计划、海报/卡片 |
| 商业策略、竞争、差异化 | 商业策略 | 策略报告 |
| 功能、优先级、排序、需求 | 功能优先级 | 功能矩阵 + 版本规划 |
| 信息架构、导航、内容、设计 | 设计指导 | IA方案 + 内容策略 |
| 测试、衡量、指标、效果 | 衡量成果 | 测试计划 + 指标体系 |
| 评审、检查、诊断现有角色 | 质量评审 | 12项评审报告 |
| 用户经济模型、LTV/CAC、增长策略 | CEO视角分析 | 经济模型 + 获客/留存策略 |

## 四、目录结构

```
web-persona-skill/
├── SKILL.md                     # 本文件
├── references/                  # 知识库文档（v2.5.0 + v2.6.0 + v2.7.0）
│   ├── 01-persona-basics.md         # Mulder 主轴：基础概念
│   ├── 02-measuring-results.md      # Mulder 主轴：成果衡量
│   ├── 03-persona-best-practices.md # Mulder 主轴：最佳实践
│   ├── 04-persona-driven-workflows.md # Mulder 主轴：研究工作流
│   ├── 05-ecosystem-collaboration.md # Mulder 主轴：跨技能协作
│   ├── 06-cooper-goal-directed-design.md  # v2.5 Tier 1: Cooper 派
│   ├── 07-persona-lifecycle.md            # v2.5 Tier 1: Pruitt-Adlin 派
│   ├── 08-goodwin-digital-age.md          # v2.5 Tier 1: Goodwin 派
│   ├── 09-indi-young-mental-models.md     # v2.5 Tier 2: Young 派（反人口学）
│   ├── 10-lene-nielsen-10steps.md         # v2.5 Tier 2: 欧洲学派
│   ├── 11-lean-ux-proto-personas.md       # v2.5 Tier 2: Lean UX
│   ├── 12-just-enough-research.md         # v2.5 Tier 3: Hall 决策驱动
│   ├── 13-user-story-mapping.md           # v2.5 Tier 3: Patton 衔接
│   ├── 14-norman-mental-conceptual-models.md # v2.5 Tier 3: 认知科学根基
│   ├── 15-personas-critique-and-defense.md  # v2.5 Tier 3: 批判 + 防御
│   ├── 16-mikkelson-statistical-personas.md # v2.6 A1: 量化 / 聚类（→ clustering.py）
│   ├── 17-revella-buyer-personas.md         # v2.6 A2: B2B / Buyer Personas
│   ├── 18-synthetic-ai-personas.md          # v2.6 A3: 合成 AI Persona（→ llm_prompts.py）
│   ├── 19-service-design-personas.md        # v2.6 A4: 服务设计 / Big Four
│   ├── 20-kahneman-dual-system.md           # v2.6 B1: 双系统 / Nudge
│   ├── 21-fogg-behavior-model.md            # v2.6 B2: Tiny Habits / Hooked
│   ├── 22-jtbd-persona-integration.md       # v2.6 B3: JTBD 整合
│   ├── 23-thick-data-ethnography.md         # v2.6 B4: 厚数据
│   ├── 24-kat-holmes-mismatch.md            # v2.6 C1: Mismatch 包容设计
│   ├── 25-cababa-systems-second-order.md    # v2.6 C2: 二阶后果
│   ├── 26-hofstede-cross-cultural.md        # v2.6 C3: 跨文化
│   ├── 27-bias-audit-personas.md            # v2.6 C4: 偏差审计
│   ├── 28-clustering-engineering.md         # v2.6 D1: PersonaClusterer 工程化
│   ├── 29-llm-prompt-library.md             # v2.6 D2: LLM Prompt 库
│   ├── 30-okr-roadmap-bridge.md             # v2.6 D3: Persona→OKR→Roadmap
│   ├── 31-measurement-toolkit.md            # v2.6 D4: 测量工具包
│   ├── 32-portigal-interviewing-users.md    # v2.7 E1: 深度访谈方法论
│   ├── 33-fitzpatrick-mom-test.md           # v2.7 E2: Mom Test 客户验证
│   ├── 34-torres-continuous-discovery.md    # v2.7 E3: 持续发现习惯
│   ├── 35-alvarez-lean-customer-development.md # v2.7 E4: 精益客户开发
│   ├── 36-kalbach-mapping-experiences.md    # v2.7 F1: 体验地图
│   ├── 37-quesenbery-storytelling-ux.md     # v2.7 F2: UX 叙事
│   ├── 38-kuniavsky-observing-user-experience.md # v2.7 F3: 观察方法百科
│   └── 39-christensen-competing-against-luck.md  # v2.7 F4: JTBD 原版
├── persona/                     # Python 工具包
│   ├── __init__.py              # PersonaSkill 统一入口类
│   ├── config.py                # 全局配置
│   ├── utils.py                 # 知识库加载与搜索
│   ├── templates.py             # 模板常量
│   ├── interview.py             # InterviewBuilder: 访谈提纲生成器
│   ├── survey.py                # SurveyBuilder: 问卷设计器
│   ├── segment.py               # SegmentAnalyzer: 用户细分
│   ├── persona_builder.py       # PersonaBuilder: 角色创建 + 评审
│   ├── strategy.py              # StrategyAnalyzer: 策略 + 功能 + 竞品
│   ├── design.py                # DesignAdvisor: IA + 内容 + 路径
│   ├── measure.py               # MeasureSystem: 测试 + 指标 + Bug
│   ├── clustering.py            # 🆕 v2.6 D1: PersonaClusterer（KMeans/LCA/Factor）
│   ├── llm_prompts.py           # 🆕 v2.6 D2: PersonaPromptLibrary（4 类 Prompt）
│   ├── okr_bridge.py            # 🆕 v2.6 D3: OKRBridge（Persona→Objective→KR）
│   ├── measurement_toolkit.py   # 🆕 v2.6 D4: MeasurementToolkit（NPS/CES/CSAT/Funnel）
│   └── tests/test_all.py        # 8 个测试用例
├── pyproject.toml
└── .gitignore
```

### ⛔ 何时不使用 Persona

- **选择研究方法或设计访谈** — 使用 [Universal Design Methods](https://github.com/AliDujie/universal-design-methods)
- **统计分析或 A/B 测试** — 使用 [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research)
- **理解用户 Jobs-to-be-Done** — 使用 [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill)
- **价值主张画布分析** — 使用 [Value Proposition Design](https://github.com/AliDujie/value-proposition-design)
- **数据可视化与叙事** — 使用 [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data)


## 五、知识库

### 5.1 主体方法论（Mulder 派 — 默认）

| 文件 | 核心内容 |
|------|---------|
| `references/01-persona-basics.md` | 人物角色基础概念、三种创建路径、细分原则、角色构成要素、优先级体系 |
| `references/02-measuring-results.md` | 发布前测试、发布后衡量、按角色分析指标、定量衡量体系 |
| `references/03-persona-best-practices.md` | 人物角色最佳实践、常见陷阱、成功模式 |
| `references/04-persona-driven-workflows.md` | Persona 驱动的研究工作流（跨技能协作） |
| `references/05-ecosystem-collaboration.md` | 跨技能协作完整流程（Persona → JTBD/UDM/QuantUX/VPD/SWD） |

### 5.2 扩展方法论（v2.5.0+ 新增 — 多书系融合）

#### Tier 1 · 方法论根基

| 文件 | 来源 | 核心内容 |
|------|------|---------|
| `references/06-cooper-goal-directed-design.md` | Cooper《About Face 4》 | Goal-Directed Design / 六类角色 / 三联式场景 / Foundation Document |
| `references/07-persona-lifecycle.md` | Pruitt & Adlin《Persona Lifecycle》 | 五阶段生命周期 / 7 类反模式 / 治理流程 |
| `references/08-goodwin-digital-age.md` | Goodwin《Designing for the Digital Age》 | 七阶段框架 / 五模型并用 / Persona Skeleton 优先 |

#### Tier 2 · 现代方法对照

| 文件 | 来源 | 核心内容 |
|------|------|---------|
| `references/09-indi-young-mental-models.md` | Indi Young《Mental Models》《Practical Empathy》 | Mental Model Diagram / Thinking Style Segments / 反人口学 |
| `references/10-lene-nielsen-10steps.md` | Lene Nielsen《Personas - User Focused Design》| 四视角分类 / 十步法 / 叙事五要素 / 包容性设计 |
| `references/11-lean-ux-proto-personas.md` | Gothelf《Lean UX》| Proto-Persona / 假设句式 / MVE 实验类型 / 演化路径 |

#### Tier 3 · 延伸视角

| 文件 | 来源 | 核心内容 |
|------|------|---------|
| `references/12-just-enough-research.md` | Erika Hall《Just Enough Research》| 五类研究问题 / Saturation 判断 / 反 Research Theater |
| `references/13-user-story-mapping.md` | Patton《User Story Mapping》| Story Map 三层结构 / Now/Later Map / 多边泳道 |
| `references/14-norman-mental-conceptual-models.md` | Norman《DOET》| 三模型框架 / 七步行动 / 七大设计原则 |
| `references/15-personas-critique-and-defense.md` | Chapman & Milham + Microsoft Inclusive Design | 五大批评 / 19 项防御评审 / Persona Spectrum |

### 5.3 深化扩展（v2.6.0 新增 — 量化 + 心理学 + 伦理 + 工程化）

#### A 档 · 量化与现代化

| 文件 | 来源 | 核心内容 |
|------|------|---------|
| `references/16-mikkelson-statistical-personas.md` | Mikkelson / Salminen / Brickey 等统计 Persona 文献 | KMeans/LCA/因子+聚类 / K 决策三角 / Bootstrap 稳定性 / 9 步流程 |
| `references/17-revella-buyer-personas.md` | Adele Revella《Buyer Personas》 | 5 Rings of Buying Insight / Win/Loss / B2B 决策链 5 角色 |
| `references/18-synthetic-ai-personas.md` | Park《Generative Agents》/ Salminen 2024 / PersonaHub | 三范式（Augment/Simulate/Generate）/ Persona Prompting / 4 验证关卡 / 5 伦理 |
| `references/19-service-design-personas.md` | Stickdorn《This Is Service Design Doing》 | Big Four / 6 类 Persona / Service Blueprint / 5 MoT |

#### B 档 · 心理学与行为科学

| 文件 | 来源 | 核心内容 |
|------|------|---------|
| `references/20-kahneman-dual-system.md` | Kahneman《Thinking Fast & Slow》《Noise》 | System 1/2 / 11 偏差 / NUDGES 6 原则 / Pre-mortem |
| `references/21-fogg-behavior-model.md` | BJ Fogg《Tiny Habits》/ Eyal《Hooked》 | B=MAT / Behavior Grid / Tiny Habits ABC / Hooked 4 步 |
| `references/22-jtbd-persona-integration.md` | Christensen / Klement / Wunker / Ulwick | Job 三层 / 4 Forces / ODI / Switch Interview / Persona×Jobs 多对多 |
| `references/23-thick-data-ethnography.md` | Tricia Wang / Geertz / Madsbjerg | 民族志 5 件套 / 厚描述 / Big+Thick 4 协同 / Reflexivity |

#### C 档 · 伦理与多元

| 文件 | 来源 | 核心内容 |
|------|------|---------|
| `references/24-kat-holmes-mismatch.md` | Kat Holmes《Mismatch》 | Mismatch 公式 / Spectrum 三类 / 5 排斥习惯 / Inclusive 3 原则 |
| `references/25-cababa-systems-second-order.md` | Sheryl Cababa《Closing the Loop》/ Meadows | 1st/2nd/3rd Order / Stakeholder 6 类 / Causal Loop / Anti-Persona |
| `references/26-hofstede-cross-cultural.md` | Hofstede / Hall / Meyer | 6 维度 / 中国 4 核心+7 本土 / 高低语境 / Localization Audit 9 步 |
| `references/27-bias-audit-personas.md` | Marsden & Haag / Buolamwini / Costanza-Chock | 8 病症 / 6 维 43 项 audit checklist / 5 人多元 review |

#### D 档 · 工程化（reference + 配套 Python 模块）

| 文件 | 配套代码 | 核心内容 |
|------|---------|---------|
| `references/28-clustering-engineering.md` | `persona/clustering.py` | PersonaClusterer / ClusteringResult / auto 方法选择 / Bootstrap |
| `references/29-llm-prompt-library.md` | `persona/llm_prompts.py` | 4 类 Prompt / Constitutional / 不耦合 LLM SDK |
| `references/30-okr-roadmap-bridge.md` | `persona/okr_bridge.py` | Persona→Objective→KR / RICE/ICE / 4 类 KR 模板 |
| `references/31-measurement-toolkit.md` | `persona/measurement_toolkit.py` | NPS/CES/CSAT/Funnel/Activation/Retention / OKR 联动 |

### 5.4 研究手艺与持续发现（v2.7.0 新增 — 上游 + 叙事 + 理论）

#### E 档 · 上游研究手艺 + 持续发现

| 文件 | 核心内容 | 来源 |
|------|---------|------|
| `references/32-portigal-interviewing-users.md` | 访谈六阶段 / 6 大提问类型 / Rapport 四层 / 远程访谈 / Debrief 三阶段 | Portigal《Interviewing Users》2nd ed. |
| `references/33-fitzpatrick-mom-test.md` | Mom Test 三铁律 / 过去行为好问题 / 承诺三类 / Meta-label 笔记 / Slicing | Fitzpatrick《The Mom Test》 |
| `references/34-torres-continuous-discovery.md` | OST / Weekly Touchpoints / Assumption 4 类 / Compare&Contrast / Product Trio | Torres《Continuous Discovery Habits》 |
| `references/35-alvarez-lean-customer-development.md` | Problem Hypothesis Canvas / Early Adopter 5 特征 / Pivot 6 信号 / MVP 类型 | Alvarez《Lean Customer Development》 |

#### F 档 · 体验地图、叙事与理论源头

| 文件 | 核心内容 | 来源 |
|------|---------|------|
| `references/36-kalbach-mapping-experiences.md` | 10 种地图类型 / Journey Map 五行 / Blueprint 五线 / MoT / Persona×Journey | Kalbach《Mapping Experiences》2nd ed. |
| `references/37-quesenbery-storytelling-ux.md` | UX 故事五类型 / 故事五要素 / 30 秒电梯版 / 六原则 / 受众适配 | Quesenbery & Brooks《Storytelling for UX》 |
| `references/38-kuniavsky-observing-user-experience.md` | 四象限方法选择 / CI 4 原则 / Diary Study / 可用性测试 / 多方法组合 | Kuniavsky《Observing the User Experience》2nd ed. |
| `references/39-christensen-competing-against-luck.md` | JTBD 原版 / Milkshake Story / Forces 4 力 / Circumstance / 非消费 / Hiring | Christensen《Competing Against Luck》 |

> 💡 **何时查阅扩展知识库**：默认执行 Mulder 主轴即可。当遇到决策树中的特殊情境（创业早期、复杂企业、多边平台、伦理敏感等），按需查阅对应文档。

---

## 六、Python 工具包

### 6.1 安装与依赖

纯 Python 3.8+ 实现，无外部依赖。

```python
import sys; sys.path.insert(0, "/path/to/web-persona-skill")
from persona import PersonaSkill
```

### 6.2 PersonaSkill 方法一览

`PersonaSkill` 封装全部模块，每个方法返回 Markdown 字符串。初始化: `skill = PersonaSkill("产品名")`

| 方法 | 能力 | 必填参数 | 返回 |
|------|------|---------|------|
| `generate_interview()` | 访谈提纲 | title, sections | Markdown |
| `generate_survey()` | 问卷设计 | title, survey_type | Markdown |
| `add_user()` | 添加用户数据 | user_id | -- |
| `add_segment()` | 添加细分群体 | name, description, core_goals, typical_behaviors, key_attitudes | Segment |
| `render_segments()` | 输出细分结果 | -- | Markdown |
| `add_persona()` | 创建角色 | name, short_desc, priority, quote, goals, behaviors, attitudes, bio | PersonaProfile |
| `add_scenario()` | 添加使用场景 | persona_name, title, trigger, steps, result | -- |
| `render_all_personas()` | 输出角色文档 | -- | Markdown |
| `render_persona_comparison()` | 角色对比表 | -- | Markdown |
| `review_personas()` | 质量评审(12项) | -- | Markdown |
| `add_persona_value()` | 角色商业价值 | persona_name, market_size, spending, acquisition_cost, lifetime_value, score | BusinessValue |
| `render_strategy()` | 商业策略报告 | -- | Markdown |
| `add_feature()` | 添加功能 | name, persona_needs, business_value, tech_difficulty | FeatureItem |
| `render_feature_matrix()` | 功能矩阵(P0-P3) | -- | Markdown |
| `add_competitor()` | 添加竞品 | name, features_coverage | -- |
| `render_competitor_analysis()` | 竞品分析 | -- | Markdown |
| `validate_path()` | 路径验证(3步) | persona_name, task, path | str |
| `render_ia()` | 信息架构 | -- | Markdown |
| `render_content_strategy()` | 内容策略 | -- | Markdown |
| `add_test_script()` | 测试脚本 | persona_name, steps | TestScript |
| `add_metric()` | 衡量指标 | persona_name, metric, target, source, method | MetricItem |
| `add_bug()` | Bug优先级 | description, persona, is_primary, blocks_core | str |
| `render_test_plan()` | 测试计划 | -- | Markdown |
| `render_measure_system()` | 衡量体系 | -- | Markdown |
| `search_knowledge()` | 知识库检索 | keyword | Dict |
| `generate_persona_economics()` | CEO: 经济模型 | total_users(默认100000) | Markdown |
| `generate_acquisition_strategy()` | CEO: 获客策略 | -- | Markdown |
| `generate_retention_strategy()` | CEO: 留存策略 | -- | Markdown |
| `generate_persona()` | CEO: 完整报告 | include_ceo_analysis, total_users | Markdown |

### 6.3 模块速查

| 模块文件 | 主类 | 输出类型 | 说明 |
|---------|------|---------|------|
| `interview.py` | `InterviewBuilder` -> `InterviewGuide` | Markdown / JSON | 8段落(warmup~closing)，自定义问题，研究提示 |
| `survey.py` | `SurveyBuilder` -> `Survey` | Markdown | needs/validation/satisfaction 三类问卷 |
| `segment.py` | `SegmentAnalyzer` -> `SegmentationResult` | Markdown | 用户数据+细分群体+2x2矩阵+评估 |
| `persona_builder.py` | `PersonaBuilder` -> `PersonaProfile` | Markdown | 角色文档+对比表+场景+12项质量评审 |
| `strategy.py` | `StrategyAnalyzer` -> `FeatureItem` | Markdown | 商业价值+功能矩阵(P0-P3)+竞品分析 |
| `design.py` | `DesignAdvisor` -> `PathValidation` | Markdown | 导航+内容策略+路径验证(3步规则) |
| `measure.py` | `MeasureSystem` -> `BugPriority` | Markdown | 测试脚本+指标+Bug(P0=首要角色核心阻塞) |

**角色优先级**: primary(首要) / secondary(次要) / unimportant(不重要) / negative(排斥的)

**Bug优先级**: P0=首要角色核心任务阻塞 | P1=首要角色非核心 | P2=次要角色 | P3=不影响任务

### 6.4 CEO 视角扩展分析

在角色创建完成后，可生成商业决策级分析（须先调用 `add_persona()`）:

| 方法 | 输出内容 |
|------|---------|
| `generate_persona_economics(total_users)` | 各Persona规模、CAC、LTV、LTV/CAC健康度 |
| `generate_acquisition_strategy()` | 获客渠道、预算分配、ROI、时间线 |
| `generate_retention_strategy()` | 留存率、流失预警、生命周期管理 |
| `generate_persona(include_ceo_analysis=True)` | 完整画像 + 上述全部CEO分析（一键生成） |

### 6.5 完整使用示例

```python
from persona import PersonaSkill

skill = PersonaSkill("电商平台")

# 访谈提纲
print(skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"]))

# 问卷设计
print(skill.generate_survey("需求调研", "needs", pain_points=["搜索不精准", "价格不透明"]))

# 创建角色
skill.add_persona("小明", "效率型用户", "primary", "我只想快速完成",
    goals=["快速下单"], behaviors=["频繁使用"],
    attitudes=["追求效率"], bio="小明是一位忙碌的白领...")
skill.add_persona("小红", "探索型用户", "secondary", "发现好物才开心",
    goals=["发现特色商品"], behaviors=["仔细比较"],
    attitudes=["重视体验"], bio="小红是一位年轻设计师...")
print(skill.render_all_personas())
print(skill.review_personas())

# 功能优先级
skill.add_feature("快速下单", {"小明": "高", "小红": "低"}, "高", "低")
print(skill.render_feature_matrix())

# Bug 优先级
print(skill.add_bug("首页加载慢", "小明", is_primary=True, blocks_core=True))
# -> P0: 首页加载慢 (影响首要角色的核心任务，必须立即修复)

# CEO 视角完整报告（角色文档 + 经济模型 + 获客 + 留存）
print(skill.generate_persona(include_ceo_analysis=True, total_users=100000))

# 知识库检索
print(skill.search_knowledge("细分"))
```

### 6.6 AI Agent 调用规则

| # | 规则 | 说明 |
|---|------|------|
| 1 | **统一入口** | 始终通过 `PersonaSkill` 类调用，不直接实例化子模块 |
| 2 | **返回值** | 所有方法返回 Markdown 字符串，可直接展示给用户 |
| 3 | **触发映射** | 根据用户意图匹配触发条件总表，选择对应能力 |
| 4 | **顺序执行** | 全流程按 A->D->E->F 顺序，商业分析按 G->H 顺序 |
| 5 | **知识优先** | 方法论问题先调用 `search_knowledge()` 查询知识库 |
| 6 | **先角色后分析** | CEO视角方法须先 `add_persona()` 创建角色后才可使用 |
| 7 | **交互引导** | 执行前先收集必要信息（业务类型、目标用户、预算时间等） |
| 8 | **完整交付** | 每个任务产出完整可用的文档/方案/报告 |

### 6.7 测试说明

```bash
cd web-persona-skill && python persona/tests/test_all.py
# 或: python -m pytest persona/tests/test_all.py -v
```

| 测试用例 | 覆盖模块 | 验证内容 |
|---------|---------|---------|
| `test_knowledge_loading()` | 知识库 | 加载、搜索、关键词匹配 |
| `test_interview_builder()` | 访谈(B) | 段落选择、自定义问题、Markdown/JSON |
| `test_survey_builder()` | 问卷(C) | needs/validation/satisfaction 三类型 |
| `test_segment_analyzer()` | 细分(D) | 数据管理、细分评估、矩阵输出 |
| `test_persona_builder()` | 角色(E) | 创建、场景、对比、12项质量评审 |
| `test_strategy_analyzer()` | 策略(G/H) | 商业价值、功能矩阵、竞品分析 |
| `test_design_advisor()` | 设计(I) | 导航、内容、3步规则路径验证 |
| `test_measure_system()` | 衡量(J) | 测试脚本、指标、Bug P0-P3 |

### 6.8 与其他 Skill 的协作

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 研究结果可视化 | Storytelling with Data | Persona数据 -> SWD选图表 -> SWD构建故事 |
| 价值主张验证 | Value Proposition Design | Persona目标 -> VPD画布 -> Persona验证 |
| JTBD 研究整合 | JTBD Knowledge Skill | JTBD Jobs -> Persona细分映射 -> 角色文档 |
| 定量研究支撑 | Quantitative UX Research | UXR数据 -> Persona定量验证 -> 角色精化 |

---

## 七、最佳实践

| # | 原则 | 说明 |
|---|------|------|
| 1 | 永远基于真实数据 | 不编造角色，必须有研究数据支撑 |
| 2 | 聚焦目标而非人口统计 | 年龄/性别适合营销但不适合设计决策 |
| 3 | 角色数量控制在3-6个 | 太少覆盖不全，太多难以记忆 |
| 4 | 首要角色最多2个 | 保证设计决策有明确优先级 |
| 5 | 简介是叙述型自传 | 不用列表，讲故事才能让人记住 |
| 6 | 一页纸原则 | 角色文档控制在一页内，便于传播 |
| 7 | 持续维护角色活力 | 海报张贴、会议引用、定期数据更新 |
| 8 | 角色驱动全流程 | 从信息架构到视觉设计到测试，全程引用角色 |

## 八、经典案例

| 案例 | 行业 | 核心洞察 |
|------|------|---------|
| VistaPrint | 在线印刷 | 预言模型70%准确度识别高价值用户 |
| BrownCo | 金融经纪 | 通过角色做减法而非追赶巨头 |
| CNN.com | 新闻媒体 | 6个角色推广全公司，高层分发"我们不是目标用户"T恤 |
| Best Buy | 零售 | 角色指导零售店优化，目标客户消费额提升30% |
| Sony Boom Box | 消费电子 | 用户说想要黄色但都拿了黑色，证明言行不一 |

## 九、与其他 Skill 协作

Persona 是 AliDujie UX 研究技能生态系统的用户定义层，为其他技能提供用户视角：

| 协作场景 | 协作 Skill | 工作流 |
|---------|-----------|--------|
| 角色数据可视化 | [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | Persona 数据 → SWD 选图表 → SWD 构建故事 |
| 角色到价值主张 | [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | Persona 目标/痛点 → VPD 画布 → Persona 验证 |
| JTBD 研究整合 | [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD Jobs → Persona 细分映射 → Persona 文档 |
| 角色定量验证 | [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | UXR 数据 → Persona 定量验证 → Persona 精化 |
| 角色研究方法 | [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | UDM 访谈/观察 → Persona 数据收集 → Persona 创建 |
| 角色战略分析 | [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | STM 竞争分析 → Persona 市场定位 → STM 战略建议 |

**协作示例（UDM → Persona → SWD）**：
```python
# Step 1: UDM 收集用户研究数据
# Step 2: Persona 创建角色文档
from persona import PersonaSkill
skill = PersonaSkill("电商平台")
skill.add_persona("小明", "效率型用户", "primary", goals=["快速下单"])
print(skill.render_all_personas())
# Step 3: SWD 将角色数据可视化
from swd import SWDSkill
swd = SWDSkill("用户画像汇报")
ctx = swd.build_context(audience="产品团队", cta="按首要角色优化设计")
```

**协作示例（Persona → VPD）**：
```python
# Step 1: Persona 定义目标用户
from persona import PersonaSkill
persona = PersonaSkill("SaaS 平台")
persona.add_persona("团队负责人", "效率型", "primary",
    goals=["减少会议时间", "追踪项目进度"],
    pain_points=["信息分散在多个工具"])

# Step 2: VPD 基于 Persona 设计价值主张
from vpd import VPDSkill
vpd = VPDSkill("SaaS 协作平台", "团队负责人")
canvas = vpd.analyze_canvas(product_name="TeamFlow",
    jobs=[{"job": "减少会议时间", "importance": "高"}],
    pains=[{"pain": "信息分散", "severity": "高"}],
    gains=[{"gain": "一站式工作空间", "relevance": "高"}])
print(f"匹配度: {canvas.fit_score}")
```

### 🔀 完整端到端流程：Persona → JTBD → UDM → QuantUX → VPD → SWD

一个完整的从用户定义到数据叙事的管道示例：

```python
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

# 1. Persona — 定义"为谁设计"
persona = PersonaSkill("电商平台")
persona.add_persona(name="小明", archetype="效率型用户", priority="primary",
    goals=["快速下单"], behaviors=["频繁搜索"],
    bio="忙碌白领，时间就是金钱")
persona.add_persona(name="小红", archetype="探索型用户", priority="secondary",
    goals=["发现独特商品"], behaviors=["仔细比较"],
    bio="年轻设计师，喜欢淘好物")

# 2. JTBD — 发现用户想要完成的"工作"
jtbd = JTBDSkill("电商平台")
score = jtbd.score_opportunity("快速找到想要的商品", struggle=4, alternative=3, market=4, budget=4)

# 3. UDM — 定性研究验证
udm = UDMSkill("电商平台")
interview = udm.generate_interview("用户深访", "contextual", context="购物体验")

# 4. QuantUX — 定量验证
quantux = QuantUXSkill("电商平台")
heart = quantux.build_heart_framework()

# 5. VPD — 价值主张验证
vpd = VPDSkill("电商平台", "效率型用户")
canvas = vpd.analyze_canvas(product_name="电商平台",
    jobs=[{"description": "快速下单", "importance": 5}])

# 6. SWD — 向高管呈现
swd = SWDSkill("用户研究汇报")
story = swd.build_story(protagonist="产品委员会",
    imbalance="效率型用户流失率高", call_to_action="优化搜索和下单流程")
```

## 十、参考资料

| 书名 | 作者 | 说明 |
|------|------|------|
| **赢在用户 (The User Is Always Right)** | Steve Mulder & Ziv Yaar (2006) | 本 Skill 的理论基础 |
| About Face | Alan Cooper (2014) | 目标导向设计方法 |
| The Inmates Are Running the Asylum | Alan Cooper (1999) | Persona 概念的起源 |
| Storytelling with Data | Cole Nussbaumer Knaflic (2015) | 研究结果的数据可视化与叙事 |

### AliDujie 技能生态

Persona 是 **AliDujie UX 研究技能生态系统** 的用户定义层，为其他技能提供用户视角：

| 技能 | 定位 | 协作模式 |
|------|------|---------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 方法论核心 | UDM 访谈/观察 → Persona 数据收集 → 角色创建 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | 需求洞察 | JTBD 任务聚类 → Persona 角色定义 |
| [Quantitative UX Research](https://github.com/AliDujie/Quantitative-UX-Research) | 定量研究 | Persona 假设 → QuantUX 行为验证 → 角色迭代 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 价值验证 | Persona 目标/痛点 → VPD 画布 → Persona 验证 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 数据叙事 | Persona 数据 → SWD 可视化汇报 |
| [Structured Thinking Model](https://github.com/AliDujie/Structured-Thinking-Model) | 战略框架 | STM 竞争分析 → Persona 市场定位 |

### 🔗 扩展生态 (Extended Ecosystem)

Persona 用户定义可与管理层技能结合，将用户洞察转化为组织决策：

| 扩展技能 | 协作场景 |
|---------|----------|
| [CEO Advisor](https://github.com/AliDujie/ceo-advisor) | Persona 用户经济模型 → CEO 资源分配 |
| [CPO Advisor](https://github.com/AliDujie/cpo-advisor) | Persona 细分 → CPO 产品受众优先级 |
| [CMO Advisor](https://github.com/AliDujie/cmo-advisor) | Persona 角色 → CMO 目标受众定位与 messaging |
| [CTO Advisor](https://github.com/AliDujie/cto-advisor) | Persona 技术行为 → CTO 技术投资优先级 |
| [Plan CEO Review](https://github.com/AliDujie/plan-ceo-review) | Persona 季度更新 → CEO 计划审查 |

### 💡 Pro Tip / 专业技巧
Persona 是 AliDujie 生态系统的**用户定义层**，是所有研究的起点。推荐流程：先用 Persona 创建 2-3 个证据驱动的角色，再用 [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) 发现每个角色的 Jobs，用 [UDM](https://github.com/AliDujie/universal-design-methods) 设计研究方法，用 [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) 定量验证，用 [VPD](https://github.com/AliDujie/value-proposition-design) 映射价值主张，最后用 [SWD](https://github.com/AliDujie/storytelling-with-data) 向高管呈现。从角色定义到数据故事，6 个技能串联覆盖完整用户研究生命周期。

## ❓ FAQ / 常见问题

**Q: 我应该创建多少个角色？**
建议 3-6 个。少于 3 个意味着覆盖不够，超过 6 个团队记不住。首要角色最多 2 个——保证设计决策有明确优先级。

**Q: 怎么判断角色质量好不好？**
使用 `review_personas()` 运行 12 项质量检查，涵盖证据驱动性、区分度、可执行性、可记忆性等维度。分数 > 80/100 表示质量良好。

**Q: Persona 和 JTBD 有什么区别？**
Persona 回答"为谁设计"（用户是谁），JTBD 回答"要完成什么工作"（用户想要什么结果）。两者互补：先定义角色，再发现角色的 Jobs。

**Q: 可以用分析数据创建角色吗？**
可以。从行为数据（访问频率、功能使用率）开始，再用 [UDM](https://github.com/AliDujie/universal-design-methods) 访谈补充定性洞察。`SegmentAnalyzer` 支持基于目标/行为/态度的细分，直接映射到分析数据群组。
