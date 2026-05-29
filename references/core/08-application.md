# T8 · 应用落地 — 执行协议

## 触发条件
- 用户说"Persona 怎么用" / "帮我做优先级" / "帮我做 OKR"
- T6/T7 完成后用户要求落地方案
- 用户有 Persona + 产品 backlog / 业务目标

## 输入
- Persona 文档（必须）
- 产品 backlog / 功能列表 / 业务目标（可选——有则产出更具体）

## 执行步骤

### Step 1：确认应用场景

根据用户需求选择产出类型（可多选）：

| 场景 | 产出 |
|------|------|
| 功能排优先级 | → 功能-Persona 优先级矩阵 |
| 制定 OKR / 路线图 | → Persona-OKR 映射 |
| 设计评审 | → Persona Check 清单 |
| 度量效果 | → Persona 度量方案 |
| 团队推广 | → 推广行动方案 |

如果用户没指定，全部生成。

### Step 2：产出交付物

## 产出模板 A：功能优先级矩阵

```markdown
## 功能优先级矩阵

### 评估逻辑
- Primary Persona 需求 = P0 优先
- Secondary Persona 需求 = P1
- 伤害 Primary 的功能 = 否决
- 无特定 Persona 的功能 = 降级审视

### 优先级评估

| 功能/需求 | 目标 Persona | 对 Primary 影响 | 优先级 | 决策 |
|-----------|-------------|---------------|--------|------|
| [功能1] | Primary: [名字] | 直接服务 | P0 | ✅ 做 |
| [功能2] | Secondary: [名字] | 无影响 | P1 | ✅ 做 |
| [功能3] | Supplemental | 无影响 | P2 | ⏸️ 后期 |
| [功能4] | 无明确 Persona | 可能干扰 | - | ❌ 不做 |

### 本季度建议 Top 5
1. [功能X]——因为 [Primary] 的 [痛点/目标]
2. [功能Y]——因为 [...]
3. ...
```

## 产出模板 B：Persona-OKR 映射

```markdown
## Persona → OKR 映射

### Objective 1：[基于 Primary Persona 的核心目标推导]
> 源自 [Primary Persona 名字] 的目标："[目标描述]"

| KR | 指标 | 基线 | 目标 | 衡量方式 |
|----|------|------|------|---------|
| KR1 | [具体指标] | [当前值] | [目标值] | [怎么量] |
| KR2 | [具体指标] | [当前值] | [目标值] | [怎么量] |

### Objective 2：[基于 Secondary Persona 推导]
| KR | ... |

### 路线图优先级（RICE 评分）
| 功能 | Reach | Impact | Confidence | Effort | RICE | 排序 |
|------|-------|--------|-----------|--------|------|------|
| [功能1] | [值] | [值] | [值] | [值] | [分] | 1 |
```

## 产出模板 C：设计评审 Persona Check

```markdown
## 设计评审 Persona Check

每次设计评审回答：

- [ ] 这个设计是为哪个 Persona？
- [ ] [Primary] 看到这个页面，第一反应做什么？
- [ ] [Primary] 能在 5 秒内找到 TA 最需要的信息吗？
- [ ] 这个设计解决了 [Primary] 的哪个痛点？
- [ ] 会不会让 [Secondary] 觉得被忽略？
- [ ] 有没有讨好 [Negative] 但伤害 [Primary] 的元素？

决策规则：
- Primary vs Secondary 冲突 → 优先 Primary
- 只服务 Supplemental → 降级
- 让 Primary 体验变差 → 否决
```

## 产出模板 D：度量方案

```markdown
## Persona 度量方案

### 过程指标
| 指标 | 衡量方式 | 健康值 |
|------|---------|--------|
| 引用频率 | 每周评审中提到 Persona 几次 | ≥ 3次/周 |
| 决策影响 | 每 Sprint 多少决策引用 Persona | ≥ 1次 |
| 团队认知 | 随机问成员能否说出 Primary 核心 | 80%+ |

### 结果指标
| Persona | 核心指标 | 基线 | 目标 |
|---------|---------|------|------|
| [Primary] | NPS | [值] | [值] |
| [Primary] | 核心功能使用率 | [值] | [值] |
| [Secondary] | 留存率 | [值] | [值] |

### 更新节奏
- 每月：过程指标
- 每季度：结果指标
- 每 6 月：Persona 健康检查
```

## 产出模板 E：推广方案

```markdown
## 推广方案

### 启动会（45 min）
1. 每个 Persona 一名成员认领介绍
2. 现场练习：用 Persona 评估一个待做需求
3. 约定使用规则

### 嵌入流程
- 需求文档加 "Target Persona" 必填
- 设计评审加 Persona Check
- Sprint Planning 标注对应 Persona
- 数据看板按 Persona 分列

### 保鲜
- 每月分享"Persona 指导了这个决策"案例
- 新人 Onboarding 含 Persona 速读
- 每季度健康检查
```

## 自动衔接
全部产出后：
> "应用方案已就绪。后续有新数据（访谈/问卷），随时发给我更新 Persona。"
