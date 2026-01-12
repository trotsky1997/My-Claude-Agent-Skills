# AGENTS.md and Hooks Reference

## AGENTS.md (项目指令文件)

### Overview

`AGENTS.md` is a simple alternative to `.cursor/rules/` for project-level instructions. It uses plain Markdown without YAML frontmatter.

### File Locations

- **Project root**: `AGENTS.md` (global instructions)
- **Subdirectories**: `subdir/AGENTS.md` (area-specific guidance)

### Format

```markdown
# Project Instructions

## Development Environment
- Use `pnpm install` to install dependencies
- Run `pnpm start` to start dev server

## Testing
- Run `pnpm test` to execute all tests
- Ensure all tests pass before committing

## Code Style
- Follow ESLint rules
- Use Prettier for formatting
- Use TypeScript for all new files

## Architecture
- Follow the repository pattern
- Keep business logic in service layers
```

### Features

- **Nested support**: Multiple `AGENTS.md` files can exist in subdirectories
- **Combined automatically**: More specific instructions take precedence
- **Simple format**: Plain Markdown, no YAML frontmatter required
- **Auto-loading**: Cursor IDE automatically loads `AGENTS.md` files

### Creating AGENTS.md

```bash
# Create in project root
cat > AGENTS.md << EOF
# Project Instructions

## Code Style
- Use TypeScript
- Follow project conventions

## Architecture
- Repository pattern
- Service layer for business logic
EOF

# Create in subdirectory
mkdir -p backend
cat > backend/AGENTS.md << EOF
# Backend Instructions

## API Development
- Use REST conventions
- Validate all inputs
EOF
```

### When to Use

- Simple project instructions
- Quick setup without complex rules
- Team-wide conventions
- Alternative to `.cursor/rules/` for simpler cases

### Nested Structure

```
project/
  AGENTS.md              # Project-wide instructions
  backend/
    AGENTS.md            # Backend-specific instructions
  frontend/
    AGENTS.md            # Frontend-specific instructions
```

Nested files are combined, with more specific instructions taking precedence.

## Hooks (钩子系统)

### Overview

Hooks allow you to intercept and modify agent behavior at specific lifecycle events. They run custom JavaScript code at defined points in the agent's execution.

### Hook Locations

- **Project hooks**: `.cursor/hooks/`
- **User hooks**: `~/.cursor/hooks/`

### Hook Types

1. **beforeFileEdit**: Executed before agent edits a file
2. **afterFileEdit**: Executed after agent edits a file
3. **beforeShellCommand**: Executed before agent runs a shell command
4. **afterShellCommand**: Executed after agent runs a shell command
5. **stop**: Executed when agent task completes

### Hook Format

```javascript
// .cursor/hooks/afterFileEdit.js
export default async function afterFileEdit(context) {
  const { filePath, content } = context;
  
  // Custom logic
  if (filePath.endsWith('.ts')) {
    // Auto-format, run linter, etc.
    await runLinter(filePath);
  }
  
  // Return modified content or null to keep original
  return content;
}
```

### Hook Context

Each hook receives a `context` object:

**File Edit Hooks**:
```javascript
{
  filePath: "/path/to/file",
  content: "file content",
  workspace: "/path/to/workspace"
}
```

**Shell Command Hooks**:
```javascript
{
  command: "npm install",
  workspace: "/path/to/workspace"
}
```

**Stop Hook**:
```javascript
{
  workspace: "/path/to/workspace",
  taskId: "task-id"
}
```

### Example: Auto-commit after File Edits

```javascript
// .cursor/hooks/afterFileEdit.js
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export default async function afterFileEdit(context) {
  const { filePath } = context;
  
  // Auto-commit changes
  try {
    await execAsync(`git add ${filePath}`);
    await execAsync(`git commit -m "Auto-commit: ${filePath}"`);
  } catch (error) {
    console.error('Auto-commit failed:', error);
  }
  
  return null; // Keep original content
}
```

### Example: Validate Before Shell Commands

```javascript
// .cursor/hooks/beforeShellCommand.js
export default async function beforeShellCommand(context) {
  const { command } = context;
  
  // Block dangerous commands
  const dangerous = ['rm -rf', 'format', 'dd if='];
  if (dangerous.some(cmd => command.includes(cmd))) {
    throw new Error(`Blocked dangerous command: ${command}`);
  }
  
  // Allow command to proceed
  return true;
}
```

### Example: Auto-format After Edits

```javascript
// .cursor/hooks/afterFileEdit.js
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

export default async function afterFileEdit(context) {
  const { filePath, content } = context;
  
  // Auto-format TypeScript/JavaScript files
  if (filePath.endsWith('.ts') || filePath.endsWith('.js')) {
    try {
      await execAsync(`prettier --write ${filePath}`);
      // Read formatted content
      const fs = require('fs').promises;
      const formatted = await fs.readFile(filePath, 'utf-8');
      return formatted;
    } catch (error) {
      console.error('Formatting failed:', error);
    }
  }
  
  return null; // Keep original
}
```

### Creating Hooks

```bash
# Create hook directory
mkdir -p .cursor/hooks

# Create afterFileEdit hook
cat > .cursor/hooks/afterFileEdit.js << 'EOF'
export default async function afterFileEdit(context) {
  const { filePath, content } = context;
  
  // Your logic here
  console.log(`File edited: ${filePath}`);
  
  // Return modified content or null to keep original
  return content;
}
EOF
```

### Hook Return Values

- **File edit hooks**: Return modified content (string) or `null` to keep original
- **Command hooks**: Return `true` to allow, throw error to block
- **Stop hook**: No return value needed

### Best Practices

1. **Keep hooks lightweight**: Fast execution, minimal overhead
2. **Handle errors gracefully**: Don't break agent workflow
3. **Use for automation**: Formatting, linting, auto-commit
4. **Test thoroughly**: Verify hooks work as expected
5. **Document hooks**: Add comments explaining purpose

### Common Use Cases

- **Auto-formatting**: Format code after edits
- **Auto-commit**: Commit changes automatically
- **Security**: Block dangerous commands
- **Integration**: Sync with external tools
- **Logging**: Track agent actions
