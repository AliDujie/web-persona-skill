---
name: web-persona-skill
version: "3.3.6"
description: "Persona 全流程执行 Skill（T1-T10）。给定输入（访谈稿/问卷数据/业务描述），直接产出 Persona 卡片、行为分群、访谈提纲、问卷、验证方案、应用矩阵、可用性测试脚本、旅程地图等交付物。每个任务带 Pitfalls + Verification 双闭环 + 全局 Guardrails。不是教程——是可审计的执行器。"
author: "渡劫"
---

# Web Persona Skill — 执行指令

> 本文件是 agent 执行手册。收到用户请求后，匹配触发条件 → 执行对应任务 → 产出交付物。

---

## 触发路由

根据用户输入匹配任务：

| 用户输入/意图 | 执行任务 | 协议文件 |
|---|---|---|
| "帮我做 Persona" / "我要做用户画像" / 给出产品描述 | **T1 立项** → 数据审计 + 推荐方法 + 生成计划 | `core/01-project-plan.md` |
| "帮我设计访谈" / "我要做用户访谈" | **T2 访谈设计** → 直接输出访谈提纲 + 追问工具箱 | `core/02-interview-design.md` |
| 提供访谈文字稿/笔记 | **T3 定性分析** → 提取行为变量 → 聚类 → 输出分群 | `core/03-qualitative-analysis.md` |
| "帮我设计问卷" / 给出调研维度 | **T4 问卷设计** → 直接输出完整问卷 | `core/04-survey-design.md` |
| 提供问卷/埋点/CRM 数据（CSV/表格） | **T5 定量分析** → 聚类 + 分类评分规则 | `core/05-quantitative-analysis.md` |
| "写 Persona" / 已有分群结果 | **T6 Persona 生成** → 角色卡 + 使用场景 | `core/06-persona-generation.md` |
| "验证 Persona" / 已有 Persona 需审查 | **T7 验证** → 偏差审计 + 内容审查 + 验证方案 | `core/07-validation.md` |
| "Persona 怎么用" / "按 Persona 看数据" | **T8 应用** → 优先级/OKR/度量/分列分析 | `core/08-application.md` |
| "帮我设计可用性测试" / "做用户测试" | **T9 测试设计** → 招募筛选器 + 测试脚本 | `core/09-usability-test-design.md` |
| "帮我做旅程地图" / "Journey Map" | **T10 旅程地图** → 阶段拆解 + 情绪曲线 + 机会点 | `core/10-journey-map.md` |
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

## 全局 Guardrails（v3.3 新增，借鉴 deep-research-iterative）

每个任务在 LLM 自循环时遵守以下硬上限——防止失控、Token 浪费、自我钻牛角尖。

| 任务 | 循环类型 | 硬上限 | 早停规则 |
|------|---------|-------|---------|
| T2 | 单次访谈中追问轮数 | 8 轮/题 | 同一题连续 2 轮无新信息 → 切下一题 |
| T3 | 编码迭代（提取↔变量↔饱和度） | 3 轮 | 连续 2 轮新增变量 < 1 → 强制 `<done>` |
| T3 | 段落预筛 Yes/No | 不限轮数 | Yes 段落直接进 Step 1；No 段落丢弃 |
| T5 | K 值扫描 | K=3-7 | 轮廓 > 0.5 + 簇均衡 → 直接选用；连续两 K 变化 < 0.02 → 早停 |
| T7 | 审查 ↔ 修改 ↔ 复审 | 3 轮 | 连续 2 轮无新增问题 → 强制结束 |
| T9 | 测试脚本细化 | 不需循环 | 一次性产出，不做迭代 |

**通用兜底**（所有任务）：
- 如 LLM 连续 2 次返回相同/极相似产出 → 视为已收敛，强制 `<done>`
- 任何 JSON 解析失败 → 重试 1 次 + 更严格的系统提示；2 次失败 → 用当前已有内容收尾，不再继续
- 输出报告底部强制添加运行元信息：`_循环轮数: X/Y. 输入样本: N. 产出条目: M._`

---

## 任务 T1-T10 概览

### T1 · 立项规划
- **输入**：产品/业务描述
- **执行**：现有数据审计 → 评估方法路径 → 输出项目计划
- **产出**：数据审计结果 + 方法推荐 + 时间线 + 下一步 action
- **v3.2 新增**：Step 2 现有数据审计（先挖掘已有数据再决定做什么研究）

### T2 · 访谈设计
- **输入**：产品背景 + 研究目标（可选）
- **执行**：生成完整访谈提纲 + 追问与防引导工具箱
- **产出**：访谈指南（含问题+追问提示+时间分配）+ Portigal 六种追问技术 + Mom Test 三原则 + 危险信号检测表
- **v3.2 新增**：Step 3 追问工具箱（Portigal 回响/沉默/例外探测 + Mom Test 防引导三原则 + 引导性问题危险信号）

### T3 · 定性分析
- **输入**：访谈文字稿 / 笔记 / 用户反馈文本
- **执行**：提取行为片段 → 识别行为变量 → 亲和归类 → 形成分群
- **产出**：行为变量清单 + 分群方案 + 自动衔接 T6

### T4 · 问卷设计
- **输入**：行为维度 / 研究目标 / T3 的行为变量清单
- **执行**：生成完整问卷（筛选→行为→决策→态度→人口统计）
- **产出**：可直接使用的问卷文档（含题目+选项+量表+逻辑跳转）

### T5 · 定量分析
- **输入**：CSV/Excel 数据文件
- **执行**：数据预处理 → 聚类 → 确定最优 K → 稳定性检验 → 生成分类评分规则
- **产出**：聚类结果 + **可部署的分类评分规则**（决策树 + 评分卡）+ 自动衔接 T6
- **v3.2 新增**：Step 6 分类评分规则 / Predictive Model（决策树规则+准确率+评分卡+实施建议）

### T6 · Persona 生成
- **输入**：T3 或 T5 的分群结果
- **执行**：为每个群生成 Persona 卡片 + 2-3 个完整使用场景
- **产出**：3-5 个 Persona 卡片 + 优先级 + **独立使用场景文档**
- **v3.2 新增**：Step 3 完整使用场景（300-500字/个，含行为流+决策点+失败模式，覆盖核心/极端/首次三类场景）

### T7 · 验证
- **输入**：已有 Persona 文档
- **执行**：认知偏差审计 → 多维度内容审查 → 验证方案
- **产出**：偏差审计报告 + 审查报告 + Pre-mortem + 验证方案
- **v3.2 新增**：Step 1 认知偏差自检（Kahneman 双系统 6 偏差检测 + 4 慢思维审计 + Pre-mortem）

### T8 · 应用落地
- **输入**：已有 Persona + 产品 backlog / 业务目标 / 数据
- **执行**：生成应用交付物（含 Persona 分列数据分析）
- **产出**：功能优先级矩阵 / OKR 映射 / 设计评审 checklist / 度量方案 / **Persona 分列分析报告**
- **v3.2 新增**：模板 F Persona 分列数据分析（用户→Persona 映射 + 分列指标表 + 归因分析 + 长期追踪建议）

### T9 · 可用性测试设计 ⭐ NEW
- **输入**：Persona + 要测试的产品/原型
- **执行**：生成参与者筛选器 + 测试脚本 + 观察清单
- **产出**：招募方案（筛选条件+样本量+渠道）+ 每 Persona 独立测试脚本（场景任务+观察要点+追问）+ 问题优先级评分框架

### T10 · 旅程地图 ⭐ NEW
- **输入**：Persona + 使用场景
- **执行**：扩展为 Journey Map（阶段→维度→情绪曲线→前后台对照）
- **产出**：每 Persona 完整 Journey Map + 关键时刻排序 + 改进机会优先级 + 跨 Persona 对比

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
| Fogg 行为干预 | `advanced/21-fogg-behavior-model.md` |
| 旅程地图方法 | `advanced/19-service-design-personas.md` |

完整 39 篇索引见 `references/README.md`。

---

## Tool Mapping（host-agent agnostic · v3.3 新增）

每个能力声明 Preferred 和 Fallback——任何 host agent（Claude Code / QoderWork / Cursor / 通用 OpenAI tool-calling agent / 纯对话场景）都能用这个 skill。

| 能力 | Preferred | Fallback |
|------|----------|---------|
| 行为分群（数值数据） | `persona/clustering.py` + sklearn KMeans | LLM 启发式分群（N ≤ 30 时） |
| 高级聚类（潜类别 LCA） | `persona/clustering.py` + stepmix | 降级 KMeans + 后验解读 |
| 稳定性检验 | clustering.py 内置 bootstrap_n=20 | 跳过稳定性，用 K-1/K+1 双结果对比代替 |
| LLM Prompt 库 | `persona/llm_prompts.py` + 任意 LLM SDK | 直接内联本文件中的 prompt 模板 |
| OKR 桥接 | `persona/okr_bridge.py` 自动派生 | 用 T8 模板 B 手填 |
| 度量套件 | `persona/measurement_toolkit.py` + 实时数据流 | 用 T8 模板 D + 模板 F 手填 |
| 数据读取 | pandas read_csv/read_excel | LLM 直接从用户贴入的表格文本解析 |
| 文档输入 | host 的 file API | 用户复制粘贴文本到对话 |

**Python 依赖最小集**（仅 T5/T8 工程化路径需要）：
- 必须：`pandas`, `numpy`
- 推荐：`scikit-learn>=1.3`
- 可选：`stepmix`（LCA），`scipy`（统计检验）

**纯对话 fallback**：所有 T1-T10 任务在无 Python 环境下，仅通过 LLM 推理和模板化产出仍可运行——只是 T5 的统计准确性下降（启发式分群代替 KMeans）。

---

## 元信息脚（产出报告必含 · v3.3 新增）

借鉴 deep-research-iterative 的产出元信息惯例。每个 T 任务产出报告末尾都强制添加一行：

```
---
_任务: T[N] · [任务名]. 循环轮数: [X]/[上限]. 输入: [样本量]. 产出: [条目数]. 工具: [Preferred/Fallback]._
```

例如：
```
---
_任务: T3 · 定性分析. 循环轮数: 2/3. 输入: 12 份访谈/108 段落. 产出: 9 个行为变量 / 4 个分群. 工具: LLM only._
```

让用户/审计者一眼看出任务是否健康运行（轮数是否撞上限、是否触发 fallback）。
