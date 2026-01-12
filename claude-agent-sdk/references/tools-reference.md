# Tools Reference

Complete guide to using tools with Claude Agent SDK.

## Built-in Tools

### File Operations

**Read**
- Read file contents
- Usage: `allowed_tools=["Read"]`
- Claude can read files in the working directory

**Write**
- Write new file or overwrite existing file
- Usage: `allowed_tools=["Write"]`
- Requires permission (see permission modes)

**Edit**
- Edit existing file contents
- Usage: `allowed_tools=["Edit"]`
- Claude can modify specific sections of files

**Grep**
- Search for patterns in files
- Usage: `allowed_tools=["Grep"]`
- Useful for finding code patterns, functions, etc.

**List**
- List directory contents
- Usage: `allowed_tools=["List"]`
- Claude can explore directory structure

### Command Execution

**Bash**
- Execute shell commands
- Usage: `allowed_tools=["Bash"]`
- ⚠️ Use with caution - can execute arbitrary commands

**Python**
- Execute Python code
- Usage: `allowed_tools=["Python"]`
- Runs Python code in isolated environment

### Web Operations

**WebSearch**
- Search the web
- Usage: `allowed_tools=["WebSearch"]`
- Claude can search for information online

**Fetch**
- Fetch web content
- Usage: `allowed_tools=["Fetch"]`
- Claude can retrieve web pages

## Custom Tools

### Creating Custom Tools

**Step 1: Define tool function with @tool decorator**

```python
from claude_agent_sdk import tool
from typing import Any

@tool("weather", "Get weather for a location", {"location": str, "unit": str})
async def get_weather(args: dict[str, Any]) -> dict[str, Any]:
    location = args["location"]
    unit = args.get("unit", "celsius")
    
    # Your tool logic here
    temperature = fetch_weather(location, unit)
    
    return {
        "content": [{
            "type": "text",
            "text": f"Weather in {location}: {temperature}°{unit}"
        }]
    }
```

**Step 2: Create MCP server**

```python
from claude_agent_sdk import create_sdk_mcp_server

weather_server = create_sdk_mcp_server(
    name="weather",
    version="1.0.0",
    tools=[get_weather]
)
```

**Step 3: Configure options**

```python
options = ClaudeAgentOptions(
    mcp_servers={"weather": weather_server},
    allowed_tools=["mcp__weather__weather"]
)
```

### Tool Function Requirements

**Input:**
- `args: dict[str, Any]` - Dictionary of tool arguments
- Keys match the parameter schema in @tool decorator

**Output:**
- `dict[str, Any]` with `content` field
- `content` is a list of message blocks
- Each block has `type` and content-specific fields

**Example output formats:**

```python
# Text response
return {
    "content": [{"type": "text", "text": "Result text"}]
}

# Multiple text blocks
return {
    "content": [
        {"type": "text", "text": "First part"},
        {"type": "text", "text": "Second part"}
    ]
}
```

### Multiple Tools in One Server

```python
@tool("calculate", "Perform calculations", {"expression": str})
async def calculate(args):
    result = eval(args["expression"])
    return {"content": [{"type": "text", "text": f"Result: {result}"}]}

@tool("translate", "Translate text", {"text": str, "target_lang": str})
async def translate(args):
    translated = translate_text(args["text"], args["target_lang"])
    return {"content": [{"type": "text", "text": translated}]}

@tool("search_web", "Search the web", {"query": str})
async def search_web(args):
    results = web_search(args["query"])
    return {"content": [{"type": "text", "text": results}]}

# Create server with multiple tools
multi_tool_server = create_sdk_mcp_server(
    name="utilities",
    version="1.0.0",
    tools=[calculate, translate, search_web]
)

# Selectively allow tools
options = ClaudeAgentOptions(
    mcp_servers={"utilities": multi_tool_server},
    allowed_tools=[
        "mcp__utilities__calculate",
        "mcp__utilities__translate",
        # "mcp__utilities__search_web" is NOT allowed
    ]
)
```

## Tool Naming

### Built-in Tools

Use tool name directly:
- `"Read"`
- `"Write"`
- `"Bash"`

### MCP Tools

Format: `mcp__<server_name>__<tool_name>`

Example:
- Server: `"calculator"`
- Tool: `"add"`
- Full name: `"mcp__calculator__add"`

## Tool Permissions

### Basic Permission Control

**Whitelist approach:**
```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write"]  # Only these tools allowed
)
```

**Blacklist approach:**
```python
options = ClaudeAgentOptions(
    disallowed_tools=["Bash", "Delete"]  # Block these tools
)
```

**Combined:**
```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write", "Edit", "Bash"],
    disallowed_tools=["Delete"]  # Explicitly block
)
```

### Advanced Permission Handler

**Handler signature:**
```python
async def permission_handler(
    tool_name: str,
    input_data: dict,
    context: dict
) -> dict:
    # Return permission decision
    pass
```

**Return format:**
```python
# Allow
return {
    "behavior": "allow",
    "updatedInput": input_data  # Optional: modify input
}

# Deny
return {
    "behavior": "deny",
    "message": "Reason for denial",
    "interrupt": True  # Optional: interrupt agent
}
```

**Example:**
```python
async def custom_permission_handler(tool_name: str, input_data: dict, context: dict):
    # Block writes to system directories
    if tool_name == "Write":
        file_path = input_data.get("file_path", "")
        if file_path.startswith("/system/") or file_path.startswith("/etc/"):
            return {
                "behavior": "deny",
                "message": "System directory write not allowed",
                "interrupt": True
            }
    
    # Redirect config file operations to sandbox
    if tool_name in ["Write", "Edit"]:
        file_path = input_data.get("file_path", "")
        if "config" in file_path.lower():
            safe_path = f"./sandbox/{file_path}"
            return {
                "behavior": "allow",
                "updatedInput": {**input_data, "file_path": safe_path}
            }
    
    # Allow everything else
    return {
        "behavior": "allow",
        "updatedInput": input_data
    }

options = ClaudeAgentOptions(
    can_use_tool=custom_permission_handler,
    allowed_tools=["Read", "Write", "Edit"]
)
```

## Permission Modes

**"acceptEdits"**
- Automatically accept all file edits
- No user prompts
- Use for automated workflows

**"prompt"**
- Prompt user before file operations
- Interactive mode
- Use for development/testing

**"deny"**
- Deny all file operations
- Read-only mode
- Use for analysis-only agents

## Best Practices

1. **Minimize tool access**: Only allow tools that are necessary
2. **Use permission handlers**: Implement custom logic for security
3. **Validate tool inputs**: Check inputs in custom tools
4. **Handle errors gracefully**: Return error messages in tool responses
5. **Document tool behavior**: Clear descriptions in @tool decorator
6. **Test tools independently**: Verify tools work before integrating
