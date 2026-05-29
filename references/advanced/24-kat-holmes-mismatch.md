# 24 · Kat Holmes《Mismatch》：包容性设计的方法论

> 来源：Holmes, K. *Mismatch: How Inclusion Shapes Design* (MIT Press, 2018)；Microsoft *Inclusive Design Toolkit* (2016/2019)；Microsoft *Inclusive 101* and *Persona Spectrum* materials；Disability Design Standards & W3C WCAG 2.2。
>
> Kat Holmes 是 Microsoft 包容性设计的奠基人，*Mismatch* 是 Persona Spectrum 概念的方法论之根。本笔记把"残障""能力""包容"从可有可无的合规话题，转化为 Persona 设计的核心轴线。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | Inclusive 视角（本笔记） |
|---|---|---|
| 关注核心 | 主流目标用户 | 包括边缘 / 残障 / 临时受限用户 |
| Persona 单位 | 平均/代表 | 谱系 (Spectrum)：永久/临时/情境 |
| 失败诊断 | 难用 | "排斥习惯" (Exclusion Habit) |
| 输出 | 几张主 Persona | 主 Persona + Edge Personas + Spectrum |
| 适合场景 | 注册转化、Web 任务 | 任何想长期可持续的产品 |

> 💡 **核心立场**：包容不是"做完主流再加 a11y"——把 Spectrum 嵌入早期 Persona 工作 = 同样工作量，覆盖更广。Holmes 的论证：包容性设计反而生出更多创新（OXO 厨具、字幕、电动牙刷源头都是无障碍设计）。

---

## 2. Mismatch 核心公式

> **Disability is not a personal health condition. Disability is a mismatched human interaction with the designed world.**
> 
> 残障不是个人状况。残障是人与设计世界的"错配"。

| 视角 | 含义 |
|---|---|
| 个人模型 (Medical Model) | 把残障归因于个人缺陷 |
| 社会模型 (Social Model) | 残障是设计未考虑差异的结果 |
| 错配模型 (Mismatch Model) | 任何能力差异 + 不合适设计 = 临时残障 |

> 戴墨镜在阳光下看不清屏幕 = 你也是临时视障；推婴儿车爬楼 = 临时肢障。残障不是"他们"的事。

---

## 3. Persona Spectrum（核心工具）

| 类型 | 定义 | 例（视障） | 例（语言） |
|---|---|---|---|
| **Permanent** | 永久 | 视觉缺失 | 失语症 |
| **Temporary** | 临时（数小时-数月） | 眼科手术后 | 口腔术后 |
| **Situational** | 情境 | 强光/夜间驾驶 | 嘈杂酒吧 |

> 💎 **重要发现**：每 1 名永久用户，对应数十万临时/情境用户。设计为永久 = 同时服务大量临时/情境用户。

### 3.1 Spectrum 模板

```
能力轴：视觉
├── Permanent: 全盲（约 0.5%-1% 人口）
├── Temporary: 眼科术后（每年 5%）
├── Situational: 阳光/夜间/疲劳（每天 30%+）

设计含义：
- 高对比度 + 大字号 → 服务三类共 35%+ 用户
- 屏幕阅读器兼容 → 服务永久用户兼提升 SEO
- 语音交互 → 服务三类 + 通勤用户
```

---

## 4. 排斥习惯 (Exclusion Habits)：5 类典型

| 习惯 | 症状 | 改进 |
|---|---|---|
| **Test On Self** | 设计师拿自己测试 | 招募真实多样化用户 |
| **Average Persona** | 用平均人设代替谱系 | Spectrum + Edge |
| **Default Body** | 默认健全成年男性体型 | 不同身体能力同等考虑 |
| **English-First** | 默认英语后翻译 | 多语言并行设计 |
| **Tech-Optimist Bias** | 假设用户有最新设备 | 低端设备/弱网/老旧浏览器 |

> 习惯不是恶意，但累积起来 = 系统性排斥。Holmes 主张**列出团队的"排斥习惯"** → 写到 review checklist。

---

## 5. Inclusive Design 3 原则（Microsoft Toolkit）

| 原则 | 含义 | 例 |
|---|---|---|
| **Recognize Exclusion** | 识别排斥 | 主动检索：谁可能用不了？ |
| **Learn from Diversity** | 向多样性学习 | 残障是创新源头 (One-Handed → Whole world) |
| **Solve for One, Extend to Many** | 为一人解决，推及多人 | OXO 关节炎握把 → 所有人 |

---

## 6. Edge Persona vs Extreme User

| 概念 | 含义 | 用途 |
|---|---|---|
| **Edge Persona** | 系统未考虑/被排斥的群体 | 揭示设计盲点 |
| **Extreme User** | 行为/需求极端的用户 | IDEO 设计研究法，激发创新 |

> 二者不同——Edge 是"被排除"，Extreme 是"被忽视的极端使用者"。两者都重要，但 Holmes 强调 Edge。

---

## 7. 谁在 / 谁不在：Stakeholder Mapping for Inclusion

设计前 5 问：

1. 谁会用这个产品？谁不会用？为什么？
2. 谁参与设计了？谁没机会发声？
3. 我们假设了什么默认能力？哪些用户不符合？
4. 错配可能在哪个触点出现？
5. 修了之后还会服务到哪些非目标用户？

> 这 5 问写进 PRD 模板，能在早期暴露 80% 的排斥问题。

---

## 8. Persona × Spectrum 整合模板

```yaml
persona_id: lin_jia
ability_spectrum:
  - axis: vision
    permanent_estimate: "她无；目标用户中约 0.7% 永久视障"
    temporary: "戴隐形眼镜不适；眼睛疲劳"
    situational: "夜间哄睡时摸黑用手机；强光下"
    design_implication: "深色模式 + 大字号 + 单手大触控区"
  
  - axis: motor
    permanent_estimate: "她无；目标用户中约 1.2% 永久肢障"
    temporary: "怀孕、产后腕管综合征"
    situational: "单手抱娃、抱购物袋"
    design_implication: "重要操作可单手完成；按钮 ≥ 44pt"
  
  - axis: cognitive
    permanent_estimate: "她无；约 4% ADHD/SLD"
    temporary: "睡眠不足导致专注力下降"
    situational: "多任务打断 → 中断后重新进入"
    design_implication: "断点续做、自动保存、清晰上下文"

  - axis: language
    permanent_estimate: "目标用户母语中文；约 5% 含方言/低识字率"
    temporary: "外语阅读疲劳"
    situational: "嘈杂环境 → 文字优于语音"
    design_implication: "图标+文字双标签；避免行业 jargon"

inclusive_review:
  exclusion_habits_audit:
    - "团队 8 名全员视力正常 → 加视障志愿者 review"
    - "默认横屏测试 → 加单手竖屏测试"
  edge_personas:
    - "陈奶奶, 67, 替女儿带娃，老花眼，触屏迟钝"
    - "王医生, 38, 远程问诊，戴医用手套操作"
```

---

## 9. 反模式 (Anti-patterns)

| 反模式 | 症状 | 后果 |
|---|---|---|
| **A11y 在最后** | 上线前临时加无障碍 | 改造成本高、效果差 |
| **A11y 是合规** | 仅满足 WCAG AA | 形式合规但实际不可用 |
| **Token Edge Persona** | 加 1 个轮椅形象当装饰 | 表面包容、内核排斥 |
| **不招募多样用户测试** | 用研只有大学生 | 排斥盲区不被发现 |
| **过度泛化** | "所有人通用" | 失去具体 Persona 焦点 |
| **悲情叙事** | Edge 用户被描绘为可怜 | 失去尊严的设计 |
| **Disability ≠ Old Age** | 把老人都当残障 | 误解，且老年用户也是 Spectrum 一部分 |

---

## 10. 何时使用 Inclusive 视角

✅ 用：
- 任何长期产品（包容性是可持续的护城河）
- 公共服务、政府数字化、医疗、教育
- 年龄差异大的用户群
- 海外/跨文化扩展（语言+文化都是 Spectrum）
- 法务/合规要求（WCAG / ADA / EAA）

⛔ 不用：
- 极小团队 + 极快 MVP（但应记录 IOU 清单）
- 内部工具（用户单一）— 但仍需考虑临时受限场景

---

## 11. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/persona_builder.py` | 增加 `ability_spectrum` 字段 |
| `persona/inclusive_review.py`（v2.6 新增） | 排斥习惯 audit + Spectrum 检查 |
| 15-Critique-Defense | 应对"Persona 排除少数"的批评 |
| 25-Cababa | 排斥的二阶后果 |
| 27-bias-audit | 偏差审计的具体清单 |
| 31-measurement | 包容性指标（A11y 完成率、Edge Persona 采访次数） |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| Mismatch 模型 | 残障是人与设计的错配，不是个人缺陷 |
| Spectrum 三类 | Permanent / Temporary / Situational |
| Solve for One | 为一人解决，自然推及多人 |
| 排斥习惯 5 类 | 自我测试/平均/默认体/英语/技术乐观 |
| Edge ≠ Extreme | Edge 是被排除，Extreme 是极端使用 |
| 包容是早期工作 | 不是 a11y 阶段附加的合规 |
| Persona 携带 Spectrum | 与文化/能力/语言四维同时考虑 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `frontend-design` | UI 组件按 Spectrum 设计 |
| `prd-writing` | PRD 加 Inclusive Review 段 |
| `code-review` | 代码层面 a11y review |
| `consulting-issue-tree-mece` | "谁不在"维度纳入 issue tree |
| `decision-tracker` | Edge Persona 决策跟踪 |
| `seo-technical` | 包容性设计 + SEO 双赢点 |

---

> 📚 **延伸阅读**：
> - Holmes, K. (2018). *Mismatch: How Inclusion Shapes Design*. MIT Press.
> - Microsoft (2016/2019). *Inclusive Design Toolkit*: https://www.microsoft.com/design/inclusive/
> - Sara Hendren *What Can a Body Do?* (2020)：哲学性深化。
> - Liz Jackson *The Disabled List*：残障设计师视角。
> - W3C *WCAG 2.2*（合规基线，但仅是起点）。
> - 中国情境：腾讯 *无障碍 OA*；阿里 *看见无障碍*；信息无障碍研究会公开材料。
