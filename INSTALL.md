# Web Persona Skill 安装指南

## 一、作为 AoneClaw Skill 安装（推荐）

将 `SKILL.md` 放到以下路径即可自动加载：

```bash
mkdir -p ~/.aoneclaw/skills/web-persona
cp SKILL.md ~/.aoneclaw/skills/web-persona/SKILL.md
```

安装后，在对话中使用 `skill.load('web-persona')` 即可调用。

## 二、作为 GitHub 仓库使用

直接将本目录所有文件推送到 GitHub 仓库即可：

```bash
git init
git add .
git commit -m "feat: Web Persona Skill - 完整安装包"
git remote add origin https://github.com/AliDujie/web-persona-skill.git
git push -u origin main
```

## 三、目录结构说明

```
web-persona-skill/
├── SKILL.md          # 核心Skill定义文件（548行，22KB）
├── README.md         # 仓库说明文档
├── INSTALL.md        # 本安装指南
└── docs/
    ├── 赢在用户：WEB人物角色创建和应用实践指南.pdf  # 原始参考书籍
    └── book_notes/                                    # 阅读笔记
        ├── part1_人物角色介绍.md
        └── part3c_衡量成果.md
```

## 四、Skill能力概览

- **10大模块** A-J：方法选择 → 定性研究 → 定量研究 → 用户细分 → 角色真实化 → 活力维护 → 商业策略 → 功能定义 → 结构内容设计 → 成果衡量
- **12项能力矩阵**：教练级 + 执行者级双层覆盖
- **4个实战工具模板**：研究计划、角色文档、功能矩阵、竞品分析
- **7个经典案例**：VistaPrint、BrownCo、CNN.com、Best Buy、Philips、FedEx、Sony
- **6个FAQ** + **12项质量检查清单**
