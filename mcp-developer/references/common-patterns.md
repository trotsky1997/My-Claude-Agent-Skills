# Common MCP Development Patterns

## Pattern 1: Simple Tool with Single Parameter

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="echo",
            description="Echo back the input text",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "Text to echo back"
                    }
                },
                "required": ["text"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    if name != "echo":
        raise ValueError(f"Unknown tool: {name}")
    
    text = arguments.get("text", "")
    return [types.TextContent(type="text", text=text)]
```

## Pattern 2: File Processing Tool

```python
@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    if name != "process_file":
        raise ValueError(f"Unknown tool: {name}")
    
    file_path = arguments.get("file_path")
    if not file_path:
        raise ValueError("Missing required argument: file_path")
    
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    # Process file
    result = process_file(path)
    return [types.TextContent(type="text", text=str(result))]
```

## Pattern 3: Tool with Optional Parameters

```python
@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="search",
            description="Search with optional filters",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Maximum results (default: 10)",
                        "default": 10
                    },
                    "filter": {
                        "type": "string",
                        "description": "Optional filter"
                    }
                },
                "required": ["query"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    query = arguments.get("query")
    limit = arguments.get("limit", 10)
    filter_val = arguments.get("filter")
    
    results = perform_search(query, limit=limit, filter=filter_val)
    return [types.TextContent(type="text", text=str(results))]
```

## Pattern 4: Resource Caching

```python
# Global cache
model_cache: dict[str, Model] = {}

def get_model(model_name: str = "default") -> Model:
    """Get or create model with caching"""
    global model_cache
    
    if model_name not in model_cache:
        model_cache[model_name] = Model(model_name)
    
    return model_cache[model_name]

@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    model_name = arguments.get("model", "default")
    model = get_model(model_name)
    result = model.predict(arguments["input"])
    return [types.TextContent(type="text", text=str(result))]
```

## Pattern 5: Error Handling with Context

```python
@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    try:
        # Validate inputs
        if not arguments or "input" not in arguments:
            raise ValueError("Missing required argument: input")
        
        input_data = arguments["input"]
        
        # Process with error context
        result = process(input_data)
        return [types.TextContent(type="text", text=str(result))]
    
    except ValueError as e:
        # Re-raise validation errors as-is
        raise
    except FileNotFoundError as e:
        # Wrap file errors with context
        raise RuntimeError(f"File operation failed: {str(e)}") from e
    except Exception as e:
        # Wrap unexpected errors
        error_msg = f"Error processing input: {str(e)}"
        print(error_msg, file=sys.stderr)
        raise RuntimeError(error_msg) from e
```

## Pattern 6: Multiple Return Values

```python
@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    items = process_items(arguments["items"])
    
    # Return multiple text contents
    results = []
    for item in items:
        results.append(types.TextContent(type="text", text=str(item)))
    
    return results
```

## Pattern 7: Async Resource Loading

```python
async def load_data_async(path: str) -> Data:
    """Load data asynchronously"""
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, load_data_sync, path)
    return data

@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    data = await load_data_async(arguments["path"])
    result = process(data)
    return [types.TextContent(type="text", text=str(result))]
```

## Pattern 8: SSE Mode with Authentication

```python
from aiohttp import web
from aiohttp_sse import sse_response

# Expected token (in production, load from config/env)
EXPECTED_TOKEN = "your-secret-token"

async def sse_handler(request: web.Request) -> web.StreamResponse:
    """Handle SSE connection with authentication"""
    # Check authentication
    auth_header = request.headers.get('Authorization', '')
    if not auth_header.startswith('Bearer '):
        raise web.HTTPUnauthorized()
    
    token = auth_header[7:]  # Remove 'Bearer ' prefix
    if token != EXPECTED_TOKEN:
        raise web.HTTPForbidden()
    
    # Proceed with SSE connection
    async with sse_response(request) as response:
        read_stream = request.content
        write_stream = response
        
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(...)
        )
    
    return response
```

## Pattern 9: SSE Mode with HTTPS

```python
import ssl
from aiohttp import web

def main():
    app = asyncio.run(create_app())
    
    # Create SSL context
    ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    ssl_context.load_cert_chain(
        certfile='path/to/cert.pem',
        keyfile='path/to/key.pem'
    )
    
    # Run with HTTPS
    web.run_app(
        app,
        host="0.0.0.0",
        port=8443,
        ssl_context=ssl_context
    )
```
