# Configuration Reference

Complete reference for ClaudeAgentOptions configuration.

## Tool Management

### allowed_tools

List of tools the agent can use.

```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write", "Edit", "Bash"]
)
```

**Tool name formats:**
- Built-in: `"Read"`, `"Write"`, `"Bash"`
- MCP: `"mcp__server__tool"`

### disallowed_tools

List of tools to explicitly block.

```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write", "Bash"],
    disallowed_tools=["Delete"]  # Explicitly block
)
```

### can_use_tool

Custom permission handler function.

```python
async def permission_handler(tool_name: str, input_data: dict, context: dict):
    return {"behavior": "allow", "updatedInput": input_data}

options = ClaudeAgentOptions(
    can_use_tool=permission_handler
)
```

## Conversation Control

### max_turns

Maximum number of conversation turns.

```python
options = ClaudeAgentOptions(
    max_turns=10  # Limit to 10 turns
)
```

### continue_conversation

Continue previous conversation (for query() function).

```python
options = ClaudeAgentOptions(
    continue_conversation=True
)
```

### resume

Resume a previous session by session ID.

```python
options = ClaudeAgentOptions(
    resume="session-uuid-here"
)
```

## Permissions

### permission_mode

Permission mode for file operations.

**Values:**
- `"acceptEdits"`: Automatically accept all edits
- `"prompt"`: Prompt user before operations
- `"deny"`: Deny all file operations

```python
options = ClaudeAgentOptions(
    permission_mode="acceptEdits"
)
```

### permission_prompt_tool_name

Tool name to use for permission prompts.

```python
options = ClaudeAgentOptions(
    permission_prompt_tool_name="Write"
)
```

## MCP Servers

### mcp_servers

Configure MCP servers for custom tools.

```python
from claude_agent_sdk import create_sdk_mcp_server

server = create_sdk_mcp_server(
    name="my-server",
    version="1.0.0",
    tools=[tool1, tool2]
)

options = ClaudeAgentOptions(
    mcp_servers={"my-server": server}
)
```

**Multiple servers:**

```python
options = ClaudeAgentOptions(
    mcp_servers={
        "server1": server1,
        "server2": server2
    }
)
```

## Environment

### cwd

Working directory for the agent.

```python
options = ClaudeAgentOptions(
    cwd="/path/to/project"
)
```

### env

Environment variables.

```python
options = ClaudeAgentOptions(
    env={
        "API_KEY": "secret-key",
        "DEBUG": "true"
    }
)
```

### add_dirs

Additional directories to include in context.

```python
options = ClaudeAgentOptions(
    add_dirs=["./src", "./tests", "./docs"]
)
```

## File Operations

### enable_file_checkpointing

Enable file state tracking for rewinding.

```python
options = ClaudeAgentOptions(
    enable_file_checkpointing=True,
    extra_args={"replay-user-messages": None}
)
```

### settings

Path to settings file.

```python
options = ClaudeAgentOptions(
    settings="./claude_settings.json"
)
```

## Model Configuration

### model

Claude model to use.

```python
options = ClaudeAgentOptions(
    model="claude-sonnet-4.5"
)
```

**Available models:**
- `"claude-sonnet-4.5"`: Latest Sonnet model
- `"claude-haiku-4.5"`: Fast model
- `"claude-opus-4.1"`: Advanced reasoning

### system_prompt

Custom system prompt.

```python
options = ClaudeAgentOptions(
    system_prompt="You are a helpful coding assistant."
)
```

**Or use preset:**

```python
from claude_agent_sdk import SystemPromptPreset

options = ClaudeAgentOptions(
    system_prompt=SystemPromptPreset.CODING_ASSISTANT
)
```

## Output

### output_format

Structured output format.

```python
options = ClaudeAgentOptions(
    output_format={
        "type": "json_schema",
        "schema": {
            "type": "object",
            "properties": {
                "summary": {"type": "string"},
                "code": {"type": "string"}
            }
        }
    }
)
```

### include_partial_messages

Include partial messages in stream.

```python
options = ClaudeAgentOptions(
    include_partial_messages=True
)
```

## Advanced

### hooks

Event hooks for intercepting agent behavior.

```python
from claude_agent_sdk import HookEvent

async def before_tool(tool_name: str, input_data: dict, context: dict):
    print(f"Using tool: {tool_name}")
    return input_data

options = ClaudeAgentOptions(
    hooks={
        HookEvent.BEFORE_TOOL_USE: [before_tool]
    }
)
```

### agents

Subagent definitions.

```python
options = ClaudeAgentOptions(
    agents={
        "code-reviewer": {
            "system_prompt": "You are a code reviewer.",
            "allowed_tools": ["Read", "Grep"]
        }
    }
)
```

### fork_session

Fork session for parallel execution.

```python
options = ClaudeAgentOptions(
    fork_session=True
)
```

### max_buffer_size

Maximum context buffer size.

```python
options = ClaudeAgentOptions(
    max_buffer_size=100000  # Characters
)
```

### stderr

Custom error output handler.

```python
def error_handler(msg: str):
    logging.error(f"Agent error: {msg}")

options = ClaudeAgentOptions(
    stderr=error_handler
)
```

### user

User identifier.

```python
options = ClaudeAgentOptions(
    user="user-123"
)
```

### extra_args

Additional arguments.

```python
options = ClaudeAgentOptions(
    extra_args={
        "replay-user-messages": None,
        "custom-arg": "value"
    }
)
```

### setting_sources

Setting sources for configuration.

```python
options = ClaudeAgentOptions(
    setting_sources=[
        {"type": "file", "path": "./settings.json"},
        {"type": "env", "prefix": "CLAUDE_"}
    ]
)
```

### plugins

SDK plugins.

```python
options = ClaudeAgentOptions(
    plugins=[
        {"name": "monitoring", "config": {...}}
    ]
)
```

### sandbox

Sandbox settings for code execution.

```python
options = ClaudeAgentOptions(
    sandbox={
        "enabled": True,
        "timeout": 30,
        "memory_limit": "512MB"
    }
)
```

## Configuration Best Practices

1. **Start minimal**: Begin with minimal allowed_tools, add as needed
2. **Use permission handlers**: Implement custom logic for security
3. **Set appropriate limits**: Use max_turns to prevent infinite loops
4. **Configure environment**: Set cwd and env for proper context
5. **Enable checkpointing**: Use file checkpointing for production
6. **Monitor with hooks**: Use hooks for logging and monitoring
7. **Test configurations**: Verify configurations in development first
