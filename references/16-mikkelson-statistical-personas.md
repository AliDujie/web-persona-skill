# 16 · 统计 Persona：聚类与潜变量方法

> 来源：Mikkelson, N. & McGinn, J. *Statistical Personas: Bringing Statistical Rigor to Persona Creation*（IBM/Microsoft 内部技术报告系列，2007-2014）；Tu, McGinn, et al. *"Validating personas using cluster analysis"* (CHI Workshop 2010)；Brickey, Walczak & Burgess *"A Comparative Analysis of Persona Clustering Methods"* (HFES 2012)；Salminen, J. et al. *"Are Personas Done? Evaluating Their Usefulness in the Age of Digital Analytics"* (Persona Studies, 2020)。
>
> 当 Persona 被指控"主观、不可验证、靠故事打动而非数据"时，统计 Persona 用聚类、潜类别、因子分析把数据驱动落到可计算层。本笔记整合 IBM/Microsoft/Qatar Computing Research Institute 等团队的实操经验。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | 统计 Persona（本笔记） |
|---|---|---|
| 数据来源 | 调查 + 访谈混合 | 大样本（n ≥ 200，理想 1000+）结构化数据 |
| 分群方法 | 人工识别核心特征 + 卡片分类 | KMeans / Latent Class / 因子分析 + 聚类 |
| 角色数量 | 3-5 个，研究员判定 | 由数据驱动（肘部法 / BIC / 轮廓系数决定 K） |
| 角色单位 | 行为模式代表 | 数学簇质心 (centroid) + 概率隶属度 |
| 验证方式 | 团队复盘 + 主观评估 | 重抽样稳定性 + Hold-out 集复现 |
| 适合场景 | 中小数据集、Web 产品、决策周期短 | 平台级数据、长决策周期、防御学术质疑 |

> 💡 **互补立场**：Mulder 解决"角色生成"，统计 Persona 解决"角色可信度"；项目早期可用 Mulder，进入企业级或学术汇报需用统计法回头加固。

---

## 2. 三大主流统计方法

### 2.1 KMeans 聚类（最常用）

| 项 | 内容 |
|---|---|
| 适合 | 连续/定序变量为主，目标找硬边界簇 |
| 输入 | 标准化矩阵（z-score 或 min-max） |
| 关键超参 | K（簇数）、随机种子、距离度量（默认欧式） |
| 决定 K | 肘部法（Elbow）+ 轮廓系数（Silhouette）+ Gap Statistic 三角验证 |
| 输出 | 每用户 1 个硬簇标签 + 簇质心 |
| 弱点 | 不能处理类别变量；对离群值敏感；强行球形假设 |

**经验法则**：K 一般落在 3-7；超过 7 个簇人类记不住；少于 3 个无区分价值。

### 2.2 Latent Class Analysis（潜类别分析，LCA）

| 项 | 内容 |
|---|---|
| 适合 | 类别/二元变量为主（"是否买过""选哪个"），目标找潜在类型 |
| 假设 | 同一潜类别内变量条件独立 |
| 决定类数 | BIC（贝叶斯信息准则）最小者 |
| 输出 | 每用户对每类的 **后验概率**（柔性归属） |
| 软件 | R `poLCA`、Python `stepmix`、Mplus、Latent GOLD |
| 优势 | 给出隶属概率而非硬标签——支持"该用户 70% 像 A、30% 像 B"的现实复杂性 |

> Goodwin/Pruitt 等定性派担心"统计法把人变成数字"，LCA 的概率输出恰好留出叙事空间——质心可作为骨架，再用访谈补充人格细节。

### 2.3 因子分析 + 二阶聚类（Two-Step）

| 项 | 内容 |
|---|---|
| 步骤一 | 在 30+ 题问卷上做 EFA / PCA，把题项压缩为 5-8 个因子（如"价格敏感度""探索倾向"） |
| 步骤二 | 在因子得分上做 KMeans 或层次聚类 |
| 优点 | 降维去除多重共线，簇质心可解释为因子组合 |
| 适合 | 心理量表型 Persona（NEEDS / 价值观分群） |
| 案例 | IBM Watson Customer Experience 团队按 5 因子 × 4 簇 = 4 类 Persona |

---

## 3. 操作流程（端到端 9 步）

| 步 | 动作 | 输出 | 工具 |
|---|---|---|---|
| 1 | 设计问卷/收集行为日志，确保 n ≥ 200 | 原始矩阵 | Qualtrics、ODPS、GA4 |
| 2 | 数据清洗：去缺失 > 30% 的行、识别离群 | 清洗后矩阵 | pandas、R |
| 3 | 变量选择：保留与"行为/动机"相关变量，去人口学（避免分群退化为年龄/性别） | 特征矩阵 | 业务讨论 + 相关性检查 |
| 4 | 标准化（z-score）+ 类别变量编码（One-Hot 或 LCA） | 标准化矩阵 | sklearn |
| 5 | 决定方法：连续→KMeans；类别→LCA；混合→因子+KMeans | 方法选定 | 决策树（见 §4） |
| 6 | 决定 K / 类数：3 个指标三角验证 | K=N | Elbow + Silhouette + BIC |
| 7 | 跑模型，得到簇标签 + 质心 | 簇属性表 | sklearn / poLCA |
| 8 | 稳定性验证：bootstrap 100 次重抽样，检查簇成员变化 | 稳定性分数 | scikit-learn-extra `consensus_clustering` |
| 9 | 给每个簇配定性名字 + 1-2 名典型受访者深度访谈，补充人格 | 完整 Persona | 设计师 + 文案 |

> **关键纪律**：第 7 步只是中间产物。**没有第 8 步的稳定性验证，就不要把簇当作 Persona**——否则换一批数据可能产生完全不同的分群。

---

## 4. 选择方法的决策树

```
变量类型？
├─ 全部连续/定序（如李克特量表）
│   ├─ 题目数 ≤ 10  → KMeans
│   └─ 题目数 > 20  → 因子分析 + KMeans
├─ 全部类别/二元（如是否使用过某功能）
│   └─ → Latent Class Analysis
└─ 混合
    ├─ 偏连续 → Gower 距离 + 层次聚类
    └─ 偏类别 → LCA（连续变量分箱后纳入）
```

---

## 5. K 的决策：三个指标怎么读

| 指标 | 解读 | 选 K |
|---|---|---|
| Elbow（簇内 SSE 曲线） | 找拐点：K 增加但 SSE 降幅显著变小 | 拐点处 |
| Silhouette（轮廓系数） | -1 到 1，越接近 1 越好；>0.5 优秀 | 局部最大值 |
| BIC（贝叶斯信息准则） | 越低越好；惩罚过多参数 | 最小值 |
| Gap Statistic | 比较实际数据与随机数据的 SSE 差距 | 第一次 Gap_k ≥ Gap_{k+1}-s_{k+1} 的 K |

**冲突时**：以可解释性优先——如果 K=4 数学最优但业务讲不清，就选 K=3 或 K=5；定量为辅，叙事为主。

---

## 6. 命名簇的四个原则

| 原则 | 反例 | 正例 |
|---|---|---|
| 用行为命名，不用人口学 | "30-40 岁女性" | "价格敏感的精明比较者" |
| 用形容词 + 名词组合 | "Cluster 1" | "焦虑的初次报名者" |
| 避免贬义/自带评价 | "懒惰用户" | "时间稀缺的多任务者" |
| 给一句话动机 | （只有名字） | "我想最快搞完，少出错" |

---

## 7. 反模式 (Anti-patterns)

| 反模式 | 症状 | 后果 |
|---|---|---|
| **数据钓鱼** (Data Fishing) | 反复改变量、试 K，直到出"好看"分群 | 过拟合；新数据不复现 |
| **维度爆炸** | 把 50+ 变量都放进聚类 | 维度灾难，距离失效 |
| **强行人口学** | 把年龄、性别强塞进特征 | 分群退化为人口统计，失去行为意义 |
| **跳过验证** | 不做 bootstrap 稳定性 | 簇是噪声而非信号 |
| **质心 = Persona** | 直接把簇均值当人物画像 | 缺乏人格、记不住、无法激发同理心 |
| **数学最优 = 业务最优** | 死磕 K=4 因为 BIC 最优 | 团队学不会、用不起来 |

---

## 8. 何时使用统计 Persona

✅ 用：
- 平台级产品（n 巨大且可获得）
- 学术/咨询汇报需防御方法严谨性
- 多个 stakeholder 对"为什么是这几类"持质疑
- 需要给每个用户打 Persona 标签做 A/B / 个性化（必须有概率/硬标签）

⛔ 不用：
- 早期产品（n < 100）→ 转用 Lean UX Proto-Persona
- 探索性洞察阶段 → 转用 Indi Young Mental Models
- 决策驱动型项目 → 转用 Cooper 单一 Primary 法
- 行业是 B2B 销售 → 转用 Revella Buyer Personas（见 17 号）

---

## 9. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/segment.py` | 现有的 Mulder 式分群可升级为 KMeans/LCA；见 28 号工程化文档 |
| `persona/clustering.py`（v2.6 新增） | 直接调用，输入 DataFrame 输出簇 |
| 09-Indi Young | Mental Model 的 Thinking Style 可作为聚类输入变量 |
| 02-measuring-results | 簇隶属概率可作为追踪指标（"该用户从 A 簇向 B 簇迁移"） |
| 24-Kat Holmes | 检查统计分群是否系统性遗漏边缘群体 |

---

## 10. 一个完整工作流示例

> **场景**：某保险 App 收到 1200 份用户调研问卷，30 道题（其中 18 道李克特 5 点量表）。

```
1. 清洗 → 1080 有效样本
2. EFA → 18 题压缩为 5 因子：
   - F1 价格敏感度
   - F2 风险厌恶
   - F3 数字熟练度
   - F4 家庭责任感
   - F5 自主决策倾向
3. 在 5 因子得分上跑 KMeans，K∈{3,4,5,6,7}
4. Silhouette 在 K=4 达到 0.58，BIC 在 K=4 最低 → 选 K=4
5. Bootstrap 100 次：87% 用户簇标签稳定 → 通过
6. 命名 4 簇：
   - "精打细算的家庭顶梁柱"（高 F1+F4）
   - "数字原生的极简决策者"（高 F3+F5、低 F2）
   - "稳健的二次置业者"（高 F2+F4）
   - "保守的数字旁观者"（低 F3、低 F5）
7. 每簇抽 2 人深访 → 补充故事、痛点、典型一天
8. 输出：4 张 Persona 卡片 + 1 份方法论说明书 + 簇隶属概率打回 CRM
```

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| 统计 ≠ 取代叙事 | 统计法生成骨架，定性法填充人格；二者必须配合 |
| 三方法对应三数据类型 | 连续→KMeans；类别→LCA；混合→因子+聚类 |
| K 由三指标三角决定 | Elbow + Silhouette + BIC，业务可解释性最终决定 |
| Bootstrap 验证必做 | 不做稳定性验证 = 把噪声当 Persona |
| 不让算法决定意义 | 簇命名、人格补充、何时止损都需研究员判断 |
| 与定性法是接力 | 先定性发现 → 再统计验证 → 再定性深化，循环迭代 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `analytics-data-analysis` | 跑聚类、做稳定性 bootstrap、可视化质心 |
| `mindshare-88vip-analysis` | ODPS 大样本数据 → 因子+聚类生成 Persona |
| `user-research-synthesis` | 给每个簇做深访补充故事 |
| `decision-tracker` | 追踪 Persona 在产品决策中的引用频率 |
| `consulting-frameworks` | MECE 视角审查变量选择是否合理 |

---

> 📚 **延伸阅读**：
> - Brickey, J., Walczak, S. & Burgess, T. (2012). *Comparing Semi-Automated Clustering Methods for Persona Development*. IEEE Transactions on Software Engineering, 38(3).
> - Salminen, J. et al. (2020). *A Survey of 15 Years of Data-Driven Persona Development*. International Journal of Human-Computer Interaction, 37(18).
> - Mulder & Yaar (2007). *The User Is Always Right*, Chapter 7：作者本人推荐进阶到统计法的入口。
