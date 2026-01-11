# Complete Large Codebase Reading Methodology

This document contains the complete 11-step methodology for reading and understanding large codebases efficiently.

## Overview

**Goal:** Quickly understand and modify code safely, not read every file.

**Principle:** Goal-oriented reading with progressive disclosure - start broad, drill deep as needed.

## The 11 Steps

### 1. Define Reading Task

**Don't start from directory trees. Start with a real goal.**

Large codebases should be read **around a real objective** (fix bug, add feature, debug performance, security audit). Without a goal, you'll get lost in details.

**Practice:** Write a one-sentence goal:
- "Trace HTTP request from route handler to database and back"
- "Understand how authentication tokens are validated and refreshed"
- "Find where user permissions are checked"

### 2. Run the Project First

**First hour priority (3 things):**

1. **Read README:**
   - What does the project do?
   - How to start/run?
   - What's the minimal example?

2. **Read CONTRIBUTING / Development Guide:**
   - How to run tests?
   - Code structure conventions?
   - Branch strategy?

3. **Run minimal path:**
   - Can you build locally?
   - Can you run a minimal test or demo?
   - Can you execute a simple operation?

**Why:** Running code transforms reading from guessing to verification.

### 3. Draw Architecture Map (C4 Thinking)

**Don't start with UML class diagrams. Start with "far to near" hierarchical views:**

**Level 1: System Context** - Who uses it? What external systems? What dependencies?
**Level 2: Containers** - What are the deployable units? (frontend, API, worker, DB, queue)
**Level 3: Components** - What are the key components within a container? (auth service, domain service, repository, adapter)

The C4 model is designed for this "zoom in" communication approach.

> You don't need it to be beautiful - just enough to navigate: **where's the entry point, how does data flow, where are the boundaries?**

### 4. Find Entry Point + Trace One Real Request

**More effective than "read modules" is "read one execution path":**

- Web: route/controller → service → repository → external dependency
- Async: consumer/handler → business processing → ack/retry/idempotency
- CLI/Batch: main/command → argument parsing → execution path

**Strongly recommended:**
- Use debugger to step through
- Add logging, set breakpoints
- Walk through once (many engineers consider this the fastest way to understand a large codebase)

### 5. Treat Tests as Executable Documentation

**The most reliable documentation in large codebases is often: tests + assertions + fixtures.**

If code is too old/hard to test, write **characterization tests** first - record current behavior, then refactor/change under protection. This is a classic strategy from "Working Effectively with Legacy Code."

### 6. Git Archaeology: Understand Why It's Written This Way

**When you see "weird code", don't dismiss it - ask: What historical problem is this solving?**

**Common techniques:**
- `git blame` find related commits → read commit message / PR discussion
- When encountering large refactors/formatting commits, use "trace back to parent commits" to skip noise
- This is often called "git archaeology"

### 7. Read PR / Code Review: Use Others' Explanations to Accelerate Understanding

PRs often contain: background, trade-offs, edge cases, rollback methods - easier to understand "intent" than reading final code directly.

Also, large teams/large codebases commonly emphasize **readability and code health**, as this directly determines whether newcomers can understand.

### 8. Tool Checklist (10 minutes to configure, efficiency doubled)

**Code search (faster than IDE global search):**
```bash
rg "keyword" -n .
git grep "keyword"
```

**Quick understanding of entry points and call relationships:**
```bash
rg "main\(" .
rg "router|route|controller|handler" .
```

**Git archaeology:**
```bash
git log -p -- path/to/file
git blame -w -- path/to/file
```

**Run first (replace with actual project commands):**
```bash
make test    # or npm test / mvn test / go test ./... / pytest
```

### 9. Build and Maintain Terminology Glossary

**Critical step:** Don't treat this as an afterthought. Build a living glossary from day 1.

**Why it matters:**
- **Acronyms need expansion**: CTC? CLS? DB? NMS? What do they mean?
- **Domain terms aren't self-explanatory**: Detection vs Recognition, Orientation vs CLS
- **Prevents repeated lookups**: Document once, reference everywhere
- **Facilitates communication**: Shared vocabulary for architecture discussions and code reviews

**When to build:**
- **Initial collection** (Steps 1-4): Collect terms as you encounter them during first reading pass
- **Deep dive enrichment** (Step 10): Add technical details and context during module analysis
- **Continuous maintenance**: Update definitions, add cross-references, refine relationships as understanding deepens

**What to collect:**
1. **Domain-specific terms** (OCR: detection, recognition, CLS, CTC, DB, NMS)
2. **Project-specific terms** (project name, key libraries, internal abstractions)
3. **Acronyms and abbreviations** (all caps, 2-5 letters - scan README, docs, comments)
4. **Key data structures** (from type definitions, public APIs - structs, enums, traits)
5. **Configuration terms** (from config files, config structs)
6. **Algorithm names** (from function names, comments, documentation)
7. **Process flow terms** (preprocessing, inference, postprocessing stages)
8. **Coordinate system terms** (different coordinate spaces, transformations)
9. **Error handling terms** (error types, error codes, exception names)

**How to organize:**
- **By domain**: OCR-specific, ML-specific, project-specific, general programming
- **By abstraction level**: Concepts (high-level), Algorithms (specific methods), Data Structures (types), Implementation Details (code-level)
- **By scope**: Public API (user-facing), Internal (implementation), Configuration, Output

**What each entry should include:**
- **Definition**: Clear explanation of what the term means
- **Purpose**: Why it exists, what problem it solves
- **Context**: Where and how it's used in the codebase
- **Code reference**: File paths, function names (file:line references when helpful)
- **Relationships**: Related terms, parent/child concepts, synonyms
- **Examples**: Code snippets or usage examples for complex terms
- **Acronym**: Full expansion if applicable

**Tools for term extraction:**
```bash
# Find acronyms (all caps, 2-5 letters)
rg "\b[A-Z]{2,5}\b" README.md docs/ | sort -u

# Find key structs/types
rg "^(pub )?(struct|enum|trait|type) \w+" src/ -o | sort -u

# Find configuration fields
rg "config\|Config\|CONFIG" -i .

# Find enum variants
rg "^\s+[A-Z][A-Za-z0-9_]*" src/types.rs

# Find domain terms in README/docs
rg "^\s*\*\*.*\*\*" README.md docs/
```

**Organization template:**
```markdown
## Terminology Glossary

### Domain-Specific Terms
- **Term**: Definition, context, code reference, relationships

### Project-Specific Terms
- **Term**: Definition, context, code reference, relationships

### Data Structures
- **StructName**: Purpose, usage, implementation location

### Algorithms
- **AlgorithmName**: What it does, where it's used, related concepts

### Configuration Terms
- **ConfigField**: Purpose, default value, usage context

### Process Flow Terms
- **StageName**: Where it fits in the pipeline, what it does

### Coordinate Systems
- **CoordinateSpace**: How it relates to other spaces, transformation methods

### Model/Engine Terms
- **EngineTerm**: Purpose, usage, implementation details
```

**Integration with other documentation:**
- Link terms to C4 architecture diagrams (component usage)
- Cross-reference to API flow documentation (execution steps)
- Reference module analysis documents (implementation details)
- Point to test files (usage examples)

**Maintenance checklist:**
- [ ] All acronyms have expansions
- [ ] All domain terms have clear definitions
- [ ] All key data structures are documented
- [ ] Cross-references to code are accurate
- [ ] Related terms are linked
- [ ] Examples are provided for complex terms
- [ ] Terms are classified by domain and abstraction level
- [ ] Glossary is cross-referenced throughout documentation

**Success indicators:**
✅ You can explain any domain-specific term in one sentence
✅ All acronyms have expansions and definitions
✅ Key data structures are documented with purpose and usage
✅ Terms are cross-referenced to code locations
✅ Related terms are linked together
✅ You rarely need to re-lookup the same term
✅ The glossary helps newcomers understand the codebase quickly

**See also:** [terminology-building.md](terminology-building.md) for a complete guide with detailed methodology, classification examples, and best practices.

### 10. Modules to Deep Dive (Prioritize)

**Don't try to understand everything. Prioritize:**

**High priority (core functionality):**
- Main execution flow modules
- Critical business logic
- Security-sensitive code
- Performance-critical paths

**Medium priority (important support):**
- Configuration management
- Error handling
- Logging/monitoring
- Data transformation

**Low priority (auxiliary functions):**
- Utility functions
- Unused code
- Legacy code paths
- Experimental features

### 11. Next Steps

**Based on reading goals, create action plan:**

- What parts need immediate understanding?
- What can you start modifying?
- What needs deeper research?
- How to validate understanding (tests, examples, manual verification)?

## Key Principles

### Progressive Disclosure

**Don't try to understand everything at once:**

1. **Start broad:** System context, main execution flow
2. **Drill deep:** Specific modules as needed for your goal
3. **Iterate:** Refine understanding as you work

### Goal-Oriented

**Every reading session should have a clear goal:**

- What do you want to achieve?
- What do you need to understand to achieve it?
- What can you ignore?

### Test-Driven Understanding

**Tests are the most reliable documentation:**

- Read tests to understand expected behavior
- Write characterization tests to record current behavior
- Use tests as safety net before modifications

### Git History as Documentation

**Code exists for reasons:**

- Use `git blame` and `git log` to understand context
- Don't dismiss "weird code" without understanding why it exists
- Learn from past decisions (even if you'd do differently)

### Tool-Assisted

**Use tools efficiently:**

- Code search tools (ripgrep, git grep)
- Git history tools (blame, log, diff)
- Language-specific tools (linters, formatters, documentation generators)
- Debuggers and profilers

## Documentation Structure

**When documenting your understanding, use this structure:**

```
code-reading/
├── README.md              # Index and progress tracking
├── code-reading.md        # Main framework (methodology + findings + terminology)
├── architecture.md        # C4 architecture map (Level 1-4)
├── api-flow.md            # Execution flow tracing
└── key-modules.md         # Detailed module analysis
```

**Progressive disclosure:**
- README: Overview and navigation
- Main doc: Methodology and high-level findings
- Specialized docs: Detailed analysis (loaded only when needed)

**Terminology section:**
- Include a dedicated "Terminology" or "Key Concepts and Terminology" section in `code-reading.md` (e.g., section 9)
- Build incrementally from day 1 - don't wait until everything is understood
- Cross-reference terms throughout documentation (architecture diagrams, API flows, module analysis)
- Maintain as a living document - update as understanding deepens, add relationships as connections are discovered

## Common Pitfalls

**"I don't know where to start"**
→ Define a concrete goal. Even "understand how user authentication works" is better than "understand everything."

**"The codebase is too large"**
→ Focus on your goal. Trace one execution path. Ignore unrelated modules.

**"I'm reading files alphabetically"**
→ Stop. Find the entry point. Trace an execution path. Read modules as needed.

**"I'm trying to understand everything"**
→ Don't. Focus on what you need for your goal. You can always learn more later.

**"There are no tests"**
→ Write characterization tests. Record current behavior. Use tests as documentation.

## Success Indicators

**You've successfully understood a codebase when:**

✅ You can explain the main execution flow from entry to exit
✅ You can locate where specific functionality is implemented
✅ You can trace data transformations through the system
✅ You can identify where to make changes for your goal
✅ You have a comprehensive terminology glossary that helps navigate the codebase
✅ You can explain any domain-specific term in one sentence
✅ All acronyms have clear expansions and definitions
✅ Key data structures are documented with purpose and usage
✅ Terms are cross-referenced to code locations and related documentation
✅ You rarely need to re-lookup the same term
✅ You can explain architectural decisions (even if you'd do differently)
✅ You feel confident modifying code without breaking things

**Not required:**
- ❌ Having read every file
- ❌ Memorizing every function
- ❌ Understanding every detail
