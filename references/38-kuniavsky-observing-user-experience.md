# 38 — Mike Kuniavsky · Observing the User Experience: A Practitioner's Guide to User Research (2nd ed., 2012)

> **Tier F · 观察方法与综合研究**｜关键词：用户研究全流程、Contextual Inquiry、可用性测试、定量+定性方法选择、研究项目管理

---

## 一、核心定位

Kuniavsky 是"用研方法百科全书"——覆盖从项目规划、招募、定性/定量方法执行到分析报告的**全生命周期**。如果说 Portigal 聚焦"访谈"一个方法的精深，Kuniavsky 则给出"方法菜单+选择逻辑"。对 Persona Skill 而言，它回答：**在做 Persona 之前和之后，还有哪些研究方法可以配合？**

### 1.1 研究方法 × Persona 阶段映射

| Persona 阶段 | 适合的研究方法 | Kuniavsky 覆盖章节 |
|---|---|---|
| 前期发现（谁是用户） | Contextual Inquiry / Survey / Log Analysis | Ch 6-8 |
| 数据采集（行为深挖） | Depth Interview / Diary Study / Field Observation | Ch 9-12 |
| 验证（Persona 是否准确） | Usability Test / A/B Test / Card Sort | Ch 13-16 |
| 量化校准 | Survey / Analytics / Task Analysis | Ch 17-19 |
| 持续监测 | NPS / Support Ticket Mining / Heuristic Review | Ch 20-22 |

---

## 二、研究方法选择矩阵

### 2.1 四象限框架

```
         定性（Why）          定量（How many）
    ┌─────────────────────┬─────────────────────┐
态  │ Contextual Inquiry  │ Survey              │
度  │ Depth Interview     │ A/B Test            │
/   │ Diary Study         │ Analytics (行为日志) │
行  │ Field Observation   │ Card Sort (量化版)  │
为  ├─────────────────────┼─────────────────────┤
    │ Usability Test      │ Task Analysis       │
    │ Think-Aloud         │ Eye Tracking        │
    │ Heuristic Review    │ Funnel Analysis     │
    │ Expert Review       │ Benchmark Test      │
    └─────────────────────┴─────────────────────┘
       探索性（Generative）    评估性（Evaluative）
```

### 2.2 方法选择决策树

```
你已经有产品/原型了吗？
├── No → Generative Research
│   ├── 想了解"为什么" → Contextual Inquiry / Interview
│   └── 想了解"有多少人" → Survey / Market Research
└── Yes → Evaluative Research
    ├── 想了解"能不能用" → Usability Test
    └── 想了解"用得好不好" → Analytics / NPS / Task Metrics
```

---

## 三、Contextual Inquiry 详解

### 3.1 核心原则（Beyer & Holtzblatt 四原则）

| 原则 | 含义 | 操作 |
|---|---|---|
| Context | 在用户真实环境中观察 | 去他们的工位/家里/咖啡馆 |
| Partnership | 研究者和用户是伙伴 | "你做，我看；我不懂就问" |
| Interpretation | 当场确认理解 | "我看到你刚才…是因为…对吗？" |
| Focus | 有明确的观察焦点 | 不是漫无目的看一整天 |

### 3.2 CI Session 结构

| 阶段 | 时间 | 活动 |
|---|---|---|
| Introduction | 10 min | 解释目的、获得同意、说明"请像平时一样" |
| Observation | 60-90 min | 观察+追问（Partnership 模式） |
| Wrap-up | 15 min | 总结观察、确认解读、感谢 |

### 3.3 CI 产出 → Persona 输入

| CI 观察到的 | Persona 维度 |
|---|---|
| 工作环境（桌面/工具/屏幕布局） | Context / Technology |
| 任务流程（step-by-step） | Behavioral Variables |
| 中断/Workaround | Pain Points |
| 自言自语/情绪反应 | Attitudes / Motivations |
| 与他人的交互 | Social Context / Collaboration |

---

## 四、Diary Study（日记研究）

### 4.1 适用场景

- 需要了解**一段时间内**的行为模式（而非单次访谈能捕获的）
- 行为分散在不同时间点（如：旅行规划从"想去"到"出发"可能跨 2-8 周）
- 用户自己可能也不记得所有细节

### 4.2 日记研究设计

| 要素 | 典型设置 |
|---|---|
| 时长 | 1-4 周 |
| 频率 | 每天 1-3 次记录 / 或事件触发 |
| 媒介 | 微信小程序/App内弹窗/纸质日记/语音备忘 |
| 内容 | 时间+地点+做了什么+感受+照片 |
| 样本量 | 10-20 人 |
| 激励 | 日常小额+完成奖金（防流失） |

### 4.3 日记 → Persona 映射

- 日记数据天然带**时间维度** → 可直接转化为 Journey Map 的 Phases
- 多人日记对比 → 发现行为聚类（"周末型" vs "碎片型"） → 指导 Persona 切分
- 日记中的照片/截图 = Contextual Inquiry 的远程替代品

---

## 五、可用性测试与 Persona 验证

### 5.1 基于 Persona 的测试招募

| 维度 | 做法 |
|---|---|
| 筛选标准 | 用 Persona 的行为变量作为招募 screener |
| 配额 | 每个 Persona 至少 5 人 |
| 任务设计 | 从 Persona 的 Scenario 中提取核心任务 |
| 对比分析 | Persona A vs Persona B 的完成率/时间差异 |

### 5.2 测试结果反哺 Persona

| 测试发现 | Persona 动作 |
|---|---|
| A 类用户全部完成，B 类卡住 | 确认 A/B 切分有效 |
| 同一 Persona 内表现差异巨大 | 可能需要拆分 |
| 某 Pain Point 在测试中未出现 | 重新评估该 Pain 的严重性 |
| 发现新行为模式 | 补充 Persona 的 Behavioral Variable |

---

## 六、Survey 设计与 Persona 量化

### 6.1 Survey 三种 Persona 用法

| 用法 | 目的 | 样本量 |
|---|---|---|
| 验证性 | 确认定性发现的 Persona 切分在大样本中成立 | 200-500+ |
| 量化性 | 给每个 Persona 估计市场份额 | 500-1000+ |
| 分类性 | 用聚类/LCA 从 Survey 数据发现 Persona | 300-1000+ |

### 6.2 Survey → Persona 的分析流程

```
Survey Data (N=500)
  → Factor Analysis (降维)
  → Cluster Analysis (分群)
  → Persona Draft (per cluster)
  → Cross-validate with Interview Data
```

- 与 `clustering.py` 配合：Survey 数据作为 feature matrix 输入

---

## 七、研究项目管理

### 7.1 研究计划模板

```markdown
## Research Plan

**研究问题**: [想回答什么]
**方法**: [定性/定量/混合]
**样本**: [N=? / 招募标准 / 配额]
**时间线**: [准备 → 执行 → 分析 → 报告]
**预算**: [激励费 + 工具费 + 差旅]
**交付物**: [Topline / 完整报告 / Persona Update]
**利益相关者**: [谁需要知道结果]
```

### 7.2 Kuniavsky 的研究效率原则

| 原则 | 操作 |
|---|---|
| 最小充分法 | 先明确"最少需要什么"再设计方法 |
| 迭代优于一次性 | 小样本快出结论 → 大样本验证 → 持续跟踪 |
| 三角验证 | 至少用 2 种方法验证同一发现 |
| 及时归档 | 48h 内 Topline，2 周内完整报告 |
| 客户参与 | 让利益相关者观看 1-2 场测试/访谈 |

---

## 八、多方法组合策略

### 8.1 经典三阶段组合

| 阶段 | 方法 | 输出 |
|---|---|---|
| 1. 探索 | CI + Interview (N=8-12) | 行为变量 + Proto-Persona |
| 2. 量化 | Survey (N=300-500) | 聚类验证 + 市场份额 |
| 3. 评估 | Usability Test (N=5/Persona) | 设计验证 + Persona 精化 |

### 8.2 快速版（2 周内）

| 周次 | 方法 | 输出 |
|---|---|---|
| Week 1 | 5 次 Interview + Analytics Review | Proto-Persona + Hypothesis |
| Week 2 | Quick Survey (N=100) + 3 次 Usability Test | 验证/调整 Persona |

---

## 九、反模式

| # | 反模式 | 后果 | 修复 |
|---|---|---|---|
| 1 | 方法先行 | "我们做个焦点小组吧"（不管适不适合） | 先写研究问题再选方法 |
| 2 | 样本偏差 | 只招"好说话的人" | 用行为变量做 screener，含"极端用户" |
| 3 | 分析瘫痪 | 数据太多不知从何下手 | 先出 Topline，再深挖 |
| 4 | 数据孤岛 | 每个研究独立存在，不关联 | 建立 Persona 为锚点的知识库 |
| 5 | 只做定性 | 无法说服数据导向的利益相关者 | 补 Survey/Analytics 量化验证 |
| 6 | 只做定量 | 知道"多少人"但不知"为什么" | 补 Interview/CI 定性深挖 |
| 7 | 不做三角验证 | 单一方法的偏差无法识别 | 至少 2 种方法互相验证 |

---

## 十、定量指标与 Persona 关联

### 10.1 常用 UX 指标

| 指标 | 测量什么 | Persona 用法 |
|---|---|---|
| Task Success Rate | 能不能完成 | 按 Persona 切分对比 |
| Time on Task | 效率 | 识别"效率型" vs "探索型" Persona |
| Error Rate | 出错频率 | 识别"新手" vs "专家" Persona |
| SUS / UMUX | 整体满意度 | Persona 级别的满意度排名 |
| NPS | 推荐意愿 | Persona 级别的忠诚度 |
| CES | 费力度 | 哪个 Persona 觉得最费力 |

### 10.2 与 measurement_toolkit.py 集成

- `measurement_toolkit.py` 的 register_from_kr 可以绑定 Persona 级别的 NPS/CES/CSAT
- Kuniavsky 的 Task Metrics 可以作为 custom metric 注册
- 按 Persona 切分的指标趋势 → 判断某 Persona 是否越来越满意/流失

---

## 本部分核心要点总结

1. **研究方法不是越多越好——是越匹配越好**：先写研究问题，再选方法
2. **Contextual Inquiry 是 Persona 行为变量的最富矿**：在用户真实环境中观察
3. **定性发现 + 定量验证 = 可信 Persona**：三角验证消除单一方法偏差
4. **Diary Study 捕获时间维度**：跨越"访谈只能捕获回忆"的限制
5. **可用性测试基于 Persona 招募**：每个 Persona 至少 5 人
6. **研究效率原则**：最小充分法 + 迭代 + 48h Topline 防烂尾

---

## 🔗 跨技能协作

| 场景 | 推荐协作 Skill |
|---|---|
| 访谈方法深挖 | `32-portigal-interviewing-users` |
| 问题访谈设计 | `33-fitzpatrick-mom-test` |
| CI/Diary 数据转 Persona | `web-persona-skill` → `clustering.py` |
| 量化指标追踪 | `web-persona-skill` → `measurement_toolkit.py` |
| Survey 设计 | `persona/survey.py` |
| 研究综合 | `user-research-synthesis` |
| 可用性测试设计 | `interview-kit` |
