#!/usr/bin/env python3
"""Template MCP server - customize for your use case"""

import asyncio
import sys
from pathlib import Path
from typing import Any, Optional

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
