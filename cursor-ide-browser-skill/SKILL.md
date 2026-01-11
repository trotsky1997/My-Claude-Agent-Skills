---

name: cursor-ide-browser-skills

description: Browser automation in Cursor IDE using MCP protocol server `cursor-ide-browser`. Use when (1) Automating web interactions in Cursor IDE, (2) Navigating web pages, (3) Clicking buttons or links, (4) Filling forms or input fields, (5) Taking screenshots or capturing page snapshots, (6) Debugging web pages by checking console messages or network requests, (7) Extracting information from web pages, (8) Testing web applications, (9) Interacting with web-based documentation or tools, (10) Any task requiring programmatic browser control within Cursor IDE
metadata:
  short-description: Browser automation in Cursor IDE via MCP

---

# Cursor IDE Browser Automation

Browser automation tool for Cursor IDE using MCP (Model Context Protocol) server `cursor-ide-browser` and accessibility snapshots for precise element interaction.

## Core Mechanism

**Accessibility Snapshot First**: Always get a snapshot before interacting with elements. The snapshot provides structured page information with element references (`ref`) needed for all interactions.

```javascript
// Standard workflow
browser_navigate(url="https://example.com")
browser_snapshot()  // Required: Get element references
browser_click(element="Button", ref="ref-from-snapshot")
```

## Essential Workflow

1. **Navigate** to target page
2. **Snapshot** to get element references (required before any interaction)
3. **Convert to Markdown** (⭐ Recommended) for easier searching, locating and reading
4. **Search with grep in md** to find information or locate interactive elements
5. **Interact** using refs from snapshot
6. **Wait** for dynamic content if needed
7. **Verify** with screenshots or console messages

**Quick example:**

```javascript
browser_navigate(url="https://example.com")
browser_snapshot()  // Creates .log file
mcp_snapshot-query_convert_to_markdown(file_path="snapshot.log")
grep(pattern="button|登录", path="snapshot.md")  // Find elements
browser_click(element="Login", ref="ref-from-grep-results")
```

## Key Tools

**Navigation:**

- `browser_navigate(url, position?)` - Navigate to URL
- `browser_navigate_back()` - Go back

**Page Information:**

- `browser_snapshot()` - **Required before interactions** - Get accessibility tree with element refs
- `browser_take_screenshot(fullPage?, filename?)` - Capture visual
- `browser_console_messages()` - Get console logs
- `browser_network_requests()` - Get network activity

**Element Interaction:**

- `browser_click(element, ref, doubleClick?, button?, modifiers?)` - Click element
- `browser_type(element, ref, text, submit?, slowly?)` - Type text
- `browser_hover(element, ref)` - Hover
- `browser_select_option(element, ref, values)` - Select dropdown
- `browser_press_key(key)` - Press key (supports PageDown, PageUp, ArrowDown, ArrowUp, Space, End, Home for scrolling)

**Synchronization:**

- `browser_wait_for(text?, textGone?, time?)` - Wait for text or time

**Tab Management:**

- `browser_tabs(action, index?, position?)` - Manage tabs (list/new/close/select)

## Element References

- `**element**`: Human-readable description (for permission confirmation)
- `**ref**`: Technical reference from snapshot (required for interaction)
- Refs are **page-state specific** - get a new snapshot after navigation or page changes

## Snapshot Files

Snapshots are automatically saved as YAML files:

- **Location**: `C:\Users\{username}\.cursor\browser-logs\snapshot-{timestamp}.log`
- **Format**: YAML accessibility tree with `role`, `ref`, `name`, `children`
- **Usage**: Extract `ref` values for element interactions

## Querying Snapshots

### ⭐ Recommended Workflow: Convert to Markdown + Grep

**Best practice for finding information and locating interactive elements:**

1. **Get snapshot** → Creates `.log` file
2. **Convert to Markdown** → More readable format with structured content
3. **Use grep** → Fast text search across the entire document
4. **Extract refs** → Use found refs for interactions

```javascript
// Step 1: Get page snapshot
browser_snapshot()  // Creates: snapshot-2026-01-10T23-43-30-351Z.log

// Step 2: Convert to Markdown (RECOMMENDED)
mcp_snapshot-query_convert_to_markdown(
  file_path="snapshot-2026-01-10T23-43-30-351Z.log",
  include_ref=true
) # save to snapshot-2026-01-10T23-43-30-351Z.md

// Step 3: Search with grep (much easier than querying raw YAML)
grep(pattern="搜索|button|登录", path="snapshot.md", -i=true)
grep(pattern="^\\[.*\\]\\(ref-|^\\*\\*.*\\*\\* `ref-", path="snapshot.md")  // Find all links/buttons

// Step 4: Use found refs for interaction
browser_click(element="Login button", ref="ref-found-from-grep")
```

**Why this workflow is preferred:**

- ✅ **More readable**: Markdown format is human-friendly
- ✅ **Faster search**: `grep` is more efficient than parsing YAML
- ✅ **Better context**: See surrounding content with `-C` flag
- ✅ **Easy element discovery**: Links and buttons clearly formatted
- ✅ **Preserves refs**: All element references included for interaction

**Alternative: Direct Query Tools**

For programmatic element finding, use snapshot-query MCP tools:

**Command line:**

```bash
browser_snapshot()  # Generate snapshot
uvx snapshot-query snapshot.log find-name "search"  # Find element
```

**MCP tools:**

```javascript
mcp_snapshot-query_find_by_name(file_path="snapshot.log", name="搜索")
mcp_snapshot-query_find_by_role(file_path="snapshot.log", role="button")
mcp_snapshot-query_find_by_text(file_path="snapshot.log", text="登录")
mcp_snapshot-query_find_by_regex(file_path="snapshot.log", pattern="\\d+\\s*ft", field="name")
mcp_snapshot-query_find_by_name_bm25(file_path="snapshot.log", name="search query", top_k=5)
mcp_snapshot-query_count_elements(file_path="snapshot.log")
mcp_snapshot-query_get_element_path(file_path="snapshot.log", ref="ref-xxx")
mcp_snapshot-query_extract_all_refs(file_path="snapshot.log")
```

**Integrated workflow:**

```javascript
browser_snapshot()  // Creates snapshot file
// Query snapshot to find element ref
const result = mcp_snapshot-query_find_by_name(file_path="snapshot.log", name="Login")
browser_click(element="Login", ref=result.ref)  // Use ref from query
```

**⭐ snapshot-query works with OCR results too:**

The snapshot-query tools can process OCR results from `fast-paddleocr-mcp`. After OCR processing, you get a `.snapshot.log` file that can be queried just like browser snapshots:

```javascript
// OCR generates webpage.png.snapshot.log
mcp_fast-paddleocr-mcp_ocr_image(image_path="webpage.png", language="ch")

// Query OCR results with snapshot-query
mcp_snapshot-query_find_by_text(
  file_path="webpage.png.snapshot.log",
  text="8 ft",
  case_sensitive=false
)

// Use regex to find measurements
mcp_snapshot-query_find_by_regex(
  file_path="webpage.png.snapshot.log",
  pattern="\\d+\\s*ft|cm|meters?",
  field="name"
)

// Semantic search for better results
mcp_snapshot-query_find_by_name_bm25(
  file_path="webpage.png.snapshot.log",
  name="height measurement",
  top_k=5
)

// Convert to Markdown for analysis
mcp_snapshot-query_convert_to_markdown(
  file_path="webpage.png.snapshot.log",
  include_ref=true
)
```

See [references/snapshot-query.md](references/snapshot-query.md) for complete snapshot-query documentation.

## Common Patterns

**Login flow:**

```javascript
browser_navigate(url="https://example.com/login")
browser_snapshot()
// Find username input ref from snapshot
browser_type(element="Username", ref="ref-username", text="user")
// Find password input ref from snapshot
browser_type(element="Password", ref="ref-password", text="pass")
// Find login button ref from snapshot
browser_click(element="Login", ref="ref-login-btn")
browser_wait_for(text="Welcome")
```

**Search and extract (with Markdown workflow):**

```javascript
browser_navigate(url="https://www.baidu.com/s?wd=哈梅内伊有几个孩子")
browser_snapshot()  // Creates snapshot.log
// Convert to Markdown for easier searching
mcp_snapshot-query_convert_to_markdown(
  file_path="snapshot.log",
  include_ref=true
)
// Search for information using grep
grep(pattern="六名|6个|子女", path="snapshot.md", -i=true, -C=3)
// Find interactive elements (links/buttons)
grep(pattern="^\\[.*\\]\\(ref-|^\\*\\*.*\\*\\* `ref-", path="snapshot.md")
// Click on found link using ref
browser_click(element="Article link", ref="ref-45py92vjdrs")
browser_wait_for(text="Results")
browser_take_screenshot(filename="results.png")
```

**Debug page issues:**

```javascript
browser_snapshot()
browser_console_messages()  // Check for errors
browser_network_requests()  // Check failed requests
```

**Scrolling web pages:**

```javascript
browser_press_key("PageDown")   // Scroll down one page
browser_press_key("PageUp")      // Scroll up one page
browser_press_key("ArrowDown")   // Scroll down line by line
browser_press_key("ArrowUp")     // Scroll up line by line
browser_press_key("Space")       // Scroll down one screen
browser_press_key("End")         // Scroll to bottom
browser_press_key("Home")        // Scroll to top
browser_wait_for(time=1)        // Wait after scrolling for content to load
```

**OCR processing with fast-paddleocr-mcp:**

```javascript
// Take screenshot of webpage
browser_take_screenshot(filename="webpage.png", fullPage=false)

// Process with OCR (generates .md and .snapshot.log files)
mcp_fast-paddleocr-mcp_ocr_image(
  image_path="webpage.png",
  language="ch"  // Use "ch" for Chinese+English, "en" for English only
)

// Query OCR results with snapshot-query
mcp_snapshot-query_find_by_text(
  file_path="webpage.png.snapshot.log",
  text="tallest",
  case_sensitive=false
)

// Use BM25 semantic search for better results
mcp_snapshot-query_find_by_name_bm25(
  file_path="webpage.png.snapshot.log",
  name="height tallest person",
  top_k=5
)

// Convert OCR snapshot to Markdown for easier analysis
mcp_snapshot-query_convert_to_markdown(
  file_path="webpage.png.snapshot.log",
  include_ref=true
)
```

**Cross-verification workflow:**

```javascript
// Navigate to multiple sources for verification
browser_navigate(url="https://source1.com/article")
browser_snapshot()
// Extract information from source 1

browser_navigate(url="https://source2.com/article")
browser_snapshot()
// Extract information from source 2

// Compare and verify information consistency
// Prefer authoritative sources (Wikipedia, official records, etc.)
```

## Important Notes

1. **Always snapshot before interaction** - Refs are required and page-specific
2. **⭐ Convert to Markdown first** - Use `convert_to_markdown` + `grep` for finding information and elements (much easier than querying raw YAML)
3. **Wait for dynamic content** - Use `browser_wait_for()` for async operations
4. **Refs expire** - Get new snapshot after navigation or page changes
5. **Multi-tab support** - Use `viewId` parameter or `browser_tabs()` to manage tabs
6. **Position control** - Use `position="side"` when user mentions side panel
7. **OCR limitations** - OCR may merge adjacent text (e.g., "otherreliablesourcesccordingtoG"). Key information is usually extracted correctly, but verify important details
8. **Cross-verification** - For critical information, verify across multiple authoritative sources (Wikipedia, official records, etc.)
9. **Tool combination** - Combine browser automation + OCR + snapshot-query for comprehensive web content analysis

## Best Practices & Lessons Learned

### Workflow Optimization

1. **Standard workflow**: Navigate → Snapshot → Convert to Markdown → Search → Interact
2. **OCR workflow**: Screenshot → OCR → Query with snapshot-query → Extract information
3. **Verification workflow**: Multiple sources → Extract → Compare → Verify consistency

### Tool Integration

- **Browser + OCR**: Use `browser_take_screenshot()` + `fast-paddleocr-mcp` to extract text from visual content
- **OCR + snapshot-query**: OCR generates `.snapshot.log` files that can be queried with all snapshot-query tools
- **Markdown + grep**: Convert snapshots/OCR results to Markdown for easier searching

### Key Insights

- **snapshot-query is universal**: Works with both browser snapshots and OCR results
- **Markdown conversion is recommended**: Much easier to search and read than raw YAML
- **BM25 semantic search**: Use `find_by_name_bm25()` for better relevance when exact matches are unclear
- **Cross-verification**: Always verify critical information from multiple authoritative sources
- **OCR accuracy**: Works well for key information but may merge adjacent text - verify important details

## Detailed Reference

- **Complete tool reference**: See [references/tools.md](references/tools.md) for all tools with full parameters
- **Examples and patterns**: See [references/examples.md](references/examples.md) for detailed workflows
- **Snapshot file format**: See [references/snapshot-format.md](references/snapshot-format.md) for YAML structure details
- **Snapshot querying**: See [references/snapshot-query.md](references/snapshot-query.md) for querying snapshot files

