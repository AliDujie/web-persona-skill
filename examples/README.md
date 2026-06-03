# Persona Runnable Examples / 可运行示例

These examples demonstrate Web Persona capabilities with real-world scenarios.
这些示例用真实场景演示 Web Persona 能力。

## Quick Start / 快速开始

```bash
cd examples/
python 01_persona_creation.py
python 02_survey_and_segmentation.py
python 03_feature_prioritization.py
python 04_segmentation.py
```

All examples use **zero dependencies** — pure Python standard library only.
所有示例使用**零依赖** — 仅 Python 标准库。

## Available Examples / 可用示例

### 01_persona_creation.py
Create and review data-driven user personas with quality scoring.
创建数据驱动的用户角色并进行质量评审。

**Use when / 适用场景**: Building personas for product design or marketing alignment.

```bash
python 01_persona_creation.py
```

### 02_survey_and_segmentation.py
Generate user research surveys and segment audiences.
生成用户调研问卷并进行用户分群。

**Use when / 适用场景**: Planning user research and identifying key segments.

```bash
python 02_survey_and_segmentation.py
```

### 03_feature_prioritization.py
Prioritize features using persona-weighted importance scores.
使用角色加权重要性评分进行功能优先级排序。

**Use when / 适用场景**: Deciding which features to build next based on target personas.

```bash
python 03_feature_prioritization.py
```

### 04_segmentation.py
User segmentation with behavioral clustering.
基于行为聚类的用户分群。

**Use when / 适用场景**: Discovering natural user segments from behavioral data.

```bash
python 04_segmentation.py
```

## Tips / 提示

- All examples use relative imports — just run from the `examples/` directory
- No `pip install` required — Persona is zero-dependency
- Feed Persona insights into JTBD for deeper motivation analysis
- See [USAGE.md](../USAGE.md) for detailed API documentation

## 🔗 Ecosystem Integration / 生态集成

Persona is the "who" layer of the AliDujie UX Research Ecosystem:
- **Persona → JTBD**: Persona segments → [JTBD](https://github.com/AliDujie/jtbd-knowledge-skill) opportunity scoring
- **Persona → UDM**: Persona data → [UDM](https://github.com/AliDujie/universal-design-methods) research planning
- **Persona → QuantUX**: Persona metrics → [QuantUX](https://github.com/AliDujie/Quantitative-UX-Research) validation
- **Persona → VPD**: Persona goals → [VPD](https://github.com/AliDujie/value-proposition-design) canvas mapping
- **Persona → SWD**: Persona economics → [SWD](https://github.com/AliDujie/storytelling-with-data) executive stories

See the [full pipeline example](../README.md#complete-pipeline-example) in README.md for a 6-skill end-to-end workflow.
