# Basic Commands Reference

## Interactive Mode

```bash
# Start interactive mode
agent

# With initial prompt
agent "帮我写一个 Python 函数来计算斐波那契数列"

# Specify workspace
agent --workspace /path/to/project "分析这个项目"
```

## Non-Interactive Mode

```bash
# Simple text output
agent --print "生成一个排序函数"

# JSON output (for scripts)
agent --print --output-format json "分析代码复杂度" > result.json

# Streaming output (real-time)
agent --print --output-format stream-json --stream-partial-output "重构代码"
```

## Session Management

```bash
# Create session
CHAT_ID=$(agent create-chat)
echo $CHAT_ID > .chat_id

# Resume latest session
agent resume

# Resume specific session
agent --resume <chatId>

# List all sessions
agent ls
```

## Model Selection

```bash
# List available models
agent models

# Use specific model
agent --model gpt-5.2 "生成代码"
agent --model opus-4.5-thinking "复杂推理任务"

# Switch in interactive mode
agent
> /model sonnet-4.5-thinking
```

## Output Formats

| Format | Use Case | Example |
|--------|----------|---------|
| `text` | Human reading | `agent --print "生成代码"` |
| `json` | Script processing | `agent --print --output-format json "..."` |
| `stream-json` | Real-time streaming | `agent --print --output-format stream-json --stream-partial-output "..."` |

## Sandbox and Security

```bash
# Enable sandbox (safer)
agent --sandbox enabled "执行任务"

# Disable sandbox (more permissions)
agent --sandbox disabled "执行任务"

# Force allow (careful)
agent --force "执行需要权限的操作"
```

## Browser Automation

```bash
# Enable browser support
agent --browser "测试网页功能"
```

## MCP Management

```bash
# List MCP servers
agent mcp list

# Enable server
agent mcp enable server-name

# Disable server
agent mcp disable server-name

# List tools
agent mcp list-tools server-name
```
