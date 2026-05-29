# 20 · Kahneman 双系统：Persona 的认知决策模型

> 来源：Kahneman, D. *Thinking, Fast and Slow* (Farrar, Straus & Giroux, 2011)；Kahneman, Sibony & Sunstein *Noise: A Flaw in Human Judgment* (2021)；Thaler, R. & Sunstein, C. *Nudge* (2008)；Tversky & Kahneman *Judgment under Uncertainty* (Science, 1974)。
>
> Mulder/Cooper 派 Persona 关心"用户是谁、想做什么"；Kahneman 让我们看清"用户如何决策"——98% 的日常决策由快速直觉系统完成，但 Persona 文档常常只描绘了那 2% 的理性思考者。本笔记把双系统理论系统地落入 Persona 设计。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | Kahneman 双系统视角（本笔记） |
|---|---|---|
| 决策模型 | 用户有目标 → 走流程 → 完成任务 | 用户在 System 1 自动反应 + System 2 偶尔介入 |
| 设计假设 | 提供清晰功能即可 | 必须考虑认知偏差、启发法、情境锚定 |
| 失败来源 | UI 难用、流程长 | 决策瞬间被认知捷径劫持 |
| 工具 | 卡片、流程图 | 偏差清单、Nudge 设计、System 1/2 标注 |
| 适用场景 | 任务型设计 | 决策型设计（金融/医疗/选择困难型） |

> 💡 **互补立场**：Mulder 的 Persona 描绘"我想做什么"；Kahneman 揭示"我会被什么悄悄影响"。两者结合 → 设计师既知道目标，也知道让用户偏离目标的悬崖。

---

## 2. System 1 vs System 2 核心对比

| 维度 | System 1（快） | System 2（慢） |
|---|---|---|
| 速度 | 毫秒级，自动 | 秒级以上，需努力 |
| 能耗 | 低 | 高（葡萄糖代谢上升） |
| 容量 | 大量并行 | 单线程 |
| 控制感 | "事情发生在我身上" | "我在思考" |
| 输出 | 第一印象、感觉、直觉、语言流畅性判断 | 推理、计算、策略 |
| 偏差易感性 | 极高 | 较低（但仍有） |
| Persona 表现 | "我没多想就点了那个红色按钮" | "我列了 5 个选项，比较了一下午" |

> **关键洞察**：界面设计 95% 服务 System 1；只有重大决策（购车、贷款、医疗、选职业）才大量调用 System 2。**为 Persona 标注其常用系统**，能立刻指导设计取舍。

---

## 3. 11 大认知偏差（Persona 必备清单）

| 偏差 | 解释 | Persona 设计含义 |
|---|---|---|
| **Anchoring** | 锚定 | 第一个见到的数字/选项主导后续判断 | 价目表第一行价格策略 |
| **Availability** | 可得性 | 容易想起的例子 = 觉得普遍 | 风险沟通文案 |
| **Loss Aversion** | 损失厌恶 | 失去的痛 ≈ 2.5×获得的喜 | 取消按钮 vs 确认按钮 |
| **Framing** | 框架 | "90% 存活" ≠ "10% 死亡" | 文案正面/负面切换 |
| **Default Effect** | 默认偏好 | 用户倾向不改默认值 | 默认隐私设置 |
| **Endowment Effect** | 禀赋效应 | 已拥有 = 高估价值 | 试用期、退订流失点 |
| **Confirmation Bias** | 确认偏差 | 偏向支持已有观点的信息 | 推荐算法对照组设计 |
| **Hyperbolic Discounting** | 现时偏好 | 现在 100 vs 1 个月后 105 | 长期合同/订阅设计 |
| **Status Quo Bias** | 现状偏好 | 不变 > 变 | 升级流程的迁移成本 |
| **Halo Effect** | 光环 | 美貌/品牌信任 → 理性判断打折 | 落地页第一屏视觉 |
| **Bandwagon** | 从众 | 别人都用 → 我也用 | "1 万 + 用户已选" 副本 |

> 推荐用法：**给每个 Persona 卡片写出 TOP 3 偏差**——影响力最强的 3 个，避免 11 个全列像背书无重点。

---

## 4. Nudge 设计原则（Thaler & Sunstein, 2008）

Kahneman 学派认为：你不能"教育"System 1，只能"轻推"它。

| 原则 | 中文 | 设计示例 |
|---|---|---|
| **iNcentives** | 激励让人看见 | 退休金多缴可见；省下的钱可视化 |
| **Understand mappings** | 让选择→后果可感知 | 信用卡 → 1 年利息总额提示 |
| **Defaults** | 默认即推力 | 自动入选退休金计划 |
| **Give feedback** | 实时反馈 | 跑步 App 的步数动效 |
| **Expect error** | 预期错误 | 删除前确认 / 撤销 |
| **Structure complex choices** | 结构化复杂选择 | 套餐 推荐 + 对比表 |

合并首字母 = **NUDGES**。设计 Persona 互动旅程时，逐点检查命中。

---

## 5. Persona × 双系统的标注模板

```
Persona: 林佳, 34, 二孩妈妈, 月入 1.8 万

🧠 主导决策系统（按场景）
- 日常采购：System 1（快、价格锚定、品牌从众）
- 子女教育/医疗：System 2（多对比、问朋友、查数据）
- 健康险/理财：System 2 但易疲劳 → 半路退回 System 1

⚠️ Top 3 认知偏差
1. Loss Aversion：怕"漏掉给孩子的好东西"——容易被"限时" "额度有限"打动
2. Default Effect：套餐默认推荐 = 80% 概率被选中
3. Bandwagon：评论数 > 价格 > 品牌 在最终选择中的权重

🎯 Nudge 设计建议
- Mapping：把"投资 ¥10000" → "5 年后预期 ¥X" 即时可视化
- Defaults：默认勾选"3 年期"（对她最适合的期限）
- Expect error：撤销冷静期 7 天
- Feedback：每月推送账户健康度

📌 反 Nudge（要避免的暗模式）
- 不要用倒计时制造焦虑
- 不要把"取消订阅"藏 3 层菜单
- 不要默认勾选"接受营销邮件"
```

---

## 6. Pre-mortem & Noise（少有人讲的 Kahneman 工具）

### 6.1 Pre-mortem（事前验尸）
设计前**预想失败场景**：
> "假设这个新功能上线 6 个月后彻底失败，每个 Persona 是怎么离开的？"

让团队各自写 5 个原因，再合并；常能在上线前发现盲点。

### 6.2 Noise（噪声）
《Noise》指出：决策不只有偏差 (Bias)，还有 **噪声 (Noise)**——同一案例在不同时间、不同决策者会得出不同结论。

| 类型 | 含义 | Persona 含义 |
|---|---|---|
| Level Noise | 不同人/团队基础水平差异 | 一线 vs 总部对客户优先级判断不同 |
| Pattern Noise | 同一人对不同案例的反应不一致 | 同一 PM 上午 vs 下午对 Persona 的取舍不同 |
| Occasion Noise | 同一人同一案例不同时间 | 周一 vs 周五的研究判断 |

**降噪手段**：用 Persona 卡片作为"决策锚"，让团队每次回到同一个角色定义判断；定期做"决策审计"。

---

## 7. 反模式 (Anti-patterns)

| 反模式 | 症状 | 后果 |
|---|---|---|
| **理性 Persona** | 把所有用户描绘为完全理性的优化者 | 设计与真实行为脱节 |
| **偏差列 50 条** | Persona 卡片塞满偏差但无重点 | 团队记不住，等于没列 |
| **暗黑 Nudge** | 用偏差操控用户做不利于自己的事 | 信任崩盘、监管风险 |
| **System 2 当默认** | 设计假设用户每次都细读 | 真实流量大量流失 |
| **偏差与场景脱节** | 写"该 Persona 有 Loss Aversion" 但不指明哪个屏幕 | 设计无法落点 |
| **不审计 Noise** | 只查偏差不查噪声 | 同样问题反复出现，组织层面无改善 |

---

## 8. Nudge 的伦理边界（Libertarian Paternalism）

Thaler & Sunstein 主张 **Nudge 必须满足 3 条**：

1. **EASY** to opt-out — 一键退出，不藏菜单
2. **TRANSPARENT** — 用户被告知正在被推动
3. **WELFARE-INCREASING** — 推向用户自己更想要的方向，而非平台利益

> ⚖️ 任何不满足这 3 条的"Nudge"都是 **Dark Pattern（暗模式）**。Persona 设计师有义务做 Nudge 伦理审查。

---

## 9. 何时使用双系统视角

✅ 用：
- 决策型产品（金融/保险/医疗/教育）
- 漏斗转化关键节点（注册/购买/取消）
- 高风险决策（投资、合同、捐赠）
- 改变用户长期行为（戒烟、储蓄、健身）
- 组织内部决策审计

⛔ 不用：
- 纯任务型工具（文件管理）→ Mulder 即可
- 极简内容产品（资讯阅读）→ 偏差权重低
- 已知用户高度理性（专家工具）→ System 2 主导

---

## 10. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/persona_builder.py` | 增加 `cognitive_biases`, `nudge_strategy` 字段 |
| 02-measuring-results | 用 A/B 实验验证 Nudge 效果 |
| 21-Fogg | Fogg 模型 + 偏差清单 = 行为改变工具箱 |
| 22-JTBD | Job 触发瞬间常被 System 1 捕获 |
| 27-bias-audit | 偏差清单与公平性偏差的合规审查 |
| 30-OKR-Bridge | 把 Nudge 效果写进 KR |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| 双系统是默认设定 | 用户 95% 时间在 System 1，设计要服务它 |
| Top 3 偏差胜于 30 条 | 每个 Persona 只标最关键 3 个偏差 |
| NUDGES 6 原则 | 设计旅程时逐点检查命中 |
| 暗模式禁区 | Easy/Transparent/Welfare 三条铁律 |
| Pre-mortem 必做 | 上线前预想失败 → 暴露盲点 |
| 关注 Noise 不止 Bias | 组织决策的不一致比偏差更危险 |
| 与 Mulder 互补 | 目标视角 + 决策视角 = 完整人物 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `user-psych-analyst` | 双系统理论 + 偏差清单深度落地 |
| `landing-page` | 落地页 Nudge 6 原则审查 |
| `prd-writing` | PRD 决策章节加偏差/Nudge 段 |
| `consulting-frameworks` | Pre-mortem 作为咨询工具 |
| `decision-tracker` | 跟踪 Nudge A/B 效果 |
| `analytics-data-analysis` | 行为日志中的偏差量化 |

---

> 📚 **延伸阅读**：
> - Kahneman (2011). *Thinking, Fast and Slow*. Part I-IV.
> - Thaler & Sunstein (2008). *Nudge*. 修订版含数字时代案例。
> - Kahneman, Sibony & Sunstein (2021). *Noise*. 决策一致性。
> - Behavioral Insights Team (UK Cabinet Office). *EAST Framework*：Easy/Attractive/Social/Timely——可作 Nudge 的浓缩版。
> - Schwartz, B. *Paradox of Choice*：选项过多 → System 2 瘫痪 → 默认/不决定。
