# Project Configuration with UV

## Table of Contents
- Project Structure
- pyproject.toml Configuration
- Lockfile Management
- Workspace Configuration
- Environment Variables
- Script Configuration

## Project Structure

### Standard Project Layout
```
my-project/
├── pyproject.toml      # Project configuration
├── uv.lock             # Lockfile (generated)
├── .python-version     # Pinned Python version (optional)
├── src/                # Source code (optional)
│   └── my_project/
│       └── __init__.py
├── tests/              # Tests
└── README.md
```

## pyproject.toml Configuration

### Basic Configuration
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My project description"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28.0",
    "click",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black",
]
test = [
    "pytest-cov",
    "mypy",
]
```

### Advanced Configuration
```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My project"
readme = "README.md"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "you@example.com"}
]
keywords = ["python", "cli"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
]

[project.urls]
Homepage = "https://github.com/user/my-project"
Documentation = "https://my-project.readthedocs.io"
Repository = "https://github.com/user/my-project"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "pytest>=7.0",
    "black>=23.0",
]
```

### Scripts Configuration
```toml
[project.scripts]
my-cli = "my_project.cli:main"

[project.entry-points."console_scripts"]
another-cli = "my_project.another:main"
```

## Lockfile Management

### Understanding uv.lock

The `uv.lock` file contains:
- Exact versions of all dependencies
- Dependency tree structure
- Platform-specific packages
- Hash verification

### Lockfile Best Practices

1. **Always commit lockfile**: Ensures reproducible builds
2. **Regenerate regularly**: Run `uv lock` after dependency changes
3. **Don't edit manually**: Let uv manage the lockfile
4. **Version control**: Include in git for team consistency

### Updating Lockfile
```bash
# Update all dependencies
uv lock --upgrade

# Update specific package
uv lock --upgrade-package requests

# Check lockfile consistency
uv lock --check
```

## Workspace Configuration

### Workspace Structure
```
workspace/
├── pyproject.toml      # Workspace root config
├── package-a/
│   ├── pyproject.toml
│   └── src/
├── package-b/
│   ├── pyproject.toml
│   └── src/
└── package-c/
    ├── pyproject.toml
    └── src/
```

### Workspace pyproject.toml
```toml
[tool.uv.workspace]
members = [
    "package-a",
    "package-b",
    "package-c",
]
```

### Working with Workspaces
```bash
# Initialize workspace
uv init --workspace

# Add package to workspace
uv init --package package-name

# Sync all workspace packages
uv sync --workspace

# Run command in workspace context
uv run --workspace python script.py
```

## Environment Variables

### UV Configuration
```bash
# Index URL
export UV_INDEX_URL="https://pypi.org/simple/"

# Extra index URLs
export UV_EXTRA_INDEX_URL="https://custom-index.com/"

# Cache directory
export UV_CACHE_DIR="/path/to/cache"

# Python location
export UV_PYTHON="/path/to/python"

# Offline mode
export UV_OFFLINE=1
```

### Project-Specific Variables
```bash
# In .env file (loaded automatically)
UV_INDEX_URL=https://internal-pypi.company.com/
UV_EXTRA_INDEX_URL=https://pypi.org/simple/
```

## Script Configuration

### Inline Script Dependencies
```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "requests>=2.28.0",
#   "click>=8.0",
# ]
# ///
import requests
import click

@click.command()
def main():
    click.echo("Hello from uv script!")

if __name__ == "__main__":
    main()
```

### Running Scripts
```bash
# Run with automatic dependency resolution
uv run script.py

# Run with specific Python version
uv run --python 3.12 script.py

# Run with environment variables
uv run --env-file .env script.py
```

## Python Version Pinning

### Pinning Version
```bash
# Pin to specific version
uv python pin 3.12

# Pin to minor version
uv python pin 3.12

# Creates .python-version file
```

### .python-version File
```
3.12.0
```

### Using Pinned Version
```bash
# Automatically uses .python-version
uv venv
uv run python script.py
```

## Build Configuration

### Build Backend
```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### Building Distributions
```bash
# Build wheel and source distribution
uv build

# Build only wheel
uv build --wheel

# Build only sdist
uv build --sdist
```

## Publishing

### Publishing to PyPI
```bash
# Build distributions
uv build

# Publish to PyPI
uv publish

# Publish to test PyPI
uv publish --repository testpypi
```

### Publishing Configuration
```toml
[tool.uv.publish]
repository = "pypi"  # or "testpypi"
username = "your-username"
password = "your-password"  # or use environment variable
```
