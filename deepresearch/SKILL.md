---
name: deepresearch
description: Comprehensive DeepResearch methodology for conducting rigorous, traceable research projects with quality gates, structured analysis, and decision-ready deliverables. Use when (1) Conducting deep research projects requiring evidence-based analysis, (2) Managing research progress with quality gates and artifacts, (3) Producing research reports with traceable sources and structured reasoning, (4) Applying OSINT verification techniques, (5) Using structured analytic techniques (ACH, Key Assumptions Check, Red Team), (6) Expressing uncertainty and confidence in research findings, (7) Ensuring research deliverables meet intelligence tradecraft standards (ICD 203/206/208)
metadata:
  short-description: DeepResearch methodology with quality gates and structured analysis

---

# DeepResearch Methodology

A comprehensive methodology for conducting rigorous, traceable research projects that produce decision-ready deliverables with evidence-based analysis, structured reasoning, and quality gates.

## Core Principles

1. **Artifact-driven progress**: Research is organized into 5 stages, each producing required deliverables
2. **Quality gates**: Each stage has explicit quality criteria that must be met before proceeding
3. **Traceable evidence**: Every claim must be traceable to sources with proper citation
4. **Structured analysis**: Use structured analytic techniques to mitigate bias and improve rigor
5. **Uncertainty expression**: Clearly distinguish facts, judgments, and speculation with likelihood and confidence
6. **Decision-ready outputs**: Deliverables are structured for immediate use by decision-makers

## Research Stages

### Stage A: Task Contract (0→1)
**Deliverables:**
- Task Contract: Goal, audience, time window, scope, non-goals, deliverable format
- KIQs (Key Intelligence Questions): 3-7 must-answer questions
- Success criteria: Definition of "good enough" and "unobtainable"

**Quality Gate 1:** Research questions are answerable, falsifiable, with clear time windows. Non-goals are explicit. KIQs ≤ 7 and actionable.

### Stage B: Decomposition & Planning (1→Plan)
**Deliverables:**
- Issue tree / Hypothesis set (MECE decomposition + initial hypotheses)
- Collection plan: Source map, retrieval routes, priorities, verification strategy
- Risk log: Data gaps, timeliness, compliance boundaries, conflicting evidence expectations

**Quality Gate 2:** Issue tree is MECE. Each sub-question has evidence requirements and source routes. Cross-validation design exists (at least two complementary source types).

### Stage C: Collection & Registration (Plan→Evidence)
**Deliverables:**
- Source Register: Type, time, reliability, bias risk, usable scope for each source
- Evidence Table: Claim→Evidence→Strength→Conflict→Notes
- Collection log: Query strings, timestamps, exclusion reasons (for reproducibility and audit)

**Quality Gate 3:** Key claims coverage reaches threshold (e.g., 70% of core claims have usable evidence). Evidence is from traceable sources with timestamps/versions. Conflicts are explicitly recorded.

### Stage D: Analysis & Convergence (Evidence→Judgment)
**Deliverables:**
- Structured analysis workbook: ACH/Key Assumptions Check/Red Team (at least 1-2 techniques)
- Key Judgments (3-7): Each with likelihood + confidence + evidence anchors
- Alternative explanations and flip conditions: What would change my mind / signposts

**Quality Gate 4:** At least 1 alternative explanation exists and is evaluated. Key assumptions are explicit. Most vulnerable assumption is identified. Confidence matches evidence strength.

### Stage E: Delivery & Review (Judgment→Product)
**Deliverables:**
- Deliverable (brief/memo/table/appendices package)
- QA checklist record: Fact-checking, traceable citations, consistent uncertainty expression
- Follow-up actions: Gap list, next collection suggestions, monitoring indicators

**Quality Gate 5:** Key Judgments are conclusion-first, clear language, audience-appropriate. Each judgment has traceable citations. Uncertainty is expressed consistently. Inference is distinguished from fact.

## Quick Start Workflow

1. **Create Task Contract**: Define research question, KIQs, scope, and success criteria
2. **Build Issue Tree**: MECE decomposition with initial hypotheses
3. **Develop Collection Plan**: Source map with cross-validation strategy
4. **Collect & Register**: Build Source Register and Evidence Table as you collect
5. **Analyze**: Apply structured analytic techniques (see [STRUCTURED_ANALYSIS.md](references/STRUCTURED_ANALYSIS.md))
6. **Synthesize**: Generate Key Judgments with likelihood and confidence
7. **Deliver**: Create deliverable following [REPORT_TEMPLATE.md](references/REPORT_TEMPLATE.md) and run [QA_CHECKLIST.md](references/QA_CHECKLIST.md)

## Key Resources

### Templates & Checklists
- **[PROJECT_MANAGEMENT.md](references/PROJECT_MANAGEMENT.md)**: Complete project management template with all stages, gates, and tracking tables
- **[REPORT_TEMPLATE.md](references/REPORT_TEMPLATE.md)**: Standard report template with all required sections
- **[QA_CHECKLIST.md](references/QA_CHECKLIST.md)**: Pre-delivery quality assurance checklist

### Blank Templates (Ready to Use)
- **[project-template-blank.md](assets/project-template-blank.md)**: Blank project management template (copy and fill)
- **[report-template-blank.md](assets/report-template-blank.md)**: Blank report template (copy and fill)
- **[evidence-table-template.md](assets/evidence-table-template.md)**: Blank evidence table template
- **[source-register-template.md](assets/source-register-template.md)**: Blank source register template

### Methodology Guides
- **[STRUCTURED_ANALYSIS.md](references/STRUCTURED_ANALYSIS.md)**: Structured analytic techniques (ACH, Key Assumptions Check, Red Team, etc.)
- **[OSINT_VERIFICATION.md](references/OSINT_VERIFICATION.md)**: OSINT verification techniques for UGC, images, videos, geolocation
- **[UNCERTAINTY_EXPRESSION.md](references/UNCERTAINTY_EXPRESSION.md)**: How to express likelihood, confidence, and distinguish facts/judgments/speculation

### Quality Standards
- **[RUBRIC.md](references/RUBRIC.md)**: Evaluation rubric with 8 dimensions and scoring criteria
- **[ETHICS_GUARDRAILS.md](references/ETHICS_GUARDRAILS.md)**: Compliance and ethics boundaries

## Evidence & Citation Standards

### Source Register Minimum Fields
- Type (official/company/media/academic/UGC/database)
- Provenance (who produced, when, version)
- Access path (how obtained/paid/scraped)
- Bias risks (stakeholder interests, propaganda tendency, method limitations)
- Reliability (High/Medium/Low + rationale)
- Use limits (what it can prove)

### Evidence Table Structure
- Claim (falsifiable assertion)
- Evidence (citation + summary)
- Supports/Contradicts (which hypothesis)
- Strength (Strong/Medium/Weak: based on method and independence)
- Alternative explanations
- Notes (gaps, next verification steps)

### Citation Requirements
- Each Key Judgment: At least 2 independent sources (or 1 primary authoritative + explanation why sufficient)
- Each key number/timeline node: Must be traceable to original source or clear derivation chain
- Conflicting evidence: Must be explicitly presented with explanation of choice and remaining uncertainty

## Structured Analytic Techniques

Select technique based on problem type:
- **Causal attribution / Who did it** → ACH + prioritize disconfirming evidence
- **Future prediction / Risk** → Scenario planning + indicator framework
- **Strong consensus** → Devil's Advocacy / Team A-Team B
- **Unstable key premises** → Key Assumptions Check
- **Adversary intent/behavior** → Red Team (avoid mirror imaging)

See [STRUCTURED_ANALYSIS.md](references/STRUCTURED_ANALYSIS.md) for detailed procedures.

## Uncertainty Expression

### Three Categories (Kent)
- **Fact**: Observable, verifiable with high certainty
- **Judgment/Estimate**: Evidence sufficient but still probabilistic
- **Inference/Speculation**: Limited evidence, more logic-based

### Probability Words (5-tier)
- Almost impossible
- Unlikely
- Possible
- Likely
- Almost certain

### Confidence Levels
- **High**: Multiple independent sources, consistent, high-quality methods
- **Medium**: Some independent verification, partial consistency
- **Low**: Single source, high uncertainty, limited verification

Each Key Judgment must include: Likelihood (probability word) + Confidence (High/Medium/Low) + Why (evidence and method rationale)

See [UNCERTAINTY_EXPRESSION.md](references/UNCERTAINTY_EXPRESSION.md) for detailed guidance.

## Common Failure Modes

### Scope Creep
**Symptom**: Delivery date approaching but questions multiplying, conclusions becoming vague
**Solution**: Force return to Task Contract. New questions must answer:
1. Will not doing it affect the decision?
2. Is there an evidence path? If unobtainable, move to "future work", not current scope

### Last-Minute Citation & Verification
**Symptom**: Report finished but evidence doesn't match/links broken/inconsistent metrics
**Solution**: Front-load citation and evidence registration:
- Register sources during collection (Source Register)
- Pull evidence from Evidence Table when writing conclusions (not from memory)

## Project Rhythm (1-2 week research)

- **Day 1**: Task Contract + Issue tree + Collection plan (Gate 1/2)
- **Day 2-4**: Collection + registration + initial Evidence Table (daily Gate 3)
- **Day 5**: Structured analysis (ACH/Key Assumptions Check) + initial Key Judgments (Gate 4)
- **Day 6**: Fill gaps, handle conflicts, update confidence
- **Day 7**: Deliverable writing + Red Team + QA (Gate 5)

## Daily Standup (10 minutes)
- What new "usable evidence" was added yesterday (not "what was read")
- What hypothesis/gap will be verified today
- Blockers: Can't get data? Conflicting evidence? Scope change?

## Tradecraft Review (every 2-3 days)
- Are claims covered? Are conflicts recorded?
- Is there a tendency toward "feeling-based convergence"?
- Does collection strategy need adjustment (change source types, languages, timeline)?

## Red Team / Devil's Advocate (24 hours before delivery)
- What is the most vulnerable point of your conclusion?
- Which evidence is weakest? What if it's wrong?
- Have you "missed alternative explanations"?
