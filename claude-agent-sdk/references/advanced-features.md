# Advanced Features

Advanced features and patterns for Claude Agent SDK.

## File Checkpointing

File checkpointing allows you to restore files to their state at any point in a conversation.

### Setup

**Enable checkpointing:**

```python
options = ClaudeAgentOptions(
    enable_file_checkpointing=True,
    permission_mode="acceptEdits",
    extra_args={"replay-user-messages": None}
)
```

**Capture checkpoint data:**

```python
from claude_agent_sdk import UserMessage, ResultMessage

checkpoint_id = None
session_id = None

async with ClaudeSDKClient(options) as client:
    await client.query("Refactor the authentication module")
    
    async for message in client.receive_response():
        # Capture user message UUID (checkpoint)
        if isinstance(message, UserMessage) and message.uuid:
            checkpoint_id = message.uuid
        
        # Capture session ID for resuming
        if isinstance(message, ResultMessage):
            session_id = message.session_id
```

### Rewinding Files

**Restore files to a checkpoint:**

```python
# Resume the session
async with ClaudeSDKClient(ClaudeAgentOptions(
    enable_file_checkpointing=True,
    resume=session_id
)) as client:
    # Empty prompt to open connection
    await client.query("")
    
    async for message in client.receive_response():
        # Rewind to checkpoint
        await client.rewind_files(checkpoint_id)
        break
```

### Interactive Checkpoint Example

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions, UserMessage, ResultMessage

async def main():
    options = ClaudeAgentOptions(
        enable_file_checkpointing=True,
        permission_mode="acceptEdits",
        extra_args={"replay-user-messages": None}
    )

    checkpoint_id = None
    session_id = None

    print("Running agent to add doc comments to utils.py...\n")

    async with ClaudeSDKClient(options) as client:
        await client.query("Add doc comments to utils.py")

        async for message in client.receive_response():
            if isinstance(message, UserMessage) and message.uuid and not checkpoint_id:
                checkpoint_id = message.uuid
            if isinstance(message, ResultMessage):
                session_id = message.session_id

    print("Done! Open utils.py to see the added doc comments.\n")

    if checkpoint_id and session_id:
        response = input("Rewind to remove the doc comments? (y/n): ")

        if response.lower() == "y":
            async with ClaudeSDKClient(ClaudeAgentOptions(
                enable_file_checkpointing=True,
                resume=session_id
            )) as client:
                await client.query("")
                async for message in client.receive_response():
                    await client.rewind_files(checkpoint_id)
                    break

            print("\n✓ File restored!")
        else:
            print("\nKept the modified file.")

asyncio.run(main())
```

## Hooks

Hooks allow you to intercept and modify agent behavior at specific events.

### Hook Events

- `before_tool_use`: Before tool is executed
- `after_tool_use`: After tool execution completes
- `before_message`: Before message is sent to Claude
- `after_message`: After message is received from Claude

### Hook Matchers

Hooks can be filtered by:
- Tool name
- Message type
- Custom conditions

### Example: Logging Hook

```python
from claude_agent_sdk import ClaudeAgentOptions, HookEvent

async def log_tool_use(tool_name: str, input_data: dict, context: dict):
    print(f"Tool used: {tool_name}")
    print(f"Input: {input_data}")
    return input_data  # Return modified input or original

options = ClaudeAgentOptions(
    hooks={
        HookEvent.BEFORE_TOOL_USE: [log_tool_use]
    }
)
```

## Context Management

The SDK automatically manages context to prevent exceeding limits.

### Automatic Context Management

- Context is automatically trimmed when approaching limits
- Important messages are prioritized
- File contents are summarized when needed

### Manual Context Control

**Limit context size:**

```python
options = ClaudeAgentOptions(
    max_buffer_size=100000  # Limit in characters
)
```

**Add directories to context:**

```python
options = ClaudeAgentOptions(
    add_dirs=["./src", "./tests"]  # Include these directories
)
```

## Error Handling

### Built-in Error Handling

The SDK includes built-in error handling:
- Automatic retries for transient errors
- Graceful degradation
- Error messages in ResultMessage

### Custom Error Handling

```python
async for message in query(prompt="...", options=options):
    if isinstance(message, ResultMessage):
        if message.subtype == "error":
            print(f"Error: {message.result}")
            # Handle error
        else:
            print(f"Success: {message.result}")
```

## Session Management

### Session Continuity

**Using ClaudeSDKClient:**

```python
async with ClaudeSDKClient() as client:
    # First query
    await client.query("Create a file")
    async for message in client.receive_response():
        print(message)
    
    # Follow-up - Claude remembers
    await client.query("What's in that file?")
    async for message in client.receive_response():
        print(message)
```

**Using query() with continue_conversation:**

```python
# First query
async for message in query(
    prompt="Create a file",
    options=ClaudeAgentOptions(max_turns=1)
):
    print(message)

# Continue conversation
async for message in query(
    prompt="What's in that file?",
    options=ClaudeAgentOptions(
        continue_conversation=True,
        max_turns=1
    )
):
    print(message)
```

### Multiple Sessions

**Manage multiple concurrent sessions:**

```python
async with ClaudeSDKClient() as client:
    # Session 1
    await client.query("Task 1", session_id="session1")
    async for message in client.receive_response():
        if message.session_id == "session1":
            print(f"Session 1: {message}")
    
    # Session 2 (parallel)
    await client.query("Task 2", session_id="session2")
    async for message in client.receive_response():
        if message.session_id == "session2":
            print(f"Session 2: {message}")
```

### Session Resumption

**Resume a previous session:**

```python
options = ClaudeAgentOptions(
    resume=session_id  # Resume from previous session
)

async with ClaudeSDKClient(options) as client:
    await client.query("Continue from where we left off")
    async for message in client.receive_response():
        print(message)
```

## Interrupting Agents

**Interrupt Claude mid-execution:**

```python
async with ClaudeSDKClient() as client:
    await client.query("Long running task...")
    
    # In another coroutine or after timeout
    await client.interrupt()
    
    async for message in client.receive_response():
        print(message)  # May be incomplete
```

## Production Patterns

### Pattern 1: Agent with Monitoring

```python
import logging
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

logger = logging.getLogger(__name__)

async def monitored_agent(prompt: str):
    options = ClaudeAgentOptions(
        allowed_tools=["Read", "Write"],
        stderr=lambda msg: logger.error(f"Agent error: {msg}")
    )
    
    try:
        async with ClaudeSDKClient(options) as client:
            await client.query(prompt)
            
            async for message in client.receive_response():
                logger.info(f"Message: {message}")
                yield message
    except Exception as e:
        logger.error(f"Agent failed: {e}")
        raise
```

### Pattern 2: Agent with Timeout

```python
import asyncio
from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions

async def agent_with_timeout(prompt: str, timeout: int = 60):
    options = ClaudeAgentOptions(
        max_turns=10,
        allowed_tools=["Read", "Write"]
    )
    
    async with ClaudeSDKClient(options) as client:
        try:
            await asyncio.wait_for(
                client.query(prompt),
                timeout=timeout
            )
            
            async for message in client.receive_response():
                yield message
        except asyncio.TimeoutError:
            await client.interrupt()
            raise TimeoutError("Agent execution timed out")
```

### Pattern 3: Agent with Retry

```python
import asyncio
from claude_agent_sdk import query, ClaudeAgentOptions

async def agent_with_retry(prompt: str, max_retries: int = 3):
    options = ClaudeAgentOptions(
        max_turns=5,
        allowed_tools=["Read", "Write"]
    )
    
    for attempt in range(max_retries):
        try:
            async for message in query(prompt=prompt, options=options):
                if hasattr(message, 'result'):
                    return message.result
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
    
    return None
```

## Performance Optimization

### Prompt Caching

The SDK automatically caches prompts for better performance.

### Streaming

Always use streaming mode for better responsiveness:

```python
async for message in client.receive_response():
    # Process messages as they arrive
    print(message)
```

### Batch Operations

Group related operations in a single query:

```python
# Better: Single query
await client.query("""
1. Read config.json
2. Update version number
3. Write back to file
""")

# Less efficient: Multiple queries
await client.query("Read config.json")
await client.query("Update version number")
await client.query("Write back to file")
```
