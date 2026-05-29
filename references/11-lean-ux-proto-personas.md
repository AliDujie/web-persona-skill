# 11 · Lean UX 与 Proto-Personas

> 来源：Jeff Gothelf & Josh Seiden《Lean UX: Designing Great Products with Agile Teams》第 2 版 (O'Reilly, 2016)。
>
> Lean UX 是 Lean Startup（精益创业）+ Agile（敏捷开发）+ Design Thinking 的融合方法论，对传统 Persona 提出**"先假设、后验证"**的轻量替代——Proto-Persona。本笔记基于个人学习理解整理，非原文复制。

---

## 1. 与 Mulder/Cooper/Pruitt-Adlin 的关系

| 维度 | 传统派（Mulder/Cooper） | Lean UX（Gothelf） |
|---|---|---|
| 启动门槛 | 6-12 周 + 调研预算 | 1-2 小时工作坊 |
| 数据基础 | 必需 | 可选（但**必须事后验证**） |
| 角色形态 | 完整 Foundation Document | 1 页 Proto-Persona |
| 心态 | 角色是结论 | 角色是假设 |
| 适用阶段 | 立项/重构期 | 创业期、早期 MVP、新功能探索 |

> 💡 **Lean UX 的根本立场**：在不确定性极高的早期阶段，**完美的角色研究是奢侈的浪费**。先用假设跑实验，让市场告诉你哪些假设错了。

---

## 2. Proto-Persona（假设型角色）

### 2.1 标准模板（4 象限）

```
┌──────────────────────────────────────────────────┐
│                                                  │
│  名字 + 简笔素描 / 照片                         │
│  ──────────────                                  │
│  [姓名]                                          │
│  [一句话身份]                                    │
│                                                  │
├──────────────────────────────────────────────────┤
│                                                  │
│  人口学 / 角色信息    │   行为与信念             │
│  ─────────────────    │   ─────────────         │
│  - 年龄                │   - 关键行为 1          │
│  - 职业                │   - 关键信念 2          │
│  - 与产品的关系        │   - 信息消费习惯        │
│                        │                          │
├────────────────────────┼─────────────────────────┤
│                        │                          │
│  需求与目标            │   痛点与挫败             │
│  ─────────────         │   ─────────────         │
│  - 需求 1              │   - 痛点 1              │
│  - 需求 2              │   - 痛点 2              │
│  - 目标                │   - 当前替代方案        │
│                        │                          │
└────────────────────────┴─────────────────────────┘
```

### 2.2 创建流程（30-60 分钟工作坊）

```
Step 1: 召集团队（产品 + 设计 + 工程 + 商务）
Step 2: 个人静默书写——每人独立写 2-3 个 Proto-Persona
Step 3: 墙面贴出，按相似性聚类
Step 4: 团队投票选出 2-4 个保留
Step 5: 团队共同填写 4 象限模板
Step 6: 立即列出"我们假设这个人……但我们不确定"清单
```

### 2.3 与传统 Persona 的关键区别

| 项 | Persona（传统） | Proto-Persona |
|---|---|---|
| 头像 | 真实照片 | 简笔画或素材图（避免"过于真实"幻觉） |
| 引语 | 来自访谈 | 团队推断 |
| 行为 | 来自数据 | 团队假设 |
| 状态标记 | 已验证 | **明确标注"未验证假设"** |
| 更新机制 | 每年 | **每个 Sprint 复审** |

> ⚠️ **关键纪律**：Proto-Persona 的每条描述旁应标注 `[假设]` 或 `[已验证-YYYY-MM-DD-数据来源]`。这是抵御"假设固化为信念"的防线。

---

## 3. Lean UX 闭环

```
Outcomes（结果）：业务/用户结果，而非 Output（产出）
   │
   ▼
Hypotheses（假设）：我们相信 [Outcome] 可以通过 [Output] 为 [Persona] 实现
   │
   ▼
Experiments（实验）：MVP / 原型 / A-B 测试
   │
   ▼
Learning（学习）：验证或证伪假设
   │
   ▼ （回到 Outcomes）
```

### 3.1 Hypothesis 标准句式

> "We believe that **[Outcome]** will be achieved if **[user/persona]** attain **[benefit]** with **[feature]**."

> 例："We believe that *提升注册留存* 将实现 if *Proto-Persona Alex* 能够 *3 步内完成首单* with *简化下单流程*."

每条假设必须有：
- 可测量的成功指标（如"7 天留存 ≥ 30%"）
- 可证伪的失败标准（如"如果 7 天留存 < 15%，假设错"）
- 时间盒（如"2 周内得出结论"）

### 3.2 MVP（最小可行实验）

注意：Lean UX 用的是 **Minimum Viable Experiment**（最小可行**实验**），而非 Eric Ries 的"产品"。

| 实验类型 | 验证什么 |
|---|---|
| **Smoke Test** | 需求是否存在（着陆页 + 注册按钮） |
| **Wizard of Oz** | 体验是否有价值（人工模拟自动化功能） |
| **Concierge** | 解决方案是否合用（人工服务少数用户） |
| **Prototype** | 交互能否被理解（点击式原型） |
| **Feature Stub** | 功能能否驱动行为（半成品上线） |

每个实验关联 Proto-Persona 的某条假设。

---

## 4. 从 Proto-Persona 到传统 Persona 的演化路径

```
Day 1            Sprint 2          Sprint 6           Quarter 2
─────────────────────────────────────────────────────────────►
Proto-Persona    Validated         Hybrid             Full Persona
(纯假设)         Proto-Persona     (大多已验证)        (Mulder/Cooper)
                 (部分已验证)
```

**演化触发条件**：
- 假设清单中 60% 以上已验证 → 升级为 Hybrid
- 80% 以上已验证 + 有足够样本 → 升级为完整 Persona
- 某条角色假设连续 3 次实验失败 → 删除该角色（而非修补）

> 💡 **不要永远停在 Proto**：Lean UX 不是"永远轻量"，而是"以最低成本快速进入完整研究"。Proto-Persona 是过渡形态，不是终态。

---

## 5. Lean UX 的反 Persona 时刻

Gothelf 在书中坦承：**有时根本不需要 Persona**。

| 情境 | 替代方案 |
|---|---|
| 用户类型极度同质（如内部工具） | 直接用 Job Story（任务故事） |
| 单一目标驱动（如只做支付） | 用户旅程图即可 |
| B2B 复杂决策链 | Buying Committee Map（采购委员会图）替代单角色 |
| 平台型产品（多边市场） | 每边一个简化 Proto-Persona + 互动场景 |

> 💡 **Persona 不是万能锤**。Lean UX 的清醒在于：先问"我现在最不确定什么"，再选工具。

---

## 6. 与本技能其他模块的衔接

| 本笔记产出 | 衔接模块 |
|---|---|
| Proto-Persona 4 象限模板 | `persona/templates.py` 新增 `proto_persona_template` |
| Hypothesis 句式 | `persona/strategy.py` 新增 `generate_hypothesis()` |
| 假设状态标记（[假设] / [已验证]） | `persona/persona_builder.py` 字段新增 `validation_status` |
| 演化路径触发条件 | `persona/persona_builder.py` 新增 `evaluate_evolution_readiness()` |
| MVP 实验类型库 | `persona/measure.py` 新增 `experiment_types` 配置 |

---

## 7. 何时优先使用 Lean UX

| 情境 | 推荐 |
|---|---|
| 创业 < 18 个月 | ✅ Proto-Persona 优先 |
| 新功能探索（非全新产品） | ✅ Proto + 快速验证 |
| 调研预算 = 0 | ✅ Lean UX 的本意 |
| 团队已有 Persona 但执行不下去 | ✅ 退回 Proto + 假设清单 |
| 法规/医疗/金融高风险领域 | ❌ 必须传统 Persona + 验证 |
| 大型组织、多团队协作 | ❌ Pruitt-Adlin 治理框架更合适 |

---

## 8. 与传统 Persona 的整合策略

不是"二选一"，而是**分阶段使用**：

```
阶段 1（0-6 个月）：Proto-Persona × 多次假设验证
   └─ 输出：经过验证的核心假设清单

阶段 2（6-12 个月）：进入 Goodwin 七步法
   └─ 用积累的数据补全 Foundation Document

阶段 3（12+ 个月）：进入 Pruitt-Adlin Lifecycle
   └─ 推广、嵌入工作流、定期复审
```

---

## 9. 关键引述

> "A persona without data is just a guess. Lean UX makes that explicit and short-lived." — Jeff Gothelf

> "The goal of Lean UX is not to be lean forever. It is to learn fast enough to know when you can afford to be thorough." — Lean UX, 2nd ed.

> "The biggest enemy of good UX is not bad design. It is well-designed solutions to the wrong problem." — Gothelf & Seiden

---

*笔记整理完成 | 基于 Gothelf & Seiden《Lean UX》第 2 版 | 与 Mulder 派形成"轻量假设/快速验证"互补*
