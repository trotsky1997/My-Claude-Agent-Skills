# DeepResearch Project Management Template

Complete project management template with all stages, quality gates, and tracking tables. Fill all `TODO:` items before proceeding to next stage.

## Project Basic Information

| Field | TODO |
|-------|------|
| Project Name | TODO |
| Research Lead | TODO |
| Research Subject | TODO |
| Audience / Decision-makers | TODO |
| Decision Context | TODO |
| Time Window | TODO |
| Delivery Deadline | TODO |
| Deliverable Format | TODO (Brief / Memo / Report / Table / Deck) |
| Compliance Boundaries | TODO |

---

## Stage A — Task Contract (Problem Definition)

### Research Goal (One Sentence)
> TODO

### Non-Goals (Explicitly Not Researching)
* TODO
* TODO

### Key Intelligence Questions (KIQs, 3–7 questions)
* KIQ-1: TODO
* KIQ-2: TODO
* KIQ-3: TODO
* (Add up to KIQ-7)

### Success Criteria (What is "Good Enough")
* TODO

**Quality Gate 1 Checklist:**
- [ ] Research questions are answerable, falsifiable, with clear time windows
- [ ] Non-goals are explicit (prevent scope creep)
- [ ] KIQs ≤ 7 and actionable
- [ ] Any team member can restate "what we're answering and what we're not" from Task Contract

---

## Stage B — Issue Tree & Hypotheses

### Issue Tree (MECE Decomposition)
* Branch A: TODO
  * Sub-Q: TODO
* Branch B: TODO
  * Sub-Q: TODO
* Branch C: TODO

### Initial Hypotheses (Falsifiable)

| Hypothesis | What Evidence Needed | Current Status |
|------------|----------------------|----------------|
| H1 | TODO | ⬜ |
| H2 | TODO | ⬜ |

**Quality Gate 2 Checklist:**
- [ ] Issue tree is MECE (mutually exclusive, collectively exhaustive)
- [ ] Each sub-question has evidence requirements + source map
- [ ] Cross-validation design exists (at least two complementary source types)
- [ ] Plan can guide someone else to collect, and won't follow a single path

---

## Stage C — Collection Plan

### Source Map

| Sub-Question | Primary Source | Cross Source | Retrieval Route |
|--------------|----------------|--------------|-----------------|
| Sub-Q1 | TODO | TODO | TODO |
| Sub-Q2 | TODO | TODO | TODO |

### Source Register

| Source | Type | Publication Date | Reliability | Bias Risk | Use For Proving |
|--------|------|------------------|-------------|-----------|-----------------|
| TODO | TODO | TODO | ⬜ High ⬜ Med ⬜ Low | TODO | TODO |

### Evidence Table

| Claim | Evidence | Source | Strength | Supports/Contradicts | Notes |
|-------|----------|--------|----------|---------------------|-------|
| TODO | TODO | TODO | Strong/Med/Weak | Supports H1 | TODO |

**Quality Gate 3 Checklist:**
- [ ] Key claims coverage reaches threshold (e.g., 70% of core claims have usable evidence)
- [ ] Evidence is from traceable sources with timestamps/versions
- [ ] Conflicts are explicitly recorded, not ignored
- [ ] Evidence strength grading is reasonable (Strong/Med/Weak + rationale)
- [ ] Third party can reproduce "why this conclusion" from Evidence Table

---

## Stage D — Structured Analysis

### Analysis Techniques Used
* ⬜ ACH (Analysis of Competing Hypotheses)
* ⬜ Key Assumptions Check
* ⬜ Red Team / Devil's Advocate
* ⬜ Scenario Planning

### Key Assumptions

| Assumption | Why Important | Vulnerability | How to Verify |
|------------|---------------|---------------|---------------|
| TODO | TODO | High/Med/Low | TODO |

### Key Judgments

| Judgment | Likelihood | Confidence | Evidence Anchor |
|----------|-----------|------------|-----------------|
| TODO | Possible/Likely/Almost Certain | High/Med/Low | TODO |

### Alternative Explanations
* TODO
* TODO

**Quality Gate 4 Checklist:**
- [ ] At least 1 alternative explanation exists and is evaluated
- [ ] Key assumptions are explicit
- [ ] Most vulnerable assumption is identified
- [ ] Confidence matches evidence strength
- [ ] Can clearly state "what I'm most worried about being wrong"

---

## Stage E — Deliverable Checklist

**Quality Gate 5 Checklist:**
- [ ] Judgments distinguish fact/inference
- [ ] Each conclusion is traceable
- [ ] Uncertainty is explicit
- [ ] Alternative explanations exist
- [ ] Can be used for decision-making
- [ ] Key Judgments are conclusion-first, clear language, audience-appropriate
- [ ] Each judgment has traceable citations (evidence anchors)
- [ ] Uncertainty expression is consistent (probability words + confidence + gaps)
- [ ] Inference is distinguished from fact
- [ ] Reader can make decisions without reading appendices; can audit via appendices and Evidence Table

---

## Risk & Assumption Log

| Assumption / Risk | Impact | How to Test | Owner | Status |
|-------------------|--------|-------------|-------|--------|
| TODO | High/Med/Low | TODO | TODO | ⬜ |

---

## Future Monitoring Indicators (Signposts)

| Indicator | Data Source | What It Means |
|-----------|-------------|---------------|
| TODO | TODO | TODO |

---

## Project Rhythm

| Date | Target |
|------|--------|
| Day 1 | Task Contract + Issue Tree |
| Day 2–4 | Collection + Evidence Table |
| Day 5 | ACH + Initial Judgments |
| Day 6 | Red Team + Revision |
| Day 7 | Delivery |

---

## Three Essential Tables

### 1. Project Board (Progress Tracking)
Columns: Backlog → Doing → Evidence-ready → Analysis-ready → Delivered
Card Template: KIQ/Sub-question, owner, deadline, current evidence strength, blockers

### 2. Evidence Table (Quality Core)
Fields: Claim | Evidence | Source | Strength | Supports/Contradicts | Conflicts | Notes | Next step

### 3. Risk & Assumption Log (Control Rework)
Fields: Assumption | Why needed | Vulnerability | How to test | Owner | Status

These three tables cover 80% of progress and quality issues: **Board manages rhythm, Evidence Table manages truth, Assumption Log manages reasoning risk**.
