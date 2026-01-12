---
name: claude-agent-sdk
description: Comprehensive guide for using Claude Agent SDK to build AI agents that can read files, execute commands, edit code, and perform complex workflows. Use when (1) Building autonomous AI agents with Claude, (2) Creating agents that interact with codebases and file systems, (3) Integrating custom tools and MCP servers with Claude, (4) Managing conversation sessions and context with Claude, (5) Implementing file operations, command execution, and code editing in agents, (6) Setting up permission controls and security for agent tools, (7) Using file checkpointing and session management features, (8) Building production-ready agents with error handling and monitoring
metadata:
  short-description: Build AI agents with Claude Agent SDK
---

# Claude Agent SDK

Comprehensive toolkit for building autonomous AI agents with Claude that can understand codebases, edit files, run commands, and execute complex workflows.

## Quick Start

**Installation:**

```bash
# Python
pip install claude-agent-sdk

# TypeScript
npm install @anthropic-ai/claude-agent-sdk
```

**Simple query example:**

```python
from claude_agent_sdk import query, ClaudeAgentOptions
import asyncio

async def main():
    async for message in query(
        prompt="Explain the authentication flow",
        options=ClaudeAgentOptions(
            max_turns=1,
            allowed_tools=["Read", "Grep"]
        )
    ):
        if hasattr(message, 'result'):
            print(message.result)

asyncio.run(main())
```

**Session-based conversation:**

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
import asyncio

async def main():
    async with ClaudeSDKClient() as client:
        # First query
        await client.query("What's the capital of France?")
        async for message in client.receive_response():
            print(message)
        
        # Follow-up - Claude remembers context
        await client.query("What's the population of that city?")
        async for message in client.receive_response():
            print(message)

asyncio.run(main())
```

## Core Workflows

### 1. Basic Agent Setup

**Using query() for one-shot requests:**

```python
from claude_agent_sdk import query, ClaudeAgentOptions

async for message in query(
    prompt="Analyze this codebase",
    options=ClaudeAgentOptions(
        allowed_tools=["Read", "Grep", "Bash"],
        max_turns=5
    )
):
    if hasattr(message, 'result'):
        print(message.result)
```

**Using ClaudeSDKClient for conversations:**

```python
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write", "Edit", "Bash"],
    permission_mode="acceptEdits"
)

async with ClaudeSDKClient(options=options) as client:
    await client.query("Create a hello.py file")
    async for message in client.receive_response():
        print(message)
```

### 2. Custom Tools

**Define tools with @tool decorator:**

```python
from claude_agent_sdk import tool, create_sdk_mcp_server, ClaudeAgentOptions

@tool("add", "Add two numbers", {"a": float, "b": float})
async def add(args):
    return {
        "content": [{"type": "text", "text": f"Sum: {args['a'] + args['b']}"}]
    }

@tool("multiply", "Multiply two numbers", {"a": float, "b": float})
async def multiply(args):
    return {
        "content": [{"type": "text", "text": f"Product: {args['a'] * args['b']}"}]
    }

# Create MCP server
calculator = create_sdk_mcp_server(
    name="calculator",
    version="2.0.0",
    tools=[add, multiply]
)

# Use with Claude
options = ClaudeAgentOptions(
    mcp_servers={"calc": calculator},
    allowed_tools=["mcp__calc__add", "mcp__calc__multiply"]
)
```

### 3. Tool Permissions

**Basic permission control:**

```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write"],  # Whitelist
    disallowed_tools=["Bash"],        # Blacklist
    permission_mode="acceptEdits"     # Auto-accept edits
)
```

**Advanced permission handler:**

```python
async def custom_permission_handler(tool_name: str, input_data: dict, context: dict):
    # Block writes to system directories
    if tool_name == "Write" and input_data.get("file_path", "").startswith("/system/"):
        return {
            "behavior": "deny",
            "message": "System directory write not allowed",
            "interrupt": True
        }
    
    # Redirect sensitive operations
    if tool_name in ["Write", "Edit"] and "config" in input_data.get("file_path", ""):
        safe_path = f"./sandbox/{input_data['file_path']}"
        return {
            "behavior": "allow",
            "updatedInput": {**input_data, "file_path": safe_path}
        }
    
    return {"behavior": "allow", "updatedInput": input_data}

options = ClaudeAgentOptions(
    can_use_tool=custom_permission_handler,
    allowed_tools=["Read", "Write", "Edit"]
)
```

### 4. Session Management

**Continuous conversation:**

```python
class ConversationSession:
    def __init__(self, options: ClaudeAgentOptions = None):
        self.client = ClaudeSDKClient(options)
        self.turn_count = 0

    async def start(self):
        await self.client.connect()
        
        while True:
            user_input = input(f"\n[Turn {self.turn_count + 1}] You: ")
            
            if user_input.lower() == 'exit':
                break
            elif user_input.lower() == 'interrupt':
                await self.client.interrupt()
                continue
            
            await self.client.query(user_input)
            self.turn_count += 1
            
            async for message in self.client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(block.text, end="")
            print()
        
        await self.client.disconnect()
```

### 5. File Checkpointing

**Enable checkpointing:**

```python
options = ClaudeAgentOptions(
    enable_file_checkpointing=True,
    permission_mode="acceptEdits",
    extra_args={"replay-user-messages": None}
)

checkpoint_id = None
session_id = None

async with ClaudeSDKClient(options) as client:
    await client.query("Refactor the authentication module")
    
    async for message in client.receive_response():
        if isinstance(message, UserMessage) and message.uuid:
            checkpoint_id = message.uuid
        if isinstance(message, ResultMessage):
            session_id = message.session_id

# Later: rewind to checkpoint
if checkpoint_id and session_id:
    async with ClaudeSDKClient(ClaudeAgentOptions(
        enable_file_checkpointing=True,
        resume=session_id
    )) as client:
        await client.query("")
        async for message in client.receive_response():
            await client.rewind_files(checkpoint_id)
            break
```

## Configuration

### ClaudeAgentOptions

**Essential options:**

```python
options = ClaudeAgentOptions(
    # Tool management
    allowed_tools=["Read", "Write", "Edit", "Bash"],
    disallowed_tools=["Delete"],
    
    # Conversation control
    max_turns=10,
    continue_conversation=True,
    
    # Permissions
    permission_mode="acceptEdits",  # or "prompt" or "deny"
    can_use_tool=custom_handler,
    
    # MCP servers
    mcp_servers={"my-server": custom_mcp_server},
    
    # Environment
    cwd="/path/to/working/directory",
    env={"API_KEY": "value"},
    
    # File checkpointing
    enable_file_checkpointing=True,
    
    # Model selection
    model="claude-sonnet-4.5",
    
    # System prompt
    system_prompt="You are a helpful coding assistant."
)
```

## Common Patterns

### Pattern 1: Code Analysis Agent

```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Grep", "Bash"],
    cwd="./project",
    max_turns=5
)

async with ClaudeSDKClient(options) as client:
    await client.query("Analyze the codebase structure and identify main components")
    async for message in client.receive_response():
        print(message)
```

### Pattern 2: Code Editing Agent

```python
options = ClaudeAgentOptions(
    allowed_tools=["Read", "Write", "Edit"],
    permission_mode="acceptEdits",
    cwd="./project"
)

async with ClaudeSDKClient(options) as client:
    await client.query("Add error handling to all API endpoints")
    async for message in client.receive_response():
        print(message)
```

### Pattern 3: Multi-Tool Agent

```python
# Define multiple tools
@tool("calculate", "Perform calculations", {"expression": str})
async def calculate(args):
    result = eval(args["expression"])
    return {"content": [{"type": "text", "text": f"Result: {result}"}]}

@tool("translate", "Translate text", {"text": str, "target_lang": str})
async def translate(args):
    # Translation logic
    return {"content": [{"type": "text", "text": f"Translated: {args['text']}"}]}

server = create_sdk_mcp_server(
    name="utilities",
    version="1.0.0",
    tools=[calculate, translate]
)

options = ClaudeAgentOptions(
    mcp_servers={"utilities": server},
    allowed_tools=["mcp__utilities__calculate", "mcp__utilities__translate"]
)
```

## Troubleshooting

**Common issues:**

1. **Connection errors**: Ensure API key is set in environment or options
2. **Tool not found**: Check tool name format (`mcp__server__tool` for MCP tools)
3. **Permission denied**: Verify `allowed_tools` includes the tool
4. **Session not continuing**: Use `continue_conversation=True` or `ClaudeSDKClient`
5. **File checkpointing not working**: Set `enable_file_checkpointing=True` and `extra_args={"replay-user-messages": None}`

## References

For detailed information, see:

- [api-reference.md](references/api-reference.md) - Complete API reference
- [tools-reference.md](references/tools-reference.md) - Built-in tools and custom tool creation
- [advanced-features.md](references/advanced-features.md) - Hooks, file checkpointing, and production patterns
- [configuration.md](references/configuration.md) - Complete configuration options
