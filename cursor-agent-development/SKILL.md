---
name: cursor-agent-development
description: Guides developers through using cursor-agent CLI for interactive development, session management, and implementing development-verification loops. Use when working with cursor-agent, creating projects with agent supervision, managing chat sessions, or implementing agent-based development workflows.
---

# Cursor Agent Development Workflow

This skill guides developers through effective use of `cursor-agent` (or `agent` command) for interactive development, project management, and implementing supervised development-verification loops.

## Quick Start

```bash
# Interactive mode
agent

# Non-interactive mode
agent --print "your prompt"

# Create and resume session
CHAT_ID=$(agent create-chat)
echo $CHAT_ID > .chat_id
agent --resume $(cat .chat_id)
```

For detailed command reference, see [reference/basic-commands.md](reference/basic-commands.md).

## Development-Verification Loop Pattern

Supervised development with quality gates:

### Setup

1. Create two sessions (dev + QA)
2. Define requirements and acceptance criteria

### Loop

1. **Development**: `agent --resume $DEV_CHAT --print "开发任务" > output.py`
2. **Verification**: `agent --resume $QA_CHAT --print "验收检查" > 验收报告.md`
3. **Decision**: Pass → End | Issues → Continue loop

For complete workflow details, see [reference/development-verification-loop.md](reference/development-verification-loop.md).

## Session Management

- **Create**: `CHAT_ID=$(agent create-chat)`
- **Resume**: `agent --resume <chatId>` or `agent resume`
- **List**: `agent ls`

Sessions persist across terminals and days. For detailed session management, see [reference/session-management.md](reference/session-management.md).

## Advanced Features

- **Model selection**: `agent --model <model> "prompt"`
- **Output formats**: `--output-format json|stream-json`
- **Sandbox mode**: `--sandbox enabled|disabled`
- **Browser automation**: `--browser`

For complete feature reference, see [reference/advanced-features.md](reference/advanced-features.md).

## MCP Integration

Configure MCP servers in `~/.cursor/mcp.json` or `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "server-name": {
      "url": "server-url",
      "headers": {"API_KEY": "your-key"}
    }
  }
}
```

Manage with: `agent mcp list|enable|disable|list-tools`

For detailed MCP guide, see [reference/mcp-integration.md](reference/mcp-integration.md).

## Rules, Skills, and Subagents

### Rules
Persistent context for coding standards. Location: `.cursor/rules/` or `~/.cursor/rules/`

Create with: `agent rule` or manually in `.cursor/rules/<name>/RULE.md`

### Skills
Reusable knowledge modules. Location: `.cursor/skills/` or `~/.cursor/skills/`

Create in `.cursor/skills/<name>/SKILL.md` with YAML frontmatter.

### Subagents
Specialized AI assistants. Location: `.cursor/agents/` or `~/.cursor/agents/`

Create as `.md` files with YAML frontmatter and system prompt.

### AGENTS.md
Simple project instructions. Location: `AGENTS.md` (project root or subdirectories)

Plain Markdown, no YAML required. Auto-loaded by Cursor IDE.

### Hooks
Intercept and modify agent behavior. Location: `.cursor/hooks/` or `~/.cursor/hooks/`

Hook types: `beforeFileEdit`, `afterFileEdit`, `beforeShellCommand`, `afterShellCommand`, `stop`

For detailed guides, see [reference/rules-skills-subagents.md](reference/rules-skills-subagents.md) and [reference/agents-md-hooks.md](reference/agents-md-hooks.md).

## Best Practices

1. **Clear prompts**: Be specific with requirements
2. **Iterative development**: Break tasks into steps
3. **Session persistence**: Save IDs, resume across sessions
4. **Separation**: Use different sessions for dev and verification

For workflow patterns and examples, see [reference/workflows-patterns.md](reference/workflows-patterns.md).

## Troubleshooting

- **Session not found**: Check `~/.cursor/chats/*/<chatId>/` or recreate
- **Permission issues**: Use `--sandbox enabled` or `--force` (careful)
- **MCP issues**: Check with `agent mcp list` and re-enable servers

## Configuration

### API Key

```bash
# Environment variable
export CURSOR_API_KEY="your-api-key"

# Command line
agent --api-key "your-api-key" "prompt"

# From .env file
set -a && source .env && set +a
export CURSOR_API_KEY="$OPENAI_API_KEY"  # If using OPENAI_API_KEY
```

### Custom Base URL

```bash
# For OpenAI-compatible endpoints
export OPENAI_BASE_URL="https://api.your-endpoint.com/v1"
export OPENAI_API_KEY="your-api-key"

# Load from .env
set -a && source .env && set +a
export OPENAI_BASE_URL
export OPENAI_API_KEY
```

**Note**: `cursor-agent` primarily uses `CURSOR_API_KEY`. For custom endpoints, you may need to set both `CURSOR_API_KEY` and `OPENAI_API_KEY`.

For complete configuration guide with .env examples, see [reference/configuration.md](reference/configuration.md).

## Reference Documentation

All detailed documentation is in the `reference/` directory:

- [basic-commands.md](reference/basic-commands.md) - Command reference
- [configuration.md](reference/configuration.md) - API key and base URL configuration
- [development-verification-loop.md](reference/development-verification-loop.md) - Dev-QA loop pattern
- [session-management.md](reference/session-management.md) - Session operations
- [advanced-features.md](reference/advanced-features.md) - Model selection, output formats, etc.
- [mcp-integration.md](reference/mcp-integration.md) - MCP server configuration
- [rules-skills-subagents.md](reference/rules-skills-subagents.md) - Rules, Skills, Subagents
- [agents-md-hooks.md](reference/agents-md-hooks.md) - AGENTS.md and Hooks
- [workflows-patterns.md](reference/workflows-patterns.md) - Common patterns and workflows

## Key Takeaways

1. **Sessions enable context continuity** - Use for long-term projects
2. **Development-Verification loops** - Separate concerns for quality
3. **Clear prompts** - Specific requirements yield better results
4. **Iterative approach** - Build incrementally, verify continuously
5. **Progressive disclosure** - Core info in SKILL.md, details in reference/
