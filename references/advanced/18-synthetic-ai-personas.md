# 18 · 合成 / AI 生成 Persona：LLM 时代的角色方法

> 来源：Park, J. S. et al. *Generative Agents: Interactive Simulacra of Human Behavior* (Stanford & Google, UIST 2023)；Salminen, J. et al. *"From 2,772 Segments to Five Personas: Summarizing Online Audiences with Personas Powered by GPT"* (CSCW 2024)；Wang, B. et al. *"Reasoning over Personas: A Survey of LLM-Driven Persona Methods"* (ACL 2025)；Anthropic *"Constitutional AI for Persona Simulation"* (2024)；Microsoft Research *"PersonaHub"* (2024-2025)。
>
> 2023 年起，大语言模型让"合成 Persona"从科幻变成日常工具。但工具便利的代价是：合成结果可能强化偏见、稀释真实声音、把团队拉离用户。本笔记区分**合法用法**与**滥用陷阱**。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | 合成 / AI Persona（本笔记） |
|---|---|---|
| 数据来源 | 真实用户调研 | 真实数据 + LLM 重组 / 全合成 |
| 角色单位 | 用户群体代表 | 算法生成的 prototype 或 simulacrum |
| 角色数量 | 3-5 | 1-数千（大规模 PersonaHub 可生成数万） |
| 速度 | 4-8 周 | 数小时-数天 |
| 验证 | 用户测试反馈 | 与真实数据对比 + 人类评审 + 领域专家审核 |
| 用途定位 | 设计决策驱动 | **辅助生成 + 模拟 + 测试**（不取代真实研究） |
| 风险 | 主观偏差 | 训练数据偏见放大、幻觉、声誉与伦理 |

> 💡 **核心立场**：合成 Persona 不是 Mulder 的替代品，而是 **加速器** 与 **填空器**——加速生成草稿、填充 Mulder 没采到的边角场景，但任何关键决策仍需真实用户验证。

---

## 2. 三种合成 Persona 范式

### 2.1 真数据 → AI 总结（Augmentation 范式）

| 项 | 内容 |
|---|---|
| 输入 | 真实问卷/访谈/日志 |
| LLM 角色 | 总结、归类、命名、写故事 |
| 输出 | 结构化 Persona 卡片 |
| 风险等级 | 🟢 低（数据真，AI 仅整理） |
| 代表论文 | Salminen *2772 Segments to Five Personas* (CSCW 2024) |
| 用法 | "把 200 份访谈转写丢给 LLM，生成 5 个 Persona 草稿，研究员审核" |

### 2.2 真数据 → AI 模拟（Simulation 范式）

| 项 | 内容 |
|---|---|
| 输入 | Persona 卡片 + 待模拟场景 |
| LLM 角色 | "扮演" Persona 回答问题、模拟访谈、走可用性流程 |
| 输出 | 模拟访谈记录、A/B 偏好预测 |
| 风险等级 | 🟡 中（模拟可参考但非真实) |
| 代表项目 | Stanford *Generative Agents*, Anthropic Persona Sim |
| 用法 | "用 Persona 模拟 100 名候选用户对 3 个登录页文案的反应，做粗筛" |

### 2.3 全合成 → AI 创造（Generation 范式）

| 项 | 内容 |
|---|---|
| 输入 | 极少初始信息（如行业 + 国家 + 角色） |
| LLM 角色 | 从训练数据先验中编造 Persona |
| 输出 | 全合成画像 |
| 风险等级 | 🔴 高（极易放大偏见与刻板印象） |
| 代表项目 | PersonaHub (Microsoft 2024，10亿+ 合成 Personas) |
| 用法 | 早期 brainstorm / 极小预算公司 / 训练数据生成（学术为主） |

---

## 3. 何时合法、何时不合法（决策矩阵）

| 用途 | Augmentation | Simulation | Generation |
|---|---|---|---|
| 内部 brainstorm 早期收敛 | ✅ | ✅ | ✅ |
| 写 Persona 草稿待审核 | ✅ | ⚠️ | ⚠️ |
| 文案/UI 微调粗筛 | ✅ | ✅ | ⚠️ |
| 替代用户访谈 | ❌ | ❌ | ❌ |
| 替代可用性测试 | ❌ | ❌ | ❌ |
| 决策性产品方向选择 | ⚠️ | ❌ | ❌ |
| 影响收入/法务/医疗的决策 | ❌ | ❌ | ❌ |
| 学术训练数据生成 | ✅ | ✅ | ✅ |

> **铁律**：合成 Persona 永远不是真实用户。所有可能伤害真实用户的决策必须用真实数据兜底。

---

## 4. Persona Prompting 技术（Simulation 范式实操）

### 4.1 三段式系统提示模板

```
[角色描述]
你是 {{persona.name}}, {{persona.age}} 岁, {{persona.role}}。
背景：{{persona.background}}
价值观：{{persona.values}}
当前情境：{{persona.context}}
痛点：{{persona.pain_points}}
目标：{{persona.goals}}

[行为约束]
- 用第一人称回答
- 反映真实犹豫、矛盾与情绪，不要"完美用户"
- 拒绝你不可能知道/不关心的问题
- 用日常口语，不用专业术语（除非角色设定是专家）
- 在合理时表达困惑、疲倦、抗拒

[禁止]
- 不要扮演角色之外的人
- 不要给出"对的答案"——你是 1 个人，不是用户群体
- 不要替开发者鼓掌；像真实用户那样吐槽 / 离开

[当前任务]
{{task: 走完登录流程 / 评论一段文案 / 排序 5 个功能优先级}}
```

### 4.2 5 个进阶技巧

| 技巧 | 做法 | 目的 |
|---|---|---|
| Constitutional 约束 | 在 system 中写"你不知道 2024 年后的事""你不会编造数字" | 抑制幻觉 |
| Anchor with Quotes | 在 Persona 卡片注入 3-5 句真实受访者引语 | 锚定语言风格 |
| Multi-Persona Tournament | 让多个 Persona 并行评估同一文案，看分歧 | 检验文案普适性 |
| Adversarial Devil | 加 Negative Persona / Skeptic | 找设计盲点 |
| Reflection Loop | 让 Persona 回答完，再问"刚才你说的，10% 不太诚实的部分是什么？" | 揭示社会期望偏差 |

---

## 5. 5 类反模式（必读）

| 反模式 | 症状 | 危害 |
|---|---|---|
| **AI Persona 替代用户研究** | "我们用 GPT 生成了 5 个 Persona，所以不做访谈了" | 把训练数据的中位刻板印象当用户真实声音 |
| **刻板印象放大** | "中国一二线女性白领"= LLM 默认套版 | 加深性别/地域/年龄偏见 |
| **过度可信** | 团队把模拟访谈当真实数据写进 PRD | 决策偏离真实用户 |
| **AI 幻觉报数字** | LLM 编出 "73% 的用户会..."的统计 | 错误的数据被引用，自我循环 |
| **匿名化绕过** | 用 LLM "脱敏"真实访谈再给团队 | 失去声音质感，且未必真匿名 |
| **同质化** | LLM 生成的 100 个 Personas 中 80 个相似 | 多样性虚假繁荣 |
| **不留审计痕迹** | 不记录生成时间、模型版本、Prompt | 复现失败、问题追溯失败 |

---

## 6. 合成 Persona 的伦理 5 原则

1. **透明 (Transparency)**：在 Persona 卡片**显式标注** "Synthetic / Augmented / Real"，绝不让团队误以为是真实用户。
2. **审计 (Auditable)**：记录模型 ID + Prompt + 时间，便于复现和检视。
3. **审核 (Reviewed)**：领域专家+用户研究员审核，至少 1 轮人类判断。
4. **限定 (Bounded)**：明确"该 Persona 仅用于 X 决策，不用于 Y/Z"。
5. **持续校正 (Calibrated)**：每季度用真实数据回测合成 Persona 是否仍代表趋势。

---

## 7. 合成 Persona 卡片新增字段（v2.6 推荐）

```yaml
synthetic_meta:
  type: "augmented"   # synthetic | augmented | real
  source_data: "200 voices interviews 2026-Q1"
  model: "claude-sonnet-4.5"
  generation_date: "2026-05-29"
  prompt_id: "persona-prompt-v3.2"
  human_reviewer: "user-research-team"
  validation_status: "validated"  # draft | reviewed | validated | retired
  bounded_use: ["onboarding-copy", "feature-prioritization"]
  forbidden_use: ["pricing", "medical-advice", "legal-content"]
  refresh_cadence: "quarterly"
  next_review: "2026-08-29"
```

> 这套字段直接落入本技能 v2.6 的 `persona/synthetic_meta.py`（在 D 系列工程化文档中详述）。

---

## 8. 验证 LLM 生成 Persona 的 4 道关卡

| 关卡 | 检查项 | 工具 |
|---|---|---|
| 1. 真实性比对 | 与真实数据交叉对比关键变量分布 | 卡方 / KS 检验 |
| 2. 多样性检验 | n=20 生成中独立特征数；是否相同模板 | 嵌入距离矩阵 / Jaccard |
| 3. 偏见审计 | 性别/种族/年龄/地域比例是否失衡 | demographic parity |
| 4. 人类审核 | 至少 2 名研究员独立评分 | Likert 1-5 |

> 任何一关不及格都不应进入产品决策。

---

## 9. 何时使用合成 Persona

✅ 用：
- 早期 brainstorm 找方向
- Mulder Persona 已有 → 用 LLM 写更多场景描述/Day-in-the-Life
- 文案/UI A/B 候选粗筛（仍需真人小流量验证）
- 边缘 Persona 无法采到（如低频小众群体的初步勾勒）
- 教学 / 培训 / 演练
- 学术训练数据扩增

⛔ 不用：
- 真实用户研究的替代
- 财务/医疗/法律/伦理类决策
- 当作公开"真实证据"
- 已经有真实数据但嫌麻烦不去采集
- 团队不愿意培训"合成 vs 真实"的区分意识

---

## 10. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/llm_prompts.py`（v2.6 新增） | Persona Prompting 模板库 |
| `persona/synthetic_meta.py`（v2.6 新增） | 合成 metadata 字段 |
| 09-Indi Young | Listening Session 真实数据是合成 Persona 的最佳锚点 |
| 23-Thick Data | 警惕 LLM 把"thick"压成"thin" |
| 25-Cababa | 二阶后果：合成 Persona 可能稀释真实弱势群体声音 |
| 27-bias-audit | LLM 偏见审计的具体清单 |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| 三种范式 | Augmentation 安全 > Simulation 谨慎 > Generation 高风险 |
| 不可替代真实研究 | LLM 是放大器和加速器，不是用户本身 |
| 标注合成属性 | Persona 卡片必须有 synthetic_meta 字段 |
| 审计可复现 | 记录模型/Prompt/时间，便于追溯 |
| 4 道关卡 | 真实性/多样性/偏见/人类审核 |
| 边界明确 | bounded_use + forbidden_use 必须写入 |
| 季度回测 | 真实数据校正合成 Persona |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `virtual-user-interview` | 飞猪虚拟用户访谈 = Simulation 范式案例 |
| `user-psych-analyst` | 心理学约束注入 LLM Persona |
| `analytics-data-analysis` | 验证关卡 1：真实性比对 |
| `competitive-analysis` | 用 Persona Tournament 做竞品文案对比 |
| `landing-page` | 多 Persona 并行评估页面副本 |
| `prd-writing` | Synthetic Persona 写场景章节，但需标注 |

---

> 📚 **延伸阅读**：
> - Park et al. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*. UIST'23.
> - Salminen et al. (2024). *From 2,772 Segments to Five Personas: GPT-Powered Persona Generation*. CSCW.
> - PersonaHub (Microsoft Research, 2024-2025): 10亿+ 合成 personas 训练数据集。
> - Anthropic Constitutional AI guidelines (2024): 角色模拟伦理边界。
> - 警示阅读：Bender et al. *On the Dangers of Stochastic Parrots* (FAccT 2021)——LLM 的训练数据偏见对 Persona 生成的潜在伤害。
