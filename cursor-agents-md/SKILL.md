---

name: cursor-agents-md

description: Guide for creating effective AGENTS.md files for Cursor. Use when (1) Creating new AGENTS.md files in project root, (2) Improving existing agent instructions, (3) Setting up project-specific coding guidelines, (4) Defining code style and architecture rules, (5) Writing simple agent instruction files as alternative to .cursor/rules, or any task related to Cursor AGENTS.md configuration.

metadata:
  short-description: Create or update a agents.md for cursor

---

# Cursor AGENTS.md Guide

Guide for creating effective AGENTS.md files that define project instructions for Cursor AI assistant.

> **⚠️ Important:** Write reminders in `AGENTS.md` to urge the agents to read `cursor-agents-md` skills every time before write or update `AGENTS.md`, e.g.,

   ```markdown

   > **⚠️ Important:** You must read `cursor-agents-md` skills every time before write or update this `AGENTS.md`.

   ```

> **⚠️ Important:** Before creating or updating AGENTS.md files, always consult the official Cursor documentation using `@Cursor` to ensure alignment with the latest standards, features, and limitations. Cursor's functionality and requirements may change over time, so verifying against official documentation ensures your AGENTS.md files work correctly.

## About AGENTS.md

AGENTS.md is a simple markdown file for defining agent instructions. Place it in the project root directory as an alternative to `.cursor/rules`, suitable for simple, straightforward use cases.

Unlike Project Rules, AGENTS.md is a plain markdown file without metadata or complex configuration. It's ideal for projects that only need simple, readable instructions without the additional overhead of structured rules.

### Important Limitations

- **Location:** AGENTS.md must be placed at the project root directory (not in subdirectories)
- **Scope:** Instructions apply globally across the entire project
- **Quantity:** Only one AGENTS.md file is supported per project
- **Complexity:** For more complex or scoped rules, use `.cursor/rules` directory instead, which supports multiple rule files with specific scopes and metadata configurations

## Core Principles

Effective AGENTS.md files follow these principles:

1. **Simple structure** - Plain markdown with clear sections, no YAML frontmatter
2. **Code examples over explanations** - Show what good output looks like with real snippets
3. **Be specific about stack** - Include versions and key dependencies, not just tool names
4. **Organize by topic** - Use clear headings like Code Style, Architecture, Testing
5. **Keep it concise** - Focus on essential project-specific rules

## File Structure

AGENTS.md should be:

- **Located in project root directory only** (not in subdirectories)
- Plain markdown file with no YAML frontmatter
- Organized with clear section headings
- Simple and readable, avoiding complex configuration
- Single file per project (global scope)

### When to Use AGENTS.md vs .cursor/rules

**Use AGENTS.md when:**

- You need simple, global project instructions
- All rules apply to the entire project
- You want a single, easy-to-read file
- No need for scoped or conditional rules

**Use .cursor/rules when:**

- You need multiple rule files with different scopes
- Rules should apply to specific directories or file patterns
- You need metadata or complex configuration
- You want conditional or context-specific rules

## Example: Basic AGENTS.md

```markdown
# Project Instructions

## Code Style
- Use TypeScript for all new files
- Prefer functional components in React
- Use snake_case for database columns
- Follow ESLint configuration in `.eslintrc.js`
- Maximum line length: 100 characters

## Architecture
- Follow the repository pattern
- Keep business logic in service layers
- Controllers should only handle HTTP requests/responses
- Use dependency injection for all services

## Testing
- Write unit tests for all service methods
- Use Jest for testing framework
- Aim for 80% code coverage minimum
- Place tests in `__tests__` directories adjacent to source files

## File Structure
- `src/` - Application source code
- `tests/` - Integration and E2E tests
- `docs/` - Documentation files
- `config/` - Configuration files

## Commands
- Build: `npm run build`
- Test: `npm test`
- Lint: `npm run lint --fix`
- Format: `prettier --write "src/**/*.{ts,tsx}"`

## Boundaries
- Never commit secrets or API keys
- Don't modify `node_modules/` or `vendor/` directories
- Ask before changing database schema
- Don't remove existing tests, even if they're failing
```

## Common Sections

### Code Style

Define coding standards, naming conventions, and formatting rules:

- Language preferences (TypeScript vs JavaScript)
- Naming conventions (camelCase, snake_case, etc.)
- Formatting rules (indentation, line length, etc.)
- Import/export patterns

### Architecture

Document architectural patterns and design decisions:

- Design patterns (Repository, Service Layer, MVC, etc.)
- Layer separation rules
- Dependency injection patterns
- Module organization

### Testing

Specify testing requirements and practices:

- Testing framework and tools
- Coverage requirements
- Test file organization
- Testing patterns and best practices

### File Structure

Describe project directory organization:

- Purpose of each directory
- Where to place new files
- Naming conventions for files and folders

### Commands

List commonly used commands with descriptions:

- Build commands
- Test commands
- Lint and format commands
- Development server commands

### Boundaries

Define what should never be done:

- Files/directories to never modify
- Operations requiring approval
- Security constraints

## Starter Template

```markdown
# Project Instructions

## Code Style
- Use [language] for all new files
- Follow [naming convention] for [variable types]
- Maximum line length: [number] characters
- Use [formatter] with configuration in [config file]

## Architecture
- Follow [design pattern] pattern
- Keep [layer] logic in [location]
- Use [dependency management approach]

## Testing
- Write [test type] for all [components]
- Use [testing framework]
- Aim for [coverage]% code coverage minimum
- Place tests in [location]

## File Structure
- `src/` - [description]
- `tests/` - [description]
- `docs/` - [description]

## Commands
- Build: `[command]`
- Test: `[command]`
- Lint: `[command]`
- Format: `[command]`

## Boundaries
- Never [action]
- Don't modify [files/directories]
- Ask before [action]
```

## Best Practices

### What Works

- Clear, organized sections with descriptive headings
- Specific rules with examples, not abstract descriptions
- Executable commands with flags, not just tool names
- Real code examples showing style patterns
- Project-specific constraints and boundaries
- Tech stack with versions and key dependencies

### What Fails

- Vague instructions like "write good code"
- Tool names without commands or configuration
- Abstract style descriptions without examples
- Missing file structure information
- Generic rules that don't apply to the project

## Quick Start

> **📚 Before starting:** Query `@Cursor` documentation to verify current AGENTS.md requirements and any recent changes to the format or functionality.

1. **Create AGENTS.md in project root** - Place the file at the root of your project directory (not in subdirectories)
2. **Start with essential sections** - Begin with:
  - Code Style (language, naming conventions)
  - Architecture (design patterns, structure)
  - File Structure (directory organization)
3. **Add project-specific details** - Include:
  - Commands your project uses
  - Testing requirements
  - Boundaries and constraints
4. **Keep it simple** - AGENTS.md is meant to be straightforward. If you need complex configuration, multiple scoped rules, or conditional logic, use `.cursor/rules` instead.
5. **Remember the limitations** - Only one AGENTS.md file per project, and it applies globally. For scoped rules, use `.cursor/rules`.
6. **Iterate** - Add sections as needed. The file should grow organically based on what the AI assistant needs to know about your project.

## Integrating New Information

When adding new information to AGENTS.md, follow these strategies to maintain document quality and consistency:

### 1. Identify the Right Location

**Before adding new content:**

- Review existing sections to find the most appropriate place
- Check if the information fits an existing section or needs a new one
- Consider cross-references to related sections

**Decision tree:**

- **Fits existing section?** → Add to that section, maintaining its structure
- **Related to multiple sections?** → Add to the most relevant primary section, add cross-references
- **Completely new topic?** → Create a new section with clear heading

### 2. Maintain Structural Consistency

**When adding to existing sections:**

- Follow the same formatting style (bullet points, tables, code blocks)
- Match the tone and detail level of surrounding content
- Use consistent emoji/icon patterns if the document uses them
- Preserve the section's organizational pattern (e.g., if it uses tables, continue using tables)

**Example - Good integration:**

```markdown
## Architecture
- Follow the repository pattern
- Keep business logic in service layers
- Controllers should only handle HTTP requests/responses
- Use dependency injection for all services
- **NEW:** Use event-driven architecture for cross-service communication
```

**Example - Bad integration:**

```markdown
## Architecture
- Follow the repository pattern
- Keep business logic in service layers

## NEW STUFF ABOUT EVENTS
We should use events now. This is important.
```

### 3. Update Related Sections

**When adding new information, check for:**

- **Cross-references**: Update any sections that reference the topic
- **Examples**: Add examples if the section uses them
- **Commands**: Update the Commands section if new tools are introduced
- **Boundaries**: Update Boundaries if new constraints are added
- **File Structure**: Update File Structure if new directories are mentioned

**Example workflow:**

1. Add new testing framework to Testing section
2. Update Commands section with new test command
3. Update File Structure if test files go in new location
4. Check Boundaries section for any test-related constraints

### 4. Version Control and Changelog

**Best practices for tracking changes:**

**Option A: Inline updates (for small changes)**

- Add brief notes in context: `**Updated 2024-01-15:** Changed from Jest to Vitest`
- Use strikethrough for deprecated info: `~~Use Jest~~` → `Use Vitest`

**Option B: Changelog section (recommended for significant updates)**

```markdown
## 📝 Update Log

### 2024-01-15
- ✅ Updated testing framework from Jest to Vitest
- ✅ Added new event-driven architecture pattern
- ✅ Expanded File Structure section with `events/` directory

### 2024-01-10
- ✅ Initial AGENTS.md creation
```

**Benefits of changelog:**

- Tracks evolution of project guidelines
- Helps AI understand what changed and why
- Provides context for future updates
- Makes it easier to revert if needed

### 5. Integration Checklist

Before finalizing new information:

- Content fits logically in chosen location
- Formatting matches existing style
- Related sections updated (cross-references, examples, commands)
- No duplicate information elsewhere
- Changelog entry added (if significant change)
- Code examples tested/verified (if applicable)
- Commands tested (if new commands added)

## Correcting Information

When correcting errors or outdated information in AGENTS.md, follow these practices:

### 1. Identify What Needs Correction

**Types of corrections:**

- **Factual errors**: Wrong information (e.g., incorrect command, wrong file path)
- **Outdated information**: Information that was correct but is now obsolete
- **Inconsistencies**: Conflicting information in different sections
- **Clarifications**: Ambiguous or unclear statements

**How to identify:**

- Test commands and verify they work
- Check file paths and structure
- Review for contradictions across sections
- Validate code examples

### 2. Correction Strategies

**Strategy A: Direct Replacement (for simple errors)**

```markdown
# Before
- Use Jest for testing

# After
- Use Vitest for testing
```

**Strategy B: Marked Correction (for significant changes)**

```markdown
# Before
- Use Jest for testing

# After
- Use Vitest for testing *(Updated: Jest deprecated as of 2024-01-15)*
```

**Strategy C: Strikethrough + New (for historical context)**

```markdown
- ~~Use Jest~~ → Use Vitest for testing
```

**Strategy D: Correction Note (for complex corrections)**

```markdown
## Testing
- Use Vitest for testing

> **⚠️ Correction Note (2024-01-15):** Previously documented Jest, but project migrated to Vitest for better performance. All test files use `.test.ts` extension with Vitest.
```

### 3. Handle Conflicting Information

**When information conflicts across sections:**

1. **Identify all conflicting instances**
  ```bash
   # Search for the conflicting term/phrase
   grep -r "conflicting_term" AGENTS.md
  ```
2. **Determine the correct version**
  - Test/verify which is correct
  - Check project files for actual implementation
  - Consult with team if needed
3. **Update all instances consistently**
  - Don't just fix one section
  - Update all references to maintain consistency
  - Add a note explaining the correction if significant

**Example - Fixing inconsistency:**

```markdown
# Section 1 (incorrect)
- Tests go in `tests/` directory

# Section 2 (correct)
- Tests go in `__tests__/` directory

# After correction (both sections)
- Tests go in `__tests__/` directory *(Note: Corrected from `tests/` - tests are co-located with source files)*
```

### 4. Preserve Context When Correcting

**Don't just delete wrong information - provide context:**

**Bad correction:**

```markdown
# Before
- Use Python 3.9
# After
- Use Python 3.11
```

**Good correction:**

```markdown
# Before
- Use Python 3.9
# After
- Use Python 3.11 *(Updated: Minimum version requirement changed due to new dependencies)*
```

**Why this matters:**

- Helps AI understand why the change was made
- Prevents reverting to old incorrect information
- Provides context for future decisions

### 5. Correction Workflow

**Step-by-step correction process:**

1. **Identify the error**
  - What's wrong?
  - Where is it located?
  - Are there related errors?
2. **Verify the correct information**
  - Test commands
  - Check actual project structure
  - Verify with codebase
3. **Find all instances**
  - Search for related terms
  - Check cross-references
  - Review examples
4. **Make corrections**
  - Update all instances
  - Add correction notes if significant
  - Update changelog
5. **Verify consistency**
  - Re-read relevant sections
  - Check for new inconsistencies
  - Ensure formatting is consistent
6. **Update changelog**
  ```markdown
   ## 📝 Update Log

   ### 2024-01-15
   - 🔧 Corrected: Updated Python version from 3.9 to 3.11
   - 🔧 Fixed: Test directory path corrected to `__tests__/`
   - 🔧 Clarified: Added note about event-driven architecture requirements
  ```

### 6. Correction Best Practices

**Do:**

- ✅ Correct all instances of the error, not just one
- ✅ Add context/notes for significant corrections
- ✅ Update changelog with correction entries
- ✅ Verify corrections don't introduce new errors
- ✅ Test commands/examples after correction
- ✅ Check for related sections that need updates

**Don't:**

- ❌ Only fix one instance when multiple exist
- ❌ Delete information without explanation
- ❌ Make corrections without verifying they're correct
- ❌ Ignore related sections that reference the error
- ❌ Skip updating the changelog

### 7. Handling Major Corrections

**For significant corrections (e.g., architecture changes, tool migrations):**

1. **Add a correction section at the top** (temporary, remove after a few weeks):
  ```markdown
   > **⚠️ Important Update (2024-01-15):** This document was recently updated. Key changes:
   > - Testing framework changed from Jest to Vitest
   > - Architecture pattern updated to event-driven
   > - See Update Log for details
  ```
2. **Document migration path**:
  ```markdown
   ## Migration Notes

   If you're updating from the old guidelines:
   - Replace all `jest` commands with `vitest`
   - Move test files from `tests/` to `__tests__/`
   - See [Migration Guide](./MIGRATION.md) for details
  ```
3. **Keep old information temporarily** (with strikethrough):
  ```markdown
   ## Testing
   - Use Vitest for testing
   - ~~Use Jest for testing~~ *(Deprecated as of 2024-01-15)*
  ```

## Troubleshooting

> **🔍 First step:** If you encounter issues with AGENTS.md, always check `@Cursor` documentation first for the latest troubleshooting guidance and known issues.

If AGENTS.md appears to be ignored:

- Ensure the file is named exactly `AGENTS.md` (case-sensitive)
- Verify it's located at the project root directory (not in subdirectories)
- Check that your Cursor IDE is updated to the latest version
- Query `@Cursor` documentation for current requirements and limitations
- Consult the Cursor community forums for version-specific issues

### Common Issues When Updating

**Issue: Changes not being recognized**

- Solution: Restart Cursor IDE after significant updates
- Solution: Check file encoding (should be UTF-8)
- Solution: Verify no syntax errors in markdown

**Issue: Conflicting information after updates**

- Solution: Use the correction workflow above
- Solution: Search entire document for related terms
- Solution: Add clarification notes where needed

**Issue: Document becoming too long/unorganized**

- Solution: Consider splitting into `.cursor/rules` if it exceeds ~500 lines
- Solution: Reorganize sections with clearer headings
- Solution: Move detailed examples to separate documentation files

