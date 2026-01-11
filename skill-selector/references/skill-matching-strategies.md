# Skill Matching Strategies

## Overview

This document describes strategies for matching user needs to appropriate skills based on information gathered through curiosity asking.

## Matching Dimensions

### 1. Domain Match
Match based on the domain or field of work:
- **PDF operations** → PDF skill
- **Document creation/editing** → DOCX skill
- **Python package management** → uv-python-manager skill
- **Victoria 3 modding** → victoria3-mod-dev skill
- **Browser automation** → cursor-ide-browser related skills
- **Project documentation** → cursor-agents-md skill

### 2. Task Type Match
Match based on the type of task:
- **File processing** → File-specific skills (PDF, DOCX, etc.)
- **Code generation** → Language/framework-specific skills
- **Data analysis** → Analysis/query skills
- **Automation** → Automation/workflow skills
- **Documentation** → Documentation skills

### 3. Workflow Match
Match based on the workflow or process:
- **Multi-step processes** → Skills with workflow support
- **Repetitive tasks** → Skills with automation capabilities
- **One-time tasks** → Simple, focused skills

### 4. Technical Stack Match
Match based on technologies in use:
- **Python projects** → uv-python-manager, Python-specific skills
- **Web development** → Frontend/web skills
- **Game modding** → Game-specific skills (Victoria 3, etc.)
- **Documentation** → Documentation/markdown skills

## Skill Categories

### File Processing Skills
- PDF manipulation, editing, extraction
- DOCX creation, editing, analysis
- Image processing
- Data file handling (CSV, JSON, etc.)

### Development Skills
- Package management (uv-python-manager)
- Code generation
- Project setup
- Framework-specific skills

### Documentation Skills
- AGENTS.md creation (cursor-agents-md)
- README generation
- Technical documentation
- Markdown processing

### Automation Skills
- Browser automation
- Workflow automation
- Task automation
- Script generation

### Domain-Specific Skills
- Game modding (victoria3-mod-dev)
- Industry-specific tools
- Specialized workflows

## Matching Algorithm

### Step 1: Extract Keywords
From user responses, extract:
- Domain keywords (PDF, Python, document, etc.)
- Task keywords (create, edit, process, manage, etc.)
- Technical keywords (framework, language, tool names)
- Context keywords (project, workflow, automation)

### Step 2: Score Skills
For each available skill:
1. **Name match**: Does skill name contain keywords? (high weight)
2. **Description match**: Does description contain keywords? (medium weight)
3. **Task match**: Does skill support the described task? (high weight)
4. **Context match**: Does skill fit the user's context? (medium weight)

### Step 3: Rank and Filter
- Rank skills by total score
- Filter out skills with zero relevance
- Consider multiple skills if workflow requires it

### Step 4: Recommend
- Present top 1-3 skills
- Explain why each skill matches
- Suggest skill combinations if needed

## Common Patterns

### Pattern 1: Direct Domain Match
**User**: "I need to work with PDFs"
**Match**: PDF skill (direct domain match)

### Pattern 2: Task-Based Match
**User**: "I need to create a document"
**Match**: DOCX skill (task-based, even if user didn't mention DOCX)

### Pattern 3: Technical Stack Match
**User**: "I'm working on a Python project and need to manage dependencies"
**Match**: uv-python-manager skill (technical stack + task)

### Pattern 4: Workflow Match
**User**: "I need to extract data from PDFs, process it, and create a report"
**Match**: PDF skill + data processing skill + document creation skill

### Pattern 5: Multi-Skill Workflow
**User**: "I want to set up a new Python project with proper documentation"
**Match**: uv-python-manager + cursor-agents-md (multiple skills for complete workflow)

## Edge Cases

### No Clear Match
- Ask more specific questions
- Suggest general-purpose skills
- Recommend skill creation if needed

### Multiple Possible Matches
- Present all relevant options
- Explain differences
- Let user choose or ask clarifying questions

### Partial Match
- Recommend the closest match
- Explain limitations
- Suggest alternatives or skill combinations

### Skill Not Available
- Acknowledge the gap
- Suggest closest alternative
- Recommend skill creation if appropriate

## Recommendation Format

When recommending skills, include:

1. **Skill name** (clear identifier)
2. **Why it matches** (explanation of relevance)
3. **What it can do** (capabilities summary)
4. **How to use it** (brief usage hint)
5. **Alternatives** (if applicable)

Example:
```
Based on your needs, I recommend:

**uv-python-manager**
- Why: You're working with Python projects and need dependency management
- Capabilities: Package installation, virtual environments, project setup
- Usage: Use when installing packages, managing environments, or setting up Python projects
- Alternative: If you need more advanced features, consider [other skill]
```

## Continuous Improvement

- Track which skills are recommended most often
- Identify common user needs that lack skills
- Refine matching criteria based on feedback
- Update strategies as new skills are added
