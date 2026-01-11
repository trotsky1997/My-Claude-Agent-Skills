# Structured Analytic Techniques

Guide to applying structured analytic techniques to mitigate bias, improve rigor, and produce more reliable research conclusions.

## Technique Selection Router

Select technique based on problem type:

- **Causal attribution / Who did it** → ACH + prioritize disconfirming evidence
- **Future prediction / Risk** → Scenario planning + indicator framework
- **Strong consensus** → Devil's Advocacy / Team A-Team B
- **Unstable key premises** → Key Assumptions Check
- **Adversary intent/behavior** → Red Team (avoid mirror imaging)

## ACH (Analysis of Competing Hypotheses)

**Purpose**: Systematically evaluate multiple hypotheses against evidence, prioritizing disconfirming evidence to avoid premature convergence.

**Input**: Hypothesis set H1..Hn, Evidence set E1..Em

**Output**: ACH matrix + "most discriminating evidence" list + elimination/retention rationale

**Procedure**:

1. List 3–7 mutually exclusive or distinguishable hypotheses
2. For each piece of evidence, mark against each hypothesis: Consistent (C) / Inconsistent (I) / Neutral (N)
3. **Prioritize "inconsistent evidence"** (most discriminating)
4. Output "current least-bad hypothesis" + discriminators still needing verification

**Key Principle**: Evidence that is inconsistent with a hypothesis is more valuable than evidence that is consistent (it helps eliminate hypotheses).

**Example Matrix**:

| Evidence | H1: X did it | H2: Y did it | H3: Z did it |
|----------|-------------|-------------|-------------|
| E1: Witness saw X | C | I | I |
| E2: Y has alibi | I | C | N |
| E3: Z's motive unclear | N | N | I |

**Common Failure Modes**:
- Only looking for confirming evidence
- Not seriously considering alternative hypotheses
- Premature convergence on "most likely" without systematic elimination

## Key Assumptions Check

**Purpose**: Identify and test the most critical assumptions underlying your analysis.

**Output**:
- Assumptions list (premises behind each judgment)
- Vulnerability (most fragile premise)
- Test plan (how to verify/alternative data)

**Procedure**:

1. List all assumptions underlying key judgments
2. For each assumption, assess:
   - Why is it needed?
   - How vulnerable is it? (High/Medium/Low)
   - How can it be tested?
   - What alternative evidence exists?
3. Identify the most vulnerable assumption
4. Design verification strategy

**Example**:

| Assumption | Why Needed | Vulnerability | How to Test |
|------------|------------|---------------|-------------|
| Market will grow 10% annually | Basis for revenue projection | High (depends on external factors) | Compare with historical growth, industry reports, expert forecasts |
| Competitor will not enter | Assumption for market share | Medium (public info available) | Monitor competitor announcements, hiring, R&D spending |

**When to Use**: Early in project (most useful diagnostic technique). Also use when key premises are unstable or when conclusions depend heavily on specific assumptions.

## Devil's Advocacy / Red Team

**Purpose**: Systematically challenge your own analysis by taking the strongest opposing position.

**Output**:
- Mainline judgment (your primary conclusion)
- Best case alternative (strongest counter-argument)
- What evidence would flip (flip conditions)
- Caveats (qualifiers to include in deliverable)

**Procedure**:

1. State your mainline judgment clearly
2. Identify the strongest alternative explanation
3. List all evidence that supports the alternative
4. Explain why you didn't choose it (but acknowledge its strength)
5. Identify what new evidence would cause you to flip
6. Write caveats that should appear in the deliverable

**Key Principle**: The goal is not to prove yourself wrong, but to identify the weakest points in your analysis and strengthen them.

**Example**:

**Mainline Judgment**: Company X will launch Product Y in Q2 2024.

**Best Alternative**: Company X will delay launch to Q3 2024 due to supply chain issues.

**Supporting Evidence for Alternative**:
- Supplier reports indicate component shortages
- Company X has history of delaying launches
- Q2 timeline seems aggressive given development stage

**Why Not Chosen**: Primary sources (company statements, regulatory filings) consistently indicate Q2. Supply chain issues appear manageable based on supplier diversity.

**Flip Conditions**: 
- Official announcement of delay
- Supplier bankruptcy or major disruption
- Regulatory approval delayed beyond Q1

**Caveats for Deliverable**: "Assuming no major supply chain disruptions or regulatory delays, launch expected Q2 2024."

## Scenario Planning

**Purpose**: Explore multiple plausible futures when uncertainty is high, especially for predictions or risk assessment.

**Procedure**:

1. Identify key uncertainties (2-3 most important)
2. Create scenario matrix (typically 2x2 or 2x3)
3. Develop narrative for each scenario
4. Identify indicators/signposts for each scenario
5. Assess implications for decision-making

**Example** (Market Entry Decision):

**Key Uncertainties**: Regulatory approval (Yes/No), Competitor response (Aggressive/Passive)

**Scenarios**:
- Scenario A: Approval + Passive → Fast expansion
- Scenario B: Approval + Aggressive → Price war, slow growth
- Scenario C: No Approval + Passive → Delayed entry
- Scenario D: No Approval + Aggressive → Market blocked

**Indicators**:
- Scenario A: Approval announcement, competitor focuses elsewhere
- Scenario B: Approval + competitor price cuts, marketing blitz
- Scenario C: Regulatory delay, competitor maintains status quo
- Scenario D: Regulatory rejection, competitor strengthens position

## Team A / Team B

**Purpose**: When consensus is too strong, assign separate teams to argue opposite positions.

**Procedure**:

1. Team A argues for the consensus position
2. Team B argues for the strongest alternative
3. Both teams present evidence and reasoning
4. Decision-makers evaluate both positions
5. Synthesis identifies what evidence would resolve the disagreement

**When to Use**: When there's strong consensus but high stakes, or when groupthink is suspected.

## Indicators & Signposts

**Purpose**: Identify observable signals that would confirm, disconfirm, or change your judgment.

**Output**:
- Indicator list (what to watch)
- Data sources (where to get the information)
- Thresholds (what value would trigger reassessment)
- Actions (what to do if threshold is reached)

**Example**:

| Indicator | Data Source | Threshold | Action |
|-----------|-------------|-----------|--------|
| Monthly active users decline >5% | Company quarterly reports | 2 consecutive quarters | Revise growth assumptions |
| Regulatory filing mentions new product | SEC filings, company website | Any mention | Update product roadmap analysis |
| Key executive departure | Company announcements, LinkedIn | C-suite or VP level | Assess impact on strategy execution |

## Common Bias Mitigation

### Confirmation Bias
- **Problem**: Seeking only confirming evidence
- **Solution**: ACH (prioritize disconfirming), Devil's Advocacy

### Premature Convergence
- **Problem**: Stopping analysis too early
- **Solution**: ACH (systematic elimination), Key Assumptions Check

### Mirror Imaging
- **Problem**: Assuming adversary thinks like you
- **Solution**: Red Team, scenario planning with adversary perspective

### Groupthink
- **Problem**: Consensus without critical evaluation
- **Solution**: Team A/Team B, Devil's Advocacy

### Overconfidence
- **Problem**: Expressing more certainty than evidence warrants
- **Solution**: Key Assumptions Check, explicit uncertainty expression

## Integration with Evidence Table

Always link structured analysis back to Evidence Table:

- Which evidence supports/contradicts each hypothesis (ACH)
- Which assumptions are most vulnerable (Key Assumptions Check)
- What evidence would flip the judgment (Devil's Advocacy)
- What indicators to monitor (Scenario Planning)

## References

- CIA Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis
- Heuer, Richards J. "Psychology of Intelligence Analysis"
- Kent, Sherman. "Words of Estimative Probability"
