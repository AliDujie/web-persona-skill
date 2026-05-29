# References / 参考文档

本目录存放 Web Persona 技能的方法论参考文档。

This directory contains methodology reference documents for the Web Persona skill.

## 目录结构 / Directory Structure

### 一、原版方法论（Mulder 派 — 本技能默认）

| 文件 | 内容 |
|------|------|
| `01-persona-basics.md` | 人物角色基础（定义、类型、创建方法） |
| `02-measuring-results.md` | 衡量人物角色效果（指标、验证方法、ROI） |
| `03-persona-best-practices.md` | 人物角色最佳实践（常见陷阱、成功模式） |
| `04-persona-driven-workflows.md` | Persona 驱动的研究工作流（跨技能协作指南） |
| `05-ecosystem-collaboration.md` | 跨技能协作指南（Persona → JTBD/UDM/QuantUX/VPD/SWD） |

### 二、扩展方法论（多书系融合 v2.5.0+）

#### Tier 1 · 方法论根基（必读）

| 文件 | 内容 | 来源 |
|------|------|------|
| `06-cooper-goal-directed-design.md` | Goal-Directed Design / 六类角色 / 三联式场景 | Alan Cooper《About Face 4》《Inmates》 |
| `07-persona-lifecycle.md` | 五阶段生命周期 / Foundation Document / 7 类反模式 | Pruitt & Adlin《The Persona Lifecycle》 |
| `08-goodwin-digital-age.md` | 七阶段项目框架 / 五模型并用 / Persona Skeleton | Kim Goodwin《Designing for the Digital Age》 |

#### Tier 2 · 现代方法对照（强力补充）

| 文件 | 内容 | 来源 |
|------|------|------|
| `09-indi-young-mental-models.md` | Mental Model Diagram / Thinking Style Segments / 反人口学 | Indi Young《Mental Models》《Practical Empathy》 |
| `10-lene-nielsen-10steps.md` | 四视角分类 / 十步法 / 叙事五要素 / 包容性设计 | Lene Nielsen《Personas - User Focused Design》|
| `11-lean-ux-proto-personas.md` | Proto-Persona / 假设句式 / MVE 实验类型 | Gothelf & Seiden《Lean UX》|

#### Tier 3 · 延伸视角（特定场景）

| 文件 | 内容 | 来源 |
|------|------|------|
| `12-just-enough-research.md` | 五类研究问题 / Saturation 判断 / 反 Research Theater | Erika Hall《Just Enough Research》|
| `13-user-story-mapping.md` | Story Map 三层结构 / Now/Later Map / 多边泳道 | Jeff Patton《User Story Mapping》|
| `14-norman-mental-conceptual-models.md` | 三模型框架 / 七步行动 / 七大设计原则 | Don Norman《DOET》 |
| `15-personas-critique-and-defense.md` | Chapman 五大批评 / 19 项防御评审 / Persona Spectrum | Chapman & Milham + 微软包容性设计 |

---

## 使用方法 / Usage

### 默认路径（90% 场景）
直接遵循 `01-05` 即可，这是本技能的核心 Mulder 方法论。

### 当遇到以下情况时，按需查阅扩展方法论：

| 情境 | 优先查阅 |
|------|---------|
| 创建复杂企业软件、设计驱动产品 | `06-cooper` + `08-goodwin` |
| 大型组织、多团队协作、Persona 治理 | `07-persona-lifecycle` |
| 需要去人口学分群、思维风格分群 | `09-indi-young` |
| 学术严谨度、伦理审查、叙事化角色 | `10-lene-nielsen` |
| 创业早期、无调研预算、快速假设验证 | `11-lean-ux` |
| 时间紧、决策驱动、反对过度研究 | `12-just-enough` |
| 多边平台、发布切片规划 | `13-user-story-mapping` |
| 团队需要理论根基、设计评审 | `14-norman` |
| 抵御 Persona 反模式、需要批判视角 | `15-critique-and-defense` |

详细决策路径见 `SKILL.md` 中的"方法论谱系（Methodology Lineage）"和"方法选择决策树"。

---

## 🌐 技能生态关联 / Skill Ecosystem Connections

Persona 是用户研究的起点，为其他技能提供角色锚点：

- **UDM → Persona**: UDM 的观察/访谈方法 → Persona 的角色研究数据收集
- **JTBD → Persona**: JTBD 的切换行为 → Persona 补充基于行为的细分维度
- **Persona → VPD**: Persona 的角色目标/痛点 → VPD 价值主张画布输入
- **Persona → QuantUX**: Persona 的角色假设 → QuantUX 行为数据验证和角色精化
- **Persona → SWD**: Persona 的角色档案 → SWD 进行可视化角色卡片制作

---

## 来源 / Sources

### 主体方法论
- Steve Mulder & Ziv Yaar.《The User Is Always Right: A Practical Guide to Creating and Using Personas for the Web》New Riders, 2007.

### 扩展方法论（v2.5.0+ 新增）
- Alan Cooper, Robert Reimann, David Cronin, Christopher Noessel.《About Face: The Essentials of Interaction Design》(4th ed.) Wiley, 2014.
- Alan Cooper.《The Inmates Are Running the Asylum》Sams, 1999/2004.
- John Pruitt & Tamara Adlin.《The Persona Lifecycle: Keeping People in Mind Throughout Product Design》Morgan Kaufmann, 2006.
- Kim Goodwin.《Designing for the Digital Age: How to Create Human-Centered Products and Services》Wiley, 2009.
- Indi Young.《Mental Models: Aligning Design Strategy with Human Behavior》Rosenfeld Media, 2008.
- Indi Young.《Practical Empathy: For Collaboration and Creativity in Your Work》Rosenfeld Media, 2015.
- Lene Nielsen.《Personas - User Focused Design》(2nd ed.) Springer, 2019.
- Jeff Gothelf & Josh Seiden.《Lean UX》(2nd ed.) O'Reilly, 2016.
- Erika Hall.《Just Enough Research》(2nd ed.) A Book Apart, 2019.
- Jeff Patton.《User Story Mapping: Discover the Whole Story, Build the Right Product》O'Reilly, 2014.
- Don Norman.《The Design of Everyday Things》(rev. ed.) Basic Books, 2013.
- Chapman, C. N., & Milham, R. P.《The Personas' New Clothes: Methodological and Practical Arguments against a Popular Method》HFES Annual Meeting Proceedings, 2006.
- Microsoft Design Team.《Inclusive Design: A Microsoft Design Toolkit》(Persona Spectrum), 2016.
