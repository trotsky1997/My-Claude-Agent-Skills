# Vibium Limitations and Workarounds

This document explains the specific limitations encountered when using Vibium for web data collection and how to work around them.

## Limitation 1: Cannot Directly Extract Full Page Text Content

### What It Means

Vibium's `browser_find` tool can only return basic element information:
- `tag`: HTML tag name (e.g., "h1", "p", "a")
- `text`: **Limited text content** - often truncated or empty
- `box`: Element position and size (x, y, width, height)

### Example

```python
# Try to extract paragraph text
element = browser_find(selector="p")
# Returns: tag=p, text="This domain is for use...", box={x:207, y:183, w:622, h:40}
```

**Problem:** The `text` field is often:
- Truncated (cut off mid-sentence)
- Empty for complex elements
- Only shows visible text, not hidden content
- Doesn't capture nested text properly

### Why This Happens

Vibium uses browser automation APIs that focus on element location and basic properties, not full text extraction. The text field is a convenience feature, not a comprehensive extraction tool.

### Workarounds

1. **EasyOCR + Screenshot + Scroll (RECOMMENDED - One-time solution):**
   
   This is the most reliable method for extracting full text content:
   
   ```python
   # 1. Take screenshot of current viewport
   browser_screenshot(filename="page-screenshot.png")
   
   # 2. Use EasyOCR to extract all text from screenshot
   # EasyOCR can handle multiple languages and is very accurate
   import easyocr
   reader = easyocr.Reader(['en', 'ch_sim'])  # English and Chinese
   results = reader.readtext('page-screenshot.png')
   # Returns: [[[coordinates], text, confidence], ...]
   
   # 3. Extract text and search with grep
   all_text = '\n'.join([result[1] for result in results])
   
   # 4. Use grep to search for specific content
   import re
   matches = re.findall(r'pattern', all_text)
   
   # 5. Scroll if content not found in current viewport
   # Note: Vibium doesn't have scroll, but can:
   # - Navigate to anchor links
   # - Use cursor-ide-browser for scrolling
   # - Take multiple screenshots at different scroll positions
   ```
   
   **Complete workflow:**
   ```python
   def extract_text_from_page(url, search_pattern=None, max_scrolls=5):
       """Extract all text from a page using OCR and scrolling"""
       import easyocr
       import re
       
       reader = easyocr.Reader(['en', 'ch_sim', 'ar'])  # Add languages as needed
       all_text = []
       
       # Initial screenshot
       browser_navigate(url=url)
       browser_screenshot(filename="screenshot-0.png")
       
       for i in range(max_scrolls):
           # OCR current screenshot
           results = reader.readtext(f'screenshot-{i}.png')
           page_text = '\n'.join([r[1] for r in results])
           all_text.append(page_text)
           
           # Check if search pattern found
           if search_pattern and re.search(search_pattern, page_text, re.IGNORECASE):
               break
           
           # Scroll down (using cursor-ide-browser or page navigation)
           # Take next screenshot
           browser_screenshot(filename=f"screenshot-{i+1}.png")
       
       # Combine all text
       full_text = '\n'.join(all_text)
       
       # Search with grep if pattern provided
       if search_pattern:
           matches = re.findall(search_pattern, full_text, re.IGNORECASE)
           return matches, full_text
       
       return full_text
   ```
   
   **Advantages:**
   - Works with any webpage (even JavaScript-heavy sites)
   - Extracts all visible text (including images with text)
   - Language-agnostic (supports 80+ languages)
   - Very accurate (EasyOCR is state-of-the-art)
   - No dependency on page structure or selectors
   
   **Installation:**
   ```bash
   pip install easyocr
   # First run will download models (~500MB per language)
   ```

2. **Combine with cursor-ide-browser:**
   ```python
   # Use vibium for navigation
   browser_navigate(url="https://example.com")
   
   # Use cursor-ide-browser for snapshot
   snapshot = browser_snapshot()  # Returns full accessibility tree with text
   # Save snapshot to YAML file
   # Use snapshot-query to extract text
   ```

3. **Use web_search tool:**
   - For research tasks, `web_search` provides structured information
   - More reliable for getting complete text content

4. **Extract multiple small elements:**
   ```python
   # Instead of one large element, find multiple small ones
   headings = browser_find(selector="h1, h2, h3")
   paragraphs = browser_find(selector="p")
   # Combine results manually
   ```

## Limitation 2: Complex Page Elements Are Hard to Locate

### What It Means

Many CSS selectors and element patterns don't work reliably:
- Pseudo-selectors like `:has-text()`, `:contains()`
- Complex combinators
- Dynamic selectors based on text content
- Elements that require JavaScript to render

### Examples of What Doesn't Work

```python
# ❌ These fail:
browser_find(selector=":has-text('Example')")  # Script exception
browser_find(selector="div:contains('text')")  # Not supported
browser_find(selector="[data-testid='result']")  # May not find if dynamically loaded
browser_find(selector="div > p:first-child")  # Complex combinators may fail
```

### Why This Happens

1. **Limited CSS selector support:** Vibium uses browser's native selector engine, which may not support all CSS3+ features
2. **Timing issues:** Dynamic content loads after page load, elements may not exist when searched
3. **JavaScript-rendered content:** Some elements only appear after JS execution

### Workarounds

1. **Use simple, reliable selectors:**
   ```python
   # ✅ These work:
   browser_find(selector="h1")  # Simple element
   browser_find(selector=".class-name")  # Class selector
   browser_find(selector="input[name='q']")  # Attribute selector
   browser_find(selector="textarea[name='q'], input[name='q']")  # Multiple selectors
   ```

2. **Wait for page load:**
   - Take screenshot first to verify page loaded
   - Navigate, then wait a moment before finding elements

3. **Try multiple selector variations:**
   ```python
   # Try different approaches
   element1 = browser_find(selector="input[name='search']")
   if not element1:
       element2 = browser_find(selector="input[type='text']")
   if not element2:
       element3 = browser_find(selector=".search-input")
   ```

4. **Use more generic selectors:**
   ```python
   # Instead of specific, use generic and filter results
   all_inputs = browser_find(selector="input")
   # Manually identify the right one from results
   ```

5. **Combine with snapshot-query:**
   - Get accessibility snapshot (via cursor-ide-browser)
   - Use snapshot-query's text-based search: `find_by_text("Example")`
   - More flexible than CSS selectors

## Limitation 3: Manual Information Organization Required

### What It Means

Vibium returns structured data, but you need to:
- Manually combine multiple `browser_find` results
- Extract relevant information from element properties
- Organize data into final format
- Cross-reference multiple sources

### Example Workflow

```python
# Step 1: Navigate and find elements
browser_navigate(url="https://example.com")
heading = browser_find(selector="h1")  # Returns: tag=h1, text="Example", box={...}
link = browser_find(selector="a")  # Returns: tag=a, text="Learn more", box={...}

# Step 2: Extract information manually
heading_text = heading.text  # "Example"
link_text = link.text  # "Learn more"

# Step 3: Organize into final format
result = {
    "title": heading_text,
    "link": link_text
}
```

### Why This Happens

Vibium is a **browser automation tool**, not a **data extraction framework**:
- It focuses on interaction (click, type, navigate)
- Text extraction is secondary
- No built-in data parsing or organization
- Returns raw element data, not structured information

### Workarounds

1. **Use web_search for structured data:**
   ```python
   # web_search returns organized information
   results = web_search("query")
   # Already structured, no manual organization needed
   ```

2. **Combine tools:**
   ```python
   # Use vibium to navigate
   browser_navigate(url="https://example.com")
   
   # Use cursor-ide-browser to get full snapshot
   snapshot = browser_snapshot()
   
   # Use snapshot-query to extract specific information
   headings = snapshot_query.find_by_role("heading")
   links = snapshot_query.find_by_role("link")
   
   # Organize programmatically
   ```

3. **Create extraction scripts:**
   - Write Python scripts to parse vibium results
   - Use regex or parsing libraries to extract patterns
   - Organize data automatically

4. **Use screenshots for visual verification:**
   - Take screenshots at key points
   - Manually verify extracted information
   - Useful for quality control

## Real-World Example: Collecting Information

### Task: Find all children's names of a public figure

**Using only Vibium (limited):**
```python
# 1. Navigate to Wikipedia
browser_navigate(url="https://en.wikipedia.org/wiki/Person")

# 2. Try to find information
# Problem: Can't easily extract full text from infobox
infobox = browser_find(selector=".infobox")
# Returns: tag=table, text="...", box={...}
# Text is truncated, can't see full content

# 3. Need to manually search multiple pages
# 4. Take screenshots for manual review
# 5. Manually compile information
```

**Better approach (combining tools):**
```python
# 1. Use web_search for initial structured data
results = web_search("Person children names")
# Returns: Complete list with names, dates, etc.

# 2. Use vibium to verify specific pages
browser_navigate(url="https://en.wikipedia.org/wiki/Person")
browser_screenshot(filename="verification.png")

# 3. Use cursor-ide-browser for detailed extraction
snapshot = browser_snapshot()
# Full accessibility tree with all text

# 4. Use snapshot-query to find specific information
children_section = snapshot_query.find_by_text("children")
```

## Summary

| Limitation | Impact | Best Workaround |
|------------|--------|-----------------|
| **Cannot extract full text** | Can't get complete page content | **EasyOCR + Screenshot + Scroll (recommended)** or cursor-ide-browser snapshot |
| **Complex selectors fail** | Hard to locate specific elements | Use simple selectors, try multiple variations |
| **Manual organization needed** | Time-consuming data compilation | Use web_search for structured data, combine tools, or EasyOCR + grep |

## Best Practice: Tool Combination

For comprehensive web data collection:

1. **Use web_search** for initial structured information
2. **Use vibium** for navigation and interaction
3. **Use cursor-ide-browser** for detailed text extraction
4. **Use snapshot-query** for flexible element finding
5. **Take screenshots** for verification and documentation

This multi-tool approach leverages each tool's strengths while working around their limitations.
