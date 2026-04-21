# Web Persona Skill

> 👤 **用户永远是对的：创建和应用人物角色的实践指南**

基于《赢在用户：Web 人物角色创建和应用实践指南》(The User Is Always Right) 的完整人物角色工具包。

## 🌟 为什么使用这个技能？

- **经典方法论** — 基于 Steve Mulder 人物角色经典著作，用户体验领域必读
- **全链路工具** — 从用户研究到角色创建，从商业策略到设计指导，一站式解决
- **8 大核心能力** — 访谈、问卷、细分、角色创建、策略分析、设计指导、衡量体系
- **零依赖** — 纯 Python 标准库，5 分钟上手，即刻产出
- **实战导向** — 内置质量评审、Bug 优先级计算、功能优先级矩阵

## 🚀 5 分钟快速开始

### 步骤 1: 安装技能

```bash
# 复制到你的 AI Agent skills 目录
cp -r skills/web-persona-skill ~/.aoneclaw/skills/
```

### 步骤 2: 作为 Python 包使用

```python
import sys
sys.path.insert(0, "/path/to/web-persona-skill")
from persona import PersonaSkill, InterviewBuilder, PersonaBuilder
```

### 步骤 3: 开始使用

```python
# ===== 统一入口 =====
skill = PersonaSkill("飞猪旅行")

# ===== 场景 1: 生成用户访谈提纲 =====
guide = skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"])
print(guide)
# 输出：包含开场白、目标探索、行为分析、痛点挖掘的结构化提纲

# ===== 场景 2: 设计调查问卷 =====
survey = skill.generate_survey(
    "需求调研",
    "needs",
    pain_points=["找酒店耗时", "价格不透明"],
    goals=["快速完成预订", "找到性价比高的选择"]
)
print(survey)
# 输出：需求型问卷，包含筛选问题、核心问题、人口统计

# ===== 场景 3: 创建人物角色 =====
skill.add_persona(
    "小明",
    "效率型用户",
    "primary",
    "我只想快速完成",
    goals=["快速完成任务"],
    behaviors=["频繁使用搜索功能", "很少浏览"],
    attitudes=["追求效率", "对价格不敏感"],
    bio="小明是一位忙碌的白领，经常出差，希望快速完成酒店预订..."
)

skill.add_persona(
    "小红",
    "探索型用户",
    "secondary",
    "我喜欢发现新东西",
    goals=["发现好物", "比较不同选择"],
    behaviors=["长时间浏览", "收藏多个选项"],
    attitudes=["好奇心强", "价格敏感"],
    bio="小红是一位大学生，喜欢规划旅行，享受发现的过程..."
)

print(skill.render_all_personas())  # 完整角色文档

# ===== 场景 4: 角色质量评审 =====
review = skill.review_personas()
print(review)
# 输出：完整性评分、可信度评估、改进建议

# ===== 场景 5: 功能优先级矩阵 =====
skill.add_feature("快速预订", {"小明": "高", "小红": "低"}, "高", "低")
skill.add_feature("价格对比", {"小明": "中", "小红": "高"}, "中", "高")
skill.add_feature("个性推荐", {"小明": "低", "小红": "高"}, "低", "高")
print(skill.render_feature_matrix())
# 输出：角色×功能优先级矩阵，指导产品路线图

# ===== 场景 6: Bug 优先级自动计算 =====
print(skill.add_bug("首页加载慢", "小明", is_primary=True, blocks_core=True))
# → P0: 首页加载慢 (影响首要角色的核心任务，必须立即修复)

print(skill.add_bug("收藏功能偶尔失效", "小红", is_primary=False, blocks_core=False))
# → P2: 收藏功能偶尔失效 (影响次要角色的非核心任务，可排期修复)

# ===== 场景 7: 用户细分分析 =====
skill.segment_analyzer.add_segment("效率型", size=0.4, value=0.6)
skill.segment_analyzer.add_segment("探索型", size=0.3, value=0.3)
skill.segment_analyzer.add_segment("价格敏感型", size=0.3, value=0.1)
print(skill.segment_analyzer.render_matrix())
# 输出：细分规模×价值矩阵

# ===== 场景 8: 设计指导 =====
advisor = skill.design_advisor
print(advisor.info_architecture_recommendation("效率型用户为主"))
print(advisor.content_strategy_recommendation("探索型用户为主"))

# ===== 场景 9: 衡量体系 =====
measure = skill.measure_system
print(measure.add_usability_goal("预订流程", "完成率", 0.85))
print(measure.render_test_script("快速预订"))

# ===== 知识库搜索 =====
from persona import load_knowledge, search_knowledge
results = search_knowledge("细分")
for topic, paragraphs in results.items():
    print(f"[{topic}] 找到 {len(paragraphs)} 个相关段落")
```

## 💡 8 大核心能力

| 能力 | 模块 | 功能 |
|------|------|------|
| **访谈框架** | `InterviewBuilder` | 按段落自动生成定制化访谈提纲 |
| **问卷设计** | `SurveyBuilder` | 支持需求型/验证型/满意度型三种问卷自动生成 |
| **用户细分** | `SegmentAnalyzer` | 数据管理、细分评估、矩阵可视化 |
| **角色创建** | `PersonaBuilder` | 完整角色文档生成、对比表、质量评审 |
| **商业策略** | `StrategyAnalyzer` | 角色价值评估、功能优先级矩阵、竞品分析 |
| **设计指导** | `DesignAdvisor` | 信息架构、内容策略、路径验证 |
| **衡量成果** | `MeasureSystem` | 测试脚本、指标体系、Bug 优先级自动计算 |
| **知识库** | `load_knowledge()` | 结构化文档，支持关键词搜索 |

## 📁 文件结构

```
web-persona-skill/
├── skills/persona/
│   └── SKILL.md                 # AI Agent 技能定义
├── persona/                     # Python 包（纯标准库）
│   ├── __init__.py              # API 入口与 PersonaSkill 统一类
│   ├── config.py                # 全局配置与常量
│   ├── utils.py                 # 知识库加载与文本工具
│   ├── templates.py             # 模板定义（访谈、角色、报告）
│   ├── interview.py             # 访谈提纲生成器
│   ├── survey.py                # 问卷设计生成器
│   ├── segment.py               # 用户细分分析器
│   ├── persona_builder.py       # 人物角色文档生成器
│   ├── strategy.py              # 商业策略与功能优先级
│   ├── design.py                # 信息架构与内容策略
│   └── measure.py               # 测试计划与衡量体系
├── docs/
│   └── book_notes/              # 书籍知识笔记
│       ├── 01-persona-basics.md
│       └── 02-measuring-results.md
├── pyproject.toml
├── requirements.txt
└── README.md                    # 本文件
```

## 🔗 相关技能

本技能是 **AliDujie UX 研究技能生态系统** 的一部分：

- **[Universal-Design-Methods](https://github.com/AliDujie/universal-design-methods)** — 100 种设计研究方法
- **[JTBD-Knowledge-Skill](https://github.com/AliDujie/jtbd-knowledge-skill)** — Jobs-to-be-Done 理论、进步力量分析
- **[Quantitative-UX-Research](https://github.com/AliDujie/Quantitative-UX-Research)** — 量化研究、HEART 框架、A/B 测试
- **[Value-Proposition-Design](https://github.com/AliDujie/value-proposition-design)** — 价值主张画布、商业模式设计
- **[Storytelling-with-Data](https://github.com/AliDujie/storytelling-with-data)** — 数据叙事、可视化设计

**推荐工作流**：
1. 用 JTBD 理解用户深层动机
2. **用本技能创建人物角色和用户细分** ← 从动机到画像
3. 用 Universal-Design-Methods 设计验证研究
4. 用 Quantitative-UX-Research 量化细分规模
5. 用 Value-Proposition-Design 设计针对性方案
6. 用 Storytelling-with-Data 向团队传达角色洞察

## 📦 依赖

- Python >= 3.8
- **无外部依赖**（纯标准库实现）
- 兼容 macOS / Linux / Windows

## 📚 关于《The User Is Always Right》

- **书名**: The User Is Always Right: A Practical Guide to Creating and Using Personas
- **作者**: Steve Mulder & Ziv Yaar
- **出版**: New Riders, 2007
- **地位**: 人物角色方法奠基之作，用户体验领域经典
- **适用**: UX 研究员、产品经理、设计师、市场人员

## 🎯 人物角色核心概念速查

| 概念 | 说明 |
|------|------|
| **首要角色 (Primary)** | 设计的主要目标，不能忽略其需求 |
| **次要角色 (Secondary)** | 重要但不主导设计决策 |
| **补充角色 (Supplemental)** | 用于完整描述用户群体 |
| **被排斥角色 (Served Excluding)** | 明确不服务的用户类型 |
| **用户细分** | 基于行为、态度、目标的群体划分 |
| **功能优先级矩阵** | 角色×功能重要性评估工具 |

## 📜 许可

本技能仅供内部学习和研究使用。

## 👨‍💻 作者

- **GitHub**: [@AliDujie](https://github.com/AliDujie)
- **Emp ID**: 27768
- **Nickname**: 渡劫
