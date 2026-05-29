# 23 · Thick Data：人类学方法对抗大数据失效

> 来源：Wang, T. *"Why Big Data Needs Thick Data"* (Ethnography Matters/Medium, 2013)；Wang, T. *Live with the Data You're Reporting On* (TED, 2017)；Geertz, C. *The Interpretation of Cultures* (1973)（"thick description" 一词来源）；Madsbjerg, C. & Rasmussen, M. *The Moment of Clarity: Using the Human Sciences to Solve Your Toughest Business Problems* (HBR Press, 2014)；Salmon, T. & Ranganathan, S. *Designing for the Digital Age in Asia* (2024)。
>
> Tricia Wang 是 Nokia 失败案例的亲历者：2009 年她做民族志研究，发现底层用户准备买 iPhone-like 智能机，但 Nokia 数据团队说"我们的销售数据不支持这个判断"。结果 Nokia 错过黄金窗口。Thick Data 是对"data-driven"的纠偏——大数据告诉你**做什么**，厚数据告诉你**为什么、什么时候、何种情境**。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | Thick Data 视角（本笔记） |
|---|---|---|
| 数据观 | 调查 + 访谈混合 | 民族志 + 深度参与观察 + 大数据互补 |
| 时间投入 | 4-8 周 | 数月-数年（可深度沉浸） |
| 单位 | 用户群体代表 | 文化语境中的"他者" |
| 输出 | Persona 卡片 | Persona + 文化叙事 + 社会脉络 |
| 适合场景 | 数字产品决策 | 跨文化、新兴市场、深度行为变化 |
| 失败诊断 | 角色错 | 文化盲、情境盲、数据假象 |

> 💡 **互补立场**：Big Data + Thick Data = "广 + 深"。Mulder 偏中观；Thick Data 让 Persona 拥有真正的文化厚度。

---

## 2. Thick Data vs Thin Data

| 项 | Thin Data（薄数据） | Thick Data（厚数据） |
|---|---|---|
| 来源 | 日志、调查、点击流 | 民族志、田野、参与观察 |
| 优势 | 规模、可重复、可量化 | 情境、动机、矛盾、文化 |
| 弱势 | 失情境、失意义 | 难量化、难规模化 |
| 提问 | "How many?" | "Why? What does this mean to them?" |
| 单位 | 数据点 | 故事 |

> Wang 的核心论点：**当数据失败时，缺的不是更多数据，而是更厚数据**。

---

## 3. 民族志方法核心 5 件套

| 方法 | 中文 | 一句话 |
|---|---|---|
| **Participant Observation** | 参与观察 | 与研究对象共同生活/工作一段时间 |
| **Field Notes** | 田野笔记 | 当天写下所见所闻，含情绪与体感 |
| **Open-ended Interview** | 开放式访谈 | 不带假设的对话 |
| **Artifact Collection** | 物件收集 | 用户使用的物品、痕迹、照片 |
| **Thick Description** | 厚描述（Geertz） | 描述行为同时还原其文化意义 |

> Thick Description 经典例子（Geertz）：眨眼是物理动作；眨眼是阴谋的暗号；眨眼是嘲笑——同一动作三层意义，研究员要"读懂"。

---

## 4. 操作流程（端到端 7 步）

| 步 | 动作 | 时长 |
|---|---|---|
| 1 | 选定研究文化语境（地域 / 群体 / 情境） | 1 周 |
| 2 | 进入田野：建立信任、获得 access | 1-4 周 |
| 3 | 参与观察 + 田野笔记 | 4-12 周 |
| 4 | 关键访谈：6-15 名 informant，3-5 小时/人 | 4-8 周 |
| 5 | 物件收集：照片、视频、用户使用过的物品 | 持续 |
| 6 | 厚描述：每个故事写"行为 + 意义 + 文化脉络"3 层 | 2-4 周 |
| 7 | 与大数据交叉：用统计验证厚数据洞察、用厚数据解释数据异常 | 2-4 周 |

> 中国情境推荐：阿里巴巴有 **乡村发现** 项目（2014-2018）派研究员入驻县城/乡村数月，是国内最系统的民族志 Persona 研究。

---

## 5. Persona × Thick Data 增强模板

```yaml
persona_id: lin_jia
thick_data_layer:
  cultural_context:
    - "二线城市核心家庭，双方都是独生子女"
    - "孩子教育被视为家族投资"
    - "婆媳关系紧张，以孩子为中心斡旋"
  daily_rhythm:
    - "5:50 起床 → 21:30 哄睡前都是高强度多线程"
    - "唯一独处时刻：21:30-22:30 厨房洗碗时"
  artifacts:
    - "冰箱贴：兴趣班课程表 + 家庭吵架便签"
    - "手机首屏 12 个图标：6 个孩子相关、3 个家庭群、2 个工作、1 个微博"
  contradictions:
    - "口头说理性消费，实际为孩子常冲动购买"
    - "想要时间给自己，但'休息时间' 反而内疚"
  thick_quotes:
    - "我妈说我惯孩子，我妈不知道现在的妈不'惯'就被同事嘲笑"
    - "省下来这 200 块钱，我自己半年都不会用"
  cultural_metaphors:
    - "妈妈像家里的'路由器'：所有信息都从我这里转一手"
```

---

## 6. Big Data + Thick Data 协同模式

| 模式 | 说明 | 案例 |
|---|---|---|
| **Validate** | 厚数据假设 → 大数据验证规模 | 田野发现"妈妈群"现象 → 大数据查看微信群活跃度 |
| **Explain** | 大数据异常 → 厚数据解释原因 | 数据显示某品类周日下午激增 → 田野发现"祖辈带娃高峰" |
| **Discover** | 大数据未捕捉 → 厚数据发现 | 数据未显示低线女性买智能机意愿，田野发现已经准备买 |
| **Triangulate** | 同主题三方法验证 | 民族志 + 调查 + 行为日志同时收 |

> Wang 的口号：**"Bring the human back to data."**

---

## 7. 反模式 (Anti-patterns)

| 反模式 | 症状 | 后果 |
|---|---|---|
| **数据傲慢** | "数据都说 X，不用做田野" | 错过文化拐点 |
| **田野浪漫化** | 把研究对象写成"高贵原始" | 失去严谨与判断 |
| **走马观花** | 田野 1-2 天就出报告 | 看到的只是表演性行为 |
| **不写 Thick Description** | 只记录行为不解释意义 | 报告内容薄如观察日记 |
| **失去反身性** | 不反思研究员自己的偏见 | 把研究员的世界观投射给受访者 |
| **数据敌对** | 民族志派与数据派互不通气 | 公司决策两套语言互撕 |
| **采访即田野** | 把 30 分钟访谈当民族志 | 完全不是同一种方法 |

---

## 8. Reflexivity（反身性）：研究员的位置

民族志的核心纪律：**研究员是工具的一部分**——你的性别、阶层、口音、外表都影响 informant 给你的信息。

### 8.1 反身性 4 问
1. 我对这个群体有什么先见？
2. 受访者把我当作什么角色？这影响他怎样表演？
3. 我的访谈记录中，哪些是我"想看到"的？
4. 我有没有边缘化或浪漫化对方？

> 推荐做法：田野日记**单独一栏**记"我今天的情绪与判断偏移"。

---

## 9. 何时使用 Thick Data

✅ 用：
- 进入新文化/新地域/新人群（中国下沉、海外、银发、Z 世代）
- 大数据失效或矛盾
- 创新机会探索（数据无法预见的趋势）
- 长期行为变化（家庭结构、消费转型）
- 公司决策出现"数据看不到但用户在变"的盲区

⛔ 不用：
- 已知场景的 UI 微调
- 资源预算紧迫（< 6 周）
- 单纯漏斗优化（直接打开 GA）
- 团队不具备质化研究背景（容易做坏）

---

## 10. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/persona_builder.py` | 增加 `thick_data_layer` 字段 |
| 09-Indi Young | Listening Session 是 Thick Data 的轻量版 |
| 16-Statistical | 大数据 + 厚数据协同模式 |
| 18-Synthetic AI | LLM 易把 thick 压成 thin，需要厚数据回填 |
| 26-Hofstede | 文化维度提供宏观坐标，厚数据补微观纹理 |
| 27-bias-audit | 反身性写入研究审计 |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| Thick ≠ Thin | 大数据缺的是意义不是规模 |
| 民族志 5 件套 | 参与观察 + 田野笔记 + 开放访谈 + 物件 + 厚描述 |
| Geertz 厚描述 | 行为+意义+文化脉络三层 |
| 反身性 | 研究员是工具，自审才能看清 |
| 大+厚协同 4 模式 | Validate / Explain / Discover / Triangulate |
| Persona 携带文化层 | thick_data_layer 字段 |
| 数据敌对要弥合 | 数据团队与田野团队需共同语言 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `empathy-story` | 厚描述 → 共情叙事天然映射 |
| `mindshare-88vip-analysis` | 大数据+厚数据协同：飞猪 88VIP 心智 |
| `analytics-data-analysis` | 数据异常 → 厚数据解释 |
| `user-research-synthesis` | 田野笔记编码与主题分析 |
| `decision-tracker` | 厚数据洞察进入决策记录 |
| `consulting-frameworks` | 厚数据补足"软因素"维度 |

---

> 📚 **延伸阅读**：
> - Wang, T. *Why Big Data Needs Thick Data* (2013, Medium/Ethnography Matters)。
> - Geertz, C. (1973). *The Interpretation of Cultures*。
> - Madsbjerg & Rasmussen (2014). *The Moment of Clarity*。
> - Madsbjerg, C. (2017). *Sensemaking: The Power of the Humanities in the Age of the Algorithm*。
> - 中国情境：项飚 *把自己作为方法*（人类学反身性）；李骏 *底层之死*（深度民族志典范）。
