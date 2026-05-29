# 25 · Cababa《Closing the Loop》：系统性思维与二阶后果

> 来源：Cababa, S. *Closing the Loop: Systems Thinking for Designers* (Rosenfeld Media, 2023)；Meadows, D. *Thinking in Systems: A Primer* (2008)；Costanza-Chock, S. *Design Justice: Community-Led Practices to Build the Worlds We Need* (MIT Press, 2020)；IDEO *The Little Book of Design Research Ethics* (2019)；ACM Code of Ethics 2018。
>
> Cababa 在多家科技公司做 UX 后发现一个反直觉规律：**设计越成功，用户越多，二阶后果越被忽视**。Persona 帮助你专注主用户，却遮蔽了你的设计在系统中的副作用。本笔记把"我们设计的世界，会反过来塑造谁"作为 Persona 设计的伦理问责轴。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | 系统性视角（本笔记） |
|---|---|---|
| 时间维度 | 注册-激活-购买短期闭环 | 1-3-10 年长期反馈环 |
| 利益相关方 | 主用户 + 决策者 | 用户 + 非用户 + 社会 + 生态 |
| 失败诊断 | 转化率/留存差 | 已成功但产生负外部性 |
| 输出 | Persona 卡片 | Persona + 系统图 + 二阶后果地图 |
| 适合场景 | 任意 | 规模化产品、平台、AI、公共服务 |

> 💡 **核心论点**：每个成功 Persona 服务的背后，可能存在 Anti-Persona——被你的设计**间接伤害**或**被剥夺机会**的群体。系统性思维让这些隐形群体浮出水面。

---

## 2. 一阶/二阶/三阶后果

| 阶 | 含义 | 例（外卖平台） |
|---|---|---|
| **1st-Order** | 直接的、设计预期的后果 | 用户 30 分钟收到饭，骑手获得收入 |
| **2nd-Order** | 间接、未预期但可推演 | 骑手为达时效闯红灯；本地餐馆数字化加速 |
| **3rd-Order** | 系统级、长期、生态影响 | 街头小餐馆消失；骑手保险/工伤社会成本；城市步行文化变化 |

> Cababa 的纪律：**每个 Persona 的核心 Job 都要做 1→2→3 阶推演**——至少把团队的视野扩展到 3 阶。

---

## 3. Stakeholder Universe（不止用户）

| 类型 | 中文 | 例 |
|---|---|---|
| **Direct Users** | 直接用户 | 主 Persona |
| **Adjacent Users** | 邻近用户 | 服务你的人（骑手、客服） |
| **Non-Users** | 非用户 | 受影响但没用产品（街边摊主） |
| **Future Users** | 未来用户 | 5-10 年后受影响的世代 |
| **Implicated** | 牵连方 | 训练数据贡献者、内容创作者 |
| **Environment** | 环境 | 能耗、电子垃圾、土地 |

> 每个 Persona 旁边写至少 3 类"非主用户"——团队眼界立刻扩大。

---

## 4. Causal Loop Diagrams（因果环图）

Meadows 经典工具，Cababa 简化为 Persona 友好版。

### 4.1 强化环 (Reinforcing Loop, R)
```
活跃用户↑ → 内容产出↑ → 推荐效果↑ → 活跃用户↑↑（飞轮）
```

### 4.2 平衡环 (Balancing Loop, B)
```
推送频次↑ → 短期点击↑ → 用户疲劳↑ → 卸载率↑ → 推送频次↓（自我矫正）
```

### 4.3 延迟反馈
```
增长压力 → 推送过频 → ... 6 个月后 → 留存崩塌（延迟）
```

> 📐 **画图纪律**：箭头标 + / − ；闭合环用 R / B 标注；明确**延迟**（双竖线 ‖）。

---

## 5. Pre-mortem 升级版（含二阶）

### 经典 Pre-mortem（Kahneman 派）
> 假设产品上线 6 个月失败了，原因是什么？

### 系统性 Pre-mortem（Cababa）
> 假设产品**极其成功**——5 年后有 1 亿用户。请回答：
> 1. 谁因此变得更不平等？
> 2. 哪些行业/职业被替代？被替代者去了哪里？
> 3. 我们提供了什么便利，同时使什么变得困难？
> 4. 训练数据来自谁？他们获得了什么？
> 5. 用户依赖产品后，失去了什么独立能力？
> 6. 监管/法律有什么追溯风险？
> 7. 出问题时，谁来负责修复？

> 上述清单写进 PRD 的"Risks & Mitigations"段。

---

## 6. Anti-Persona / Counter-Persona

不是"恶意用户"（Cooper 的 Negative Persona 已涵盖）；而是**被你的设计意外伤害的群体**。

| 维度 | Negative Persona (Cooper) | Anti-Persona (Cababa) |
|---|---|---|
| 是什么 | 不为之设计的用户 | 设计成功后被伤害的非用户 |
| 关注焦点 | 防过度迁就 | 伦理问责 |
| 例 | "薅羊毛者" | "短视频上瘾的青少年""被替代的本地小店主" |

### 6.1 Anti-Persona 模板

```yaml
anti_persona_id: replaced_local_seller
description: "二线城市干洗店主, 52, 经营 15 年, 月营收 ¥1.8 万"
how_were_they_harmed:
  - "团购平台压价 → 利润率从 25% 降至 8%"
  - "线上化要求 → 不熟悉数字工具，焦虑增加"
  - "新客户被平台抢走，老客户被'优惠券'挖走"
mitigations:
  - "为非数字化商家设计低门槛入驻路径"
  - "保护性定价底线（不允许低于成本）"
  - "线下数字化培训公益项目"
review_cadence: "每年一次"
```

---

## 7. Trauma-Informed Design（创伤知情设计）

Cababa 引用社会工作领域的 Trauma-Informed Care，主张设计需考虑"用户可能携带创伤"。

### 7.1 创伤知情 5 原则
| 原则 | 设计含义 |
|---|---|
| Safety | 物理与心理安全感 |
| Trustworthiness | 透明、不隐藏选项 |
| Choice | 提供退出/拒绝选项 |
| Collaboration | 与用户共建而非单向推送 |
| Empowerment | 强化用户能动性 |

### 7.2 创伤知情场景（举例）
- 金融 App 在还款日前 3 天发"友好提醒"，而非"再不还就上征信！"
- 医疗 App 让用户能控制谁能看自己的诊断
- 社交平台允许"屏蔽某关键词"以避免重复触发

---

## 8. 反模式 (Anti-patterns)

| 反模式 | 症状 | 后果 |
|---|---|---|
| **只看 1st-Order** | 只追北极星指标 | 二阶副作用累积 |
| **Stakeholder 缩水** | 仅 Direct Users | 非用户群体被忽视 |
| **NPI 心态 (Not Persona's Issue)** | "这不是我们 Persona 的问题" | 推卸伦理责任 |
| **Pre-mortem 只看失败** | 不做"成功后果想象" | 看不到尺度风险 |
| **Anti-Persona 形式化** | 列出但无 owner | 沦为装饰 |
| **创伤知情只剩 UI 文案** | 不改流程 / 数据收集 | 表面温和、内核仍剥夺 |
| **系统图过度复杂** | 50 节点画图 | 团队读不懂 |

---

## 9. 系统性 Persona 8 步流程

| 步 | 动作 |
|---|---|
| 1 | 主 Persona + Job 已就绪 |
| 2 | 列 Stakeholder Universe（6 类） |
| 3 | 画 1-2 张 Causal Loop Diagram（R + B + 延迟） |
| 4 | 系统性 Pre-mortem 7 问 |
| 5 | 列 2-3 个 Anti-Persona |
| 6 | 标记 Trauma-Informed 高风险触点 |
| 7 | 决定缓释措施（Mitigation Plan） |
| 8 | 设审计周期（季/年），写进文档治理 |

---

## 10. 何时使用系统性视角

✅ 用：
- 平台型产品（双边/多边）
- 涉及 AI / 推荐算法
- 影响生计/健康/教育/金融
- 政府/公共服务
- 已有规模 + 监管关注
- 内部 Ethics Review 被强制执行

⛔ 不用：
- 极早期 MVP（但仍记录 IOU）
- 内部工具（系统外溢小）
- 个人爱好项目

---

## 11. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/persona_builder.py` | 增加 `anti_personas`, `causal_loops`, `mitigations` |
| `persona/systems_review.py`（v2.6 新增） | 系统性 Pre-mortem 工作流 |
| 15-Critique-Defense | 应对"Persona 同质化伤害"批评 |
| 18-Synthetic AI | 合成 Persona 二阶后果（声音稀释） |
| 24-Kat Holmes | 排斥 = 二阶后果之一 |
| 27-bias-audit | 偏差 + 系统后果联动审计 |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| 三阶后果 | 推演到 3 阶才看到真问题 |
| Stakeholder 6 类 | 用户之外还有非用户/未来/牵连/环境 |
| Causal Loop 是基础工具 | R+B+延迟 + 标注 |
| 系统性 Pre-mortem | 想象成功后果，找盲点 |
| Anti-Persona | 被设计意外伤害的非用户 |
| Trauma-Informed | 5 原则贯穿全旅程 |
| 审计是文档治理 | 不是一次会议 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `consulting-frameworks` | 系统思维与 issue tree 互补 |
| `architecture-design` | 系统级架构含伦理风险评估 |
| `prd-writing` | PRD 增加 Anti-Persona / Mitigations 段 |
| `decision-tracker` | 二阶后果决策记录 |
| `security-review` | 安全审计 + 伦理审计联动 |
| `competitive-analysis` | Anti-Persona = 竞争对手潜在客户 |

---

> 📚 **延伸阅读**：
> - Cababa, S. (2023). *Closing the Loop: Systems Thinking for Designers*。
> - Meadows, D. (2008). *Thinking in Systems: A Primer*。
> - Costanza-Chock, S. (2020). *Design Justice*。
> - Lupton, E. (ed.) (2021). *Extra Bold: A Feminist, Inclusive, Anti-racist Design Guide*。
> - 中国情境：刘擎 *做一个清醒的现代人*；项飚 *附近的消失*（关于平台经济的二阶后果）。
