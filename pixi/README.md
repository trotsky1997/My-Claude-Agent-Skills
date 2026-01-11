# Pixi Skill

Comprehensive skill package for using Pixi, a fast and reproducible package management tool.

## Structure

```
pixi/
├── SKILL.md                    # Core workflows and common operations (<500 lines)
├── README.md                   # This file
└── references/                 # Detailed documentation
    ├── manifest.md             # Complete manifest reference
    ├── commands.md             # Full command reference
    └── advanced.md             # Advanced features and patterns
```

## Quick Access

- **SKILL.md**: Start here for common workflows and quick reference
- **references/manifest.md**: Complete `pixi.toml` reference
- **references/commands.md**: All CLI commands with examples
- **references/advanced.md**: Advanced patterns, CI/CD, Docker, etc.

## Usage

This skill will automatically trigger when you need help with:
- Managing Python/project dependencies
- Setting up reproducible environments
- Creating task runners and build pipelines
- Working with multiple environments
- Installing global CLI tools
- Building conda packages
- Setting up CI/CD with Pixi

## Design Principles

Following the doc-to-skill methodology:
- **Progressive disclosure**: Essential → SKILL.md → references/ (loaded on demand)
- **80/20 rule**: 20% most common content in SKILL.md, 80% detailed in references/
- **Actionability first**: Commands and examples prioritized
- **No duplication**: Information lives in one place only
- **Trigger clarity**: Description includes all use cases
