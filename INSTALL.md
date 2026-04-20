# Web Persona Skill 安装指南

## 一、作为 AoneClaw Skill 安装（推荐）

将整个目录复制到 skills 路径即可自动加载：

```bash
mkdir -p ~/.aoneclaw/skills/web-persona
cp -r SKILL.md persona/ docs/ ~/.aoneclaw/skills/web-persona/
```

安装后，在对话中使用 `skill.load('web-persona')` 即可调用。

## 二、作为 Python 包使用

```bash
# 克隆仓库
git clone https://code.alibaba-inc.com/fliggy-design-UR/web-persona-skill.git
cd web-persona-skill

# 直接使用（无需安装，纯标准库）
python3 -c "from persona import PersonaSkill; print('OK')"
```

## 三、目录结构说明

```
web-persona-skill/
├── SKILL.md              # 核心Skill定义文件（697行）
├── README.md             # 项目说明
├── INSTALL.md            # 本安装指南
├── pyproject.toml        # 构建配置
├── requirements.txt      # 依赖声明（纯标准库，无外部依赖）
├── persona/              # Python 工具包（11个模块，2600+行代码）
│   ├── __init__.py       # PersonaSkill 统一入口类
│   ├── config.py         # 配置与常量
│   ├── templates.py      # 模板定义
│   ├── utils.py          # 工具函数
│   ├── interview.py      # 访谈提纲生成器
│   ├── survey.py         # 问卷设计生成器
│   ├── segment.py        # 用户细分分析器
│   ├── persona_builder.py # 角色文档生成器
│   ├── strategy.py       # 商业策略与功能优先级
│   ├── design.py         # 信息架构与内容策略
│   └── measure.py        # 测试计划与衡量体系
└── docs/
    └── book_notes/       # 书籍知识笔记
        ├── part1_人物角色介绍.md
        └── part3c_衡量成果.md
```

## 四、Skill能力概览

- **10大模块** A-J：方法选择 → 定性研究 → 定量研究 → 用户细分 → 角色创建 → 活力维护 → 商业策略 → 功能定义 → 结构内容设计 → 成果衡量
- **24个执行指令**：每个模块含知识库+可直接执行的指令
- **11个Python模块**：提供完整的编程API
- **7个经典案例** + **6个FAQ** + **12项质量检查清单**
