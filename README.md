# Web Persona Skill

基于《赢在用户：Web人物角色创建和应用实践指南》(The User Is Always Right) 的完整人物角色工具包。

## 功能概览

- **知识库**: 结构化 Markdown 文档，涵盖人物角色理论、研究方法、案例精华等
- **访谈框架** (`InterviewBuilder`): 按段落自动生成定制化访谈提纲
- **问卷设计** (`SurveyBuilder`): 支持需求型/验证型/满意度型三种问卷自动生成
- **用户细分** (`SegmentAnalyzer`): 数据管理、细分评估、矩阵可视化
- **角色创建** (`PersonaBuilder`): 完整角色文档生成、对比表、质量评审
- **商业策略** (`StrategyAnalyzer`): 角色价值评估、功能优先级矩阵、竞品分析
- **设计指导** (`DesignAdvisor`): 信息架构、内容策略、路径验证
- **衡量成果** (`MeasureSystem`): 测试脚本、指标体系、Bug优先级自动计算

## 快速开始

```python
from persona import PersonaSkill, InterviewBuilder, PersonaBuilder

# 统一入口
skill = PersonaSkill("飞猪旅行")

# 生成访谈提纲
guide = skill.generate_interview("用户访谈", ["goals", "behaviors", "pain_points"])
print(guide)

# 设计调查问卷
survey = skill.generate_survey("需求调研", "needs", pain_points=["找酒店耗时", "价格不透明"])
print(survey)

# 创建人物角色
skill.add_persona("小明", "效率型用户", "primary", "我只想快速完成",
                  goals=["快速完成任务"], behaviors=["频繁使用"],
                  attitudes=["追求效率"], bio="小明是一位忙碌的白领...")
skill.add_persona("小红", "探索型用户", "secondary", "我喜欢发现新东西",
                  goals=["发现好物"], behaviors=["浏览为主"],
                  attitudes=["好奇心强"], bio="小红是一位大学生...")
print(skill.render_all_personas())

# 质量评审
print(skill.review_personas())

# 功能优先级
skill.add_feature("快速预订", {"小明": "高", "小红": "低"}, "高", "低")
print(skill.render_feature_matrix())

# Bug优先级自动计算
print(skill.add_bug("首页加载慢", "小明", is_primary=True, blocks_core=True))
# → P0: 首页加载慢 (影响首要角色的核心任务，必须立即修复)
```

## 知识库搜索

```python
from persona import load_knowledge, search_knowledge

# 搜索关键词
results = search_knowledge("细分")
for topic, paragraphs in results.items():
    print(f"[{topic}] 找到 {len(paragraphs)} 个相关段落")
```

## 文件结构

```
├── SKILL.md                    # Skill 定义文件
├── README.md                   # 项目说明
├── INSTALL.md                  # 安装指南
├── pyproject.toml              # 构建配置
├── requirements.txt            # 依赖声明
├── persona/                    # Python 包
│   ├── __init__.py             # API 入口与 PersonaSkill 统一类
│   ├── config.py               # 全局配置与常量
│   ├── utils.py                # 知识库加载与文本工具
│   ├── templates.py            # 模板定义（访谈、角色、报告）
│   ├── interview.py            # 访谈提纲生成器
│   ├── survey.py               # 问卷设计生成器
│   ├── segment.py              # 用户细分分析器
│   ├── persona_builder.py      # 人物角色文档生成器
│   ├── strategy.py             # 商业策略与功能优先级
│   ├── design.py               # 信息架构与内容策略
│   └── measure.py              # 测试计划与衡量体系
└── docs/
    └── book_notes/             # 书籍知识笔记
        ├── part1_人物角色介绍.md
        └── part3c_衡量成果.md
```

## 依赖

纯 Python 标准库实现，无外部依赖，兼容 Python 3.8+。

## Credits

Based on: *The User Is Always Right: A Practical Guide to Creating and Using Personas* by Steve Mulder and Ziv Yaar (New Riders, 2007)
