# Snapshot File Format

Detailed documentation of snapshot log file structure and format.

## File Location

Snapshot files are saved to:
```
C:\Users\{username}\.cursor\browser-logs\snapshot-{timestamp}.log
```

## File Naming

Format: `snapshot-{ISO 8601 timestamp}.log`

Examples:
- `snapshot-2026-01-09T15-00-42-849Z.log`
- `snapshot-2026-01-09T16-30-15-123Z.log`

Timestamp format: `YYYY-MM-DDTHH-MM-SS-millisecondsZ` (UTC)

## File Format

Snapshot files use **YAML format** representing the page's accessibility tree structure.

### Basic Structure

Each element contains:

```yaml
- role: {element role}
  ref: {unique reference identifier}
  name: {optional element name/text}
  children:
    - {child elements}
```

### Field Descriptions

#### `role` (required)
Element role type following WAI-ARIA role specification.

Common values:
- `generic`: Generic container element
- `link`: Link
- `button`: Button
- `textbox`: Text input field
- `img`: Image
- `list`: List container
- `listitem`: List item
- `heading`: Heading
- `pagedescription`: Page description
- And others following WAI-ARIA standards

#### `ref` (required)
Unique reference identifier for the element.

- Format: `ref-{random string}`
- Examples: `ref-zketxgetcys`, `ref-b8rs5tdhk3e`
- **Critical**: This `ref` value is used for all element interactions (click, type, etc.)
- **Page-specific**: Refs are only valid for the current page state
- **Temporary**: Refs change with each new snapshot

#### `name` (optional)
Element name or text content.

Typically contains:
- Button text
- Link text
- Input field labels
- Image alt text
- Other accessibility text (what screen readers would read)

#### `children` (optional)
List of child elements.

- If element has children, this field contains array of child elements
- Child elements follow the same structure
- Represents the accessibility tree hierarchy

## Example

```yaml
- role: generic
  ref: ref-zketxgetcys
  children:
    - role: img
      ref: ref-zd3798voq9
    - role: pagedescription
      name: 欢迎进入 腾讯网,盲人用户使用操作智能引导，请按快捷键Ctrl+Alt+R；阅读详细操作说明请按快捷键Ctrl+Alt+问号键。
      ref: ref-us13t9giybd
      children:
        - role: img
          ref: ref-z0obxnpx1y
    - role: generic
      ref: ref-p37ecs217hp
      children:
        - role: generic
          ref: ref-6z2ca9bkkxf
          children:
            - role: generic
              ref: ref-wuz1gvkset
              children:
                - role: generic
                  ref: ref-62u5o5sunu
                  children:
                    - role: generic
                      ref: ref-r2kez4jj9y
                      children:
                        - role: link
                          ref: ref-mzigpg3ijr
                    - role: generic
                      ref: ref-zhx4wavxy6q
                      children:
                        - role: generic
                          ref: ref-sh2bokrxotn
                          children:
                            - role: textbox
                              ref: ref-b8rs5tdhk3e
                            - role: button
                              name: 搜索
                              ref: ref-b9k8zlttiah
                              children:
                                - role: img
                                  ref: ref-z4ue1duqv2
```

## File Size

- **Simple pages**: Few KB to tens of KB
- **Complex pages** (news portals, SPAs): Can reach 100+ KB
- Example: Tencent homepage snapshot ~88 KB (1590 lines)

## Use Cases

### 1. Element Discovery
Find element references for browser automation:
```yaml
# Search for button in snapshot file
- role: button
  name: 搜索
  ref: ref-b9k8zlttiah
```

### 2. Page Structure Analysis
Understand page hierarchy and element relationships.

### 3. Accessibility Analysis
Check element roles and names for accessibility compliance.

### 4. Historical Comparison
Compare snapshots from different times to track page changes.

## Querying Snapshots

For complete snapshot querying guide, see [references/snapshot-query.md](references/snapshot-query.md).

### Quick Examples

**Command line:**
```bash
# Find element by name
uvx snapshot-query snapshot.log find-name "搜索"

# Find by role
uvx snapshot-query snapshot.log find-role button

# Find by ref
uvx snapshot-query snapshot.log find-ref ref-b9k8zlttiah
```

**MCP tools:**
```javascript
mcp_snapshot-query_find_by_name(
  file_path="snapshot-2026-01-09T15-00-42-849Z.log",
  name="搜索"
)
```

### Using grep/ripgrep

**Windows (PowerShell):**
```powershell
Select-String -Path "snapshot-*.log" -Pattern "搜索"
Select-String -Path "snapshot-*.log" -Pattern "role: button"
```

**Linux/Mac:**
```bash
grep "搜索" snapshot-*.log
grep "role: button" snapshot-*.log
```

### Using Python

```python
import yaml

with open('snapshot.log', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

def find_buttons(items):
    buttons = []
    for item in items:
        if item.get('role') == 'button':
            buttons.append(item)
        if 'children' in item:
            buttons.extend(find_buttons(item['children']))
    return buttons

buttons = find_buttons(data)
for button in buttons:
    print(f"Button: {button.get('name', 'N/A')}, ref: {button.get('ref')}")
```

## Important Notes

1. **Ref Validity**: Refs are only valid for the current page state. After navigation or page changes, get a new snapshot.

2. **File Growth**: Each `browser_snapshot()` call creates a new file. Clean up old logs periodically.

3. **Privacy**: Snapshot files may contain page content. Protect sensitive information.

4. **YAML Parsing**: Use proper YAML parser (e.g., `yaml.safe_load()` in Python) to avoid parsing errors.

5. **Encoding**: Files use UTF-8 encoding to support international characters.
