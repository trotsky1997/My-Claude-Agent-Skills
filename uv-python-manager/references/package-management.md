# Advanced Package Management with UV

## Table of Contents
- Installation Methods
- Dependency Resolution
- Lockfile Management
- Version Constraints
- Development Dependencies
- Optional Dependencies
- Extras
- Index Configuration

## Installation Methods

### Basic Installation
```bash
uv pip install package-name
uv pip install package-name==1.2.3
uv pip install "package-name>=1.0,<2.0"
```

### From Requirements Files
```bash
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt
```

### Editable Installs
```bash
uv pip install --editable .
uv pip install -e ./local-package
```

### From Git Repositories
```bash
uv pip install git+https://github.com/user/repo.git
uv pip install git+https://github.com/user/repo.git@branch
uv pip install git+https://github.com/user/repo.git@tag
```

### From Local Archives
```bash
uv pip install ./package.tar.gz
uv pip install ./package.whl
```

## Dependency Resolution

uv uses a fast dependency resolver that handles:
- Version conflicts
- Dependency trees
- Optional dependencies
- Platform-specific packages

### Resolving Conflicts
```bash
# Check for conflicts
uv pip check

# Upgrade to resolve conflicts
uv pip install --upgrade package-name
```

## Lockfile Management

### Generating Lockfiles
```bash
# Generate lockfile from requirements
uv pip compile requirements.in -o requirements.txt

# Update lockfile
uv lock --upgrade

# Update specific package
uv lock --upgrade-package package-name
```

### Using Lockfiles
```bash
# Install from lockfile
uv sync

# Verify lockfile
uv lock --check
```

## Version Constraints

### Constraint Syntax
```bash
# Exact version
package==1.2.3

# Version range
package>=1.0,<2.0
package~=1.2.0  # Compatible release

# Pre-release
package>=1.0.0a1

# Version wildcards
package==1.*
```

### Adding with Constraints
```bash
uv add "requests>=2.28.0,<3.0"
uv add "django~=4.2.0"
```

## Development Dependencies

### Adding Dev Dependencies
```bash
uv add --dev pytest
uv add --dev black ruff mypy
```

### Group Dependencies
```bash
uv add --group test pytest pytest-cov
uv add --group lint black ruff
```

## Optional Dependencies

### Installing with Extras
```bash
uv pip install "package[extra1,extra2]"
uv add "package[extra1,extra2]"
```

### Common Extras Patterns
```bash
# Development extras
uv add "package[dev]"

# Testing extras
uv add "package[test]"

# Multiple extras
uv add "package[dev,test,docs]"
```

## Index Configuration

### Using Custom Index
```bash
uv pip install --index-url https://pypi.org/simple/ package-name
uv pip install --extra-index-url https://custom-index.com/ package-name
```

### Authentication
```bash
# Using credentials in URL
uv pip install --index-url https://user:pass@index.com/ package-name

# Using environment variables
export UV_INDEX_URL="https://user:pass@index.com/"
```

## Performance Tips

1. **Use global cache**: uv automatically caches packages globally
2. **Parallel downloads**: uv downloads packages in parallel
3. **Fast resolver**: uv's resolver is significantly faster than pip
4. **Incremental updates**: Only updates what's changed

## Migration from pip

### Direct Replacements
- `pip install` → `uv pip install`
- `pip uninstall` → `uv pip uninstall`
- `pip list` → `uv pip list`
- `pip show` → `uv pip show`
- `pip freeze` → `uv pip freeze`

### Additional Features
- Faster execution (10-100x)
- Better dependency resolution
- Universal lockfile support
- Workspace support
