---

name: skill-selector

description: Self-driven skill selection system that uses internal curiosity asking (self-questioning) to analyze user requests, infer context from available information, and automatically recommend the most appropriate skills. Use when (1) User requests are ambiguous or unclear, (2) Multiple skills could potentially match a request, (3) User needs help discovering available skills, (4) Understanding user context is needed before recommending skills, or (5) User asks "what skills are available" or "which skill should I use".

---

# Skill Selector

## Overview

The skill-selector uses **internal curiosity asking**—a self-questioning approach where the agent asks itself strategic questions and answers them based on available context—to understand user needs and automatically recommend the most appropriate skills. Instead of asking the user questions, the agent analyzes the request, examines available context (files, project structure, conversation history), asks itself key questions internally, infers answers from context, and then matches those needs to available skills.

## Core Workflow

### 1. Analyze the Request

When a user's request is unclear or could match multiple skills:

- **Examine the request** - Parse what the user is asking for
- **Check available context** - Look at open files, project structure, conversation history
- **Identify gaps** - Determine what information is missing
- **Infer from context** - Use available information to fill gaps

### 2. Self-Questioning (Internal Curiosity Asking)

**Ask yourself** strategic questions internally and answer them based on available context:

- **Context**: "What is the user trying to accomplish overall?" → Answer by analyzing the request and project context
- **Task specifics**: "What exact operations are needed?" → Answer by examining file types, project structure, or explicit mentions
- **Technical constraints**: "What languages, frameworks, platforms?" → Answer by checking file extensions, imports, config files
- **Scope**: "One-time task or repeated workflow?" → Answer by analyzing the nature of the request
- **Outcome**: "What does success look like?" → Answer by understanding the stated goal

**Key principle**: Answer these questions yourself using available context before asking the user. Only ask the user if context is truly insufficient.

See [curiosity-asking-guide.md](references/curiosity-asking-guide.md) for detailed self-questioning strategies and patterns.

### 3. Discover Available Skills

List all available skills using the helper script:

```bash
python scripts/list_skills.py --format json
```

The script scans `$CODEX_HOME/skills` (default: `~/.codex/skills`) and extracts skill metadata from each skill's SKILL.md frontmatter. Use JSON format for programmatic matching.

### 4. Match Needs to Skills

After answering your internal questions, match the inferred needs to skills using:

- **Domain match**: PDF operations → PDF skill
- **Task match**: Create document → DOCX skill  
- **Technical stack match**: Python projects → uv-python-manager skill
- **Workflow match**: Multi-step processes → Multiple skills

See [skill-matching-strategies.md](references/skill-matching-strategies.md) for detailed matching algorithms and patterns.

### 5. Recommend and Explain

Present recommendations directly with:

- **Skill name** (clear identifier)
- **Why it matches** (explanation based on your analysis)
- **What it can do** (capabilities summary)
- **How to use it** (brief usage hint)
- **Alternatives** (if multiple options exist)

**No need to ask the user for confirmation** - proceed with the recommendation based on your analysis.

## Self-Questioning Patterns

### For Ambiguous Requests

**User**: "I need help with files"

**Ask yourself internally**:

1. "What type of files?" → Check open files, file extensions, project structure
2. "What operations needed?" → Analyze the request verb (read, edit, convert, analyze?)
3. "How many files?" → Check if single file is open or multiple files mentioned
4. "What's the end goal?" → Infer from request context and project type

**Answer from context**: If user has a PDF open → PDF skill. If Python files → Python-related skills.

### For Technical Tasks

**User**: "I want to manage dependencies"

**Ask yourself internally**:

1. "What language/project type?" → Check file extensions (.py → Python, package.json → Node.js)
2. "What specific tasks?" → Analyze request (install, update, lock, resolve?)
3. "What tools currently used?" → Check for requirements.txt, pyproject.toml, package.json
4. "Replace or add capabilities?" → Infer from context

**Answer from context**: If pyproject.toml exists → uv-python-manager skill. If requirements.txt → pip/uv skills.

### For Multi-Step Workflows

**User**: "I need to create a presentation"

**Ask yourself internally**:

1. "What's it about?" → Check project context, open files, conversation history
2. "Existing content or new?" → Check if content files exist
3. "What format?" → Infer from context (PowerPoint, Google Slides, PDF?)
4. "Branding requirements?" → Check for brand assets or style guides
5. "Regular updates?" → Analyze request nature

**Answer from context**: If brand assets exist → brand-guidelines skill. If starting from scratch → document creation skills.

## Best Practices

### Do's

- ✅ **Answer questions yourself first** - Use available context to infer answers
- ✅ **Check files and project structure** - Examine open files, file extensions, config files
- ✅ **Analyze conversation history** - Use previous context to understand current request
- ✅ **Make educated inferences** - It's better to infer and be slightly wrong than to ask unnecessarily
- ✅ **Proceed with confidence** - Once you've analyzed, recommend directly

### Don'ts

- ❌ Don't ask the user questions you can answer from context
- ❌ Don't ask for information that's visible in open files
- ❌ Don't ask "what language" if .py files are open
- ❌ Don't ask "what project type" if project structure is clear
- ❌ Don't hesitate - analyze, infer, recommend

## Example Self-Questioning Flow

```
User: "I need help with my project"

[Internal self-questioning]
Q: "What type of project?"
A: [Check open files] → pyproject.toml, .py files → Python project

Q: "What specific help needed?"
A: [Analyze request] → Generic "help" suggests multiple areas, but context shows...

Q: "What's in the project?"
A: [Check files] → Has pyproject.toml (dependency management), no AGENTS.md (documentation needed)

[Direct recommendation without asking user]
You: "Based on your Python project, I recommend:

**uv-python-manager**
- Why: Your project uses pyproject.toml and you're working with Python
- Capabilities: Package installation, virtual environments, project setup
- Usage: Use when installing packages, managing environments, or setting up Python projects

**cursor-agents-md**
- Why: Your project doesn't have AGENTS.md yet, and you may need project documentation
- Capabilities: Creating AGENTS.md files, project documentation, coding guidelines
- Usage: Use when setting up project-specific agent instructions or documentation

I can help you get started with either of these right away."
```

## Resources

### scripts/list_skills.py

Lists all available skills with their metadata. Can output in text, JSON, or markdown format.

**Usage**:

```bash
# Text format (default)
python scripts/list_skills.py

# JSON format
python scripts/list_skills.py --format json

# Markdown format
python scripts/list_skills.py --format markdown

# Custom skills directory
python scripts/list_skills.py --skills-dir /path/to/skills
```

### references/curiosity-asking-guide.md

Comprehensive guide on curiosity asking techniques, question patterns, and best practices for understanding user needs.

### references/skill-matching-strategies.md

Detailed strategies for matching user needs to skills, including matching algorithms, common patterns, and edge cases.

## When to Use This Skill

Use skill-selector when:

1. **User requests are ambiguous** - Need clarification before proceeding
2. **Multiple skills could match** - Need to identify the best fit
3. **User asks about available skills** - Help discover what's available
4. **Context is unclear** - Need to understand user's situation first
5. **User explicitly asks for skill recommendations** - "Which skill should I use?"

## Integration with Other Skills

After recommending a skill:

- Help the user understand how to use it
- Offer to help with the actual task using the recommended skill
- Suggest skill combinations if a workflow requires multiple skills

## Context Sources for Self-Answering

When answering your internal questions, check these sources in order:

1. **Open files** - File extensions, imports, content
2. **Project structure** - Directory layout, config files
3. **Conversation history** - Previous messages and context
4. **File names** - Often reveal project type and purpose
5. **Code content** - Imports, function names, comments
6. **Config files** - package.json, pyproject.toml, requirements.txt, etc.

## Adaptive Analysis

Adjust your analysis depth based on:

- **Request clarity**: Clear requests → quick analysis, unclear → deeper exploration
- **Context richness**: Rich context → confident inference, sparse → more careful analysis
- **Complexity**: Simple tasks → direct match, complex → multi-skill workflow
- **Urgency**: Quick tasks → fast analysis, long-term → thorough exploration

