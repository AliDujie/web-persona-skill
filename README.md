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

## 依赖

Python >= 3.8，无外部依赖。

## 许可

MIT License
