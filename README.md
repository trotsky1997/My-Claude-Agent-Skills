# My Claude Agent Skills

A collection of specialized skills that extend Codex/Claude Agent capabilities with domain-specific knowledge, workflows, and tool integrations.

## What are Skills?

Skills are modular, self-contained packages that extend AI agent capabilities by providing:
- **Specialized workflows** - Multi-step procedures for specific domains
- **Tool integrations** - Instructions for working with specific file formats or APIs
- **Domain expertise** - Company-specific knowledge, schemas, business logic
- **Bundled resources** - Scripts, references, and assets for complex tasks

Each skill consists of a `SKILL.md` file (required) with YAML frontmatter metadata and Markdown instructions, plus optional bundled resources (scripts, references, assets).

## Available Skills

### Development Tools

- **ast-grep** - Guide for writing ast-grep rules to perform structural code search and analysis
- **codebase-reading** - Systematic methodology for reading and understanding large codebases efficiently
- **cursor-agents-md** - Guide for creating effective AGENTS.md files for Cursor IDE
- **github-cli** - Comprehensive guide for using GitHub CLI (gh) to interact with GitHub
- **mcp-developer** - Guide for developing Model Context Protocol (MCP) servers

### Python Development

- **python-debugging** - Toolkit for debugging Python code autonomously without IDE support
- **pytest-testing** - Comprehensive guide for writing and running pytest tests
- **pypi-publisher** - Guide for publishing Python packages to PyPI
- **uv-python-manager** - Guide for using uv, a fast Python package and project manager
- **pixi** - Guide for using Pixi, a fast package management tool for Python, Rust, C/C++, etc.

### Browser & Web Automation

- **cursor-ide-browser-skill** - Browser automation in Cursor IDE using MCP protocol
- **vibium-browser-automation** - Comprehensive guide for using Vibium browser automation tool

### Research & Documentation

- **deepresearch** - Comprehensive DeepResearch methodology for rigorous research projects
- **doc-to-skill** - Convert documentation into structured Agent Skills following progressive disclosure principles

### Utilities

- **skill-selector** - Self-driven skill selection system using internal curiosity asking
- **victoria3-mod-dev** - Comprehensive Victoria 3 modding skill for creating and modifying game mods

## Skill Structure

Each skill follows a standard structure:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description)
│   └── Markdown instructions
└── Optional resources/
    ├── scripts/      - Executable code (Python/Bash/etc.)
    ├── references/   - Detailed documentation (loaded on demand)
    └── assets/       - Templates, files used in output
```

### Design Principles

- **Progressive disclosure** - Essential info in SKILL.md, detailed docs in references/
- **80/20 rule** - 20% most common content in SKILL.md, 80% detailed in references/
- **Actionability first** - Commands and examples prioritized
- **No duplication** - Information lives in one place only
- **Trigger clarity** - Description includes all use cases

## Usage

Skills are designed to be used with AI agents that support the Agent Skills specification. When a skill's description matches your task, the agent will automatically load and use the skill's knowledge.

To use these skills:

1. **Clone this repository** to your skills directory
2. **Configure your AI agent** to recognize skills from this location
3. **Ask questions or request tasks** - Skills will trigger automatically based on their descriptions

## Repository Structure

```
.
├── README.md                    # This file
├── .system/                     # System skills (skill-creator, skill-installer)
└── [skill-name]/               # Individual skill directories
    ├── SKILL.md                # Core skill definition
    ├── references/             # Detailed documentation (optional)
    ├── scripts/                # Executable utilities (optional)
    └── assets/                 # Templates and resources (optional)
```

## Contributing

To create a new skill or update an existing one, refer to the **skill-creator** skill for guidance on:
- Skill structure and metadata
- Writing effective skill descriptions
- Organizing references and resources
- Best practices for skill design

## References

- [Agent Skills Specification](https://agentskills.io/specification)
- [Cursor Rules Documentation](https://cursor.com/docs/context/rules)
- [AgentSkills Documentation](https://agentskills.io/home)

## License

Each skill may have its own license. Check individual skill directories for license information.
