# Uncertainty Expression Guide

How to clearly express likelihood, confidence, and distinguish facts, judgments, and speculation in research findings.

## Three Categories (Kent Framework)

### Fact
- **Definition**: Observable, verifiable with high certainty
- **Example**: "Company X filed SEC Form 10-K on March 15, 2024"
- **Language**: Direct statements, no qualifiers needed

### Judgment / Estimate
- **Definition**: Evidence sufficient but still probabilistic
- **Example**: "Company X is likely to exceed revenue targets based on Q1-Q3 performance"
- **Language**: Use probability words, express confidence level

### Inference / Speculation
- **Definition**: Limited evidence, more logic-based
- **Example**: "If market conditions hold, Company X may expand to Europe"
- **Language**: Explicitly mark as inference, state evidence limitations

## Probability Words (5-Tier System)

Use consistent probability words. Avoid mixing systems.

| Probability Word | Typical Meaning | When to Use |
|------------------|-----------------|-------------|
| **Almost impossible** | <5% chance | Strong evidence against |
| **Unlikely** | 10-30% chance | Evidence points against, but possible |
| **Possible** | 30-70% chance | Evidence mixed or insufficient |
| **Likely** | 70-90% chance | Evidence points toward |
| **Almost certain** | >90% chance | Strong evidence supporting |

**Important**: If you cannot assign a probability ranking, use only "possible" and explain why you cannot be more specific.

## Confidence Levels

Confidence reflects your assessment of the **quality and reliability of the evidence** supporting your judgment, not the probability of the event itself.

### High Confidence
- **Evidence Quality**: Multiple independent, high-quality sources
- **Independence**: Sources are independent of each other
- **Consistency**: Sources agree, or conflicts are explained
- **Gaps**: Minimal information gaps affecting the judgment

### Medium Confidence
- **Evidence Quality**: Some independent verification, mixed quality
- **Independence**: Partial independence
- **Consistency**: Some agreement, some conflicts
- **Gaps**: Some information gaps, but not critical

### Low Confidence
- **Evidence Quality**: Single source, or low-quality sources
- **Independence**: Limited or no independent verification
- **Consistency**: Conflicting or insufficient information
- **Gaps**: Significant information gaps affecting judgment

## Expressing Likelihood + Confidence

**Key Rule**: Don't mix likelihood and confidence in the same sentence in a way that causes confusion.

### Good Examples

**Example 1**:
- "Company X is **likely** to launch Product Y in Q2 2024 (**high confidence**). This judgment is based on official statements, regulatory filings, and supplier contracts, all indicating Q2 timeline."

**Example 2**:
- "Market growth is **possible** but uncertain (**low confidence**). Available data is limited to two industry reports with conflicting projections, and no independent verification is available."

**Example 3**:
- "Regulatory approval is **almost certain** (**high confidence**). Multiple independent sources (regulatory statements, industry analysts, company disclosures) consistently indicate approval is proceeding normally."

### Bad Examples (Avoid)

**Bad 1**: "It's likely with high confidence" (redundant, confusing)
- **Better**: "It's likely (**high confidence**)" or "It's almost certain (**high confidence**)"

**Bad 2**: "Probably maybe" (vague, evasive)
- **Better**: "Possible (**low confidence**)" with explanation

**Bad 3**: "Apparently" or "Reportedly" without assessment
- **Better**: "According to [source], X occurred. We assess this as **likely** (**medium confidence**) based on [reason]."

## Words to Avoid (Kent's "Weasel Words")

These words shift responsibility away from the analyst and reduce usefulness:

- **"Apparently"** (without assessment)
- **"Seemingly"** (without assessment)
- **"Reportedly"** (without assessment)
- **"Allegedly"** (legal term, not appropriate for analysis)
- **"It is said that"** (vague attribution)

**Instead**: Make a judgment and take responsibility:
- "Based on [sources], we assess X as **likely** (**medium confidence**)"
- "Evidence suggests X, but verification is limited (**low confidence**)"

## Template for Key Judgments

Each Key Judgment should follow this structure:

```
**KJ-X**: [Conclusion sentence]

- **Likelihood**: [Probability word: Almost impossible/Unlikely/Possible/Likely/Almost certain]
- **Confidence**: [High/Medium/Low]
- **Rationale**: [Why this likelihood and confidence level]
- **Evidence Anchor**: [1-2 sentences pointing to most critical evidence]
- **Alternative Explanations**: [What else could explain this, why not chosen]
- **Flip Conditions**: [What evidence would change this judgment]
```

### Example

**KJ-1**: Company X will launch Product Y in Q2 2024.

- **Likelihood**: Likely
- **Confidence**: High
- **Rationale**: Multiple independent sources (company statements, regulatory filings, supplier contracts) consistently indicate Q2 timeline. No conflicting evidence found.
- **Evidence Anchor**: Company CEO stated Q2 launch in earnings call (Source 1). Regulatory filing shows Q1 completion of required approvals (Source 2). Supplier contracts specify Q2 delivery dates (Source 3).
- **Alternative Explanations**: Launch could be delayed to Q3 if supply chain issues emerge, but current evidence does not support this scenario.
- **Flip Conditions**: Official announcement of delay, major supplier disruption, regulatory approval delayed beyond Q1.

## Uncertainty Sources

When expressing uncertainty, explain where it comes from:

1. **Evidence gaps**: Missing information
2. **Source reliability**: Questions about source credibility
3. **Conflicting evidence**: Multiple sources disagree
4. **Method limitations**: Analysis method has limitations
5. **Time/context**: Information may be outdated or context-dependent

### Example

"Market size is **likely** 10-15 million users (**medium confidence**). Uncertainty comes from: (1) Limited independent verification (only two industry reports available), (2) Reports use different methodologies, (3) Data is 6 months old, market may have changed."

## What Would Change Our Mind (Flip Conditions)

For each Key Judgment, explicitly state:

1. **What evidence would significantly increase confidence?**
2. **What evidence would decrease confidence or change the judgment?**
3. **What signals/indicators should be monitored?**

### Example

**Current Judgment**: Company X will maintain market share (**likely**, **medium confidence**)

**Would Increase Confidence**:
- Q4 financial results showing stable market share
- Independent market research confirming position
- Competitor announcements indicating no major shifts

**Would Decrease Confidence or Change Judgment**:
- Competitor launches disruptive product
- Regulatory changes affecting Company X's advantage
- Major customer defections announced

**Monitoring Indicators**:
- Quarterly market share reports
- Competitor product launches
- Customer satisfaction surveys
- Regulatory announcements

## Calibration

Good uncertainty expression is **calibrated**: When you say "likely" (70-90%), the event should actually occur 70-90% of the time over many judgments.

**Common Calibration Errors**:
- **Overconfidence**: Saying "almost certain" when evidence only supports "likely"
- **Underconfidence**: Saying "possible" when evidence strongly supports "likely"
- **Inconsistency**: Using different probability words for similar evidence strength

**Improving Calibration**:
- Review past judgments: Did events occur at the rate your probability words suggested?
- Use structured techniques (ACH, Key Assumptions Check) to assess evidence more systematically
- Get feedback from others on your uncertainty expression

## References

- Kent, Sherman. "Words of Estimative Probability" (CIA)
- ICD 203: Analytic Standards (uncertainty expression requirements)
- Tetlock, Philip. "Superforecasting" (calibration techniques)
