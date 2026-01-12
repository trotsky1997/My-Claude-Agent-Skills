# Advanced Features Reference

## Model Selection

### Available Models

- `auto` - Auto selection (recommended)
- `composer-1` - Composer 1
- `gpt-5.1-codex-max` - GPT-5.1 Codex Max
- `gpt-5.1-codex-max-high` - GPT-5.1 Codex Max High
- `gpt-5.2` - GPT-5.2
- `gpt-5.2-high` - GPT-5.2 High
- `opus-4.5-thinking` - Claude 4.5 Opus (Thinking) (default)
- `opus-4.5` - Claude 4.5 Opus
- `sonnet-4.5` - Claude 4.5 Sonnet
- `sonnet-4.5-thinking` - Claude 4.5 Sonnet (Thinking)
- `gemini-3-pro` - Gemini 3 Pro
- `gemini-3-flash` - Gemini 3 Flash
- `grok` - Grok

### Model Selection Strategy

**Quick Tasks**: `gemini-3-flash` or `sonnet-4.5`
```bash
agent --model gemini-3-flash "快速生成简单代码"
```

**Complex Reasoning**: `thinking` models
```bash
agent --model opus-4.5-thinking "分析复杂的架构问题"
```

**Code Generation**: `gpt-5.2` or `gpt-5.1-codex-max`
```bash
agent --model gpt-5.2 "生成完整的 REST API"
```

**Auto Selection**: `auto` (recommended)
```bash
agent --model auto "让系统自动选择最佳模型"
```

## Output Formats

### Text Output (Default)

```bash
agent --print "生成代码"
```

### JSON Output

```bash
# Structured output for scripts
agent --print --output-format json "分析项目结构" > analysis.json

# Process with jq
agent --print --output-format json "分析代码" | jq '.response'
```

### Streaming JSON Output

```bash
# Real-time streaming
agent --print --output-format stream-json --stream-partial-output "生成长文档"
```

## Sandbox Mode

### Enable Sandbox

```bash
agent --sandbox enabled "执行任务"
```

**Sandbox Features**:
- Limits file system access
- Controls network access (`networkAccess: "allowlist"`)
- Restricts command execution

### Disable Sandbox

```bash
agent --sandbox disabled "执行任务"
```

## Browser Automation

### Enable Browser Support

```bash
agent --browser "测试网页功能"
```

### Use Cases

- Frontend development and testing
- Web automation workflows
- Page analysis and extraction
- E2E testing

## Cloud Mode

```bash
# Start cloud mode (opens Composer picker)
agent --cloud
```

**Features**:
- Integration with Cursor IDE
- Uses cloud Composer
- Syncs to Cursor account

## Custom Headers

```bash
# Add custom HTTP headers
agent --header "X-Custom-Header: value" "你的提示"

# Multiple headers
agent --header "Header1: value1" --header "Header2: value2" "提示"
```

## Workspace Specification

```bash
# Specify workspace directory
agent --workspace /path/to/project "分析这个项目"
```

## Configuration Files

### CLI Configuration

**Location**: `~/.cursor/cli-config.json`

```json
{
  "permissions": {
    "allow": ["Shell(ls)"],
    "deny": []
  },
  "model": {
    "modelId": "default",
    "displayModelId": "auto"
  },
  "privacyCache": {
    "ghostMode": false,
    "privacyMode": 3
  },
  "approvalMode": "allowlist",
  "sandbox": {
    "mode": "disabled",
    "networkAccess": "allowlist"
  }
}
```

### Privacy Modes

```json
{
  "privacyCache": {
    "ghostMode": false,      // Ghost mode
    "privacyMode": 3         // Privacy level (0-3)
  }
}
```

**Privacy Levels**:
- `0`: Lowest privacy
- `3`: Highest privacy (default)

## Performance Optimization

### Model Selection

- Quick tasks: Use `gemini-3-flash` or `sonnet-4.5`
- Complex tasks: Use `opus-4.5-thinking` or `gpt-5.2`
- Code generation: Use `gpt-5.2` or `gpt-5.1-codex-max`

### Output Format

- Script processing: Use `json` format
- Real-time feedback: Use `stream-json`
- Human reading: Use default `text` format

### Session Management

- Create dedicated sessions for long-term projects
- Clean up old sessions regularly
- Use session ID files for management
