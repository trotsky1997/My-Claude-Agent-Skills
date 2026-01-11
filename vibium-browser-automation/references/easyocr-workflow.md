# EasyOCR + Screenshot + Scroll Workflow

**The Ultimate Solution for Text Extraction with Vibium**

This workflow solves all text extraction limitations by using OCR (Optical Character Recognition) on screenshots, enabling full-page text extraction regardless of page structure.

## Overview

**Strategy:**
1. Take screenshots of the webpage (multiple if needed for scrolling)
2. Use EasyOCR to extract all visible text from screenshots
3. Use grep/regex to search for specific content in OCR text
4. Scroll page and repeat if content spans multiple viewports

## Installation

```bash
pip install easyocr
# First run will download models (~500MB per language)
```

## Basic Implementation

### Simple Single Screenshot

```python
import easyocr
import re

# 1. Navigate and screenshot with vibium
browser_navigate(url="https://example.com")
browser_screenshot(filename="page.png")

# 2. Initialize EasyOCR reader
reader = easyocr.Reader(['en', 'ch_sim'])  # Add languages as needed

# 3. Extract text from screenshot
results = reader.readtext('page.png')
# Returns: [[[x1,y1],[x2,y2],[x3,y3],[x4,y4]], text, confidence], ...]

# 4. Extract just the text
all_text = '\n'.join([result[1] for result in results])

# 5. Search with grep/regex
pattern = r'your.*pattern'
matches = re.findall(pattern, all_text, re.IGNORECASE)

print("Found matches:", matches)
print("Full text:", all_text)
```

## Advanced: Multi-Scroll Implementation

Since Vibium doesn't have direct scroll support, we use workarounds:

### Method 1: Using Cursor IDE Browser for Scrolling

```python
import easyocr
import re
from cursor_ide_browser import browser_scroll, browser_snapshot

def extract_text_with_scrolling(url, search_pattern=None, scroll_pages=5):
    """Extract text from a long page by scrolling"""
    reader = easyocr.Reader(['en', 'ch_sim'])
    all_text_parts = []
    
    # Navigate with vibium
    browser_navigate(url=url)
    
    for i in range(scroll_pages):
        # Take screenshot with vibium
        browser_screenshot(filename=f"screenshot-{i}.png")
        
        # OCR current viewport
        results = reader.readtext(f'screenshot-{i}.png')
        page_text = '\n'.join([r[1] for r in results])
        all_text_parts.append(page_text)
        
        # Check if we found what we're looking for
        if search_pattern:
            if re.search(search_pattern, page_text, re.IGNORECASE):
                print(f"Found pattern at scroll position {i}")
                break
        
        # Scroll using cursor-ide-browser (if available)
        # Or use page down key simulation
        browser_scroll(down=True, pixels=800)  # Adjust as needed
        
        # Wait for content to load
        import time
        time.sleep(0.5)
    
    # Combine all text
    full_text = '\n\n--- PAGE BREAK ---\n\n'.join(all_text_parts)
    
    # Search with grep
    if search_pattern:
        matches = re.findall(search_pattern, full_text, re.IGNORECASE)
        return matches, full_text
    
    return full_text
```

### Method 2: Using Page Anchors/URLs

For pages with anchors or pagination:

```python
def extract_text_from_paginated_page(base_url, max_pages=10):
    """Extract text from paginated content"""
    reader = easyocr.Reader(['en', 'ch_sim'])
    all_text = []
    
    for page in range(1, max_pages + 1):
        # Navigate to each page
        url = f"{base_url}?page={page}"
        browser_navigate(url=url)
        browser_screenshot(filename=f"page-{page}.png")
        
        # OCR
        results = reader.readtext(f'page-{page}.png')
        page_text = '\n'.join([r[1] for r in results])
        
        # Check if page has content
        if len(page_text.strip()) < 10:  # Empty page threshold
            break
        
        all_text.append(page_text)
    
    return '\n\n--- PAGE BREAK ---\n\n'.join(all_text)
```

### Method 3: JavaScript Scroll (if page supports)

For pages that respond to URL hash changes or have "Load More" buttons:

```python
def scroll_with_javascript():
    """Scroll page using JavaScript (via cursor-ide-browser if available)"""
    # This requires evaluating JavaScript on the page
    # May need cursor-ide-browser's evaluate_script functionality
    pass
```

## Real-World Example: Finding Specific Information

### Task: Find all children's names from a Wikipedia page

```python
import easyocr
import re

def find_children_names(url):
    """Find children names from a Wikipedia biography page"""
    reader = easyocr.Reader(['en', 'ch_sim', 'ar'])  # Support multiple languages
    
    # Navigate to page
    browser_navigate(url=url)
    browser_screenshot(filename="wikipedia-page.png")
    
    # OCR entire page
    results = reader.readtext('wikipedia-page.png')
    all_text = '\n'.join([r[1] for r in results])
    
    # Search for children section
    # Pattern 1: "Children:" or "Children" followed by names
    children_pattern = r'(?:Children|Sons|Daughters)[:\s]+(.*?)(?:\n\n|\n[A-Z]|$)'
    
    # Pattern 2: Look for bullet points or numbered lists with names
    name_list_pattern = r'(?:^|\n)[•\-\d+\.]\s*([A-Z][a-z]+\s+[A-Z][a-z]+)'
    
    # Try multiple patterns
    matches1 = re.findall(children_pattern, all_text, re.MULTILINE | re.IGNORECASE)
    matches2 = re.findall(name_list_pattern, all_text)
    
    print("Potential children names found:")
    print("Method 1:", matches1)
    print("Method 2:", matches2)
    
    # Also search for specific name patterns
    # E.g., "Firstname Lastname" where Lastname matches the parent
    parent_lastname = "Khamenei"  # Example
    full_name_pattern = rf'([A-Z][a-z]+)\s+{parent_lastname}'
    full_names = re.findall(full_name_pattern, all_text)
    
    return {
        'children_section': matches1,
        'name_list': matches2,
        'full_names': full_names,
        'full_text': all_text
    }

# Usage
result = find_children_names("https://en.wikipedia.org/wiki/Ali_Khamenei")
print(result)
```

## Optimizing OCR Performance

### Language Selection

Choose only languages you need to reduce model size and improve speed:

```python
# For English only
reader = easyocr.Reader(['en'])

# For Chinese and English
reader = easyocr.Reader(['en', 'ch_sim'])

# For multilingual pages
reader = easyocr.Reader(['en', 'ch_sim', 'ar', 'fa'])  # English, Chinese, Arabic, Persian
```

### Confidence Threshold

Filter low-confidence results:

```python
results = reader.readtext('page.png')
# Filter by confidence (0-1 scale)
high_confidence_text = [
    r[1] for r in results 
    if r[2] > 0.7  # Only keep results with >70% confidence
]
```

### Region of Interest (ROI)

For better accuracy, focus on specific areas:

```python
# After taking full screenshot, you can crop to specific regions
from PIL import Image

img = Image.open('page.png')
# Crop to specific region (left, top, right, bottom)
roi = img.crop((100, 200, 800, 1000))  # Example coordinates
roi.save('roi.png')

# OCR only the ROI
results = reader.readtext('roi.png')
```

## Grep Patterns for Common Tasks

### Finding Names

```python
# Full names (Firstname Lastname)
name_pattern = r'[A-Z][a-z]+\s+[A-Z][a-z]+'

# Names with titles
titled_name = r'(?:Mr|Mrs|Ms|Dr|Prof)\.?\s+[A-Z][a-z]+\s+[A-Z][a-z]+'
```

### Finding Dates

```python
# Various date formats
date_pattern = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{2}-\d{2}'
```

### Finding Email Addresses

```python
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
```

### Finding Phone Numbers

```python
# Various phone formats
phone_pattern = r'(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
```

## Complete Workflow Example

```python
import easyocr
import re
import os
from pathlib import Path

class VibiumOCRExtractor:
    """Complete OCR-based text extraction workflow"""
    
    def __init__(self, languages=['en', 'ch_sim']):
        self.reader = easyocr.Reader(languages, gpu=False)  # Set gpu=True if available
        self.screenshot_dir = Path("screenshots")
        self.screenshot_dir.mkdir(exist_ok=True)
    
    def extract_page_text(self, url, scroll_positions=None):
        """Extract text from a single page or multiple scroll positions"""
        browser_navigate(url=url)
        
        if scroll_positions is None:
            # Single screenshot
            screenshot_path = self.screenshot_dir / "page.png"
            browser_screenshot(filename=str(screenshot_path))
            return self._ocr_screenshot(screenshot_path)
        else:
            # Multiple screenshots
            all_text = []
            for i, pos in enumerate(scroll_positions):
                # Navigate to position (if URL-based) or scroll
                screenshot_path = self.screenshot_dir / f"page-{i}.png"
                browser_screenshot(filename=str(screenshot_path))
                text = self._ocr_screenshot(screenshot_path)
                all_text.append(f"--- Position {i} ---\n{text}")
            return '\n\n'.join(all_text)
    
    def _ocr_screenshot(self, image_path):
        """OCR a single screenshot"""
        results = self.reader.readtext(str(image_path))
        return '\n'.join([r[1] for r in results])
    
    def search_in_text(self, text, pattern, case_sensitive=False):
        """Search for pattern in OCR text"""
        flags = 0 if case_sensitive else re.IGNORECASE
        matches = re.findall(pattern, text, flags)
        return matches
    
    def find_specific_info(self, url, search_patterns):
        """Find specific information using multiple patterns"""
        text = self.extract_page_text(url)
        
        results = {}
        for name, pattern in search_patterns.items():
            matches = self.search_in_text(text, pattern)
            results[name] = matches
        
        return {
            'matches': results,
            'full_text': text
        }

# Usage
extractor = VibiumOCRExtractor(['en', 'ch_sim'])

# Find specific information
patterns = {
    'names': r'[A-Z][a-z]+\s+Khamenei',
    'dates': r'\d{4}',
    'locations': r'[A-Z][a-z]+,\s+[A-Z][a-z]+'
}

result = extractor.find_specific_info(
    "https://en.wikipedia.org/wiki/Ali_Khamenei",
    patterns
)

print("Found matches:", result['matches'])
```

## Advantages of This Approach

1. **Works with any webpage** - Even JavaScript-heavy or dynamically loaded content
2. **Language agnostic** - Supports 80+ languages
3. **No selector dependency** - Doesn't rely on page structure
4. **Captures all visible text** - Including text in images, iframes, etc.
5. **Handles complex layouts** - Works with tables, columns, etc.
6. **Very accurate** - EasyOCR is state-of-the-art OCR technology

## Limitations

1. **Requires installation** - EasyOCR needs to be installed and models downloaded
2. **Slower than DOM extraction** - OCR takes time, especially for large images
3. **Memory usage** - OCR models can be large (hundreds of MB per language)
4. **Screenshot quality matters** - Low resolution or poor quality images reduce accuracy
5. **Scrolling support** - Vibium doesn't have native scroll, need workarounds

## Best Practices

1. **Reuse reader instance** - Don't create new reader for each screenshot (expensive)
2. **Choose appropriate languages** - Only load languages you need
3. **Use confidence thresholding** - Filter low-confidence results
4. **Cache screenshots** - Save screenshots for debugging and reprocessing
5. **Combine with other methods** - Use OCR for complex cases, DOM extraction for simple ones
