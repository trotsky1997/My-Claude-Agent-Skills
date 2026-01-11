---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

---
name: README
model: fast
---

# DeepResearch Subagents

This directory contains Cursor subagent definitions for the DeepResearch evidence-chain production line.

## Available Subagents

| File | Subagent Name | Role |
|------|---------------|------|
| `research-lead.md` | research-lead | Research Lead / Owner |
| `collection-strategist.md` | collection-strategist | Collection Strategist / Source Map Designer |
| `verification-expert.md` | verification-expert | OSINT Verification Expert |
| `evidence-librarian.md` | evidence-librarian | Evidence Librarian / Sourcing |
| `methodologist.md` | methodologist | Analytic Methodologist |
| `quant-analyst.md` | quant-analyst | Data Analyst |
| `domain-expert.md` | domain-expert | Domain Expert |
| `editor.md` | editor | Editor / Storyliner |
| `qa-gatekeeper.md` | qa-gatekeeper | QA / Ethics Gatekeeper |
| `devils-advocate.md` | devils-advocate | Devil's Advocate |

## Usage in Cursor

These subagents are automatically available in Cursor when:
1. Cursor is in Nightly mode (Settings > Cursor Settings > Beta > Nightly)
2. Subagents feature is enabled (Settings > Cursor Settings > Subagents)

### Invoking Subagents

Use the Task tool in Cursor to invoke a specific subagent:

```
@research-lead Create a Task Contract for researching [topic]
@collection-strategist Design a Source Map for these claims: [claims]
@verification-expert Verify this image: [image URL]
@evidence-librarian Register this evidence: [evidence details]
@methodologist Apply ACH to these hypotheses: [hypotheses]
@quant-analyst Check consistency of these numbers: [numbers]
@domain-expert Validate this mechanism: [mechanism description]
@editor Package this research into a report: [research content]
@qa-gatekeeper Perform QA on this report: [report]
@devils-advocate Challenge this conclusion: [conclusion]
```

## Workflow Integration

Subagents work together in a 12-stage workflow:

1. **research-lead**: Stage 0 (Task Contract), Stage 1 (KIQ & Claim Draft)
2. **collection-strategist**: Stage 2 (Source Map Design), Stage 3 (Collection)
3. **verification-expert**: Stage 4 (OSINT Verification)
4. **evidence-librarian**: Stage 5 (Evidence Registration)
5. **methodologist**: Stage 6 (Structured Reasoning)
6. **quant-analyst**: Stage 7 (Data Consistency)
7. **devils-advocate**: Stage 8 (Counter-World Attack)
8. **domain-expert**: Stage 9 (Domain Validation)
9. **editor**: Stage 10 (Conclusion Packaging)
10. **qa-gatekeeper**: Stage 11 (QA Gate)

See [../../SKILL.md](../../SKILL.md) "Evidence-Chain Production Line" section for detailed workflow.

## Weekly Rituals

Subagents participate in weekly rituals:

- **Claim Review** (Monday): research-lead + methodologist
- **Kill Point Review** (Wednesday): devils-advocate + research-lead
- **Conflict Evidence Stand-up** (Friday): evidence-librarian + all
- **Devil's Day** (Bi-weekly): devils-advocate + all
- **QA Pre-Gate** (Before delivery): qa-gatekeeper + editor

See [../../SKILL.md](../../SKILL.md) "Weekly Research Rituals" section for detailed rituals.

## File Format

Each subagent file follows this format:

```yaml
---
name: subagent-name
description: Brief description of role and responsibilities
model: inherit
---

# Role Name

[System prompt with detailed instructions]
```

## Customization

To customize a subagent:

1. Edit the corresponding `.md` file
2. Modify the `description` field for triggering
3. Update the system prompt for behavior changes
4. Restart Cursor to load changes

## References

- Main DeepResearch skill: [../../SKILL.md](../../SKILL.md) (contains all subagent documentation, workflow, and rituals)
