# Rules, Skills, and Subagents Reference

## Rules (规则)

### Rule Types

| Type | Description | Configuration |
|------|-------------|---------------|
| **Always Apply** | Applied to every session | `alwaysApply: true` |
| **Apply Intelligently** | Agent decides based on description | `description: "...", alwaysApply: false` |
| **Apply to Specific Files** | Applied when files match patterns | `globs: "**/*.ts", description: "..."` |
| **Apply Manually** | Only when @-mentioned | `description: "...", alwaysApply: false` |

### Rule File Structure

```
.cursor/rules/
  my-rule/
    RULE.md           # Main rule file (required)
    scripts/          # Helper scripts (optional)
```

### RULE.md Format

```markdown
---
description: Brief description (required for intelligent/manual rules)
globs: "**/*.ts"      # File pattern (required for file-specific rules)
alwaysApply: false    # Set to true for Always Apply rules
---

# Rule Title

Your rule content here...

@template-file.ts     # Reference files included when rule triggers
```

### Creating Rules

```bash
# Use built-in command
agent rule

# Or manually create
mkdir -p .cursor/rules/my-rule
cat > .cursor/rules/my-rule/RULE.md << EOF
---
description: Your rule description
alwaysApply: false
---

# Rule Title
Your rule content...
EOF
```

### Nested Rules

```
project/
  .cursor/rules/        # Project-wide rules
  backend/
    .cursor/rules/      # Backend-specific rules
  frontend/
    .cursor/rules/      # Frontend-specific rules
```

## Skills (技能)

### Skill Structure

```
skill-name/
├── SKILL.md          # Required - main instructions
├── reference.md      # Optional - detailed documentation
└── examples.md       # Optional - usage examples
```

### Storage Locations

| Type | Path | Scope |
|------|------|-------|
| Project | `.cursor/skills/skill-name/` | Current project |
| User | `~/.cursor/skills/skill-name/` | All projects |
| Built-in | `~/.cursor/skills-cursor/` | System (read-only) |

### SKILL.md Format

```markdown
---
name: skill-name
description: Brief description with trigger terms. Use when [scenarios].
---

# Skill Name

## Instructions
Step-by-step guidance...

## Examples
Concrete examples...
```

### Creating Skills

```bash
# Use built-in skill (follow creating-skills guidance)

# Or manually create
mkdir -p .cursor/skills/my-skill
cat > .cursor/skills/my-skill/SKILL.md << EOF
---
name: my-skill
description: What it does. Use when [scenarios].
---

# My Skill
Instructions...
EOF
```

### Using Skills in cursor-agent

```bash
# Method 1: Reference in prompt
agent --print "根据这个技能：
$(cat .cursor/skills/my-skill/SKILL.md)
执行任务..."

# Method 2: Via MCP (if integrated)
# Skills can be exposed as MCP tools
```

## Subagents (子代理)

### Subagent Locations

| Location | Scope | Priority |
|----------|-------|----------|
| `.cursor/agents/` | Current project | Higher |
| `~/.cursor/agents/` | All projects | Lower |

### Subagent Format

```markdown
---
name: code-reviewer
description: Expert code reviewer. Proactively reviews code for quality and security. Use immediately after writing code.
---

You are a senior code reviewer ensuring high standards.

When invoked:
1. Run git diff to see changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code clarity and readability
- Security vulnerabilities
- Error handling
- Test coverage
```

### Creating Subagents

```bash
# Project subagent
mkdir -p .cursor/agents
cat > .cursor/agents/code-reviewer.md << EOF
---
name: code-reviewer
description: Expert code reviewer. Use proactively after code changes.
---

You are a code reviewer...
EOF

# User subagent (available across projects)
mkdir -p ~/.cursor/agents
cat > ~/.cursor/agents/debugger.md << EOF
---
name: debugger
description: Debugging specialist. Use when encountering errors or bugs.
---

You are a debugging expert...
EOF
```

### Using Subagents

- Subagents are automatically available in Cursor IDE
- Agent decides when to delegate based on description
- Use "proactively" in description to encourage automatic use
- Invoke manually with `@subagent-name` in chat

## Integration Summary

| Feature | IDE Support | CLI Support | Usage |
|---------|-------------|-------------|-------|
| Rules | ✅ Auto-loaded | ⚠️ Reference in prompts | Persistent context |
| Skills | ✅ Auto-loaded | ⚠️ Reference in prompts | Reusable knowledge |
| Subagents | ✅ Auto-available | ❌ IDE-only | Specialized assistants |
