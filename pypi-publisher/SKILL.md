---
name: pypi-publisher
description: Comprehensive guide for publishing Python packages to PyPI. Use when (1) Publishing new Python packages to PyPI, (2) Updating existing packages with new versions, (3) Troubleshooting PyPI upload errors, (4) Setting up automated publishing workflows, (5) Managing version numbers and package metadata, (6) Using API tokens for secure publishing, (7) Testing packages before production release, or any PyPI publishing tasks.
metadata:
  short-description: Publish Python packages to PyPI

---

# PyPI Publisher

Complete workflow for publishing Python packages to PyPI with best practices, error handling, and automation.

## Critical Pre-Publish Checklist

**ALWAYS run tests before publishing.** Never skip this step.

1. **Run full test suite**
   ```bash
   python -m pytest tests/ -v --tb=short
   ```
   - All tests must pass
   - Check code coverage if applicable
   - Fix any failures before proceeding

2. **Verify version numbers are consistent**
   - `pyproject.toml`: `version = "X.Y.Z"`
   - `package/__init__.py`: `__version__ = "X.Y.Z"`
   - Any other version references (e.g., `mcp_server.py` server_version)

3. **Check for uncommitted changes**
   - Review git status
   - Commit or stash changes as needed

4. **Clean old build artifacts**
   ```bash
   # Windows PowerShell
   Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue
   
   # Linux/Mac
   rm -rf dist/ build/ *.egg-info
   ```

## Publishing Workflow

### Step 1: Build Package

```bash
uv build
# or
python -m build
```

Verify output:
- `dist/package-name-X.Y.Z.tar.gz` (source distribution)
- `dist/package_name-X.Y.Z-py3-none-any.whl` (wheel)

### Step 2: Validate Package

```bash
uvx twine check dist/*
```

Must pass before uploading. Fix any warnings or errors.

### Step 3: Choose Publishing Target

**Test PyPI (recommended for first-time publishing):**
```bash
uvx twine upload --repository testpypi dist/*
```

**Production PyPI:**
```bash
uvx twine upload dist/*
```

### Step 4: Authentication

**Using API Token (recommended):**

Windows PowerShell:
```powershell
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = "pypi-your-api-token-here"
uvx twine upload dist/* --non-interactive
```

Linux/Mac:
```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-your-api-token-here
uvx twine upload dist/* --non-interactive
```

**Create API Token:**
1. Go to https://pypi.org/manage/account/token/
2. Create new token (scope: entire account or specific project)
3. Copy token immediately (only shown once)
4. Use as password with username `__token__`

## Common Errors and Solutions

### "File already exists" (400 Bad Request)

**Cause:** Version already published to PyPI.

**Solution:**
1. Increment version number in `pyproject.toml` and `__init__.py`
2. Rebuild package
3. Upload again

**Version numbering:**
- Patch: `0.1.0` → `0.1.1` (bug fixes)
- Minor: `0.1.0` → `0.2.0` (new features, backward compatible)
- Major: `0.1.0` → `1.0.0` (breaking changes)

### "NonInteractive: Credential not found"

**Cause:** Missing authentication credentials.

**Solution:**
- Set `TWINE_USERNAME` and `TWINE_PASSWORD` environment variables
- Or use `--non-interactive` flag with credentials
- Or create `~/.pypirc` config file

### "Package check failed"

**Cause:** Package metadata or structure issues.

**Solution:**
- Run `twine check dist/*` to see specific errors
- Fix metadata in `pyproject.toml`
- Rebuild and check again

### Import errors after publishing

**Cause:** Package structure or import paths incorrect.

**Solution:**
- Verify `[tool.hatch.build.targets.wheel]` packages configuration
- Check `__init__.py` files exist
- Test local installation: `pip install -e .`

## Automated Publishing Script

For PowerShell (Windows):

```powershell
# Run tests first
python -m pytest tests/ -v --tb=short
if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed! Aborting publish." -ForegroundColor Red
    exit 1
}

# Build
uv build
if ($LASTEXITCODE -ne 0) { exit 1 }

# Check
uvx twine check dist/*
if ($LASTEXITCODE -ne 0) { exit 1 }

# Upload (set credentials first)
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = "your-token"
uvx twine upload dist/* --non-interactive
```

## Version Management

**Always update version in these locations:**
1. `pyproject.toml`: `version = "X.Y.Z"`
2. `package/__init__.py`: `__version__ = "X.Y.Z"`
3. Any hardcoded version strings in code (e.g., MCP server version)

**Semantic versioning:**
- MAJOR: Breaking changes
- MINOR: New features (backward compatible)
- PATCH: Bug fixes

## Post-Publish Verification

1. **Check PyPI page:**
   ```
   https://pypi.org/project/your-package-name/X.Y.Z/
   ```

2. **Test installation:**
   ```bash
   pip install your-package-name==X.Y.Z
   ```

3. **Verify functionality:**
   - Import package
   - Run basic functionality
   - Check CLI commands work (if applicable)

## Best Practices

1. **Always test before publishing**
   - Run full test suite
   - Test actual package installation
   - Verify end-to-end functionality

2. **Use Test PyPI first**
   - Test new publishing workflow
   - Verify package metadata
   - Catch issues before production

3. **Use API tokens, not passwords**
   - More secure
   - Can be scoped to specific projects
   - Can be revoked easily

4. **Version consistently**
   - Follow semantic versioning
   - Update all version references
   - Document changes in CHANGELOG

5. **Automate what you can**
   - Use scripts for repetitive steps
   - Include test runs in automation
   - Add validation checks

6. **Handle errors gracefully**
   - Check exit codes
   - Provide clear error messages
   - Stop on failures (don't continue with broken state)

## Quick Reference

**Essential commands:**
```bash
# Test
python -m pytest tests/ -v

# Build
uv build

# Check
uvx twine check dist/*

# Upload (Test PyPI)
uvx twine upload --repository testpypi dist/*

# Upload (Production)
uvx twine upload dist/*
```

**Version update locations:**
- `pyproject.toml`
- `package/__init__.py`
- Code files with version strings

**Common file patterns:**
- `dist/*.whl` - Wheel distribution
- `dist/*.tar.gz` - Source distribution
- `build/` - Temporary build files (can delete)
- `*.egg-info/` - Package metadata (can delete)

## Automated Publishing Scripts

Pre-built scripts are available in `scripts/`:

- **`publish.ps1`** - PowerShell script for Windows
  ```powershell
  .\publish.ps1 --test                    # Publish to Test PyPI
  .\publish.ps1 --token "pypi-xxx"        # Publish to Production with token
  ```

- **`publish.sh`** - Bash script for Linux/Mac
  ```bash
  chmod +x publish.sh
  ./publish.sh --test                     # Publish to Test PyPI
  ./publish.sh --token "pypi-xxx"         # Publish to Production with token
  ```

These scripts automatically:
- Run tests before publishing
- Build and validate package
- Handle authentication
- Provide clear error messages
