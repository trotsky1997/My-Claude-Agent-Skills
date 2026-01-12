# MCP Integration Reference

## MCP Overview

MCP (Model Context Protocol) extends cursor-agent functionality through external servers and tools.

## Configuration

### Configuration Files

- **Global**: `~/.cursor/mcp.json`
- **Project**: `.cursor/mcp.json` (project root)

### Configuration Format

```json
{
  "mcpServers": {
    "server-name": {
      "url": "server-url",
      "headers": {
        "API_KEY": "your-api-key"
      }
    },
    "command-server": {
      "command": "python",
      "args": ["path/to/server.py"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

## Management Commands

### List Servers

```bash
# List all configured MCP servers
agent mcp list
```

### Enable/Disable Servers

```bash
# Enable server
agent mcp enable server-name

# Disable server
agent mcp disable server-name
```

### List Tools

```bash
# List available tools for a server
agent mcp list-tools server-name
```

### Login/Authentication

```bash
# Authenticate with MCP server
agent mcp login server-name
```

## Using MCP Tools

### In Interactive Mode

MCP tools are automatically available:

```bash
agent
> Use the context7 tool to query documentation
```

### In Non-Interactive Mode

```bash
# Auto-approve MCP servers
agent --print --approve-mcps "使用 MCP 工具完成任务"
```

## Common MCP Servers

### Context7

```json
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp",
      "headers": {
        "CONTEXT7_API_KEY": "your-api-key"
      }
    }
  }
}
```

**Tools**:
- `query-docs`: Query library documentation
- `resolve-library-id`: Resolve library names to IDs

### Filesystem

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/allowed/path"]
    }
  }
}
```

### GitHub

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token"
      }
    }
  }
}
```

## MCP Cache

**Location**: `~/.cursor/projects/<project-path>/mcp-cache.json`

Stores:
- Tool lists and metadata
- Tool parameters and descriptions
- Server connection info

**Benefits**:
- Faster loading
- Offline support
- Performance optimization

## Troubleshooting

### Server Not Loading

```bash
# Check server status
agent mcp list

# Re-enable server
agent mcp enable server-name

# Check configuration
cat ~/.cursor/mcp.json | python3 -m json.tool
```

### Connection Errors

1. Verify API keys and credentials
2. Check network connectivity
3. Review server logs
4. Test server independently

### Tool Not Available

```bash
# List tools to verify
agent mcp list-tools server-name

# Check cache
cat ~/.cursor/projects/.../mcp-cache.json | jq '.["server-name"]'
```
