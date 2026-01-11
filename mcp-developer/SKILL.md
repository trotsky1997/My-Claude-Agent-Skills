---
name: mcp-developer
description: Comprehensive guide for developing Model Context Protocol (MCP) servers. Use when (1) Creating new MCP servers, (2) Implementing MCP tools and handlers, (3) Testing MCP servers, (4) Debugging MCP communication issues, (5) Setting up stdio-based MCP servers, (6) Setting up SSE (Server-Sent Events) based MCP servers, (7) Handling MCP errors and exceptions, (8) Structuring MCP server code, or any MCP development tasks.
metadata:
  short-description: Develop MCP servers (stdio and SSE modes)

---

# MCP Developer

Complete guide for developing Model Context Protocol (MCP) servers with Python, covering server setup, tool implementation, error handling, and testing.

## Core MCP Concepts

**Model Context Protocol (MCP)** enables AI agents to securely access tools and data sources via JSON-RPC 2.0 over stdio.

**Key Components:**
- **Server**: Handles tool definitions and execution
- **Tools**: Exposed capabilities (functions the AI can call)
- **stdio**: Communication channel (standard input/output)
- **JSON-RPC 2.0**: Protocol for requests/responses

## Basic Server Structure

### 1. Imports and Setup

```python
import asyncio
import sys
from typing import Any, Optional
from pathlib import Path

try:
    from mcp.server import NotificationOptions, Server
    from mcp.server.models import InitializationOptions
    import mcp.server.stdio
    import mcp.types as types
except ImportError:
    print("Error: mcp package is not installed. Please install it with: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Initialize MCP server
server = Server("your-server-name")
```

**Critical:** Always handle import errors gracefully. MCP servers run in isolated environments where dependencies might be missing.

### 2. Define Tools

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools"""
    return [
        types.Tool(
            name="tool_name",
            description="Clear description of what the tool does",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "Parameter description"
                    },
                    "param2": {
                        "type": "string",
                        "description": "Optional parameter",
                        "default": "default_value"
                    }
                },
                "required": ["param1"]  # List required parameters
            }
        )
    ]
```

**Best Practices:**
- Use clear, descriptive tool names (snake_case)
- Write detailed descriptions (AI agents read these)
- Mark required vs optional parameters explicitly
- Provide default values for optional parameters
- Use appropriate JSON Schema types (string, number, boolean, object, array)

### 3. Implement Tool Handlers

```python
@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    """Handle tool calls"""
    
    # Validate tool name
    if name != "tool_name":
        raise ValueError(f"Unknown tool: {name}")
    
    # Validate required arguments
    if not arguments or "param1" not in arguments:
        raise ValueError("Missing required argument: param1")
    
    param1 = arguments["param1"]
    if not isinstance(param1, str):
        raise ValueError("param1 must be a string")
    
    # Get optional arguments with defaults
    param2 = arguments.get("param2", "default_value")
    
    try:
        # Your tool logic here
        result = perform_operation(param1, param2)
        
        # Return result as TextContent
        return [types.TextContent(type="text", text=str(result))]
    
    except Exception as e:
        # Wrap errors in RuntimeError for clear error messages
        error_msg = f"Error processing {param1}: {str(e)}"
        print(error_msg, file=sys.stderr)
        raise RuntimeError(error_msg) from e
```

**Error Handling:**
- Always validate input parameters
- Check types explicitly
- Provide clear error messages
- Use `RuntimeError` for user-facing errors
- Log errors to stderr for debugging

### 4. Main Entry Point

**For stdio mode (most common):**

```python
async def main_async():
    """Async main entry point for the MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="your-server-name",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )

def main():
    """Main entry point (synchronous wrapper)"""
    asyncio.run(main_async())

if __name__ == "__main__":
    main()
```

**For SSE (Server-Sent Events) mode:**

See [SSE Mode Implementation](#sse-mode-implementation) section below.

### 5. Enable Module Execution

Create `__main__.py` to enable `python -m package.mcp_server`:

```python
"""Enable running as python -m package.mcp_server"""

from .mcp_server import main

if __name__ == "__main__":
    main()
```

## Common Patterns

### Lazy Initialization with Caching

```python
# Global cache
resource_cache: dict[str, Resource] = {}

def get_resource(key: str = "default") -> Resource:
    """Get or create resource with caching"""
    global resource_cache
    
    if key not in resource_cache:
        resource_cache[key] = Resource(key)
    
    return resource_cache[key]
```

### File Path Validation

```python
from pathlib import Path

# Validate file exists
file_path = Path(arguments["file_path"])
if not file_path.exists():
    raise FileNotFoundError(f"File not found: {file_path}")

if not file_path.is_file():
    raise ValueError(f"Path is not a file: {file_path}")
```

### Temporary File Management

```python
import tempfile
import os

# Create temporary file
temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
temp_path = temp_file.name
temp_file.close()

try:
    # Use temp file
    process_file(temp_path)
finally:
    # Always clean up
    try:
        if os.path.exists(temp_path):
            os.unlink(temp_path)
    except Exception:
        pass  # Ignore cleanup errors
```

### Returning Multiple Results

```python
# Return multiple text contents
results = []
for item in processed_items:
    results.append(types.TextContent(type="text", text=str(item)))
return results
```

## Testing MCP Servers

### Unit Testing Structure

```python
import pytest
from unittest.mock import MagicMock, patch
from paddleocr_cli.mcp_server import handle_list_tools, handle_call_tool

@pytest.mark.asyncio
async def test_list_tools():
    """Test tool listing"""
    tools = await handle_list_tools()
    assert len(tools) == 1
    assert tools[0].name == "tool_name"
    assert "param1" in tools[0].inputSchema["properties"]

@pytest.mark.asyncio
async def test_call_tool_success():
    """Test successful tool call"""
    with patch("module.external_dependency") as mock_dep:
        mock_dep.return_value = "expected_result"
        
        result = await handle_call_tool("tool_name", {"param1": "value"})
        
        assert len(result) == 1
        assert result[0].type == "text"

@pytest.mark.asyncio
async def test_call_tool_validation():
    """Test input validation"""
    with pytest.raises(ValueError, match="Missing required argument"):
        await handle_call_tool("tool_name", {})
```

**Testing Best Practices:**
- Mock external dependencies (APIs, file I/O, heavy computations)
- Test both success and error paths
- Validate input schema matches implementation
- Use `pytest-asyncio` for async tests
- Test edge cases (empty inputs, invalid types, missing files)

### End-to-End Testing

```python
import asyncio
from mcp_server import handle_call_tool, handle_list_tools

async def test_e2e():
    # Test tool listing
    tools = await handle_list_tools()
    print(f"Tools: {[t.name for t in tools]}")
    
    # Test tool execution
    result = await handle_call_tool("tool_name", {"param1": "test_value"})
    print(f"Result: {result}")

asyncio.run(test_e2e())
```

## Common Errors and Solutions

### "Unknown tool" Error

**Cause:** Tool name mismatch between `list_tools` and `call_tool`.

**Solution:**
- Ensure tool names match exactly (case-sensitive)
- Check for typos in tool name strings
- Verify `@server.call_tool()` handler checks tool name

### "Missing required argument" Error

**Cause:** Client didn't provide required parameter.

**Solution:**
- Check `inputSchema["required"]` includes all mandatory parameters
- Validate arguments exist before accessing
- Provide clear error messages indicating which parameter is missing

### Import Errors at Runtime

**Cause:** Dependencies not installed in MCP server environment.

**Solution:**
- Wrap imports in try-except blocks
- Print helpful error messages to stderr
- Exit gracefully with `sys.exit(1)`
- Document dependencies in `pyproject.toml`

### stdio Communication Issues

**Cause:** Server not properly configured for stdio.

**Solution:**
- Use `mcp.server.stdio.stdio_server()` context manager
- Ensure `server.run()` is called with proper streams
- Don't use `print()` for normal output (use stderr for errors only)
- Return results via `types.TextContent` or appropriate content types

### Type Validation Errors

**Cause:** Arguments don't match expected types.

**Solution:**
- Always validate argument types explicitly
- Use `isinstance()` checks
- Convert types when appropriate (e.g., `str()` for paths)
- Provide clear error messages with expected vs actual types

## Best Practices

1. **Always validate inputs**
   - Check required parameters exist
   - Validate types explicitly
   - Verify file paths exist and are files (not directories)

2. **Handle errors gracefully**
   - Wrap exceptions in user-friendly messages
   - Log errors to stderr for debugging
   - Use `RuntimeError` for operational errors

3. **Use async/await correctly**
   - All tool handlers must be async
   - Use `@pytest.mark.asyncio` for async tests
   - Don't block the event loop

4. **Cache expensive resources**
   - Lazy initialization for heavy objects
   - Cache by key (e.g., language, model type)
   - Reuse instances across tool calls

5. **Clean up resources**
   - Use try-finally for temporary files
   - Close file handles
   - Clean up temporary directories

6. **Test thoroughly**
   - Unit tests for each tool
   - Test error cases
   - End-to-end tests with real inputs
   - Mock external dependencies

7. **Document clearly**
   - Clear tool descriptions (AI agents read these)
   - Document parameter types and requirements
   - Include examples in descriptions

## Project Structure

```
project/
├── package/
│   ├── __init__.py          # Package version
│   ├── __main__.py          # Enable python -m package.mcp_server
│   └── mcp_server.py        # Main MCP server implementation
├── tests/
│   └── test_mcp_server.py   # Unit tests
├── pyproject.toml           # Package metadata, dependencies
└── README.md                 # Documentation
```

## Quick Reference

**Essential imports:**
```python
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.server.stdio
import mcp.types as types
```

**Tool definition:**
```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [types.Tool(name="...", description="...", inputSchema={...})]
```

**Tool handler:**
```python
@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict]) -> list[types.TextContent]:
    # Validate and process
    return [types.TextContent(type="text", text="result")]
```

**Main entry:**
```python
async def main_async():
    async with mcp.server.stdio.stdio_server() as (read, write):
        await server.run(read, write, InitializationOptions(...))
```

## Testing Checklist

- [ ] All tools listed correctly
- [ ] Input schema matches implementation
- [ ] Required parameters validated
- [ ] Type validation works
- [ ] Error handling tested
- [ ] Edge cases covered
- [ ] End-to-end test passes
- [ ] No resource leaks (temp files cleaned up)

## SSE Mode Implementation

SSE (Server-Sent Events) mode allows MCP servers to run over HTTP, enabling remote access and web integration. This is useful for:
- Remote MCP servers
- Web-based clients
- Cross-network communication
- Integration with web applications

### SSE Server Setup

```python
import asyncio
from aiohttp import web
from aiohttp_sse import sse_response
from mcp.server import Server, NotificationOptions
from mcp.server.models import InitializationOptions
import mcp.types as types

# Initialize MCP server (same as stdio mode)
server = Server("your-server-name")

# Define tools (same as stdio mode)
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    # ... same implementation as stdio mode
    pass

@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    # ... same implementation as stdio mode
    pass

# SSE endpoint handler
async def sse_handler(request: web.Request) -> web.StreamResponse:
    """Handle SSE connection for MCP communication"""
    async with sse_response(request) as response:
        # Create read/write streams from SSE
        read_stream = request.content
        write_stream = response
        
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="your-server-name",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )
    
    return response

# HTTP server setup
async def create_app() -> web.Application:
    """Create aiohttp application with SSE endpoint"""
    app = web.Application()
    
    # Add CORS middleware for cross-origin requests
    from aiohttp_cors import setup as cors_setup, ResourceOptions
    cors = cors_setup(app, defaults={
        "*": ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods="*"
        )
    })
    
    # Register SSE endpoint
    app.router.add_get("/sse", sse_handler)
    
    # Health check endpoint
    async def health_check(request: web.Request) -> web.Response:
        return web.json_response({"status": "ok"})
    
    app.router.add_get("/health", health_check)
    
    return app

def main():
    """Start HTTP server with SSE support"""
    app = asyncio.run(create_app())
    web.run_app(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
```

### SSE Dependencies

Add to `pyproject.toml`:

```toml
[project]
dependencies = [
    "mcp",
    "aiohttp>=3.9.0",
    "aiohttp-sse>=0.8.0",
    "aiohttp-cors>=0.7.0",
]
```

### SSE Client Configuration

For MCP clients using SSE mode:

```json
{
  "mcpServers": {
    "your-server": {
      "url": "http://localhost:8000/sse"
    }
  }
}
```

### SSE vs stdio Mode

| Feature | stdio Mode | SSE Mode |
|---------|-----------|----------|
| **Communication** | Standard input/output | HTTP with Server-Sent Events |
| **Use Case** | Local, same-machine | Remote, web-based |
| **Setup** | Simple (no HTTP server) | Requires HTTP server |
| **Network** | No network required | Requires network access |
| **CORS** | Not applicable | May need CORS configuration |
| **Security** | Process isolation | Need authentication/HTTPS |

**Choose stdio mode when:**
- Server runs on same machine as client
- Simple local integration
- No network access needed

**Choose SSE mode when:**
- Remote server access needed
- Web-based clients
- Cross-network communication
- Integration with web applications

### SSE Best Practices

1. **Use HTTPS in production**
   ```python
   import ssl
   
   ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
   ssl_context.load_cert_chain('cert.pem', 'key.pem')
   
   web.run_app(app, host="0.0.0.0", port=8000, ssl_context=ssl_context)
   ```

2. **Add authentication**
   ```python
   async def sse_handler(request: web.Request) -> web.StreamResponse:
       # Check authentication token
       token = request.headers.get('Authorization')
       if token != f"Bearer {expected_token}":
           raise web.HTTPUnauthorized()
       
       # ... rest of handler
   ```

3. **Handle connection errors gracefully**
   ```python
   async def sse_handler(request: web.Request) -> web.StreamResponse:
       try:
           async with sse_response(request) as response:
               # ... server.run()
       except asyncio.CancelledError:
           # Client disconnected
           pass
       except Exception as e:
           print(f"SSE error: {e}", file=sys.stderr)
           raise
   ```

4. **Add request logging**
   ```python
   from aiohttp import web
   
   async def logging_middleware(app, handler):
       async def middleware_handler(request):
           print(f"{request.method} {request.path}")
           return await handler(request)
       return middleware_handler
   
   app.middlewares.append(logging_middleware)
   ```

## Additional Resources

**Common patterns:** See `references/common-patterns.md` for:
- Simple tool patterns
- File processing patterns
- Resource caching patterns
- Error handling patterns
- Multiple return values
- Async resource loading

**Template code:**
- `scripts/template_mcp_server.py` - Complete stdio mode starter template
- `scripts/template_mcp_server_sse.py` - Complete SSE mode starter template

**Key lessons from real development:**
- Always test with actual MCP clients before publishing
- Validate all inputs explicitly (don't trust client data)
- Handle API version changes gracefully (e.g., PaddleOCR 2.7+ format changes)
- Use end-to-end tests to catch integration issues
- Mock external dependencies in unit tests for speed
- Clean up temporary files in finally blocks
