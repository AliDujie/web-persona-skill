# Web Persona Skill

基于《赢在用户：Web 人物角色创建和应用实践指南》(The User Is Always Right) 的完整人物角色工具包。

## 为什么使用

- **经典方法论** — 基于 Steve Mulder 人物角色经典著作
- **全链路工具** — 从用户研究到角色创建，从商业策略到设计指导
- **CEO 视角** — 内置用户经济模型、获取策略、留存策略分析
- **零依赖** — 纯 Python 标准库实现

## 快速开始

```python
from persona import PersonaSkill

skill = PersonaSkill("电商平台")

# 生成用户访谈提纲
guide = skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"])

# 创建人物角色
skill.add_persona("小明", "效率型用户", "primary", "我只想快速完成",
    goals=["快速完成任务"], behaviors=["频繁使用搜索"])
print(skill.render_all_personas())

# CEO 视角：用户经济模型 + 获取/留存策略
report = skill.generate_persona(include_ceo_analysis=True)
```

## 文件结构

```
web-persona-skill/
├── SKILL.md              # AI Agent 技能定义
├── persona/              # Python 包（纯标准库）
│   ├── __init__.py       # PersonaSkill 统一入口
│   ├── config.py         # 配置与常量
│   ├── interview.py      # 访谈提纲生成器
│   ├── survey.py         # 问卷设计器
│   ├── segment.py        # 用户细分分析器
│   ├── persona_builder.py
│   ├── strategy.py       # 商业策略与功能优先级
│   ├── design.py         # 信息架构与内容策略
│   └── measure.py        # 测试计划与衡量体系
├── references/           # 知识库文档
├── pyproject.toml
└── README.md
```

## 相关技能

- [Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods) — 100 种设计研究方法
- [JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill) — Jobs-to-be-Done 理论
- [Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research) — 量化研究、HEART 框架
- [Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design) — 价值主张画布
- [Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data) — 数据叙事与可视化

## 实际案例

### 案例 1：电商平台人物角色创建

```python
from persona import PersonaSkill

skill = PersonaSkill("电商平台")

# 添加主要角色
skill.add_persona(
    name="小明",
    archetype="效率型用户",
    type="primary",
    quote="我只想快速找到想要的商品",
    goals=["快速完成任务", "获得个性化推荐"],
    behaviors=["频繁使用搜索", "比价后再购买"]
)

skill.add_persona(
    name="小红",
    archetype="探索型用户",
    type="secondary",
    quote="我喜欢发现新品和优惠",
    goals=["发现新品", "获取优惠信息"],
    behaviors=["浏览推荐", "关注直播"]
)

print(skill.render_all_personas())
# 输出：2 个角色档案，包含目标、行为、痛点、设计指导
```

### 案例 2：访谈提纲与问卷设计

```python
# 生成用户访谈提纲
guide = skill.generate_interview(
    "新用户上手体验访谈",
    dimensions=["goals", "behaviors", "pain_points", "motivations"]
)
print(guide)
# 输出：结构化访谈提纲，覆盖 4 个维度

# 生成问卷
survey = skill.design_survey("用户细分问卷", sample_size=500)
print(f"问卷题目数: {survey.question_count}")
```

### 案例 3：CEO 视角用户经济模型

```python
# CEO 视角：用户经济模型 + 获取/留存策略
report = skill.generate_persona(include_ceo_analysis=True)
print(report)
# 输出包含：
# - 用户经济模型（LTV、CAC、留存曲线）
# - 获取策略（渠道优先级、转化漏斗）
# - 留存策略（关键行为、流失预警）
```

## 故障排除

| 问题 | 原因 | 解决方案 |
|------|------|----------|
| 角色画像过于笼统 | 研究数据不足 | 补充用户访谈，用 UDM 方法收集更多洞察 |
| 角色数量过多 | 细分过度 | 合并相似角色，保留 3-5 个核心角色 |
| 设计指导不具体 | 角色与功能脱节 | 为每个角色编写具体的用户故事和使用场景 |
| Bug 优先级混乱 | 缺乏角色视角 | 按角色影响面排序：Primary > Secondary > Negative |

## 扩展阅读

| 书籍 | 作者 | 关联能力 |
|------|------|----------|
| 《The User Is Always Right》 | Steve Mulder & Ziv Yaar | 全书方法论基础 |
| 《Persona Lifecycle》 | John Pruitt & Tamara Adlin | 角色生命周期管理 |
| 《Just Enough Research》 | Erika Hall | 精益用户研究方法 |
| 《Observing the User Experience》 | Mike Kuniavsky | 用户观察与访谈技巧 |

## 技能生态导航

与其他 AliDujie 技能协同使用，构建完整用户体验研究体系：

| 关联技能 | 协同场景 | 工作流示例 |
|----------|----------|------------|
| [Universal Design Methods](https://github.com/AliDujie/universal-design-methods) | 角色研究数据收集 | UDM 访谈/观察 → Persona 角色创建 |
| [Storytelling with Data](https://github.com/AliDujie/storytelling-with-data) | 角色故事可视化呈现 | Persona 角色 → SWD 图表向团队展示 |
| [Quantitative UX Research](https://github.com/AliDujie/quantitative-ux-research) | 定量验证角色规模 | Persona 细分 → QuantUX 样本量验证 |
| [JTBD Knowledge](https://github.com/AliDujie/jtbd-knowledge-skill) | JTBD 驱动角色细分 | JTBD 任务聚类 → Persona 角色定义 |
| [Value Proposition Design](https://github.com/AliDujie/value-proposition-design) | 角色驱动价值设计 | Persona 角色 → VPD 客户画像 |

## 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.5 | 2026-04-23 | 添加实际案例、故障排除、扩展阅读、技能生态导航 |
| v1.4 | 2026-04-23 | 添加技能生态导航表、Last Updated 徽章 |
| v1.3 | 2026-04-22 | 初始版本 |

## 依赖

Python >= 3.8，无外部依赖。

## 许可

MIT License

---

*Last Updated: 2026-04-23 | AliDujie Skill Ecosystem*
