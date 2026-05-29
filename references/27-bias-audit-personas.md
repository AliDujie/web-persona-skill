# 27 · 偏差审计：Persona 的公平性 / 性别 / 种族 / 年龄检视

> 来源：Marsden, N. & Haag, M. *"Stereotypes and Politics: Reflections on Personas"* (CHI 2016)；Turner, P. & Turner, S. *"Is Stereotyping Inevitable When Designing with Personas?"* (Design Studies, 2011)；Costanza-Chock, S. *Design Justice* (MIT Press, 2020)；Buolamwini, J. & Gebru, T. *Gender Shades* (FAT* 2018)；Eubanks, V. *Automating Inequality* (St. Martin's Press, 2018)；Cao, Y. et al. *Auditing Personas: A Systematic Bias Audit Framework* (CHI 2024)；Salminen, J. et al. *"Persona Perception"* studies (2018-2023)。
>
> Persona 文档常常无意中固化性别 / 阶层 / 种族 / 年龄 / 地域刻板印象——15 号文件已经讨论了 Chapman & Milham 的批评，本笔记给出**可操作的偏差审计清单**与流程，让 Persona 的伦理审查从"意识"变成"工程化检查项"。

---

## 1. 与 Mulder《赢在用户》的关系

| 维度 | Mulder（本技能默认） | 偏差审计视角（本笔记） |
|---|---|---|
| 输出焦点 | 角色描述 | 角色描述 + 偏差自审报告 |
| 失败诊断 | 角色不准确 | 角色刻板、隐含歧视、伤害特定群体 |
| 工具 | 卡片模板 | 6 维 audit checklist + 团队多元 review |
| 适合场景 | 任意 Persona 项目 | 任何要发布、影响决策的 Persona |
| 核心问题 | "他是谁" | "我们写的他是否反映/强化了刻板印象？" |

> 💡 **核心立场**：偏差不是写作问题，是**结构性问题**。哪怕用最善意的语言写 Persona，仍可能因团队同质化、数据偏斜、案例选择而生成系统性偏差。审计不是一次性的，而是治理流程。

---

## 2. Persona 8 类常见偏差病症

| 病症 | 中文 | 一句话 | 例 |
|---|---|---|---|
| **Gender Stereotyping** | 性别刻板 | 行为/职业/兴趣按性别假设 | "她爱购物""他爱科技" |
| **Racial / Ethnic Stereotyping** | 种族/民族刻板 | 用名字/外貌暗示行为 | 某族群=某品类爱好者 |
| **Class Stereotyping** | 阶层刻板 | 收入决定品位/智商 | "下沉=低教育" |
| **Age Stereotyping** | 年龄刻板 | 老人=不会用科技 | "她 65 岁，不懂 App" |
| **Ableism** | 健全主义 | 默认健全身体 | 全部 Persona 健全 |
| **Heteronormativity** | 异性恋默认 | 家庭=父母+孩子 | 默认异性婚姻 |
| **Geographic Bias** | 地域偏差 | 一线/海外为默认 | "用户来自北上广深" |
| **Linguistic Bias** | 语言偏差 | 母语英文/普通话默认 | 不考虑方言/低识字率 |

---

## 3. 偏差来源：6 个根因

| 根因 | 一句话 |
|---|---|
| 1. 团队同质化 | 团队 8 男 0 女写"她"的 Persona |
| 2. 数据采集偏斜 | 招募只在一线城市、互联网渠道 |
| 3. 描述语言偷懒 | 用"妈妈很温柔""妻子料理家务"省字 |
| 4. 视觉素材偏差 | 头像图库以白人/年轻人为主 |
| 5. 编辑思维定式 | "Persona 要有戏剧性"→ 浮夸特征 |
| 6. 不审计的治理 | 无 review 流程，问题未被看见 |

---

## 4. 6 维 Bias Audit Checklist（推荐落地）

### 4.1 Gender 维度（10 项）
1. 行为是否预设性别？
2. 职业/收入是否因性别而异？
3. 家务/育儿默认归属哪一性别？
4. 兴趣（科技/购物/汽车/美妆）是否性别绑定？
5. 决策力描述（"她需要丈夫同意"）是否合理？
6. 视觉素材是否反映多元身份？
7. 是否包含非二元性别 Persona（如适用）？
8. 称呼/代词是否一致与尊重？
9. 引语是否避免性别化情绪修饰（"歇斯底里"）？
10. 数据来源男女比例是否相符 actual base rate？

### 4.2 Race / Ethnicity 维度（8 项）
1. 名字是否暗示族群？
2. 行为是否与族群刻板挂钩？
3. 视觉素材族群多元性？
4. 案例是否包含少数族裔的真实声音？
5. 语言风格是否避免"他者化"（"他们这种人"）？
6. 是否过度强调族群差异而忽略个体？
7. 数据采集是否覆盖少数族裔？
8. 报告中族群相关结论是否标注样本量？

### 4.3 Age 维度（7 项）
1. 老年 Persona 是否默认"不会用科技"？
2. 年轻 Persona 是否默认"无家庭责任"？
3. 中年 Persona 是否被忽略？
4. 年龄段划分是否过度粗粒度（"老年人"涵盖 60-90）？
5. 视觉素材年龄段是否多元？
6. 是否考虑代际间互助（孙辈帮祖辈用 App）？
7. "数字原住民" / "数字移民" 标签使用是否谨慎？

### 4.4 Class / Socioeconomic 维度（7 项）
1. 收入是否决定品位/智识描述？
2. 下沉/低收入 Persona 是否被浪漫化或污名化？
3. 教育程度是否被等同于"理解能力"？
4. 价格敏感是否被等同于"低价值用户"？
5. 是否包含真实下沉/低收入用户访谈？
6. 视觉素材是否反映多阶层？
7. 高净值 Persona 是否避免"成功学"叙事？

### 4.5 Ability 维度（6 项）
1. 是否所有 Persona 默认健全？
2. 是否纳入 Spectrum（24 号 Kat Holmes）？
3. 视觉素材是否包含残障用户？
4. 操作流程是否考虑临时受限？
5. 文案/视觉对比度是否合规？
6. 是否邀请残障用户参与 Persona Review？

### 4.6 Family / Sexuality 维度（5 项）
1. 家庭结构是否默认异性婚姻？
2. 是否包含单亲 / 同性 / 丁克 / 多代同堂？
3. 婚育状况是否被预设？
4. 称呼是否性别中性可选？
5. 数据采集是否覆盖多元家庭结构？

> 💎 总计 43 项检查 = 一份 Persona 文档至少应通过其中相关项的 80%。

---

## 5. 团队多元 Review（5 人法）

| 角色 | 任务 |
|---|---|
| Persona 作者 | 提供草稿 |
| 多元身份成员 | 至少 1 名异性别 + 1 名其他族群/阶层身份 |
| Inclusive 专家 | 跑 a11y / 包容审计 |
| 法务/合规 | 检查歧视风险 |
| 真实用户代表 | 至少 1 名目标用户群体成员（用户咨询委员会形式） |

> Persona 提交前由 5 人独立打分（1-5）+ 文字反馈，作者修订 → 二轮 review。

---

## 6. Persona 反偏差写作 8 原则

| 原则 | 一句话 |
|---|---|
| 1. 用具体行为代替形容词 | "她每天 21:30 后单独刷 30 分钟视频" 优于 "她爱看视频" |
| 2. 不用名字作族群标签 | 名字不暗示行为 |
| 3. 多元而非装饰 | 不放 1 个族群代表当点缀 |
| 4. 引语来自真实访谈 | 不杜撰浮夸语录 |
| 5. 避免怜悯叙事 | 不把弱势 Persona 写得"可怜" |
| 6. 视觉素材库审计 | 头像、生活照、姿态多元 |
| 7. 标注 base rate | 重要数据写出"基于 n=X 样本" |
| 8. 标注偏差风险 | 文档底部加 limitations 段 |

---

## 7. Persona × Bias Audit 模板

```yaml
persona_id: lin_jia
bias_audit:
  conducted_by: "design-team-2026Q2"
  review_date: "2026-05-29"
  reviewers:
    - "Author（女）"
    - "M（男, 二孩父亲, 反向视角）"
    - "Y（残障专家）"
    - "L（法务合规）"
    - "C（用户代表，三线城市妈妈）"
  
  scores:
    gender: 4.5/5
    race_ethnicity: NA  # 单一族群项目
    age: 4/5
    class: 3.5/5  # 待加强：下沉视角
    ability: 4/5
    family_sexuality: 3/5  # 待加强：纳入单亲变体
  
  issues_found:
    - "原稿写'她爱逛街' → 改为'她每周末与孩子一起去商场玩' "
    - "原稿仅有'丈夫' → 增加'若离异/单亲版本' Edge Persona"
    - "视觉头像需替换为真实用户匿名照"
  
  limitations:
    - "数据基于一二线城市，下沉地区结论需另做研究"
    - "未覆盖单亲/同性家庭，需 Edge Persona 补充"
    - "样本中 92% 母语普通话，方言地区另议"
  
  next_review: "2026-Q3"
```

---

## 8. 反模式 (Anti-patterns)

| 反模式 | 症状 | 后果 |
|---|---|---|
| **"我们没有偏见"** | 不做审计 | 隐性偏见仍存 |
| **审计是公关** | 只做表面修辞 | 内核仍刻板 |
| **Token 多元** | 加 1 张少数族裔图当装饰 | 数据/叙事仍单一 |
| **Bias = 写作问题** | 把审计交给文案 | 不解决数据/团队问题 |
| **审计无后续** | 找出问题不修订 | 文档治理失败 |
| **怕踩雷不写** | Persona 全部模糊化 | 失去具体性，无指导价值 |

---

## 9. 何时使用 Bias Audit

✅ 用：
- 任何**对外发布**或**影响产品决策**的 Persona
- 团队同质化（性别/族群/年龄结构单一）
- 海外/跨文化项目
- 涉及金融/医疗/教育/招聘等高敏感领域
- 监管审查 / 内部 Ethics Review
- AI / 推荐算法的训练数据生成

⛔ 不用：
- 内部纯技术工具（Persona 不影响外部用户）
- 极早期 brainstorm 草稿（但应有 IOU）

---

## 10. 与本技能其他部分的衔接

| 衔接位置 | 用法 |
|---|---|
| `persona/bias_audit.py`（v2.6 新增） | 6 维 43 项 checklist 自动化 |
| `persona/persona_builder.py` | 增加 `bias_audit` 字段 |
| 15-Critique-Defense | 应对 Persona 刻板印象批评 |
| 18-Synthetic AI | LLM 偏差审计高度相关 |
| 24-Kat Holmes | Ability 维度的实施 |
| 26-Hofstede | 跨文化偏差审计 |

---

## 本部分核心要点总结

| 要点 | 一句话 |
|---|---|
| 偏差是结构性 | 不只是写作问题 |
| 8 类病症 | Gender/Race/Class/Age/Ability/Sexuality/Geo/Lang |
| 6 维 43 项 audit | 落地清单 |
| 5 人多元 review | 团队多元才能看到盲点 |
| 8 写作原则 | 具体行为 / 不名字标签 / 真实引语 |
| 标注 limitations | 主动声明覆盖范围 |
| 治理>事件 | 审计是文档治理流程 |

---

## 🔗 跨技能协作

| 协作技能 | 协作场景 |
|---|---|
| `code-review` | 代码层审计：Persona-driven 算法是否公平 |
| `prd-writing` | PRD 增加 Bias Audit 段 |
| `decision-tracker` | 偏差争议决策记录 |
| `consulting-issue-tree-mece` | issue tree 添加 "谁不在" 维度 |
| `security-review` | 公平性审计纳入安全 review |
| `analytics-data-analysis` | base rate / demographic parity 量化 |

---

> 📚 **延伸阅读**：
> - Marsden & Haag (2016). *Stereotypes and Politics: Reflections on Personas*. CHI'16.
> - Buolamwini & Gebru (2018). *Gender Shades*. FAT*'18.
> - Costanza-Chock (2020). *Design Justice*。
> - Eubanks (2018). *Automating Inequality*。
> - Noble, S. (2018). *Algorithms of Oppression*。
> - 中国情境：李银河 *性的问题*；项飚 *系统：阿里巴巴 16 年*；周大鸣 *都市边缘人*。
