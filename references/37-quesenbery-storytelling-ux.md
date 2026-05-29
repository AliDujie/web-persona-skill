# 37 — Whitney Quesenbery & Kevin Brooks · Storytelling for User Experience: Crafting Stories for Better Design (2010)

> **Tier F · 体验地图与叙事**｜关键词：UX Storytelling、Persona Narrative、Scenario Writing、Stakeholder Communication、Story Structure

---

## 一、核心定位

这本书解决的是"Persona 写了没人看"的痼疾。**好的 Persona 不是数据表——是故事**。Quesenbery & Brooks 提供了完整的"UX 叙事工程学"：什么时候用什么类型的故事、故事的结构怎么搭、怎么让利益相关者在情感上接纳用户视角。

### 1.1 为什么 Persona 需要故事

| 纯数据 Persona | 故事化 Persona |
|---|---|
| "25-35岁，男性，月入2万" | "小王每天早上7:50挤上地铁，单手刷手机比价…" |
| 被读一次就塞进抽屉 | 被反复引用、口口相传 |
| 只有UX团队看 | 开发、CEO、市场都在讨论 |
| 抽象、难共情 | 具象、引发行动 |

---

## 二、UX 故事的五种类型

### 2.1 类型总览

| # | 故事类型 | 用途 | 长度 | Persona 关系 |
|---|---|---|---|---|
| 1 | Origin Story | 解释"为什么做这个产品" | 1-2 段 | 绑定核心 Persona 的核心 Pain |
| 2 | Concept Story | 描绘未来愿景 | 0.5-1 页 | 展示 Persona 的理想体验 |
| 3 | Scenario | 具体使用场景 | 1-3 段 | Persona × Context × Task |
| 4 | Persona Story | 人物背景叙事 | 1-2 页 | Persona 核心文档的一部分 |
| 5 | Persuasion Story | 说服利益相关者 | 30 秒口述 | 用 Persona 痛点推动决策 |

### 2.2 选择决策

```
你想达成什么？
├── 让团队理解"为什么做" → Origin Story
├── 让团队想象"做成后什么样" → Concept Story
├── 指导交互设计细节 → Scenario
├── 让 Persona 活起来 → Persona Story
└── 推动一个具体决策 → Persuasion Story
```

---

## 三、故事的结构学（Story Anatomy）

### 3.1 核心五要素

| 要素 | UX 对应 | 示例 |
|---|---|---|
| Character | Persona | "效率达人小王" |
| Setting | Context（时间/地点/设备/情境） | "周五晚高峰，手机4G信号弱" |
| Conflict | Pain Point / Obstacle | "搜了5分钟找不到想要的酒店" |
| Action | 用户的行为/决策 | "放弃搜索，打开竞品App" |
| Resolution | 结果（好/坏/悬念） | "在竞品30秒完成预订" |

### 3.2 三幕结构在 UX 中的应用

```
Act I · Setup     → Persona + Context + 需求/目标
Act II · Conflict → 使用产品时遇到的障碍/摩擦
Act III · Resolution → 成功解决 / 失败流失 / 寻找替代方案
```

### 3.3 故事弧线与情绪曲线

```
情绪 ↑
     │     ╭──╮ 期望高峰
     │    ╱    ╲
     │   ╱      ╲──╮ 挫折低谷
     │  ╱           ╲
     │ ╱             ╲───── 放弃/或回升
     │╱
     └──────────────────────── 时间 →
```

- 情绪曲线 = Journey Map 的 Feelings 行的叙事化版本
- 同一组数据，表格版给分析，故事版给共情

---

## 四、Persona Story 写作指南

### 4.1 结构模板

```markdown
## [Persona 名称] 的故事

### 背景
[1-2 段描述这个人的生活/工作环境、核心驱动力]

### 一天的场景
[用第三人称叙述一个典型日/关键事件]
- 时间锚点（早晨/通勤/午休/晚上）
- 具体细节（设备、环境、心理状态）
- 自然引出与产品的接触点

### 关键时刻
[描述一个 Moment of Truth：决策/挫折/惊喜]

### 心声
> "[用第一人称，一句话概括这个人最深的需求/焦虑]"
```

### 4.2 写作六原则

| # | 原则 | 反面 |
|---|---|---|
| 1 | 具体（Concrete） | "他有时候会…" → "周三下午3点他…" |
| 2 | 可信（Credible） | 超人般完美 → 有弱点/限制 |
| 3 | 有情感（Emotional） | 冷冰冰数据 → 有焦虑/期待/失望 |
| 4 | 有冲突（Conflict） | 一帆风顺 → 遇到障碍才有故事 |
| 5 | 简洁（Concise） | 3 页流水账 → 1 页精华 |
| 6 | 有行动意义（Actionable） | 读完"哦好感人" → 读完"我们应该改X" |

---

## 五、Scenario 写作详解

### 5.1 四类 Scenario

| 类型 | 用途 | 示例 |
|---|---|---|
| Context Scenario | 探索：这个人在什么情境下会用产品？ | "小王出差前一晚…" |
| Key Path Scenario | 设计：核心任务的理想流程 | "搜索→筛选→预订→确认" |
| Validation Scenario | 测试：能否完成？会卡在哪？ | 可用性测试脚本 |
| Edge Case Scenario | 防御：异常情况怎么处理？ | "网络断了/输入错误/退款" |

### 5.2 Scenario 写作公式

```
[Persona] + [Context/Trigger] + [Goal] + [Actions] + [Outcome]

示例：
"效率达人小王(Persona)在出差前一晚(Context)想快速订到公司附近的酒店(Goal)，
 他打开App搜索、用地图筛选、看了3条评价后下单(Actions)，
 全程2分钟完成，收到确认短信(Outcome)"
```

---

## 六、故事的受众适配

### 6.1 不同听众需要不同故事

| 受众 | 关心什么 | 故事重点 |
|---|---|---|
| CEO/高管 | 商业影响、市场机会 | 流失成本、转化率故事 |
| 工程师 | 技术约束、可行性 | 异常场景、边界条件 |
| 设计师 | 用户情感、交互细节 | 情绪曲线、微时刻 |
| 市场/运营 | 用户语言、传播性 | 用户原话、口碑场景 |
| 客服 | 常见问题、痛点 | 投诉/求助场景 |

### 6.2 "电梯故事"（30 秒版）

```
模板：
"我们的用户 [Persona名] 经常 [痛点行为]，
 因为 [根因]。
 如果我们 [方案]，
 他们就能 [期望结果]。"

示例：
"我们的用户小王经常在出差前一晚花30分钟比价酒店，
 因为现有搜索结果排序和他的偏好不匹配。
 如果我们加入个性化推荐，
 他就能在2分钟内完成预订，不再流失到竞品。"
```

---

## 七、视觉叙事技巧

### 7.1 故事 + 视觉 = 双重编码

| 技巧 | 方法 | 效果 |
|---|---|---|
| Storyboard | 4-6 格漫画 | 非设计师也能秒懂流程 |
| Photo Persona | 真实照片+场景图 | 增强真实感 |
| Day-in-the-Life Video | 1-2 分钟剪辑 | 高管注意力收割器 |
| Quote Cards | 一张卡=一句用户原话+照片 | 贴墙/Slack 传播 |
| Journey Comic | 旅程地图漫画化 | 长走廊/办公室展示 |

### 7.2 Persona Poster 设计要素

```
┌────────────────────────────────────────┐
│ [Photo]  Name · Archetype Tagline      │
│                                        │
│ "一句话心声引用"                         │
│                                        │
│ ┌──────────┐  ┌──────────┐            │
│ │ Goals    │  │ Pains    │            │
│ └──────────┘  └──────────┘            │
│                                        │
│ 一个典型场景的 2-3 句叙事               │
│                                        │
│ Key Behaviors: □□□□□ (可视化尺度)       │
└────────────────────────────────────────┘
```

---

## 八、故事的验证（Story Testing）

### 8.1 三层验证

| 层次 | 验证方法 | 通过标准 |
|---|---|---|
| Authenticity（真实） | 给受访者看："这像你吗？" | 至少 3/5 人认为"很像" |
| Resonance（共鸣） | 给团队看："你遇到过这种人吗？" | 开发+市场能补充细节 |
| Actionability（可行动） | 给设计师看："这让你想到什么改进？" | 能具体列出 2+ 设计行动 |

### 8.2 故事迭代

```
Draft Story → Internal Review (团队)
  → Validation Interview (用户)
  → Revise → Final Story → 纳入 Persona Document
```

---

## 九、反模式

| # | 反模式 | 后果 | 修复 |
|---|---|---|---|
| 1 | Data Dump | Persona 是统计报告，无人阅读 | 加 1 段故事 + 1 句心声 |
| 2 | Fiction（纯编造） | 听起来好但与现实脱节 | 每句叙述可追溯到访谈数据 |
| 3 | Happy-only Story | 只讲成功路径 | 必须有 Conflict（痛点/挫折） |
| 4 | One Story Fits All | 给所有受众讲同一版 | 按受众调整重点和长度 |
| 5 | Story Without Persona | 泛泛"用户"无具体人物 | 绑定特定 Persona |
| 6 | Too Long | 3 页没人看完 | 电梯版 30 秒 + 完整版 1 页 |
| 7 | 无后续行动 | 故事变"情感消费" | 每个故事末尾附"设计启示" |

---

## 十、Persona 叙事质量评估

| 维度 | 1 分（差） | 5 分（优） |
|---|---|---|
| 具体性 | "有些用户有时候…" | "小王每周三下午3点…" |
| 情感性 | 冷冰冰的属性列表 | 读完你能感受到焦虑/期待 |
| 可信度 | 像广告文案 | 像纪录片旁白 |
| 冲突性 | 一帆风顺 | 有明确的障碍/决策点 |
| 行动性 | 读完"嗯了解了" | 读完"我们应该改X" |
| 简洁性 | 3 页 | 1 页以内 |

---

## 本部分核心要点总结

1. **Persona 的终极考验是"有没有人在日常决策中引用它"**——故事是让 Persona 被记住的唯一手段
2. **五种故事类型适配五种场合**：不要用 Concept Story 做可用性测试，不要用 Scenario 说服 CEO
3. **故事五要素 = Character + Setting + Conflict + Action + Resolution**
4. **30 秒电梯版是最小可用单位**：能在走廊里口述的 Persona 故事才是活的 Persona
5. **可追溯性保障真实性**：每句叙述背后应该有访谈数据支撑
6. **故事需要按受众适配**：CEO 看商业影响，工程师看边界条件

---

## 🔗 跨技能协作

| 场景 | 推荐协作 Skill |
|---|---|
| Persona 叙事化表达 | `web-persona-skill` 主流程 |
| Journey Map 可视化 | `36-kalbach-mapping-experiences` |
| 用户原话采集 | `32-portigal-interviewing-users` |
| 故事转为设计 Scenario | `prd-writing` |
| 数据故事化 | `storytelling-with-data` |
| 故事用于汇报 | `ceo-weekly-final` / `gm-weekly-final` |
