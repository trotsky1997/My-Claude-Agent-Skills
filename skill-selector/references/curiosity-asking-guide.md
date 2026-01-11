# Self-Questioning Guide for Skill Selection

## Overview

Internal curiosity asking (self-questioning) is a systematic approach where the agent asks itself strategic questions and answers them based on available context. Instead of asking the user questions, the agent analyzes the request, examines available information (files, project structure, conversation history), asks itself key questions internally, infers answers from context, and then matches needs to skills.

## Core Principles

### 1. Answer Questions Yourself First
- Ask yourself questions internally
- Answer them using available context (files, project structure, conversation)
- Only ask the user if context is truly insufficient

### 2. Start Broad, Then Narrow
- Begin with broad self-questions to understand the overall goal
- Progressively ask more specific questions based on what you discover
- Use context to narrow down possibilities

### 3. Infer from Available Information
- Check open files, file extensions, imports
- Examine project structure and config files
- Analyze conversation history
- Make educated inferences rather than asking

### 4. Identify Constraints from Context
- Technical constraints: Check file types, imports, config files
- Time constraints: Analyze request urgency and nature
- Scope constraints: Infer from request type (one-time vs. repeated)

### 5. Discover Hidden Requirements
- What the user explicitly states
- What the user implies (infer from context)
- What the project structure suggests
- What common patterns indicate

## Self-Question Categories

### Context Discovery Questions (Ask Yourself)

**Purpose**: Understand the broader context and motivation

**Questions to ask yourself**:
- "What is the user trying to accomplish overall?" → Answer by analyzing the request
- "What problem are they solving?" → Answer by examining project context
- "What's the end goal?" → Answer by understanding stated objectives
- "Is this part of a larger project?" → Answer by checking project structure

**How to answer**: Check project files, directory structure, conversation history

### Task-Specific Questions (Ask Yourself)

**Purpose**: Understand the specific task requirements

**Questions to ask yourself**:
- "What type of files/data?" → Answer by checking open files, file extensions
- "What operations needed?" → Answer by analyzing request verbs
- "How often?" → Answer by inferring from request nature
- "What's the expected output?" → Answer by understanding the goal

**How to answer**: Examine file types, analyze request language, check project patterns

### Technical Context Questions (Ask Yourself)

**Purpose**: Understand technical constraints and environment

**Questions to ask yourself**:
- "What languages/frameworks?" → Answer by checking file extensions (.py, .js, .ts)
- "What tools/platforms?" → Answer by examining config files (package.json, pyproject.toml)
- "Any specific requirements?" → Answer by checking project structure and dependencies
- "Current workflow?" → Answer by analyzing existing files and patterns

**How to answer**: Check file extensions, imports, config files, project structure

### Outcome Questions (Ask Yourself)

**Purpose**: Understand success criteria and expectations

**Questions to ask yourself**:
- "What would success look like?" → Answer by understanding the goal
- "What's most important?" → Answer by analyzing request priorities
- "Any quality/performance requirements?" → Answer by checking project type and context

**How to answer**: Infer from request nature, project type, and common patterns

## Self-Questioning Flow Patterns

### Pattern 1: Exploratory Self-Analysis
For ambiguous or unclear requests:

1. **Context**: "What is the user trying to accomplish?" → Check request, project files
2. **Scope**: "One-time or repeated?" → Analyze request nature and project patterns
3. **Details**: "What specific operations?" → Examine request verbs and file types
4. **Constraints**: "Technical requirements?" → Check file extensions, config files

**Answer from**: Request analysis, file examination, project structure

### Pattern 2: Clarification Self-Analysis
For partially clear requests:

1. **Confirm**: "The user needs [restate request]" → Verify by checking context
2. **Expand**: "What else is involved?" → Check related files and project structure
3. **Refine**: "Specific requirements?" → Examine config files and dependencies

**Answer from**: Context analysis, file examination, pattern recognition

### Pattern 3: Validation Self-Analysis
For seemingly clear requests:

1. **Verify**: "My understanding: [restate]" → Confirm by checking available context
2. **Explore alternatives**: "Could [alternative] work?" → Consider multiple skill options
3. **Check completeness**: "Anything missing?" → Review project structure for gaps

**Answer from**: Direct context analysis, skill matching, completeness check

## Skill Matching Strategy

After gathering information through curiosity asking, match user needs to skills:

### 1. Direct Match
- User explicitly mentions a domain or tool
- Example: "I need to work with PDFs" → PDF skill

### 2. Task-Based Match
- User describes a task that a skill supports
- Example: "I need to create a document" → DOCX skill

### 3. Workflow Match
- User describes a workflow that requires multiple skills
- Example: "I need to extract data, process it, and create a report" → Multiple skills

### 4. Context Match
- User's context suggests a skill
- Example: Working with Python projects → uv-python-manager skill

## Example Conversations

### Example 1: Ambiguous Request

**User**: "I need help with files"

**Curiosity Questions**:
1. "What type of files are you working with?" (PDF, DOCX, images, code files?)
2. "What do you need to do with them?" (read, edit, convert, analyze?)
3. "How many files are we talking about?" (one file, a few, many?)
4. "What's the end goal?" (extract info, modify content, organize?)

**Outcome**: Identifies specific skill (e.g., PDF skill, DOCX skill, or file management)

### Example 2: Technical Task

**User**: "I want to manage dependencies"

**Self-Questions and Answers**:
1. Q: "What programming language or project type?"
   A: [Check files] → pyproject.toml exists → Python project

2. Q: "What specific dependency management tasks?"
   A: [Analyze request] → "manage dependencies" suggests install, update, lock operations

3. Q: "What tools currently used?"
   A: [Check config] → pyproject.toml → Using modern Python packaging (possibly uv)

4. Q: "Replace or add capabilities?"
   A: [Infer] → Request suggests need for dependency management → uv-python-manager

**Outcome**: Recommend uv-python-manager skill directly

### Example 3: Multi-Step Workflow

**User**: "I need to create a presentation"

**Self-Questions and Answers**:
1. Q: "What's it about?"
   A: [Check project context] → Python project → Likely technical presentation

2. Q: "Existing content or new?"
   A: [Check files] → No presentation files → Starting from scratch

3. Q: "What format?"
   A: [Infer from context] → Common formats: PowerPoint, PDF, or web-based

4. Q: "Branding requirements?"
   A: [Check for assets] → No brand assets found → Standard format

5. Q: "Regular updates?"
   A: [Analyze request] → "create" suggests one-time, but could be ongoing

**Outcome**: Recommend document creation skills, possibly brand-guidelines if assets exist

## Best Practices

### Do's
- ✅ **Answer questions yourself first** - Use context to infer answers
- ✅ **Check files before asking** - Open files reveal project type and needs
- ✅ **Analyze project structure** - Directory layout and config files provide answers
- ✅ **Use conversation history** - Previous context helps understand current request
- ✅ **Make educated inferences** - Better to infer and be slightly wrong than ask unnecessarily
- ✅ **Proceed confidently** - Once analyzed, recommend directly

### Don'ts
- ❌ Don't ask the user questions you can answer from context
- ❌ Don't ask "what language" if .py files are open
- ❌ Don't ask "what project type" if project structure is clear
- ❌ Don't ask for information visible in open files
- ❌ Don't hesitate - analyze, infer, recommend
- ❌ Don't make the user provide information you can discover yourself

## Integration with Skill Selection

1. **Gather context** through self-questioning and context analysis
2. **Answer questions yourself** using available information
3. **Identify key requirements** from your analysis
4. **Match requirements** to available skills
5. **Recommend skills directly** with explanation (no need to confirm)

## Context Sources for Self-Answering

When answering your internal questions, check these sources in priority order:

1. **Open files** - File extensions, imports, content, file names
2. **Project structure** - Directory layout, config files, dependencies
3. **Conversation history** - Previous messages, established context
4. **File names** - Often reveal project type, purpose, and structure
5. **Code content** - Imports, function names, comments, patterns
6. **Config files** - package.json, pyproject.toml, requirements.txt, etc.

## Adaptive Analysis

Adjust your analysis depth based on:
- **Request clarity**: Clear requests → quick analysis, unclear → deeper exploration
- **Context richness**: Rich context → confident inference, sparse → careful analysis
- **Complexity**: Simple tasks → direct match, complex → multi-skill workflow
- **Urgency**: Quick tasks → fast analysis, long-term → thorough exploration
