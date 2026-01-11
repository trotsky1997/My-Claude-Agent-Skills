# Complete Tool Reference

All available browser automation tools with full parameter details.

## Navigation Tools

### browser_navigate
Navigate to a URL.

**Parameters:**
- `url` (string, required): Target URL
- `viewId` (string, optional): Browser tab ID. Omit to use last interacted tab
- `position` (string, optional): 
  - `"active"` (default): Open in current editor group
  - `"side"`: Open in side panel (use when user mentions "side", "beside", "side panel")

**Example:**
```javascript
browser_navigate(url="https://example.com", position="side")
```

### browser_navigate_back
Navigate back to previous page.

**Parameters:**
- `viewId` (string, optional): Browser tab ID

**Example:**
```javascript
browser_navigate_back()
```

## Page Information Tools

### browser_snapshot
Capture accessibility snapshot of current page. **Required before any element interaction.**

**Parameters:**
- `viewId` (string, optional): Browser tab ID

**Returns:**
- Accessibility tree structure
- Element references (`ref`) for all interactive elements
- Element roles, names, and states
- Snapshot also saved to local log file

**Snapshot Log Files:**
- Location: `C:\Users\{username}\.cursor\browser-logs\snapshot-{timestamp}.log`
- Format: YAML accessibility tree
- Filename: `snapshot-{ISO 8601 timestamp}.log`

**Example:**
```javascript
browser_snapshot()
```

### browser_take_screenshot
Capture page screenshot.

**Parameters:**
- `type` (string, optional): Image format, default `"png"`
- `filename` (string, optional): Save filename. Default: `page-{timestamp}.{png|jpeg}`
- `element` (string, optional): Element description (for element screenshot)
- `ref` (string, optional): CSS selector (for element screenshot)
- `fullPage` (boolean, optional): Capture full scrollable page, default `false`
- `viewId` (string, optional): Browser tab ID

**Example:**
```javascript
browser_take_screenshot(fullPage=true)
browser_take_screenshot(element="Login form", ref="form#login")
```

### browser_console_messages
Get all console messages from page.

**Parameters:**
- `viewId` (string, optional): Browser tab ID

**Returns:**
- All console messages (errors, warnings, logs)

**Example:**
```javascript
browser_console_messages()
```

### browser_network_requests
Get all network requests since page load.

**Parameters:**
- `viewId` (string, optional): Browser tab ID

**Returns:**
- Network request details (URL, method, status, response)

**Example:**
```javascript
browser_network_requests()
```

## Element Interaction Tools

### browser_click
Click a page element.

**Parameters:**
- `element` (string, required): Element description (for permission)
- `ref` (string, required): Element reference from snapshot
- `doubleClick` (boolean, optional): Double click, default `false`
- `button` (string, optional): Mouse button, default `"left"`
- `modifiers` (array, optional): Modifier keys (e.g., `["Control", "Shift"]`)
- `viewId` (string, optional): Browser tab ID

**Example:**
```javascript
browser_click(element="Login button", ref="ref-login-btn", doubleClick=false)
```

### browser_type
Type text into editable element.

**Parameters:**
- `element` (string, required): Element description (for permission)
- `ref` (string, required): Element reference from snapshot
- `text` (string, required): Text to type
- `submit` (boolean, optional): Submit (press Enter), default `false`
- `slowly` (boolean, optional): Type character by character (for key handlers), default `false`
- `viewId` (string, optional): Browser tab ID

**Example:**
```javascript
// Normal typing
browser_type(element="Username", ref="ref-username", text="myusername")

// Type and submit
browser_type(element="Search", ref="ref-search", text="query", submit=true)

// Character by character (triggers key events)
browser_type(element="Code editor", ref="ref-editor", text="console.log('hello')", slowly=true)
```

### browser_hover
Hover over element.

**Parameters:**
- `element` (string, required): Element description (for permission)
- `ref` (string, required): Element reference from snapshot
- `viewId` (string, optional): Browser tab ID

**Example:**
```javascript
browser_hover(element="Menu item", ref="ref-menu-item")
```

### browser_select_option
Select option in dropdown.

**Parameters:**
- `element` (string, required): Element description (for permission)
- `ref` (string, required): Element reference from snapshot
- `values` (array, required): Values to select (single or multiple)
- `viewId` (string, optional): Browser tab ID

**Example:**
```javascript
// Single select
browser_select_option(element="Country", ref="ref-country", values=["USA"])

// Multi-select
browser_select_option(element="Tags", ref="ref-tags", values=["tag1", "tag2"])
```

### browser_press_key
Press keyboard key.

**Parameters:**
- `key` (string, required): Key name (e.g., `"ArrowLeft"` or character `"a"`)
- `viewId` (string, optional): Browser tab ID

**Example:**
```javascript
browser_press_key(key="ArrowLeft")
browser_press_key(key="a")
// For key combinations, call multiple times
browser_press_key(key="Control")
browser_press_key(key="c")
```

## Synchronization Tools

### browser_wait_for
Wait for text to appear/disappear or wait for time.

**Parameters:**
- `time` (number, optional): Wait time in seconds
- `text` (string, optional): Text to wait for
- `textGone` (string, optional): Text to wait for to disappear
- `viewId` (string, optional): Browser tab ID

**Note:** At least one of `time`, `text`, or `textGone` must be provided.

**Example:**
```javascript
browser_wait_for(text="Loading complete")
browser_wait_for(textGone="Loading...")
browser_wait_for(time=3)
browser_wait_for(text="Page loaded", time=5)
```

## Window Management Tools

### browser_resize
Resize browser window.

**Parameters:**
- `width` (number, required): Window width
- `height` (number, required): Window height
- `viewId` (string, optional): Browser tab ID

**Example:**
```javascript
browser_resize(width=1920, height=1080)
```

### browser_tabs
List, create, close, or select browser tabs.

**Parameters:**
- `action` (string, required): Operation type
  - `"list"`: List all tabs
  - `"new"`: Create new tab
  - `"close"`: Close tab
  - `"select"`: Select tab
- `index` (number, optional): 
  - For `"select"`: Required, tab index to select
  - For `"close"`: Optional, default closes current tab
- `position` (string, optional): Only for `"new"` action
  - `"active"` (default): Open in current editor group
  - `"side"`: Open in side panel

**Example:**
```javascript
browser_tabs(action="list")
browser_tabs(action="new", position="side")
browser_tabs(action="select", index=0)
browser_tabs(action="close")
```
