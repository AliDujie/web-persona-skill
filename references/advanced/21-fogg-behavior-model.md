# 21 · Fogg 行为模型：B = MAT 与 Tiny Habits

> 来源：Fogg, BJ. *Tiny Habits: The Small Changes That Change Everything* (Houghton Mifflin Harcourt, 2019)；Fogg, BJ. *A Behavior Model for Persuasive Design* (Persuasive '09)；Stanford Behavior Design Lab 公开材料；Hooked: Eyal, N. *Hooked: How to Build Habit-Forming Products* (Portfolio, 2014)。
>
> Fogg 的核心公式：**B = MAT**，行为发生 = 动机 × 能力 × 触发器三者同时齐备。这条公式让"为什么用户没行动"变成可诊断、可干预的工程问题。本笔记把 Fogg 模型嵌入 Persona，让每个角色的行为概率可设计、可测量。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | Fogg 行为模型（本笔记） |
|---|---|---|
| 角色单位 | 静态人物画像 | 行为发生概率 = M × A × T |
| 关注问题 | 用户是谁、想要什么 | 为什么没动？ / 怎样让他动？ |
| 工具 | 卡片、目标列表 | Behavior Grid、Tiny Habits Recipe |
| 输出 | Persona 文档 | Persona × 行为干预清单 |
| 适合场景 | 设计静态体验 | 改变行为（健康、教育、储蓄、留存） |
| 失败诊断 | UI 不好、流程乱 | M / A / T 哪一项太低 |

> 💡 **互补立场**：Mulder 描绘"角色"，Fogg 拆解"行为"。两者结合 → Persona 不只是画像，而是携带可触发行为公式的"行动包"。

---

## 2. B = MAT 公式

```
Behavior = Motivation × Ability × Trigger
```

| 因子 | 含义 | 三连示例（健身 App） |
|---|---|---|
| **M (Motivation)** | 动机：感受 / 期望 / 归属 | 想瘦想健康想被认可 |
| **A (Ability)** | 能力：时间/钱/体力/脑力/环境/惯例 | 5 分钟内能完成的运动 |
| **T (Trigger)** | 触发：火花/促进/信号 | App 推送或闹钟 |

> 💎 **Fogg 黄金率**：M 难改、A 易改 → **优先把行为变得更容易**，而非鸡血般提升动机。这条与"鸡汤式产品"思路相反。

---

## 3. Behavior Grid（行为网格）

Fogg 把行为按 5 个维度组合成 15 类（5 类型 × 3 时长）：

| 类型 | Green（一次） | Blue（一段时间） | Purple（永久） |
|---|---|---|---|
| **Dot** 做新行为 | 一次安装 App | 试用 30 天 | 永久使用 |
| **Span** 增加现行为 | 多走 1 公里 | 一周多走 10 公里 | 每天多走 1 公里 |
| **Path** 减少行为 | 少喝 1 杯咖啡 | 减咖啡因 1 个月 | 永久减咖啡因 |
| **Wash** 停止行为 | 跳过 1 次广告 | 1 周不熬夜 | 永久戒熬夜 |
| **Decrease** | — | — | — |

> 给 Persona 的每条行为打 Behavior Grid 标签 → 知道该用哪种干预。**新建永久行为**最难，需 Tiny Habits（见 §5）。

---

## 4. 触发器三类型 (Triggers)

| 类型 | 适用场景 | 示例 |
|---|---|---|
| **Spark（火花）** | 动机低 + 能力够 | 鼓舞人心的视频、社会证明 |
| **Facilitator（促进）** | 动机高 + 能力低 | "一键下载""教程视频" |
| **Signal（信号）** | 动机高 + 能力够，差临门一脚 | 推送、闹钟、提醒 |

⚠️ 错配最常见：动机低却使劲推 Signal → 厌烦、关推送、卸载。**先诊断，再触发**。

---

## 5. Tiny Habits 法（Fogg 2019）

让永久行为生根的工程化方法，3 步：

### 5.1 ABC 公式

```
After I [现有锚点 Anchor],
I will [极小新行为 Behavior],
to feel [庆祝 Celebration].
```

### 5.2 Tiny Habits 七纪律

| 纪律 | 一句话 |
|---|---|
| 1. 极小 (Tiny) | 行为缩到 30 秒内能做完 |
| 2. 锚定 (Anchor) | 嫁接到已有日常行为后 |
| 3. 庆祝 (Celebrate) | 立即正向情绪强化 |
| 4. 弹性 (Elastic) | 心情好做满，不好做最小版 |
| 5. 接受失误 (Forgive) | 漏一天不沮丧，第二天接上 |
| 6. 系统视角 (System) | 不靠意志力，靠环境/惯例设计 |
| 7. 演进 (Grow) | 习惯稳定后再加量 |

### 5.3 Persona × Tiny Habits 配方示例

> Persona: 高强, 41, 软件工程师, 想戒夜宵但已失败 5 次

```
After I close my laptop at 22:00,
I will drink one glass of warm water,
to feel "I'm taking care of myself tonight".
```

——比"今晚开始不吃夜宵"成功率高 6-10 倍（Fogg 实验数据）。

---

## 6. Hooked 模型：Persona × 习惯产品（Eyal, 2014）

Eyal 在 Fogg 基础上提出 4 步循环：

| 阶段 | 含义 | 设计要点 |
|---|---|---|
| **Trigger** | 外部 → 内部触发演进 | 推送/邮件 → 习得性"无聊就开" |
| **Action** | 简单行为 | B = MAT 现身 |
| **Variable Reward** | 不可预测奖励 | 三类：tribe（社交认同）/ hunt（信息发现）/ self（精进感） |
| **Investment** | 用户投入 | 内容、关注、积分、个性化 → 形成转换成本 |

> ⚖️ **伦理告诫**：Hooked 是双刃剑——可造正向习惯（学习/健身），也可造成瘾（赌博/无限滚动）。Eyal 后来写了 *Indistractable* 反思过度成瘾。Persona 设计师必须做意图审查。

---

## 7. Persona × Fogg 落地模板

```yaml
persona_id: lin_jia
behavior_target: "每周打开 App ≥ 4 次"

motivation:
  level: medium
  drivers:
    - "孩子健康"
    - "省时间"
  blockers:
    - "信息过载"
    - "怀疑功效"

ability:
  level: low
  obstacles:
    time_cost: "10 分钟（高于她的 5 分钟阈值）"
    cognitive: "首页太复杂"
    money: "免费即可"
  improvements:
    - 首屏 3 秒抓住核心信息
    - 推送时段调到 21:00（孩子入睡后）

triggers:
  current: "每日 9:00 push（命中率 12%）"
  proposed:
    type: "Signal"
    timing: "21:05"
    anchor: "After kids sleep"
    copy: "5 分钟看完今日辅食推荐"
  
tiny_habits_recipe:
  after: "After I tuck in the kids at 21:00"
  i_will: "Open the App and read one tip"
  to_feel: "I'm a thoughtful mom tonight"

success_metric:
  week_4_open_rate: 25%   # 当前 12%
  month_3_retention: 40%  # 当前 22%
```

---

## 8. 反模式 (Anti-patterns)

| 反模式 | 症状 | 后果 |
|---|---|---|
| **狂打鸡血** | 不停推送鼓舞内容 | 动机不稳，脱敏 |
| **行为太大** | 让用户"每天 30 分钟" | 多数失败 |
| **缺锚点** | 让用户"每天某时" | 没有具体生活钩子 → 忘 |
| **滥用 Variable Reward** | 无限滚动 / 老虎机式 | 注意力剥削、监管风险 |
| **触发不分类** | 都用 Signal | 动机低用户被骚扰 |
| **跳过庆祝** | 完成无反馈 | 习惯不固化 |
| **不诊断 MAT** | 直接堆功能 | 不知道哪一项卡住 |

---

## 9. 何时使用 Fogg 模型

✅ 用：
- 习惯型产品（健身 / 学习 / 储蓄 / 阅读）
- 留存提升项目
- 改变用户长期行为
- 漏斗优化（看 M/A/T 哪一段流失）
- 教育 / 公共健康 / 政策 Nudge

⛔ 不用：
- 一次性任务（购票、找路）→ Mulder/Cooper 即可
- 强目标驱动场景（DDL 已存在）→ 触发自然存在
- 完全无动机用户 → Fogg 也救不了，先诊断为什么动机为零

---

## 10. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/persona_builder.py` | 增加 `motivation_level`, `ability_obstacles`, `trigger_strategy` |
| 02-measuring-results | M/A/T 漏斗指标分别测量 |
| 20-Kahneman | Fogg 与 System 1 配合：让正确行为变 System 1 |
| 22-JTBD | Job → Trigger 自然映射 |
| 30-OKR-Bridge | 行为目标 → KR 落地 |
| 31-measurement | Tiny Habits 留存追踪指标 |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| B = MAT | 行为 = 动机 × 能力 × 触发，缺一不可 |
| 优先降难度 | A 比 M 容易改，先把行为变小 |
| Tiny Habits 是工程 | ABC 公式 + 7 纪律 |
| 三类触发 | Spark / Facilitator / Signal 按 M/A 状况选 |
| Behavior Grid | 给行为分类→选合适干预 |
| Hooked 有伦理边界 | Variable Reward 不能滥用 |
| Persona 携带 MAT | 把行为概率写进 Persona 卡片 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `onboarding-flow` | 新用户激活 = Tiny Habits 第一次执行 |
| `churn-analysis` | 流失诊断 = M/A/T 哪一项失效 |
| `nps-weekly-pipeline` | NPS 提升 = 把核心行为做成习惯 |
| `analytics-data-analysis` | 行为日志拆 M/A/T 漏斗 |
| `landing-page` | Spark 类触发器的设计 |
| `support-docs` | Facilitator 类触发器的承载 |

---

> 📚 **延伸阅读**：
> - Fogg (2019). *Tiny Habits*. 全书。
> - Eyal (2014). *Hooked*；Eyal (2019). *Indistractable*（反思版）。
> - Duhigg, C. (2012). *The Power of Habit*：Cue-Routine-Reward 与 Fogg 互补。
> - Wendel, S. (2020). *Designing for Behavior Change*（更工程化的整合）。
> - Stanford Behavior Design Lab: https://behaviordesign.stanford.edu/
