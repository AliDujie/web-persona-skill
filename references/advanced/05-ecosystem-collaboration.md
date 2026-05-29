# Persona 跨技能协作指南

> Web Persona 如何与 AliDujie 生态系统中的其他技能协作

---

## Persona 在生态系统中的位置

Persona 是 7 技能工作流的 **起点**，定义"为谁设计"：

```
Persona (你在这里) → JTBD → UDM → QuantUX → VPD → SWD
```

## Persona → 其他技能的数据流转

### Persona → JTBD：从角色到深层需求

Persona 定义"谁"，JTBD 回答"他们想完成什么"：

| Persona 输出 | → JTBD 输入 | 处理方式 |
|---------|-----------|---------|
| 角色目标 | Job 描述 | 转化为 Job Story |
| 行为模式 | 使用场景 | 映射到 Job 阶段 |
| 痛点 | 阻碍因素 | Forces of Progress 分析 |
| 角色细分 | 细分市场 | Job-based 细分策略 |

**协作示例：**
```python
# Step 1: Persona 定义角色
from persona import PersonaSkill
persona = PersonaSkill("旅行平台")
persona.add_persona("小明", "效率型用户", "primary",
                    "我只想快速完成预订",
                    goals=["快速找到酒店", "一键支付"])

# Step 2: JTBD 基于角色挖掘深层需求
from jtbd import JTBDSkill
jtbd = JTBDSkill("旅行平台")
# 用 Persona 的 goals 作为 JTBD 的 Job 输入
score = jtbd.score_opportunity("快速完成预订", struggle=4, importance=5)
```

### Persona → UDM：从角色到研究方法

Persona 角色指导 UDM 选择研究方法和招募标准：

| Persona 输出 | → UDM 输入 | 处理方式 |
|---------|-----------|---------|
| 角色描述 | 招募标准 | 精准招募参与者 |
| 行为模式 | 情境访谈场景 | 在真实场景观察 |
| 角色优先级 | 研究优先级 | 优先研究 primary persona |
| 设计指导 | 可用性测试任务 | 基于角色目标设计任务 |

**协作示例：**
```python
from persona import PersonaSkill
from udm import UDMSkill

persona = PersonaSkill("旅行平台")
persona.add_persona("小明", "效率型用户", "primary", "我只想快速完成预订")

# 基于 Persona 生成研究计划
udm = UDMSkill("旅行平台")
# Persona 的 primary 角色决定研究重点
interview = udm.generate_interview("情境访谈", "contextual")
```

### Persona → QuantUX：从假设到验证

Persona 行为假设需要 QuantUX 定量验证：

| Persona 输出 | → QuantUX 输入 | 验证方法 |
|---------|-----------|---------|
| 行为描述 | 日志分析过滤器 | 行为路径验证 |
| 角色细分 | 分层分析维度 | CSat 分角色统计 |
| 使用频率 | HEART 指标基线 | 各角色 Engagement 对比 |

**协作示例：**
```python
from persona import PersonaSkill
from quantux import QuantUXSkill

persona = PersonaSkill("旅行平台")
persona.add_persona("小明", "效率型用户", "primary", "快速完成预订")

# 验证 Persona 行为假设
quantux = QuantUXSkill("旅行平台")
# 用日志分析验证角色行为模式
heart = quantux.build_heart_framework()
# 分角色计算满意度
csat = quantux.analyze_csat("Q1", 500, {1: 15, 2: 25, 3: 70, 4: 190, 5: 200})
```

### Persona → VPD：从角色到价值主张

Persona 角色直接映射 VPD 画布的客户画像：

| Persona 输出 | → VPD 画布位置 |
|---------|---------------|
| 角色目标 | 客户工作 (Jobs) |
| 痛点 | 客户痛点 (Pains) |
| 期望收益 | 客户收益 (Gains) |
| 行为特征 | 客户细分 |

**协作示例：**
```python
from persona import PersonaSkill
from vpd import VPDSkill

persona = PersonaSkill("旅行平台")
persona.add_persona("小明", "效率型用户", "primary",
                    "快速完成预订",
                    goals=["快速找到酒店"],
                    behaviors=["价格比较"],
                    attitudes=["时间就是金钱"])

# 用 Persona 数据填充 VPD 画布
vpd = VPDSkill("旅行平台", "效率型用户")
canvas = vpd.analyze_canvas(
    product_name="旅行平台",
    jobs=["快速找到性价比酒店"],
    pains=["搜索耗时"],
    gains=["节省时间"]
)
```

### Persona → SWD：从角色到数据叙事

Persona 数据通过 SWD 转化为团队对齐的可视化报告：

| Persona 输出 | → SWD 呈现 |
|---------|-----------|
| 角色档案 | 角色卡片可视化 |
| 功能优先级 | 优先级矩阵图 |
| Bug 影响 | 按角色影响排序 |
| 用户经济模型 | ROI 仪表盘 |

**协作示例：**
```python
from persona import PersonaSkill
from swd import SWDSkill

persona = PersonaSkill("旅行平台")
persona.add_persona("小明", "效率型用户", "primary", "快速完成预订")

# 用 SWD 呈现 Persona 研究结果
swd = SWDSkill("用户角色研究报告")
context = swd.build_context(audience="产品团队", cta="对齐角色认知")
chart = swd.recommend_chart(data_type="comparison", category_count=3)
```

## 反向引用：其他技能 → Persona

| 来源技能 | → Persona 的反馈 | 场景 |
|---------|----------------|------|
| JTBD | Job-based 角色细分 | 发现基于行为的细分比人口统计更准确 |
| UDM | 研究数据丰富角色 | 访谈发现更新角色目标和痛点 |
| QuantUX | 行为数据验证角色 | 日志数据确认/修正角色行为假设 |
| VPD | 价值匹配度评估 | 角色与价值主张的匹配度评分 |
| SWD | 可视化角色影响力 | 高管报告中角色驱动的决策展示 |

## 完整工作流示例

```python
# 7 技能端到端工作流
from persona import PersonaSkill
from jtbd import JTBDSkill
from udm import UDMSkill
from quantux import QuantUXSkill
from vpd import VPDSkill
from swd import SWDSkill

project = "旅行平台"

# 1. Persona: 定义用户
persona = PersonaSkill(project)
persona.add_persona("小明", "效率型用户", "primary", "快速完成预订")
persona.add_persona("小红", "探索型用户", "secondary", "发现好deal")

# 2. JTBD: 基于角色挖掘深层需求
jtbd = JTBDSkill(project)
score = jtbd.score_opportunity("快速完成预订", struggle=4, importance=5)

# 3. UDM: 执行用户研究
udm = UDMSkill(project)
methods = udm.recommend_methods("理解用户预订行为", phase=1)

# 4. QuantUX: 定量验证
quantux = QuantUXSkill(project)
heart = quantux.build_heart_framework()

# 5. VPD: 设计价值主张
vpd = VPDSkill(project, "效率型用户")
canvas = vpd.analyze_canvas(product_name=project, jobs=["快速找到酒店"])

# 6. SWD: 呈现给利益相关者
swd = SWDSkill(f"{project} 研究报告")
story = swd.build_story(protagonist="产品团队",
                       imbalance="用户流失源于核心痛点未解决",
                       call_to_action="批准优化预算")

print("✅ 完整工作流完成！")
```

## 最佳实践

1. **Persona 先行** — 一切从角色开始，后续技能都基于 Persona 展开
2. **用数据驱动** — 基于真实研究数据创建角色，避免凭空想象
3. **定期更新** — 随着新数据进入，持续精化角色
4. **团队对齐** — 用 SWD 将角色可视化，确保团队共享理解
5. **验证假设** — 用 QuantUX 验证角色行为假设
