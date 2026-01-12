# Configuration Reference

## API Key Configuration

### Method 1: Environment Variable

```bash
# Set API key as environment variable
export CURSOR_API_KEY="your-api-key"

# Use in commands
agent "your prompt"
```

### Method 2: Command Line Parameter

```bash
# Pass API key directly
agent --api-key "your-api-key" "your prompt"
```

### Method 3: Shell Configuration

Add to your shell profile (`~/.zshrc`, `~/.bashrc`, etc.):

```bash
# ~/.zshrc or ~/.bashrc
export CURSOR_API_KEY="your-api-key"
```

Then reload:
```bash
source ~/.zshrc  # or source ~/.bashrc
```

### Method 4: Per-Session Configuration

```bash
# In a script or single session
CURSOR_API_KEY="your-api-key" agent "your prompt"
```

## Custom Base URL Configuration

### Using Environment Variables

For custom OpenAI-compatible API endpoints:

```bash
# Set custom base URL
export OPENAI_BASE_URL="https://api.your-endpoint.com/v1"

# Set API key
export OPENAI_API_KEY="your-api-key"

# Use with cursor-agent
agent "your prompt"
```

### Using Custom Headers

You can also use `--header` to add custom headers:

```bash
# Add custom base URL via header (if supported by your endpoint)
agent --header "X-API-Base-URL: https://api.your-endpoint.com/v1" \
      --api-key "your-api-key" \
      "your prompt"
```

### Configuration File Approach

Create a configuration script:

```bash
#!/bin/bash
# config-agent.sh

export OPENAI_BASE_URL="https://api.your-endpoint.com/v1"
export OPENAI_API_KEY="your-api-key"
export CURSOR_API_KEY="your-api-key"

# Run agent with configuration
agent "$@"
```

Make it executable and use:
```bash
chmod +x config-agent.sh
./config-agent.sh "your prompt"
```

## CLI Configuration File

### Location

`~/.cursor/cli-config.json`

### Current Structure

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

**Note**: The CLI config file doesn't directly support API key or base URL configuration. Use environment variables instead.

## Environment Variables Summary

| Variable | Purpose | Example |
|----------|---------|---------|
| `CURSOR_API_KEY` | Cursor API authentication | `export CURSOR_API_KEY="sk-..."` |
| `OPENAI_API_KEY` | OpenAI-compatible API key | `export OPENAI_API_KEY="sk-..."` |
| `OPENAI_BASE_URL` | Custom API endpoint | `export OPENAI_BASE_URL="https://api.example.com/v1"` |
| `NO_OPEN_BROWSER` | Disable browser auto-open | `export NO_OPEN_BROWSER=1` |

## Complete Configuration Example

### For Custom OpenAI-Compatible Endpoint

```bash
#!/bin/bash
# setup-custom-api.sh

# Configure custom endpoint
export OPENAI_BASE_URL="https://api.openrouter.ai/v1"
export OPENAI_API_KEY="sk-or-v1-..."
export CURSOR_API_KEY="sk-or-v1-..."

# Verify configuration
echo "Base URL: $OPENAI_BASE_URL"
echo "API Key: ${OPENAI_API_KEY:0:10}..."

# Test connection
agent --print "Hello, test connection"
```

### For Local LLM Server

```bash
#!/bin/bash
# setup-local-llm.sh

# Configure local endpoint
export OPENAI_BASE_URL="http://localhost:1234/v1"
export OPENAI_API_KEY="not-needed"  # Some local servers don't require key

# Use with agent
agent --print "Test local LLM"
```

**Note**: Cursor Agent CLI requires OpenAI-compatible API format. Local LLMs must support OpenAI API format to work.

## Verification

### Check Configuration

```bash
# Check environment variables
echo "CURSOR_API_KEY: ${CURSOR_API_KEY:0:10}..."
echo "OPENAI_BASE_URL: $OPENAI_BASE_URL"
echo "OPENAI_API_KEY: ${OPENAI_API_KEY:0:10}..."

# Test authentication
agent status
```

### Test Connection

```bash
# Simple test
agent --print "Test connection" --output-format json
```

## Best Practices

1. **Use environment variables** for API keys (never hardcode)
2. **Use shell profiles** for persistent configuration
3. **Use scripts** for project-specific configurations
4. **Verify configuration** before use
5. **Keep API keys secure** (use `.env` files with `.gitignore`)

## Security Considerations

### .env File Approach

Create `.env` file (add to `.gitignore`):

```bash
# .env
CURSOR_API_KEY=your-api-key
OPENAI_BASE_URL=https://api.example.com/v1
OPENAI_API_KEY=your-api-key
OPENAI_MODEL=gpt-3.5-turbo  # Optional: specify model
```

Load in script:

```bash
#!/bin/bash
# Load .env file
set -a
source .env
set +a

# Export for agent (cursor-agent uses OPENAI_API_KEY and OPENAI_BASE_URL)
export OPENAI_API_KEY
export OPENAI_BASE_URL

# Optionally set CURSOR_API_KEY from OPENAI_API_KEY
if [ -z "$CURSOR_API_KEY" ] && [ -n "$OPENAI_API_KEY" ]; then
    export CURSOR_API_KEY="$OPENAI_API_KEY"
fi

# Use agent
agent "your prompt"
```

**Complete example script**:

```bash
#!/bin/bash
# test-custom-api.sh

# Load .env
set -a
source .env
set +a

# Export variables
export OPENAI_API_KEY
export OPENAI_BASE_URL

# Optionally set CURSOR_API_KEY from OPENAI_API_KEY
if [ -z "$CURSOR_API_KEY" ] && [ -n "$OPENAI_API_KEY" ]; then
    export CURSOR_API_KEY="$OPENAI_API_KEY"
fi

# Test connection
agent --print "Test connection" --output-format json
```

### Testing .env Configuration

**Test script for .env loading**:

```bash
#!/bin/bash
# test-env-config.sh

# Load .env
set -a
source .env
set +a

# Check variables
echo "OPENAI_BASE_URL: ${OPENAI_BASE_URL:-未设置}"
echo "OPENAI_API_KEY: ${OPENAI_API_KEY:+已设置}"
echo "OPENAI_MODEL: ${OPENAI_MODEL:-未设置}"

# Test agent status
agent status
```

**Important Notes**:

1. **cursor-agent uses CURSOR_API_KEY**: The CLI primarily uses `CURSOR_API_KEY` for authentication, not `OPENAI_API_KEY` directly
2. **Custom base URL**: Setting `OPENAI_BASE_URL` may require additional configuration depending on the endpoint
3. **API compatibility**: Custom endpoints must be OpenAI API-compatible
4. **Environment precedence**: Environment variables override config file settings

### Real-World Example

Based on actual testing with custom endpoint:

```bash
# .env file
OPENAI_API_KEY=sk-...
OPENAI_BASE_URL=http://14.103.60.158:3001/v1
OPENAI_MODEL=nex-agi/deepseek-v3.1-nex-1

# Load and use
set -a
source .env
set +a

# Set CURSOR_API_KEY if needed
export CURSOR_API_KEY="$OPENAI_API_KEY"

# Use agent
agent --print "test"
```

**Test Results**:
- ✅ `.env` file loads successfully
- ✅ Environment variables are set correctly
- ⚠️ May require `CURSOR_API_KEY` to be set explicitly
- ⚠️ Custom base URL may need endpoint-specific configuration

### Gitignore

```bash
# .gitignore
.env
*.key
*_api_key.txt
```

## Troubleshooting

### API Key Not Working

```bash
# Check if key is set
echo $CURSOR_API_KEY

# Try explicit parameter
agent --api-key "your-key" "test"

# Check authentication status
agent status
```

### Base URL Not Working

```bash
# Verify environment variable
echo $OPENAI_BASE_URL

# Test endpoint directly
curl -X POST "$OPENAI_BASE_URL/chat/completions" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-3.5-turbo","messages":[{"role":"user","content":"test"}]}'
```

### Configuration Not Persisting

```bash
# Check shell profile
cat ~/.zshrc | grep CURSOR_API_KEY

# Reload shell profile
source ~/.zshrc

# Or add to profile
echo 'export CURSOR_API_KEY="your-key"' >> ~/.zshrc
```

## Integration with Other Tools

### Using with Docker

```dockerfile
# Dockerfile
FROM node:18

ENV CURSOR_API_KEY=""
ENV OPENAI_BASE_URL=""
ENV OPENAI_API_KEY=""

# Your application
```

### Using with CI/CD

```yaml
# .github/workflows/ci.yml
env:
  CURSOR_API_KEY: ${{ secrets.CURSOR_API_KEY }}
  OPENAI_BASE_URL: ${{ secrets.OPENAI_BASE_URL }}
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

steps:
  - name: Run agent
    run: agent --print "test"
```
