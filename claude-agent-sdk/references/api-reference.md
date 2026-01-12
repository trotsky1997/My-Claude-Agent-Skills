# Claude Agent SDK API Reference

Complete API reference for Claude Agent SDK (Python).

## Core Classes

### ClaudeSDKClient

Main client class for managing conversation sessions with Claude.

#### Methods

**`__init__(self, options: ClaudeAgentOptions | None = None)`**
- Initialize the client with optional configuration
- Parameters:
  - `options` (ClaudeAgentOptions | None): Optional configuration object

**`async connect(self, prompt: str | AsyncIterable[dict] | None = None)`**
- Connect to Claude and optionally send an initial prompt
- Parameters:
  - `prompt` (str | AsyncIterable[dict] | None): Optional initial prompt or message stream

**`async query(self, prompt: str | AsyncIterable[dict], session_id: str = "default")`**
- Send a new request to Claude in streaming mode
- Parameters:
  - `prompt` (str | AsyncIterable[dict]): User's prompt or message stream
  - `session_id` (str): Conversation session identifier (default: "default")

**`async receive_messages(self) -> AsyncIterator[Message]`**
- Receive all messages from Claude as an async iterator
- Returns: AsyncIterator[Message]

**`async receive_response(self) -> AsyncIterator[Message]`**
- Receive messages until and including a ResultMessage
- Returns: AsyncIterator[Message]

**`async interrupt(self)`**
- Send interrupt signal to Claude (only works in streaming mode)

**`async rewind_files(self, user_message_uuid: str)`**
- Restore files to their state at a specific user message
- Requires `enable_file_checkpointing=True`
- Parameters:
  - `user_message_uuid` (str): UUID of the user message

**`async disconnect(self)`**
- Disconnect from Claude session

#### Context Manager Usage

```python
async with ClaudeSDKClient(options) as client:
    await client.query("Hello")
    async for message in client.receive_response():
        print(message)
```

### query() Function

Simple function for one-shot queries.

**`query(prompt: str | AsyncIterable[dict], options: ClaudeAgentOptions) -> AsyncIterator[Message]`**
- Execute a single query with Claude
- Parameters:
  - `prompt` (str | AsyncIterable[dict]): User prompt or message stream
  - `options` (ClaudeAgentOptions): Configuration options
- Returns: AsyncIterator[Message]

**Example:**

```python
async for message in query(
    prompt="Explain authentication",
    options=ClaudeAgentOptions(max_turns=1)
):
    if hasattr(message, 'result'):
        print(message.result)
```

## Message Types

### UserMessage

Represents a user message in the conversation.

- `uuid` (str | None): Message UUID (for checkpointing)
- `content` (str): Message content

### AssistantMessage

Represents Claude's response.

- `content` (list[Block]): Message content blocks
- Common block types:
  - `TextBlock`: Text content
  - `ToolUseBlock`: Tool usage
  - `ToolResultBlock`: Tool results

### ResultMessage

Final result message from Claude.

- `result` (str): Final result text
- `session_id` (str): Session identifier
- `subtype` (str): "success" or "error"

## Tool Decorators

### @tool

Decorator for defining custom tools.

**`@tool(name: str, description: str, parameters: dict[str, type])`**

**Example:**

```python
@tool("add", "Add two numbers", {"a": float, "b": float})
async def add(args: dict[str, Any]) -> dict[str, Any]:
    return {
        "content": [{"type": "text", "text": f"Sum: {args['a'] + args['b']}"}]
    }
```

**Tool function signature:**
- Input: `args: dict[str, Any]` - Tool arguments
- Output: `dict[str, Any]` with `content` field containing message blocks

### create_sdk_mcp_server

Create an MCP server from tool functions.

**`create_sdk_mcp_server(name: str, version: str, tools: list[Callable]) -> McpServerConfig`**

**Example:**

```python
server = create_sdk_mcp_server(
    name="calculator",
    version="2.0.0",
    tools=[add, multiply]
)
```

## ClaudeAgentOptions

Complete configuration options for Claude agents.

### Tool Management

- `allowed_tools` (list[str]): Whitelist of allowed tools
- `disallowed_tools` (list[str]): Blacklist of disallowed tools
- `can_use_tool` (Callable | None): Custom permission handler

### Conversation Control

- `max_turns` (int | None): Maximum conversation turns
- `continue_conversation` (bool): Continue previous conversation
- `resume` (str | None): Session ID to resume

### Permissions

- `permission_mode` (str | None): "acceptEdits", "prompt", or "deny"
- `permission_prompt_tool_name` (str | None): Tool name for permission prompts

### MCP Servers

- `mcp_servers` (dict[str, McpServerConfig] | str | Path): MCP server configurations

### Environment

- `cwd` (str | Path | None): Working directory
- `env` (dict[str, str]): Environment variables
- `add_dirs` (list[str | Path]): Additional directories to include

### File Operations

- `enable_file_checkpointing` (bool): Enable file state tracking
- `settings` (str | None): Settings file path

### Model Configuration

- `model` (str | None): Model name (e.g., "claude-sonnet-4.5")
- `system_prompt` (str | SystemPromptPreset | None): System prompt

### Output

- `output_format` (OutputFormat | None): Structured output format
- `include_partial_messages` (bool): Include partial messages in stream

### Advanced

- `hooks` (dict[HookEvent, list[HookMatcher]] | None): Event hooks
- `agents` (dict[str, AgentDefinition] | None): Subagent definitions
- `fork_session` (bool): Fork session for parallel execution
- `max_buffer_size` (int | None): Maximum buffer size
- `stderr` (Callable[[str], None] | None): Error output handler
- `user` (str | None): User identifier
- `extra_args` (dict[str, str | None]): Additional arguments
- `setting_sources` (list[SettingSource] | None): Setting sources
- `plugins` (list[SdkPluginConfig]): SDK plugins
- `sandbox` (SandboxSettings | None): Sandbox configuration

## Built-in Tools

### File Operations

- `Read`: Read file contents
- `Write`: Write file contents
- `Edit`: Edit file contents
- `Grep`: Search files for patterns
- `List`: List directory contents

### Command Execution

- `Bash`: Execute shell commands
- `Python`: Execute Python code

### Web Operations

- `WebSearch`: Search the web
- `Fetch`: Fetch web content

Tool names follow format: `mcp__server__tool` for MCP tools, or direct name for built-in tools.
