# 29 · 工程化：Persona × LLM Prompt Library

> 来源：本技能 18 号《合成 AI Persona》方法论笔记的代码化实现；OpenAI/Anthropic 官方 system-prompt 最佳实践；Park et al. *Generative Agents* (2023)。
>
> D 系列工程化文档第 2 篇。提供 `persona/llm_prompts.py` 模块——把 Persona 卡片转为可重复使用的 LLM 系统提示，支持 4 种用法：模拟访谈、文案评估、Devil's Advocate、Multi-Persona Tournament。

---

## 1. 模块定位

| 项 | 内容 |
|---|---|
| 模块路径 | `persona/llm_prompts.py` |
| 主类 | `PersonaPromptLibrary`、`PersonaPrompt` |
| 输入 | `PersonaProfile`（PersonaBuilder 输出） + 任务参数 |
| 输出 | 字符串 system + user prompts，可直接喂给 LLM API |
| 依赖 | 仅标准库 |
| 设计目标 | **不耦合任何 LLM SDK**，输出原始 prompt 字符串 |

> ⚠️ 模块只生成 prompts 字符串。具体调用 OpenAI / Anthropic / 通义千问 / DeepSeek 等 API，由调用方负责。

---

## 2. 4 种核心 Prompt 类型

| 类型 | 用途 | 谁调用 |
|---|---|---|
| **simulated_interview** | 让 LLM 扮演 Persona 接受访谈 | 早期 brainstorm / 文案 A/B 候选粗筛 |
| **copy_evaluation** | 让多个 Persona 独立评估同一段文案 | 多元视角检验 |
| **devils_advocate** | 让 LLM 扮演反向 Persona / 怀疑者 | 找设计盲点 |
| **multi_persona_tournament** | 多 Persona 并行评估同一方案 | 找最普适方案 |

---

## 3. 接口预览

```python
from persona import PersonaBuilder
from persona.llm_prompts import PersonaPromptLibrary

builder = PersonaBuilder("我的产品")
builder.add(name="林佳", priority="primary", quote="少手忙脚乱",
            goals=["快速搞定辅食"], behaviors=["晚 21 点后用手机"],
            attitudes=["怕错过孩子需求"], bio="二孩妈，34岁...")

profile = builder.profiles[0]
lib = PersonaPromptLibrary()

# 1. 模拟访谈
prompt = lib.simulated_interview(
    profile,
    task="评估新功能：'一键周末辅食备餐'",
    questions=["你愿意试吗？为什么？", "什么会让你放弃？"],
)
print(prompt.system)  # 系统提示
print(prompt.user)    # 用户提示

# 2. 文案评估
prompt = lib.copy_evaluation(
    profile,
    copy_text="3 分钟搞定全周辅食，省心妈妈都在用",
    rubric=["共鸣度 1-5", "可信度 1-5", "可行动 1-5"],
)
```

---

## 4. 提示工程的 5 大原则

| 原则 | 一句话 |
|---|---|
| 1. Constitutional 约束 | 显式禁止幻觉、编数字、超出角色 |
| 2. Anchor with Quotes | 注入真实引语保持语言风格 |
| 3. 接受不完美 | 让 Persona 表达犹豫、矛盾、抗拒 |
| 4. 明确产出格式 | 指定 JSON / 表格 / 自然语言 |
| 5. 标注合成属性 | 输出末尾自带"（synthetic, model=X）"声明 |

---

## 5. 与 PersonaBuilder 的整合

模块直接消费 `persona_builder.PersonaProfile`，无需重复定义字段。

```python
class PersonaPromptLibrary:
    def simulated_interview(self, profile, *, task, questions, language="zh"): ...
    def copy_evaluation(self, profile, *, copy_text, rubric, language="zh"): ...
    def devils_advocate(self, profile, *, target, angle="skeptic", language="zh"): ...
    def multi_persona_tournament(self, profiles, *, scenarios, rubric, language="zh"): ...
```

---

## 6. 安全审计字段（v2.6 新增）

每个生成的 PersonaPrompt 自带 metadata：

```python
@dataclass
class PersonaPrompt:
    system: str
    user: str
    metadata: Dict[str, Any]   # persona_id, task, language, generated_at
    safety_warnings: List[str] # 用法限制提示
```

---

## 7. 反模式 (Anti-patterns)

| 反模式 | 症状 | 修复 |
|---|---|---|
| 不写 Constitutional | LLM 编 73% 之类幻觉数字 | 强制注入"不准编数字"约束 |
| 把模拟当真实数据 | 写进 PRD 当用户访谈 | 输出末尾强制声明合成属性 |
| 过度同质化 | 多 Persona 输出相似 | 引入 diversity 提示 + 真实引语 |
| 角色泄露 | LLM 跳出 Persona 自称 AI | system prompt 强约束 + 后处理过滤 |
| 不留审计 | 不存 prompt + 输出 | metadata 字段 + 时间戳 |

---

## 8. 何时使用本模块

✅ 用：
- 早期 brainstorm 候选文案/功能
- Persona Tournament 找普适方案
- Devil's Advocate 找盲点
- 教学 / 培训演练

⛔ 不用：
- 替代真实用户访谈
- 影响真实用户决策的关键节点
- 不审计的全自动化

---

## 9. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| 18-Synthetic AI 方法论 | 本模块即其代码实现 |
| `persona_builder.PersonaProfile` | 直接消费现有 Persona |
| 27-bias-audit | 输出后必跑 LLM 偏差审计 |
| 30-okr-bridge | 模拟评估 → 转化为 KR |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| 4 种 prompt 类型 | 访谈/评估/反向/Tournament |
| 不耦合 LLM SDK | 仅输出字符串 |
| Constitutional 约束 | 抑制幻觉 |
| 合成属性显式标注 | 避免误用 |
| 与现有 Profile 集成 | 无需重复字段 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `virtual-user-interview` | 飞猪虚拟访谈直接套用本库 |
| `landing-page` | 多 Persona 评估落地页副本 |
| `prd-writing` | PRD 场景章节用模拟访谈生成草稿 |
| `competitive-analysis` | Persona Tournament 评估竞品文案 |
