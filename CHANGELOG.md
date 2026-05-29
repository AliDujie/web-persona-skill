## v3.0.0 (2026-05-29) — Complete architectural restructure

**From "book index" to "execution manual" — organized by what you DO, not what you READ.**

### Added
- **8 core operation manuals** (`references/core/01-08`): project-setup, qualitative-research, quantitative-research, mixed-method, analysis-clustering, persona-creation, validation, application
- New `references/core/` and `references/advanced/` directory structure

### Changed
- All 39 existing reference files moved to `references/advanced/` (preserved as deep-dive dictionary)
- **SKILL.md** completely rewritten: 864 lines → ~120 lines focused quick-reference
- **README.md** rewritten for v3.0 structure
- Each core doc cross-references relevant advanced files
- Knowledge organized by execution lifecycle stage, not by book/author

### Why
- v2.5–v2.7 grew to 39 references organized by book — comprehensive but hard to navigate
- Users needed to know "which book" instead of "what step am I at"
- v3.0 puts execution flow first, keeps all depth accessible via advanced/

---

## v2.7.0 (2026-05-29) — Research craft & continuous discovery expansion

**Completing the full upstream-to-downstream persona lifecycle: from interview technique to narrative expression.**

### Added
- **8 new reference documents** in `references/32-39`, organized into 2 tracks:
  - 📗 **E · Research Craft & Continuous Discovery** (4): `32-portigal-interviewing-users.md`, `33-fitzpatrick-mom-test.md`, `34-torres-continuous-discovery.md`, `35-alvarez-lean-customer-development.md`
  - 📘 **F · Experience Mapping, Narrative & Theory** (4): `36-kalbach-mapping-experiences.md`, `37-quesenbery-storytelling-ux.md`, `38-kuniavsky-observing-user-experience.md`, `39-christensen-competing-against-luck.md`
- **SKILL.md v2.7 decision tree** with 8 new branches covering research craft, continuous discovery, journey mapping, UX storytelling, observation methods, and JTBD origin theory
- **SKILL.md `§5.4` knowledge base** with E/F two-segment tables
- **references/README.md v2.7 E/F index** + extended situation-based lookup table

### Changed
- SKILL.md frontmatter `description` rewritten: 30+ books, adds Portigal/Fitzpatrick/Torres/Alvarez/Kalbach/Quesenbery/Kuniavsky/Christensen
- SKILL.md title paragraph adds E/F tracks (upstream research + mapping/narrative)
- SKILL.md directory tree adds `references/32-39` with E/F track annotations
- pyproject.toml description rewritten with v2.7 scope
- Version synced to 2.7.0 across `SKILL.md` / `pyproject.toml` / `persona/__init__.py` / `README.md`

### Sources integrated (v2.7 new)
- **E · Research Craft**: Steve Portigal《Interviewing Users》(2nd ed., 2024); Rob Fitzpatrick《The Mom Test》(2013); Teresa Torres《Continuous Discovery Habits》(2021); Cindy Alvarez《Lean Customer Development》(2014)
- **F · Mapping & Narrative**: Jim Kalbach《Mapping Experiences》(2nd ed., 2021); Whitney Quesenbery & Kevin Brooks《Storytelling for User Experience》(2010); Mike Kuniavsky《Observing the User Experience》(2nd ed., 2012); Clayton Christensen, Taddy Hall, Karen Dillon & David S. Duncan《Competing Against Luck》(2016)

---

## v2.6.0 (2026-05-29) — ABCD deep-dive: quantitative + psychology + ethics + engineering

**Major release — from "multi-perspective meta-decider" to "meta-decider + quantitative engine + behavioral psychology + ethics + engineering code".**

### Added
- **16 new reference documents** in `references/16-31`, organized into 4 tracks:
  - 🟢 **A · Quantitative & Modern** (4): `16-mikkelson-statistical-personas.md`, `17-revella-buyer-personas.md`, `18-synthetic-ai-personas.md`, `19-service-design-personas.md`
  - 🟣 **B · Psychology & Behavioral Science** (4): `20-kahneman-dual-system.md`, `21-fogg-behavior-model.md`, `22-jtbd-persona-integration.md`, `23-thick-data-ethnography.md`
  - 🟠 **C · Ethics & Diversity** (4): `24-kat-holmes-mismatch.md`, `25-cababa-systems-second-order.md`, `26-hofstede-cross-cultural.md`, `27-bias-audit-personas.md`
  - 🔵 **D · Engineering** (4): `28-clustering-engineering.md`, `29-llm-prompt-library.md`, `30-okr-roadmap-bridge.md`, `31-measurement-toolkit.md`
- **4 new Python modules** in `persona/` (paired with D-track refs):
  - `persona/clustering.py` — `PersonaClusterer` + `ClusteringResult`, three methods (KMeans / LCA / Factor+Cluster) with auto-selection, bootstrap stability, `to_persona_drafts()` feeding PersonaBuilder; sklearn required, stepmix optional
  - `persona/llm_prompts.py` — `PersonaPromptLibrary` + `PersonaPrompt`, 4 prompt classes (simulated_interview / copy_evaluation / devils_advocate / multi_persona_tournament), Constitutional bilingual templates, decoupled from any LLM SDK
  - `persona/okr_bridge.py` — `OKRBridge` + `Objective`/`KeyResult`/`RoadmapItem`/`OKRPlan` dataclasses, `derive_okrs(profiles)` auto-Objective + 4 KR templates, `score_roadmap` RICE/ICE with persona-priority weighting
  - `persona/measurement_toolkit.py` — `MeasurementToolkit` + `Metric`/`MetricSnapshot`, 6 metric types (NPS/CES/CSAT/goal_conversion/activation/retention/custom), `register_from_kr` OKR bridge, `report_okr_progress` review
- **SKILL.md decision tree extension** with 16 v2.6 deep-dive branches covering each new methodology
- **SKILL.md `§5.3` knowledge base** with A/B/C/D 4-segment table and reference→code mapping
- **references/README.md v2.6 four-segment index** with situation-based lookup table extension

### Changed
- SKILL.md frontmatter `description` rewritten to reflect 23+ books and 4-dimensional positioning (meta-decider + quantitative + psychology + engineering)
- SKILL.md directory tree extended with all 16 new references and 4 new persona modules
- pyproject.toml description rewritten with v2.6 module list
- Version synced to 2.6.0 across `SKILL.md` / `pyproject.toml` / `persona/__init__.py` / `README.md`

### Sources integrated (v2.6 new)
- **A · Quantitative**: Mikkelson / Salminen / Brickey statistical persona literature; Adele Revella《Buyer Personas》; Park《Generative Agents》(UIST 2023); Salminen *From 2,772 Segments to Five Personas* (CSCW 2024); Microsoft Research *PersonaHub*; Stickdorn《This Is Service Design Doing》
- **B · Psychology**: Daniel Kahneman《Thinking, Fast and Slow》《Noise》; Thaler & Sunstein《Nudge》; BJ Fogg《Tiny Habits》; Nir Eyal《Hooked》; Christensen《Competing Against Luck》; Klement《When Coffee and Kale Compete》; Wunker《Jobs to be Done》; Ulwick ODI; Tricia Wang *Why Big Data Needs Thick Data*; Geertz《Interpretation of Cultures》; Madsbjerg《The Moment of Clarity》
- **C · Ethics**: Kat Holmes《Mismatch》; Microsoft Inclusive Design Toolkit; Sheryl Cababa《Closing the Loop》; Donella Meadows《Thinking in Systems》; Sasha Costanza-Chock《Design Justice》; Hofstede《Cultures and Organizations》; Erin Meyer《The Culture Map》; Edward Hall《Beyond Culture》; Marsden & Haag *Stereotypes and Politics*; Buolamwini & Gebru *Gender Shades*; Eubanks《Automating Inequality》
- **D · Engineering**: John Doerr《Measure What Matters》; Christina Wodtke《Radical Focus》; Marty Cagan《Inspired》; Frederick Reichheld《The Ultimate Question 2.0》; Matthew Dixon《The Effortless Experience》; scikit-learn / stepmix; OpenAI/Anthropic prompt-engineering best practices

---

## v2.5.0 (2026-05-29) — Multi-book methodology integration

**Major release — expanded from single-source (Mulder) to multi-book persona methodology system.**

### Added
- **10 new reference documents** in `references/`:
  - Tier 1 (Foundation): `06-cooper-goal-directed-design.md`, `07-persona-lifecycle.md`, `08-goodwin-digital-age.md`
  - Tier 2 (Modern): `09-indi-young-mental-models.md`, `10-lene-nielsen-10steps.md`, `11-lean-ux-proto-personas.md`
  - Tier 3 (Specialized): `12-just-enough-research.md`, `13-user-story-mapping.md`, `14-norman-mental-conceptual-models.md`, `15-personas-critique-and-defense.md`
- **SKILL.md "Methodology Lineage"** section listing 9 methodology schools and 12+ classic works
- **SKILL.md "Method Selection Decision Tree"** — auto-recommends methodology based on project stage / complexity / org maturity
- **references/README.md** restructured into three-tier index with situation-based lookup table

### Changed
- SKILL.md frontmatter `description` updated to reflect multi-book scope
- SKILL.md "Five · Knowledge Base" section expanded from 2 entries to 15
- SKILL.md "Four · Directory Structure" updated to show all 15 reference files
- README.md "What's New" section restructured with v2.5.0 release highlights and "Earlier Releases" archive
- Version synced to 2.5.0 across `SKILL.md` / `pyproject.toml` / `persona/__init__.py` / `README.md`

### Sources integrated
- Alan Cooper et al.《About Face 4》《Inmates》
- Pruitt & Adlin《The Persona Lifecycle》
- Kim Goodwin《Designing for the Digital Age》
- Indi Young《Mental Models》《Practical Empathy》
- Lene Nielsen《Personas - User Focused Design》(2nd ed.)
- Gothelf & Seiden《Lean UX》(2nd ed.)
- Erika Hall《Just Enough Research》(2nd ed.)
- Jeff Patton《User Story Mapping》
- Don Norman《The Design of Everyday Things》
- Chapman & Milham《The Personas' New Clothes》(HFES 2006)
- Microsoft Design Team《Inclusive Design》(Persona Spectrum)

## v2.4.97 (2026-05-26)

- Repo maintenance: added Examples badge (3 runnable scripts), added examples/ reference to Resources section, ecosystem cross-reference audit
- Version sync across README badge/SKILL.md/pyproject.toml/__init__.py

## v2.4.96 (2026-05-25)
- Version bump to 2.4.96 across all files, duplicate header consolidation in README

## v2.4.95 (2026-05-25)
- Version sync across all files, ecosystem cross-reference verification

## v2.4.93 (2026-05-22)
- Repo maintenance: version sync across README badge, SKILL.md, pyproject.toml, __init__.py
- Ecosystem cross-reference verification across all 6 AliDujie skills

## v2.4.91 (2026-05-22)
- Ecosystem badge consistency check across all 6 AliDujie skills
- Version bump to 2.4.91 across README/SKILL.md/pyproject.toml/__init__.py

## v2.4.90 (2026-05-22)
- SKILL.md frontmatter: synced version to 2.4.90, added `author` field, moved badge outside YAML boundary
- Repo maintenance: added 'Persona Anti-Patterns Quick Reference' (CN/EN) to Pro Tips
- Enhanced ecosystem cross-reference with 6-skill pipeline code recipes
- Added 'Segmentation → Persona → Validation' 3-step workflow guide
- Updated version across README/SKILL.md/pyproject.toml/__init__.py

## v2.4.88 (2026-05-21)
- Added Persona Anti-Patterns Table with before/after examples
- Enhanced ecosystem cross-references with ASCII pipeline diagram
- Version sync across README/SKILL.md/pyproject.toml/__init__.py

## v2.4.87 (2026-05-20)
- Added Persona Validation Checklist (golden rules table)
- Added Segmentation Quick Guide (3-step workflow)
- Version sync across all files

## v2.4.83 (2026-05-19)
- Repo maintenance: synced versions across README/SKILL.md/pyproject.toml
- Added segmentation-first pro tip workflow before persona creation
- Enhanced anti-patterns section with concrete examples

## v2.4.82 (2026-05-19)
- Added segmentation-first pro tip before persona creation, improved version history

## v2.4.81 (2026-05-19)
- Added persona anti-patterns to USAGE.md and improved README completeness

## v2.4.80 (2026-05-19)
- Synced SKILL.md version + ecosystem improvements

## v2.4.79 (2026-05-16)
- Fixed footer version mismatch (v2.4.75 → v2.4.78) in README.md
- Verified ecosystem cross-references and bilingual consistency across all 7 skills
- Version alignment: pyproject.toml, __init__.py, SKILL.md, README.md badge

# Changelog

## v2.4.78 (2026-05-16)

- Repo maintenance: Added `__version__` to `__all__` export list for proper `from persona import __version__`
- Verified version alignment across pyproject.toml, SKILL.md, README, and `__init__.py`

## v2.4.77 (2026-05-16)

- Repo maintenance: enhanced English Features at a Glance
- Improved What's New callout formatting
- Verified ecosystem cross-references and bilingual consistency
- Confirmed all persona reference docs linked in CN+EN


## v2.4.73 (2026-05-16)

- Synced Python `__version__` with SKILL.md version
- Verified all persona builder and survey code examples
- Confirmed ecosystem cross-references across all 7 skills
- Checked bilingual (CN/EN) consistency in README and SKILL.md
- Refreshed last-updated badges

## v2.4.71 (2026-05-15)

- Repo maintenance: verified all code examples smoke-test pass
- Verified ecosystem cross-references across all 7 skills
- Checked bilingual (CN/EN) consistency in README and SKILL.md

## v2.4.70 (2026-05-15)

- Repository maintenance: aligned `pyproject.toml` version with SKILL.md (v2.4.70)
- Aligned package `__version__` in `persona/__init__.py` with SKILL.md (v2.4.70)
- Verified all ecosystem cross-references and bilingual consistency
- Refreshed last-updated date

## v2.4.69 (2026-05-15)

- Repository maintenance: aligned `pyproject.toml` version with SKILL.md

## v2.4.68 (2026-05-15)

- Repo maintenance: version bump; verified version alignment across SKILL.md, README, and pyproject.toml

## v2.4.67 (2026-05-15)

- Repo maintenance: version bump; verified version alignment across SKILL.md, README, and pyproject.toml

## v2.4.66 (2026-05-15)

- Repo maintenance: version bump; verified version alignment across SKILL.md, README, and pyproject.toml

## v2.4.65 (2026-05-15)

- Repo maintenance: version bump; verified version alignment across SKILL.md, README, and pyproject.toml

## v2.4.64 (2026-05-14)

- Repo maintenance: add cross-skill reference section to 02-measuring-results.md, expand ecosystem collaboration coverage

## v2.4.63 (2026-05-14)

- Repo maintenance: add cross-skill reference sections to key reference docs (01-persona-basics.md, 04-persona-driven-workflows.md), expand ecosystem collaboration coverage

## v2.4.62 (2026-05-14)

- Repo maintenance: standardize badge ordering (Python → License) and License badge format across all 6 AliDujie skill repos for visual consistency

## v2.4.61 (2026-05-14)

- Repo maintenance: sync README version badges/footers to pyproject.toml (2.4.59→2.4.60), fix CN TOC capability count (9→10), update changelog

## v2.4.60 (2026-05-14)

- Repo maintenance: fix broken TOC anchor link (#-end-to-end-workflow-all-7-skills → #-end-to-end-ecosystem-workflow)

## v2.4.58 (2026-05-14)

- Repo maintenance: added "Why Teams Choose Persona" comparison tables (CN/EN) with specific before/after impact data, enhanced promotional content in "Why Use This Skill?" sections

## v2.4.57 (2026-05-13)

- Repo maintenance: deduplicated changelog entries, removed standalone Changelog section, enhanced version table consistency

## v2.4.55 (2026-05-13)

- Repo maintenance: added persona-driven workflows reference doc (04-persona-driven-workflows.md), updated references README

## v2.4.32 (2026-05-13)

- Routine repo maintenance: verified all standard files, ecosystem link consistency, Last Updated timestamp
- No breaking changes

## v2.4.31 (2026-05-13)

- Added Structured Thinking Model to Quick Decision Guide (CN + EN) for better cross-skill discoverability
- Verified version alignment across README.md, SKILL.md, and pyproject.toml
- No breaking changes

## v2.4.30 (2026-05-13)

- Repo maintenance: added "When to use Persona" decision guide to SKILL.md, added cross-skill workflow examples to README, version bump to 2.4.30

## v2.4.28 (2026-05-13)

- Repo maintenance: added references/README.md index, standardized ecosystem documentation

## v2.4.27 (2026-05-13)

- Repo maintenance: aligned footer version badge with SKILL.md (v2.4.26→v2.4.27), added end-to-end ecosystem integration workflow example

## v2.4.26 (2026-05-13)

- Repo maintenance: fixed footer version mismatch, added ecosystem workflow Pro Tip, bumped to v2.4.26

## v2.4.25 (2026-05-13)

- Repo maintenance: added English Dependencies section, verified ecosystem cross-references

## v2.4.24 (2026-05-13)

- Repo maintenance: added anti-persona Pro Tip (CN+EN), enhanced Persona-UDM research integration example

## v2.4.23 (2026-05-13)

- Repo maintenance: fixed English changelog table missing markdown separator, added Contributing link to footer, enhanced cross-skill collaboration examples with Persona-to-VPD workflow code snippet, aligned all version references

## v2.4.21 (2026-05-13)

- Repo maintenance: fixed README footer version mismatch (footer was 2 versions behind badge), aligned all version references across README/SKILL.md/pyproject.toml/CHANGELOG, verified ecosystem cross-references and bilingual consistency

## v2.4.20 (2026-05-13)

- Repo maintenance: verified ecosystem cross-reference consistency; version alignment across all files (pyproject.toml, SKILL.md, README); ensured Last Updated timestamp current

## v2.4.17 (2026-05-13)

- Fixed changelog table `| |` formatting bug in README.md (both CN and EN sections)
- Added end-to-end workflow entry to English Table of Contents
- Aligned all version references across README.md, SKILL.md, and pyproject.toml

## v2.4.16 (2026-05-13)

- Added English TOC and 5-min Quick Start Checklist
- Improved English Quick Start example code, enhanced Features at a Glance table descriptions

## v2.4.15 (2026-05-13)

- Improved English Quick Start example code clarity
- Enhanced Features at a Glance table descriptions
- Aligned SKILL.md frontmatter version with README and pyproject.toml

## v2.4.14 (2026-05-13)

- Added FAQ sections (CN/EN) to README for improved discoverability
- Added CODE_OF_CONDUCT.md to all skill repositories
- Added .github/ISSUE_TEMPLATE/ with bug report and feature request templates
- Maintained cross-repo consistency and version alignment

## v2.2.6 (2026-05-13)

- Repo maintenance: aligned pyproject.toml version (2.2.3→2.2.5) and SKILL.md version (2.2.4→2.2.5) with README badge; verified ecosystem cross-reference consistency

## v2.2.5 (2026-05-13)

- Updated README badge and Last Updated timestamp

## v2.2.4 (2026-05-13)

- Added Chinese Quick Decision Guide table for bilingual consistency
- Added English End-to-End Workflow section (e-commerce persona workflow)
- Updated SKILL.md version to v2.2.4

## v2.2.2 (2026-05-13)

- Fixed version mismatch: SKILL.md (v2.4.19) and pyproject.toml (v2.1.0) aligned to v2.2.2
- Added Quantitative UX Research and Structured Thinking Model to collaboration table
- Updated version references across all files

## v2.2.1 (2026-05-13)

- Added English Features at a Glance, Who Is This For, Best Practices, Troubleshooting sections

## v2.2.0 (2026-05-13)

- Added English section, FAQ, version badge, fixed ecosystem links

## v2.1.0 (2026-05-13)

- Added Structured Thinking Model (🧠) to ecosystem ASCII diagrams (CN and EN sections)
- Verified cross-references consistency across all related skills tables
- Updated version numbers, badges, and Last Updated dates
