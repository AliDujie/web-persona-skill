# Persona 驱动的研究工作流

> 如何以人物角色为核心，驱动整个用户研究生命周期

---

## Persona 在生态系统中的位置

Persona 是 7 技能工作流的 **起点**，定义"为谁设计"：

```
Persona (你在这里) → JTBD → UDM → QuantUX → VPD → SWD
```

## Persona 作为研究锚点

证据驱动的人物角色是所有后续研究的锚点：

| 后续技能 | 如何使用 Persona | 具体协作方式 |
|---------|-----------------|------------|
| JTBD | 角色 → Jobs 映射 | 每个 Persona 对应一组特定的 Jobs to be Done |
| UDM | 角色 → 研究设计 | 基于 Persona 的行为特征设计针对性研究方法 |
| QuantUX | 角色 → 行为验证 | 验证 Persona 的行为假设是否成立 |
| VPD | 角色 → 价值主张 | 为不同 Persona 创建差异化的价值主张画布 |
| SWD | 角色 → 故事主角 | 将 Persona 作为数据叙事的主角 |

## Persona 驱动工作流

### 阶段 1: 创建证据驱动的角色

```python
from persona import PersonaSkill

persona = PersonaSkill("旅行平台")

# 基于真实数据创建角色（非虚构假设）
persona.add_persona(
    name="效率型商旅用户",
    short_desc="碎片时间工作，重视效率和确定性",
    priority="primary",
    quote="我不想浪费时间，帮我找到最合适的就行",
    goals=["快速完成预订", "确保行程可靠"],
    behaviors=["高频使用", "移动端优先", "不比较价格"],
    attitudes=["时间 > 金钱", "确定性 > 最优价"],
    bio="32岁，咨询公司合伙人，每月出差 8-12 次"
)
```

### 阶段 2: Persona → JTBD（从角色到需求）

```python
from jtbd import JTBDSkill

jtbd = JTBDSkill("旅行平台")

# Persona 的行为特征映射到 JTBD 框架
# 效率型商旅用户的核心 Job: "在最短时间完成可靠的差旅预订"
# 情感 Job: "确保出差不会出问题（不耽误会议）"
# 社会 Job: "展现专业形象（公司报销合规）"
```

### 阶段 3: Persona → UDM（从角色到研究）

```python
from udm import UDMSkill

udm = UDMSkill("旅行平台")

# 基于 Persona 设计研究方法
methods = udm.recommend_methods(
    "了解效率型商旅用户的预订痛点",
    phase=1  # 探索阶段
)
# 推荐：情境访谈（跟随出差）+ 日记研究（记录决策过程）
```

### 阶段 4: Persona → VPD（从角色到价值主张）

```python
from vpd import VPDSkill

vpd = VPDSkill("旅行平台", "效率型商旅用户")

# 为这个 Persona 设计专属价值主张
canvas = vpd.analyze_canvas(
    product_name="商旅优选",
    jobs=["快速预订", "行程管理"],
    pains=["搜索耗时", "行程变动"],
    gains=["一键复购", "自动提醒"]
)
```

## Persona 细分策略

### 行为细分（推荐）

| 维度 | 说明 | 数据源 |
|------|------|--------|
| 使用频率 | 高频 vs 低频 | 日志分析 |
| 任务类型 | 预订 vs 管理 vs 报销 | 行为数据 |
| 设备偏好 | 移动端 vs PC 端 | 使用数据 |
| 价格敏感度 | 价格驱动 vs 效率驱动 | 交易数据 |

### 态度细分

| 维度 | 说明 | 数据源 |
|------|------|--------|
| 风险偏好 | 保守 vs 冒险 | 选择行为 |
| 品牌忠诚 | 平台忠诚 vs 比价 | 使用模式 |
| 创新接受度 | 早期采用 vs 跟随 | 功能使用 |

## Persona 验证方法

创建 Persona 后，需要验证其有效性：

### 定量验证

1. **行为聚类分析**：使用 QuantUX 验证行为模式是否存在显著分组
2. **A/B 测试**：测试不同 Persona 对功能变化的响应差异
3. **留存分析**：验证 Persona 间的留存率差异是否显著

### 定性验证

1. **招募匹配**：按 Persona 描述招募用户，验证是否容易找到匹配者
2. **行为预测**：预测 Persona 的行为，观察是否与实际一致
3. **团队共识**：团队成员是否对同一 Persona 有相同理解

## Persona 更新机制

Persona 不是一次性产物，需要定期更新：

| 触发条件 | 更新方式 |
|---------|---------|
| 新市场进入 | 新增 Persona |
| 产品重大改版 | 更新行为特征 |
| 用户行为显著变化 | 调整优先级 |
| 新数据源可用 | 补充量化验证 |

## 常见 Persona 陷阱

| 陷阱 | 表现 | 避免方法 |
|------|------|---------|
| 虚构角色 | 基于假设而非数据 | 始终用行为数据支撑 |
| 过多角色 | 创建 10+ 个 Persona | 限制在 3-5 个，区分 Primary/Secondary |
| 静态角色 | 创建后不再更新 | 定期验证和更新 |
| 过度描述 | 关注无关细节（宠物、爱好） | 聚焦与产品设计相关的特征 |
| 无人使用 | 创建后束之高阁 | 将 Persona 融入每个设计评审 |

---

*本文档是 AliDujie Web Persona 技能生态系统的补充参考。*
