> **⚠️ Important:** You must read `cursor-agents-md` skills every time before write or update this `AGENTS.md`.

# DeepResearch Project Instructions

This file defines project-specific instructions for DeepResearch work. It must be created using the `cursor-agents-md` skill and updated whenever project guidelines change.

## Project Overview

This is a DeepResearch project following the evidence-chain production line methodology. All research work must adhere to the DeepResearch methodology defined in the skill.

## Research Guidelines

### Methodology
- Follow the 12-stage evidence-chain production line workflow
- Use subagents for specialized tasks (research-lead, collection-strategist, verification-expert, etc.)
- Apply quality gates at each stage before proceeding
- Maintain traceable evidence chains for all claims

### Quality Standards
- All Key Judgments must include: Likelihood + Confidence + Evidence anchors
- Each claim must be traceable to sources with proper citations
- Conflicts must be explicitly recorded, not hidden
- Uncertainty must be expressed consistently using probability words

### Tools
- **cursor-ide-browser**: Use for information collection, OSINT verification, and source archiving
- **cursor-agents-md**: Use when updating this AGENTS.md file

## File Structure

```
project-root/
├── AGENTS.md (this file - project instructions)
├── .cursor/
│   └── agents/ (subagent definitions)
├── [research-files]/
│   ├── Task-Contract.md
│   ├── Source-Register.md
│   ├── Evidence-Table.md
│   └── [deliverables]/
```

## Boundaries

- **Never skip quality gates**: Each stage must pass its quality gate before proceeding
- **Never hide conflicts**: Conflicting evidence must be explicitly recorded
- **Never create AGENTS.md manually**: Always use `@cursor-agents-md` skill
- **Never proceed without AGENTS.md**: Research cannot start until AGENTS.md exists
- **Never update AGENTS.md without reading cursor-agents-md**: Always consult the skill first

## Commands

- Create/update AGENTS.md: `@cursor-agents-md [instruction]`
- Invoke research-lead: `@research-lead [task]`
- Invoke collection-strategist: `@collection-strategist [task]`
- Invoke verification-expert: `@verification-expert [task]`

## Update Log

### [Date]
- Initial AGENTS.md created using cursor-agents-md skill
- DeepResearch methodology guidelines added
