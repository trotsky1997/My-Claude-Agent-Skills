#!/usr/bin/env python3
"""Template MCP server with SSE (Server-Sent Events) support - customize for your use case"""

import asyncio
import sys
from pathlib import Path
from typing import Any, Optional

try:
    from aiohttp import web
    from aiohttp_sse import sse_response
    from aiohttp_cors import setup as cors_setup, ResourceOptions
except ImportError:
    print("Error: SSE dependencies not installed. Install with: pip install aiohttp aiohttp-sse aiohttp-cors", file=sys.stderr)
    sys.exit(1)

try:
    from mcp.server import NotificationOptions, Server
    from mcp.server.models import InitializationOptions
    import mcp.types as types
except ImportError:
    print("Error: mcp package is not installed. Please install it with: pip install mcp", file=sys.stderr)
    sys.exit(1)

# Initialize MCP server
server = Server("your-server-name")

# Global state (if needed)
# cache: dict[str, Any] = {}


@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List available tools"""
    return [
        types.Tool(
            name="your_tool",
            description="Description of what your tool does",
            inputSchema={
                "type": "object",
                "properties": {
                    "param1": {
                        "type": "string",
                        "description": "Parameter description"
                    }
                },
                "required": ["param1"]
            }
        )
    ]


@server.call_tool()
async def handle_call_tool(name: str, arguments: Optional[dict[str, Any]]) -> list[types.TextContent]:
    """Handle tool calls"""
    if name != "your_tool":
        raise ValueError(f"Unknown tool: {name}")
    
    # Validate arguments
    if not arguments or "param1" not in arguments:
        raise ValueError("Missing required argument: param1")
    
    param1 = arguments["param1"]
    if not isinstance(param1, str):
        raise ValueError("param1 must be a string")
    
    try:
        # Your tool logic here
        result = process_tool(param1)
        
        # Return result
        return [types.TextContent(type="text", text=str(result))]
    
    except Exception as e:
        error_msg = f"Error processing {param1}: {str(e)}"
        print(error_msg, file=sys.stderr)
        raise RuntimeError(error_msg) from e


def process_tool(param: str) -> str:
    """Process tool input and return result"""
    # Implement your logic here
    return f"Processed: {param}"


async def sse_handler(request: web.Request) -> web.StreamResponse:
    """Handle SSE connection for MCP communication"""
    # Optional: Add authentication
    # token = request.headers.get('Authorization')
    # if token != f"Bearer {expected_token}":
    #     raise web.HTTPUnauthorized()
    
    try:
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
    
    except asyncio.CancelledError:
        # Client disconnected
        print("Client disconnected", file=sys.stderr)
        raise
    except Exception as e:
        print(f"SSE error: {e}", file=sys.stderr)
        raise


async def health_check(request: web.Request) -> web.Response:
    """Health check endpoint"""
    return web.json_response({"status": "ok", "server": "your-server-name"})


async def create_app() -> web.Application:
    """Create aiohttp application with SSE endpoint"""
    app = web.Application()
    
    # Add CORS middleware for cross-origin requests
    cors = cors_setup(app, defaults={
        "*": ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods="*"
        )
    })
    
    # Register endpoints
    app.router.add_get("/sse", sse_handler)
    app.router.add_get("/health", health_check)
    
    # Optional: Add logging middleware
    # async def logging_middleware(app, handler):
    #     async def middleware_handler(request):
    #         print(f"{request.method} {request.path}")
    #         return await handler(request)
    #     return middleware_handler
    # app.middlewares.append(logging_middleware)
    
    return app


def main():
    """Start HTTP server with SSE support"""
    app = asyncio.run(create_app())
    
    # For production, use HTTPS:
    # import ssl
    # ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    # ssl_context.load_cert_chain('cert.pem', 'key.pem')
    # web.run_app(app, host="0.0.0.0", port=8000, ssl_context=ssl_context)
    
    # For development:
    web.run_app(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()
