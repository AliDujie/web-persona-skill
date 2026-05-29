# 15 · Persona 批评与防御 (Critique & Defense)

> 来源：Christopher N. Chapman & Russell P. Milham《The Personas' New Clothes: Methodological and Practical Arguments against a Popular Method》(HFES 2006 Annual Meeting Proceedings) + 后续多篇学术批评 + Microsoft Inclusive Design《Persona Spectrum》框架。
>
> 本笔记汇总学界对 Persona 方法的核心批评，并给出防御性整合策略。任何成熟用研专家都应了解方法论的局限性。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 为什么需要这一章

Mulder/Cooper/Goodwin 派均高度推崇 Persona，但学术界从 2006 年起持续批评。一个真正成熟的 Persona 实践应：
- **承认局限**：知道 Persona 不能解决什么
- **预设防御**：在创建时就规避已知陷阱
- **保留备选**：当 Persona 失败时，知道该用什么替代

> 💡 **关键立场**：批评不是反对 Persona，而是抵御对 Persona 的过度依赖。

---

## 2. Chapman & Milham 五大批评

### 2.1 No Proven Validity（无验证效度）
- Persona 缺乏统计学意义上的"代表性"证明
- 无法验证一个 Persona 是否真的"代表"某个用户群
- 多元用户的多维分布**无法**被 3-5 个角色精确代表

### 2.2 Easy to Fabricate（容易伪造）
- Persona 的"创作"性质让数据缺失易被叙事填补
- 团队成员的偏见会被嵌入"事实"中
- 无法区分"基于研究的角色"与"投射的角色"

### 2.3 Confused with Archetypes / Stereotypes（与原型/刻板印象混淆）
- 用户难以区分"角色描述"与"刻板印象"
- 经过几次会议，Persona 容易退化为简化标签

### 2.4 Multivariate Distribution Issue（多元分布问题）
- 用户在多维度上的分布是连续的、复杂的
- 用 3-5 个"点"代表整个分布，遗漏 95% 的变异
- 边缘用户被系统性忽略

### 2.5 Lack of Falsifiability（不可证伪）
- Persona 的描述太模糊，几乎任何观察都可被解读为"符合"
- 无法定义"什么样的证据会推翻这个 Persona"

---

## 3. 实践中的常见 Persona 病症

学界与业界总结的具体病症：

| 病症 | 症状 | 根本原因 |
|---|---|---|
| **Stereotyping**（刻板化） | "足球妈妈""硅谷男"——人口学标签替代行为 | 偷懒，用文化套路代替研究 |
| **False Precision**（虚假精确） | "Alex 27.3 岁，月收入 ¥18,500"——精确但无意义 | 误把数字当严谨 |
| **Confirmation Bias**（确认偏见） | 数据筛选只为印证已有 Persona | 创建时就有结论 |
| **Sunk Cost / Zombie Persona**（沉没成本/僵尸角色） | 已过时却仍在引用 | 没人愿意承认初始投入浪费 |
| **Decoration Persona**（装饰性角色） | 在墙上但不进决策流程 | 缺乏 Birth & Maturation 治理 |
| **Persona Inflation**（角色膨胀） | 角色越加越多，最后 12 个 | 团队怕"漏掉"任何用户 |
| **One-shot Persona**（一次性角色） | 创建后再不更新 | 缺乏 Lifecycle 退役机制 |
| **Cargo Cult Persona**（货物崇拜） | 模仿大公司格式但无内部验证 | 形式主义 |

---

## 4. 防御性整合策略

### 4.1 数据透明化
- 每个角色字段标注数据来源（访谈编号、问卷题号、分析图表）
- 公开 factoid pile（事实卡片堆），团队可追溯每条描述
- 引入 Pruitt-Adlin 的 Foundation Document 流程

### 4.2 显式假设标记
- 每个未验证字段标 `[假设]`
- 已验证字段标 `[已验证-YYYY-MM-DD-数据来源]`
- 见 `11-lean-ux-proto-personas.md`

### 4.3 边缘 Persona 检查
- 故意创建 1-2 个 **Edge Persona**（边缘角色）
- 即使不为他们设计，也用作"如果照顾到他们，主流角色一定也满足"的完整性检查
- 见 Microsoft Inclusive Design "Persona Spectrum"

### 4.4 多视角并用
- Persona（行为分群）+ Mental Model（认知地图）+ JTBD（任务清单）
- 三视角交叉验证，避免单一视角偏见
- 不一致处即未知机会

### 4.5 强制退役机制
- 设定 12-18 个月强制复审
- 数据漂移 > 30% 触发更新
- 业务方向转型触发重建

### 4.6 可证伪性条款
- 每个 Persona 显式声明："以下数据出现时，本角色失效"
- 例：转化漏斗中该角色占比 < 10% 持续 3 个月

---

## 5. Persona Spectrum（角色光谱）— 微软包容性设计

替代单一 Persona 的现代框架：

```
能力差异不是二元的，而是连续光谱：

视觉                                       移动
─────────────────────────────────►      ─────────────────────────────────►
Permanent      Temporary    Situational    Permanent      Temporary    Situational
全盲           眼疾恢复     强光下          单臂           受伤         手抱孩子
```

### 5.1 三类能力差异
- **Permanent**（永久性）：全盲、单臂、聋
- **Temporary**（临时性）：眼疾、骨折、耳道感染
- **Situational**（情境性）：强光、抱孩子、嘈杂环境

### 5.2 设计含义
- 为永久残障设计的功能，自然惠及临时与情境性需求
- 大幅扩展用户基数（如语音输入解决"全盲 + 抱孩子开车 + 受伤"三类）
- 替代传统 Persona 中"主流角色 + 1 个 accessibility 角色"的二元结构

> 💡 **整合建议**：在传统 Persona 集合上叠加 Persona Spectrum 维度——每个角色额外回答"这个角色在哪些能力维度上有局限？"

---

## 6. 何时 Persona 不适用——替代方案地图

| Persona 失效情境 | 替代方案 |
|---|---|
| 用户类型极度同质（如内部工具） | **Job Story** / **Use Case** |
| 单一目标驱动（如只做支付） | **User Journey Map** |
| B2B 复杂决策链 | **Buying Committee Map**（采购委员会图） |
| 平台型多边市场 | **Multi-sided Persona Lanes**（见 `13-user-story-mapping.md`） |
| 行为差异极大、无法聚类 | **Mental Model Diagram**（见 `09-indi-young-mental-models.md`） |
| 决策驱动而非行为驱动 | **Thinking Style Segments** |
| 探索阶段无数据 | **Proto-Persona** + 假设清单（见 `11-lean-ux-proto-personas.md`） |
| 学术研究/伦理敏感 | **Ad-Hoc Persona** + 包容性检查 |

---

## 7. 防御性 Persona Review Checklist（19 项）

在原有 12 项基础上扩展为 19 项防御性评审：

```
□  1. 是否有数据来源标注？
□  2. 是否标记[假设]/[已验证]状态？
□  3. 是否避免使用人口学作为分群依据？
□  4. 是否避免刻板印象（stereotype）？
□  5. 是否包含痛点和能力局限？
□  6. 是否能与 1-2 个其他角色明确区分？
□  7. 是否有清晰的优先级（Primary/Secondary/Negative）？
□  8. 是否有 Experience/End/Life 三层目标？
□  9. 是否绑定具体场景（Context Scenario）？
□ 10. 是否描述与产品的关系（Awareness/Consider/Use/Advocate）？
□ 11. 是否能驱动至少一个具体设计决策？
□ 12. 是否有"被检验为错"的可证伪条件？
─── 防御性新增 ───
□ 13. 是否声明数据收集时间和样本量？
□ 14. 是否包含 Edge Persona 或 Persona Spectrum 维度？
□ 15. 是否避免虚假精确（具体到小数点的人口学）？
□ 16. 是否设定过期/复审日期？
□ 17. 是否标注"本角色不适用的场景"？
□ 18. 是否有备选方法（如该角色失效用什么）？
□ 19. 是否经过至少 1 名"角色目标人群"代表的审阅？
```

---

## 8. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| 19 项防御性评审 | `persona/persona_builder.py` 的 `review_persona()` 从 12 项扩展至 19 项 |
| Persona Spectrum 维度 | `persona/persona_builder.py` 新增 `ability_spectrum` 字段 |
| 失效替代方案地图 | SKILL.md 决策树新增"何时不用 Persona"分支 |
| 退役评估机制 | `persona/lifecycle.py`（未来扩展） |
| 假设状态标记 | `persona/persona_builder.py` 字段级 `validation_status` |

---

## 9. 关键引述

> "Personas are not data. They are inferences from data. Treating them as data is the most common methodological error in user research." — Chapman & Milham, 2006

> "If your persona has never been wrong, it has never been tested." — adapted from Karl Popper

> "The right question is not 'Should we use personas?' but 'Have we earned the right to use personas, and have we built the discipline to retire them?'" — Anonymous, common UXR mantra

---

## 10. 总结：成熟实践的双重立场

```
肯定立场                       警惕立场
────────────                   ────────────
Persona 是有用的工具    +      Persona 不是真理
驱动决策对齐            +      可能掩盖个体差异
帮助同理心              +      可能强化刻板印象
节省后期沟通成本        +      投资必须能退出
```

**双重立场 = 既用且疑**——这是任何成熟方法论实践者的基本姿态。

---

*笔记整理完成 | 基于 Chapman & Milham 学术批评 + Microsoft Inclusive Design + 业界反模式总结 | 提供 Persona 方法的批判性视角与防御策略*
