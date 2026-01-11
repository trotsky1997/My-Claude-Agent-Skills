---
name: vibium-browser-automation
description: Comprehensive guide for using Vibium browser automation tool via MCP. Use when (1) Automating web interactions in Cursor IDE, (2) Navigating web pages, (3) Taking screenshots, (4) Clicking buttons or links, (5) Filling forms or input fields, (6) Finding elements on web pages, (7) Web scraping tasks, (8) Testing websites, or any task requiring programmatic browser control within Cursor IDE
metadata:
  short-description: Browser automation with Vibium MCP

---

# Vibium Browser Automation

Guide for using Vibium browser automation tool through MCP protocol in Cursor IDE.

## Available Tools

| Tool | Description | Notes |
|------|-------------|-------|
| `browser_launch` | Start browser (visible by default) | Use `headless: false` for debugging |
| `browser_navigate` | Go to URL | Waits for page load |
| `browser_find` | Find element by CSS selector | Returns element info (tag, text, box) |
| `browser_click` | Click an element | Waits for element to be clickable |
| `browser_type` | Type text into an element | Waits for element to be editable |
| `browser_screenshot` | Capture viewport | Saves to `Pictures/Vibium/` by default |
| `browser_quit` | Close browser | Clean up when done |

## Core Workflows

### Basic Navigation and Screenshot

```python
# Launch browser
browser_launch(headless=False)

# Navigate to page
browser_navigate(url="https://example.com")

# Take screenshot
browser_screenshot(filename="example.png")

# Close browser
browser_quit()
```

### Finding and Interacting with Elements

```python
# Find element
element = browser_find(selector="h1")
# Returns: tag=h1, text="Example", box={x:100, y:200, w:300, h:50}

# Click element
browser_click(selector="a")

# Type into input
browser_type(selector="input[name='q']", text="search query")
```

### Form Filling

```python
# Navigate to form page
browser_navigate(url="https://example.com/form")

# Fill multiple fields
browser_type(selector="input[name='name']", text="John Doe")
browser_type(selector="input[name='email']", text="john@example.com")
browser_type(selector="input[name='phone']", text="123-456-7890")

# Take screenshot of filled form
browser_screenshot(filename="form-filled.png")
```

## Best Practices

### CSS Selectors

**Use simple, reliable selectors:**
- ✅ `input[name="q"]` - Attribute selectors
- ✅ `textarea[name="q"]` - Element + attribute
- ✅ `h1`, `a`, `button` - Simple element selectors
- ✅ `.class-name` - Class selectors
- ❌ `:has-text()` - Not supported
- ❌ Complex pseudo-selectors - May fail

**Multiple selectors for flexibility:**
```python
# Try multiple selectors if unsure
browser_find(selector="textarea[name='q'], input[name='q']")
```

### Error Handling

**Connection issues:**
- If browser connection fails, relaunch: `browser_launch()`
- Check if browser is still running before operations

**Element not found:**
- Wait for page to load before finding elements
- Use more generic selectors if specific ones fail
- Take screenshot to inspect page state

**Timeouts:**
- Some operations may timeout after 30s
- Break complex tasks into smaller steps
- Take screenshots at key points for debugging

### Screenshot Management

- Screenshots save to `C:\Users\<user>\Pictures\Vibium\` on Windows
- Use descriptive filenames: `google-search-typed.png`
- Take screenshots before/after important actions for debugging

## Limitations and Workarounds

For detailed explanation of limitations and comprehensive workarounds, see [limitations.md](references/limitations.md).

### No Snapshot Log Support

**Problem:** Vibium doesn't support saving accessibility snapshots (YAML format).

**Workaround:** Combine with `cursor-ide-browser`:
1. Use vibium for browser operations
2. Use `cursor-ide-browser`'s `browser_snapshot` to get accessibility snapshot
3. Save snapshot to YAML file
4. Use `snapshot-query` tools to analyze snapshot

### No Keyboard Actions

**Problem:** Can't press Enter or other keys directly.

**Workaround:**
- For form submission, find and click submit button instead
- For search, find search button and click it
- Or navigate directly to result URL if possible

### Limited Selector Support

**Problem:** Some advanced CSS selectors don't work.

**Workaround:**
- Use basic selectors (element, class, attribute)
- Try multiple selector variations
- Use `browser_find` to test selectors before clicking/typing

### Text Extraction Limitations

**Problem:** Cannot directly extract full page text content.

**Recommended Solution: EasyOCR + Screenshot + Scroll + Grep**

This is the most reliable one-time solution:
1. Take screenshot with `browser_screenshot()`
2. Use EasyOCR to extract all text from image
3. Use grep/regex to search in OCR text
4. Scroll page and repeat for full content

See [limitations.md](references/limitations.md) for complete implementation.

**Other Workarounds:**
- Combine with `cursor-ide-browser` snapshot for full text extraction
- Use `web_search` tool for structured information
- Extract multiple small elements instead of large ones

### Manual Information Organization

**Problem:** Need to manually combine and organize data from multiple `browser_find` results.

**Workaround:**
- Use `web_search` for pre-structured data
- Combine tools (vibium + cursor-ide-browser + snapshot-query)
- Create extraction scripts for automated organization

## Common Patterns

### Web Search Automation

```python
# Navigate to search engine
browser_navigate(url="https://www.google.com")

# Find search box
browser_find(selector="textarea[name='q'], input[name='q']")

# Type search query
browser_type(selector="textarea[name='q']", text="your query")

# Take screenshot
browser_screenshot(filename="search-typed.png")

# Note: Can't press Enter, need to find and click search button
# Or navigate directly to search results URL
```

### Information Extraction

```python
# Navigate to page
browser_navigate(url="https://example.com")

# Find elements
heading = browser_find(selector="h1")
links = browser_find(selector="a")

# Extract information from results
# Results include: tag, text, box (position/size)
```

### Multi-Page Workflow

```python
# Page 1
browser_navigate(url="https://example.com/page1")
browser_screenshot(filename="page1.png")

# Page 2
browser_navigate(url="https://example.com/page2")
browser_screenshot(filename="page2.png")

# Page 3
browser_navigate(url="https://example.com/page3")
element = browser_find(selector=".target")
browser_click(selector=".target")
browser_screenshot(filename="page3-clicked.png")
```

## Troubleshooting

### Browser Connection Lost

**Symptoms:** "failed to get browsing context" errors

**Solution:**
```python
# Relaunch browser
browser_launch(headless=False)
# Then retry operations
```

### Element Not Found

**Symptoms:** "element not found" errors

**Solutions:**
1. Wait for page to fully load
2. Use more generic selectors
3. Take screenshot to verify page state
4. Try alternative selectors

### Timeout Errors

**Symptoms:** Operations timeout after 30s

**Solutions:**
1. Break task into smaller steps
2. Take screenshots between steps
3. Verify page loaded correctly before operations

### Search/Form Submission

**Problem:** Can't press Enter to submit

**Solutions:**
1. Find submit button and click it
2. Navigate directly to result URL
3. Use form action URL with parameters

## Integration with Other Tools

### Combining with cursor-ide-browser

For tasks requiring accessibility snapshots:

1. Use vibium for browser operations
2. Use cursor-ide-browser for snapshot capture
3. Save snapshot to YAML
4. Use snapshot-query for analysis

### Combining with web_search

For research tasks:

1. Use web_search for initial information gathering
2. Use vibium to visit specific URLs found
3. Extract detailed information with browser_find
4. Take screenshots for documentation

## Example Use Cases

### 1. Website Screenshot Collection

```python
urls = ["https://example.com", "https://example.org", "https://example.net"]
for i, url in enumerate(urls):
    browser_navigate(url=url)
    browser_screenshot(filename=f"site-{i+1}.png")
```

### 2. Form Data Entry

```python
browser_navigate(url="https://example.com/form")
browser_type(selector="input[name='name']", text="Test User")
browser_type(selector="input[name='email']", text="test@example.com")
browser_type(selector="input[name='phone']", text="123-456-7890")
browser_screenshot(filename="form-filled.png")
```

### 3. Information Research

```python
# Search for information
browser_navigate(url="https://www.google.com/search?q=your+query")
browser_screenshot(filename="search-results.png")

# Find and click first result
first_result = browser_find(selector=".g h3 a")
browser_click(selector=".g h3 a")
browser_screenshot(filename="result-page.png")
```

## Key Takeaways

1. **EasyOCR for text extraction** - Use EasyOCR + Screenshot + Scroll + Grep for reliable full-page text extraction (see [easyocr-workflow.md](references/easyocr-workflow.md))
2. **Keep selectors simple** - Use basic CSS selectors for reliability
3. **Take screenshots often** - Helps with debugging and documentation
4. **Handle errors gracefully** - Relaunch browser if connection lost
5. **Combine tools** - Use vibium with other browser tools for advanced features
6. **Test selectors first** - Use `browser_find` to verify selectors before clicking/typing
7. **No keyboard actions** - Use clicks instead of key presses
8. **No snapshot logs** - Use cursor-ide-browser for accessibility snapshots
