# Examples and Patterns

Common browser automation patterns and complete examples.

## Basic Patterns

### Login Flow

```javascript
// 1. Navigate to login page
browser_navigate(url="https://example.com/login")

// 2. Get snapshot to find element refs
browser_snapshot()

// 3. Fill username (ref from snapshot)
browser_type(element="Username input", ref="ref-username", text="myusername")

// 4. Fill password (ref from snapshot)
browser_type(element="Password input", ref="ref-password", text="mypassword")

// 5. Click login button (ref from snapshot)
browser_click(element="Login button", ref="ref-login-btn")

// 6. Wait for login to complete
browser_wait_for(text="Welcome")

// 7. Verify with screenshot
browser_take_screenshot(filename="login-success.png")
```

### Search and Extract

```javascript
// Navigate and search
browser_navigate(url="https://example.com")
browser_snapshot()

// Find search box ref from snapshot, then type and submit
browser_type(element="Search box", ref="ref-search", text="query", submit=true)

// Wait for results
browser_wait_for(text="Results")

// Capture results
browser_take_screenshot(filename="results.png")
browser_snapshot()  // Get new snapshot with results
```

### Form Filling

```javascript
browser_navigate(url="https://example.com/form")
browser_snapshot()

// Fill multiple fields
browser_type(element="Name", ref="ref-name", text="John Doe")
browser_type(element="Email", ref="ref-email", text="john@example.com")
browser_select_option(element="Country", ref="ref-country", values=["USA"])
browser_type(element="Message", ref="ref-message", text="Hello world")

// Submit form
browser_click(element="Submit", ref="ref-submit")
browser_wait_for(text="Thank you")
```

## Advanced Patterns

### Multi-Tab Workflow

```javascript
// Open first tab
browser_navigate(url="https://example.com/page1")
browser_snapshot()
browser_click(element="Link", ref="ref-link1")

// Open second tab in side panel
browser_tabs(action="new", position="side")
browser_navigate(url="https://example.com/page2", viewId="new-tab-id")

// Switch between tabs
browser_tabs(action="select", index=0)
browser_snapshot()  // Work with first tab

browser_tabs(action="select", index=1)
browser_snapshot()  // Work with second tab
```

### Dynamic Content Handling

```javascript
browser_navigate(url="https://example.com/dynamic")
browser_snapshot()

// Click button that loads content
browser_click(element="Load more", ref="ref-load-more")

// Wait for new content
browser_wait_for(textGone="Loading...")
browser_wait_for(text="New content loaded")

// Get new snapshot with updated elements
browser_snapshot()

// Interact with new elements
browser_click(element="New button", ref="ref-new-button")
```

### Error Debugging

```javascript
browser_navigate(url="https://example.com")
browser_snapshot()

// Check for console errors
const consoleMessages = browser_console_messages()
// Look for errors in output

// Check network requests
const networkRequests = browser_network_requests()
// Look for failed requests

// Take screenshot for visual debugging
browser_take_screenshot(filename="debug.png")
```

### Character-by-Character Input

For elements that require key event handlers:

```javascript
browser_snapshot()
browser_type(
  element="Code editor",
  ref="ref-editor",
  text="console.log('hello')",
  slowly=true  // Types character by character
)
```

## Integration with Snapshot Query

Combine with snapshot-query for element discovery. See [references/snapshot-query.md](references/snapshot-query.md) for complete guide.

**Basic pattern:**
```javascript
// 1. Get snapshot
browser_snapshot()
// Snapshot saved to: C:\Users\{username}\.cursor\browser-logs\snapshot-{timestamp}.log

// 2. Query snapshot to find element refs
const result = mcp_snapshot-query_find_by_name(
  file_path="snapshot-2026-01-09T15-00-42-849Z.log",
  name="搜索"
)

// 3. Use ref from query result
browser_click(element="搜索", ref=result.ref)
```

**Using BM25 for better matching:**
```javascript
browser_snapshot()
const results = mcp_snapshot-query_find_by_name_bm25(
  file_path="snapshot.log",
  name="submit button",
  top_k=1
)
browser_click(element="Submit", ref=results[0].ref)
```

## Best Practices

### Always Snapshot Before Interaction

```javascript
// ❌ Wrong: No snapshot
browser_navigate(url="https://example.com")
browser_click(element="Button", ref="ref-unknown")  // Ref not available

// ✅ Correct: Snapshot first
browser_navigate(url="https://example.com")
browser_snapshot()  // Get refs
browser_click(element="Button", ref="ref-from-snapshot")
```

### Wait for Dynamic Content

```javascript
// ❌ Wrong: No wait
browser_click(element="Load", ref="ref-load")
browser_click(element="Result", ref="ref-result")  // May not exist yet

// ✅ Correct: Wait for content
browser_click(element="Load", ref="ref-load")
browser_wait_for(text="Content loaded")
browser_snapshot()  // Get new refs
browser_click(element="Result", ref="ref-result")
```

### Handle Page Changes

```javascript
// After navigation or page change, get new snapshot
browser_navigate(url="https://example.com/page1")
browser_snapshot()
browser_click(element="Link", ref="ref-link")

// Page changed, get new snapshot
browser_snapshot()  // New refs needed
browser_click(element="New page button", ref="ref-new-button")
```

### Error Handling Pattern

```javascript
try {
  browser_navigate(url="https://example.com")
  browser_snapshot()
  browser_click(element="Button", ref="ref-button")
  browser_wait_for(text="Success")
} catch (error) {
  // Debug on failure
  browser_console_messages()
  browser_take_screenshot(filename="error.png")
  throw error
}
```
