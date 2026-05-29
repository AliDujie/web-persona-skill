---
name: web-persona-skill
version: "3.1.0"
description: "Persona 全流程执行 Skill。给定输入（访谈稿/问卷数据/业务描述），直接产出 Persona 卡片、行为分群、访谈提纲、问卷、验证方案、应用矩阵等交付物。不是教程——是执行器。"
author: "渡劫"
---

# Web Persona Skill — 执行指令

> 本文件是 agent 执行手册。收到用户请求后，匹配触发条件 → 执行对应任务 → 产出交付物。

---

## 触发路由

根据用户输入匹配任务：

| 用户输入/意图 | 执行任务 | 协议文件 |
|---|---|---|
| "帮我做 Persona" / "我要做用户画像" / 给出产品描述 | **T1 立项** → 推荐方法 + 生成计划 | `core/01-project-plan.md` |
| "帮我设计访谈" / "我要做用户访谈" | **T2 访谈设计** → 直接输出访谈提纲 | `core/02-interview-design.md` |
| 提供访谈文字稿/笔记 | **T3 定性分析** → 提取行为变量 → 聚类 → 输出分群 | `core/03-qualitative-analysis.md` |
| "帮我设计问卷" / 给出调研维度 | **T4 问卷设计** → 直接输出完整问卷 | `core/04-survey-design.md` |
| 提供问卷/埋点/CRM 数据（CSV/表格） | **T5 定量分析** → 跑聚类 → 输出统计分群 | `core/05-quantitative-analysis.md` |
| "写 Persona" / 已有分群结果 | **T6 Persona 生成** → 输出完整角色卡 | `core/06-persona-generation.md` |
| "验证 Persona" / 已有 Persona 需审查 | **T7 验证** → 输出验证方案 + 执行审查 | `core/07-validation.md` |
| "Persona 怎么用" / 需要落地方案 | **T8 应用** → 输出优先级矩阵/OKR/度量方案 | `core/08-application.md` |
| 同时有访谈稿 + 定量数据 | **T3+T5 混合分析** → 定性+定量交叉 → 输出 | 按顺序执行 T3 → T5 → T6 |

**快捷路径**：用户直接丢访谈稿或数据 → 跳过 T1/T2，直接进入 T3 或 T5 → 自动衔接 T6 输出 Persona。

---

## 执行原则

1. **输入即执行** — 用户给了数据就开始干活，不要反复确认"要不要帮你做"
2. **缺什么问什么** — 只问执行必须的信息（产品是什么、目标用户大致范围），不问教科书式的准备清单
3. **直接给交付物** — 输出是可直接使用的文档/卡片/代码结果，不是"建议你这样做"
4. **每步有明确产出** — 每个任务结束都要产出具体文件/结构化内容
5. **自动衔接** — 如果上一步的输出是下一步的输入，自动继续（除非用户叫停）

---

## 任务 T1-T8 概览

### T1 · 立项规划
- **输入**：产品/业务描述
- **执行**：评估是否适合做 Persona → 推荐方法路径 → 输出项目计划
- **产出**：方法推荐 + 时间线 + 团队配置建议 + 下一步 action

### T2 · 访谈设计
- **输入**：产品背景 + 研究目标（可选）
- **执行**：生成完整访谈提纲（开场→核心→追问→收尾）
- **产出**：可直接使用的访谈指南文档（含具体问题 + 追问提示 + 时间分配）

### T3 · 定性分析
- **输入**：访谈文字稿 / 笔记 / 用户反馈文本
- **执行**：提取行为片段 → 识别行为变量 → 亲和归类 → 形成分群
- **产出**：行为变量清单 + 分群方案（每群特征描述）+ 自动衔接 T6

### T4 · 问卷设计
- **输入**：行为维度 / 研究目标 / T3 的行为变量清单
- **执行**：生成完整问卷（筛选→行为→决策→态度→人口统计）
- **产出**：可直接使用的问卷文档（含题目+选项+量表+逻辑跳转）

### T5 · 定量分析
- **输入**：CSV/Excel 数据文件
- **执行**：数据预处理 → 调用 clustering.py → 确定最优 K → 稳定性检验
- **产出**：聚类结果（每簇特征+占比+关键差异）+ 自动衔接 T6

### T6 · Persona 生成
- **输入**：T3 或 T5 的分群结果（或用户手动提供的分群描述）
- **执行**：为每个群生成完整 Persona 卡片（名字+引语+场景叙事+目标+行为+痛点+启示）
- **产出**：3-5 个完整 Persona 卡片 + 优先级建议

### T7 · 验证
- **输入**：已有 Persona 文档
- **执行**：多维度审查（数据支撑/行为区分度/命名偏见/覆盖度）→ 生成验证方案
- **产出**：审查报告 + 验证访谈提纲 + 健康检查清单

### T8 · 应用落地
- **输入**：已有 Persona + 产品 backlog / 业务目标
- **执行**：生成应用交付物
- **产出**：功能优先级矩阵 / Persona-OKR 映射 / 设计评审 checklist / 度量方案

---

## Python 工具调用

```python
# T5 定量聚类
from persona.clustering import PersonaClusterer
result = PersonaClusterer(method="auto").fit(df, n_clusters_range=(3, 7))

# T6/T7 LLM 辅助
from persona.llm_prompts import PersonaPromptLibrary
lib = PersonaPromptLibrary()
prompt = lib.simulated_interview(profile, task="验证假设", questions=[...])

# T8 OKR 桥接
from persona.okr_bridge import OKRBridge
plan = OKRBridge().derive_okrs(persona_profiles)

# T8 度量
from persona.measurement_toolkit import MeasurementToolkit
tk = MeasurementToolkit(product="你的产品")
```

---

## 输出格式规范

### Persona 卡片标准格式（T6 产出）

```markdown
## [标签] · [名字]

> "[核心引语——一句能代表这个人的原话]"

**一句话**：[用一句话概括这个人的核心特征]

### 场景故事
[150-200字的具体场景叙事——某天某时某地，TA做了什么，为什么，遇到什么困难]

### 核心目标
- [目标1]
- [目标2]

### 关键行为
- [行为1]
- [行为2]
- [行为3]

### 痛点
- [痛点1]
- [痛点2]

### 对产品的启示
- 应该：[...]
- 不应该：[...]

### 元数据
- 优先级：Primary / Secondary / Supplemental
- 市场占比：约 X%（如有定量数据）
- 数据来源：[访谈/问卷/行为数据]
```

### 分群结果格式（T3/T5 产出）

```markdown
## 分群结果

### 群 1：[2-4字行为标签]（占比 X%）
- **核心行为**：[...]
- **与其他群的关键差异**：[...]
- **典型用户**：[简述]

### 群 2：...
```

---

## 知识库

执行过程中如需方法论深度支撑，查阅 `references/advanced/`：

| 需要 | 查阅 |
|------|------|
| Cooper 行为变量框架 | `advanced/06-cooper-goal-directed-design.md` |
| 统计聚类方法论 | `advanced/16-mikkelson-statistical-personas.md` |
| 访谈技巧深度 | `advanced/32-portigal-interviewing-users.md` |
| 认知偏差规避 | `advanced/20-kahneman-dual-system.md` |
| 偏见审查 | `advanced/27-bias-audit-personas.md` |
| 包容性设计 | `advanced/24-kat-holmes-mismatch.md` |
| B2B Buyer Persona | `advanced/17-revella-buyer-personas.md` |
| JTBD 整合 | `advanced/22-jtbd-persona-integration.md` |

完整 39 篇索引见 `references/README.md`。
