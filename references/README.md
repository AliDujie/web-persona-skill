# References 知识库索引

## 使用指南

**从哪里开始？** → 看 `core/` 目录。8 篇文档按执行阶段组织，从立项到应用全覆盖。

**想深入某个话题？** → 看 `advanced/` 目录。39 篇方法论参考，按需查阅。

---

## core/ — 核心操作手册

| # | 文件 | 内容 | 适合场景 |
|---|------|------|---------|
| 01 | project-setup | 该不该做 + 选方法 + 组团队 + 全员参与 | 项目启动前 |
| 02 | qualitative-research | 深度访谈 + 现场观察全流程 | 定性路径执行 |
| 03 | quantitative-research | 问卷设计 + 统计聚类全流程 | 定量路径执行 |
| 04 | mixed-method | 定性→定量→定性深化的衔接 | 混合路径执行 |
| 05 | analysis-clustering | 行为变量 + 亲和图 + 统计聚类 | 数据分析阶段 |
| 06 | persona-creation | 命名 + 叙事技巧 + 优先级 | 从分群到人物 |
| 07 | validation | 内部审视 + 外部验证 + 持续追踪 | 确保 Persona 站得住 |
| 08 | application | 六种应用场景 + 推广 + 保鲜 + 度量 | 做完 Persona 之后 |

---

## advanced/ — 进阶参考字典

按需查阅。每篇核心文档末尾都标注了"想深入了解→查阅 advanced/XX"。

### Mulder 系列（01-05）

| # | 文件 | 内容 |
|---|------|------|
| 01 | persona-basics | Persona 基础概念与创建方法 |
| 02 | measuring-results | Persona 效果衡量 |
| 03 | persona-best-practices | 最佳实践与常见误区 |
| 04 | persona-driven-workflows | Persona 驱动的工作流 |
| 05 | ecosystem-collaboration | 生态系统协作 |

### 经典书系（06-15）

| # | 文件 | 经典来源 |
|---|------|---------|
| 06 | cooper-goal-directed-design | Cooper《About Face》Goal-Directed Design |
| 07 | persona-lifecycle | Pruitt & Adlin《Persona Lifecycle》 |
| 08 | goodwin-digital-age | Goodwin《Designing for the Digital Age》 |
| 09 | indi-young-mental-models | Indi Young《Mental Models》 |
| 10 | lene-nielsen-10steps | Nielsen《Personas - User Focused Design》 |
| 11 | lean-ux-proto-personas | Gothelf《Lean UX》Proto-Persona |
| 12 | just-enough-research | Erika Hall《Just Enough Research》 |
| 13 | user-story-mapping | Jeff Patton《User Story Mapping》 |
| 14 | norman-mental-conceptual-models | Don Norman《Design of Everyday Things》 |
| 15 | personas-critique-and-defense | Persona 的批判与防御 |

### ABCD 深化（16-27）

| # | 文件 | 方向 |
|---|------|------|
| 16 | mikkelson-statistical | A · 统计 Persona |
| 17 | revella-buyer | A · B2B Buyer Personas |
| 18 | synthetic-ai | A · AI 合成 Personas |
| 19 | service-design | A · 服务设计 Personas |
| 20 | kahneman-dual-system | B · 认知偏差与双系统 |
| 21 | fogg-behavior | B · 行为设计模型 |
| 22 | jtbd-persona-integration | B · JTBD-Persona 整合 |
| 23 | thick-data-ethnography | B · 厚数据与民族志 |
| 24 | kat-holmes-mismatch | C · 包容性设计 |
| 25 | cababa-systems-second-order | C · 系统思维与二阶后果 |
| 26 | hofstede-cross-cultural | C · 跨文化设计 |
| 27 | bias-audit-personas | C · 偏见审查 |

### 工程化配套（28-31）

| # | 文件 | 配套代码 |
|---|------|---------|
| 28 | clustering-engineering | → `persona/clustering.py` |
| 29 | llm-prompt-library | → `persona/llm_prompts.py` |
| 30 | okr-roadmap-bridge | → `persona/okr_bridge.py` |
| 31 | measurement-toolkit | → `persona/measurement_toolkit.py` |

### 上游研究 + 体验地图（32-39）

| # | 文件 | 经典来源 |
|---|------|---------|
| 32 | portigal-interviewing-users | Portigal《Interviewing Users》 |
| 33 | fitzpatrick-mom-test | Fitzpatrick《The Mom Test》 |
| 34 | torres-continuous-discovery | Torres《Continuous Discovery Habits》 |
| 35 | alvarez-lean-customer-development | Alvarez《Lean Customer Development》 |
| 36 | kalbach-mapping-experiences | Kalbach《Mapping Experiences》 |
| 37 | quesenbery-storytelling-ux | Quesenbery《Storytelling for UX》 |
| 38 | kuniavsky-observing-user-experience | Kuniavsky《Observing the User Experience》 |
| 39 | christensen-competing-against-luck | Christensen《Competing Against Luck》 |

---

## 🌐 技能生态关联 / Skill Ecosystem Connections

Persona 是 AliDujie UX 研究生态的起点——先回答"为谁做"，再深入"做什么"和"怎么做"：

- **Persona → JTBD**: Persona 的角色行为分群 → JTBD 按角色进行机会评分
- **Persona → UDM**: Persona 的用户画像 → UDM 为不同角色选择研究方法
- **Persona → QuantUX**: Persona 的关键行为 → QuantUX 按分群验证数据指标
- **Persona → VPD**: Persona 的目标/痛点 → VPD 映射到价值主张画布
- **Persona → SWD**: Persona 的经济数据 → SWD 制作角色画像可视化叙事
- **Persona → STM**: Persona 的战略洞察 → [STM](https://github.com/AliDujie/Structured-Thinking-Model) 结构化战略分析

> 💡 **完整生态链**: Persona (用户定义) → JTBD (深层需求) → UDM (方法引擎) → VPD (价值设计) → QuantUX (数据验证) → SWD (数据叙事) → [STM](https://github.com/AliDujie/Structured-Thinking-Model) (战略决策)
