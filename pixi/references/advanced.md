# Advanced Pixi Features

Advanced features, patterns, and use cases for Pixi.

## Advanced Task Features

### Task Arguments with MiniJinja Templates

Tasks support MiniJinja templating for dynamic command generation:

```toml
[tasks]
# Basic argument
greet = { 
    cmd = "echo Hello, {{ name }}!", 
    args = [{ arg = "name", default = "World" }] 
}

# Multiple arguments
build = {
    cmd = "build.sh --mode {{ mode }} --target {{ target }}",
    args = [
        { arg = "mode", default = "debug" },
        { arg = "target", default = "{{ pixi.platform }}" }
    ]
}

# Platform-aware tasks
deploy = {
    cmd = "deploy.sh --platform {{ pixi.platform }} --env {{ environment }}",
    args = [{ arg = "environment", default = "staging" }]
}

# Using filters
format = {
    cmd = "formatter {{ path | upper }}",
    args = [{ arg = "path", default = "src" }]
}
```

### Built-in Pixi Variables

Pixi provides built-in variables in the MiniJinja context:

- `pixi.platform` - Platform name (e.g., `linux-64`, `osx-arm64`)
- `pixi.environment.name` - Current environment name
- `pixi.manifest_path` - Absolute path to manifest
- `pixi.version` - Pixi version
- `pixi.is_win`, `pixi.is_unix`, `pixi.is_linux`, `pixi.is_osx` - Platform flags

### Task Dependencies with Environment Specification

```toml
[tasks]
test-py311 = { 
    cmd = "pytest", 
    environment = "py311" 
}

test-py312 = { 
    cmd = "pytest", 
    environment = "py312" 
}

test-all = { 
    depends-on = [
        { task = "test-py311" },
        { task = "test-py312" }
    ] 
}
```

### Task Caching with Templates

Use templates in `inputs` and `outputs` for parameterized caching:

```toml
[tasks]
process-file = {
    cmd = "processor --input {{ filename }}.txt --output {{ filename }}.out",
    args = [{ arg = "filename", default = "data" }],
    inputs = ["{{ filename }}.txt"],
    outputs = ["{{ filename }}.out"]
}
```

### Clean Environment Tasks

Run tasks in minimal environment (Unix only):

```toml
[tasks]
isolated = { 
    cmd = "python isolated.py", 
    clean-env = true 
}
```

## Advanced Environment Patterns

### Solve Groups for Version Consistency

Ensure multiple environments share the same dependency versions:

```toml
[dependencies]
python = ">=3.11"
fastapi = ">=0.100"

[feature.test.dependencies]
pytest = "*"

[environments]
# Both environments solve together, sharing versions
prod = { features = [], solve-group = "prod" }
test-prod = { features = ["test"], solve-group = "prod" }
```

### Feature Composition Patterns

```toml
# Base dependencies
[dependencies]
python = ">=3.11"

# Feature layers
[feature.core.dependencies]
fastapi = "*"
uvicorn = "*"

[feature.database.dependencies]
sqlalchemy = "*"
psycopg2 = "*"

[feature.cache.dependencies]
redis-py = "*"

[feature.monitoring.dependencies]
prometheus-client = "*"

# Environment compositions
[environments]
# Minimal production
prod = ["core", "database"]

# Production with monitoring
prod-monitored = ["core", "database", "monitoring"]

# Full development
dev = ["core", "database", "cache", "monitoring"]

# Test environment (same versions as prod)
test = { 
    features = ["core", "database", "test"], 
    solve-group = "prod" 
}
```

### Environment Without Default Feature

```toml
[dependencies]
python = "*"
numpy = "*"

[feature.lint.dependencies]
ruff = "*"
mypy = "*"

[environments]
# Lint environment has only lint tools, no numpy
lint = { features = ["lint"], no-default-feature = true }
```

## Platform-Specific Advanced Configuration

### Conditional Dependencies

```toml
[dependencies]
# Shared across all platforms
python = ">=3.11"

[target.linux-64.dependencies]
glibc = "2.28"
systemd-devel = "*"

[target.osx-64.dependencies]
# macOS-specific
clang_osx-64 = "*"

[target.osx-arm64.dependencies]
# Apple Silicon
mlx = "*"

[target.win-64.dependencies]
# Windows-specific
msmpi = "~=10.1.1"
vs2022_win-64 = "*"
```

### Platform-Specific Tasks

```toml
[tasks]
# Unix tasks
[target.unix.tasks]
clean = "rm -rf build/"
build = "./build.sh"

[target.linux-64.tasks]
install = "sudo apt install deps"

[target.osx-64.tasks]
install = "brew install deps"

# Windows tasks
[target.win.tasks]
clean = "rmdir /s /q build"
build = "build.bat"

[target.win-64.tasks]
install = "winget install deps"
```

### Platform-Specific Activation

```toml
[activation]
env = { BASE_PATH = "/usr/local/bin" }

[target.win-64.activation]
scripts = ["setup_windows.bat"]
env = { BASE_PATH = "C:\\Program Files\\bin" }

[target.unix.activation]
scripts = ["setup_unix.sh"]
env = { BASE_PATH = "/usr/local/bin" }

[target.linux-64.activation.env]
PATH = "$BASE_PATH/linux:$PATH"

[target.osx-64.activation.env]
PATH = "$BASE_PATH/osx:$PATH"
```

## PyPI Advanced Configuration

### Custom Index Strategies

```toml
[pypi-options]
# Default: first-index (stops at first match, prevents dependency confusion)
index-strategy = "first-index"

# Unsafe: searches all indexes but prefers first
index-strategy = "unsafe-first-match"

# Unsafe: takes best version from any index
index-strategy = "unsafe-best-match"
```

### Build Isolation Control

```toml
[pypi-options]
# Disable build isolation for specific packages
no-build-isolation = ["detectron2", "torchvision"]

# Disable for all packages (use conda deps for build env)
no-build-isolation = true
```

### No Build / No Binary

```toml
[pypi-options]
# Don't build source distributions
no-build = true
no-build = ["package1", "package2"]  # Per-package

# Always build from source (no pre-built wheels)
no-binary = true
no-binary = ["package1", "package2"]  # Per-package
```

### Prerelease Mode

```toml
[pypi-options]
# Control pre-release version handling
prerelease-mode = "disallow"                    # Never allow
prerelease-mode = "allow"                       # Always allow
prerelease-mode = "if-necessary"                # Only if all versions are pre-release
prerelease-mode = "explicit"                    # Only if explicitly requested
prerelease-mode = "if-necessary-or-explicit"    # Default
```

## Advanced System Requirements

```toml
[system-requirements]
# Linux kernel version
linux = "5.4"

# libc version with family
libc = { family = "glibc", version = "2.28" }
libc = { family = "musl", version = "1.2.0" }

# macOS version
macos = "11.0"

# CUDA version (for GPU packages)
cuda = "12.1"

# Feature-specific requirements
[feature.cuda.system-requirements]
cuda = "12.1"
```

## Build System (Preview)

### Package Build Configuration

```toml
[workspace]
preview = ["pixi-build"]

[package]
name = "my-package"
version = "0.1.0"

[package.build]
backend = { name = "pixi-build-python", version = "0.3.*" }
channels = ["conda-forge"]
source = { path = "." }

# Alternative sources
[package.build.source]
git = "https://github.com/user/repo.git"
rev = "abc123"
subdirectory = "package"

# Backend configuration
[package.build.config]
# Backend-specific options
```

### Build Variants

Create build matrices for testing multiple configurations:

```toml
[workspace.build-variants]
python = ["3.11.*", "3.12.*"]
c_compiler_version = ["11.4", "14.0"]

[workspace.target.linux-64.build-variants]
c_compiler = ["gcc"]
c_compiler_version = ["11.4", "13.0"]
```

### Build Dependencies

```toml
# Build-time only (compilers, build tools)
[package.build-dependencies]
cmake = "*"
ninja = "*"
gcc = "*"

# Host dependencies (needed during build, linked against)
[package.host-dependencies]
python = ">=3.11"
setuptools = "*"

# Run dependencies (needed at runtime)
[package.run-dependencies]
requests = "*"
```

## Advanced Configuration Patterns

### Pinning Strategy

```toml
# In config.toml
pinning-strategy = "semver"         # Default: pin to major (or minor for v0)
pinning-strategy = "exact-version"  # Pin to exact version
pinning-strategy = "major"          # Pin to major version
pinning-strategy = "minor"          # Pin to minor version
pinning-strategy = "latest-up"      # Pin to >= current version
pinning-strategy = "no-pin"         # No pinning (*)
```

### Detached Environments

Store environments outside workspace (advanced):

```toml
# In config.toml
detached-environments = true  # Use cache directory
detached-environments = "/opt/pixi/envs"  # Custom path
```

### Proxy Configuration

```toml
# In config.toml
[proxy-config]
https = "http://proxy.example.com:8080"
http = "http://proxy.example.com:8080"
non-proxy-hosts = ["localhost", "*.internal"]
```

### Mirrors Configuration

```toml
# In config.toml
[mirrors]
"https://conda.anaconda.org/conda-forge" = [
    "https://mirror1.example.com/conda-forge",
    "https://mirror2.example.com/conda-forge"
]

# OCI registry mirrors
[mirrors."conda-forge"]
"oci://ghcr.io/channel-mirrors/conda-forge" = [
    "oci://ghcr.io/channel-mirrors/conda-forge"
]
```

### Repodata Configuration

```toml
# In config.toml
[repodata-config]
base-url = "https://conda.anaconda.org"
state-file = ".pixi/repodata.json"
ttl = 3600  # Time-to-live in seconds

# Per-channel config
[repodata-config."conda-forge"]
base-url = "https://conda-forge.org"
ttl = 7200
```

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: prefix-dev/setup-pixi@v0.5.1
        with:
          environments: test dev
      - name: Run tests
        run: pixi run --environment test pytest
      - name: Lint
        run: pixi run --environment dev lint
```

### Matrix Testing with Multiple Environments

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        environment: [py39, py310, py311]
    steps:
      - uses: actions/checkout@v4
      - uses: prefix-dev/setup-pixi@v0.5.1
        with:
          environments: ${{ matrix.environment }}
      - run: pixi run --environment ${{ matrix.environment }} test
```

## Docker Integration

### Dockerfile Example

```dockerfile
FROM ghcr.io/prefix-dev/pixi:latest
WORKDIR /app

# Copy manifest files
COPY pixi.toml pixi.lock ./

# Install production environment
RUN pixi install --environment prod --frozen

# Copy application code
COPY . .

# Run application
CMD ["pixi", "run", "--environment", "prod", "serve"]
```

### Multi-stage Docker Build

```dockerfile
# Build stage
FROM ghcr.io/prefix-dev/pixi:latest AS builder
WORKDIR /app
COPY pixi.toml pixi.lock ./
RUN pixi install --environment build
COPY . .
RUN pixi run --environment build build

# Runtime stage
FROM ghcr.io/prefix-dev/pixi:latest
WORKDIR /app
COPY pixi.toml pixi.lock ./
RUN pixi install --environment prod --frozen
COPY --from=builder /app/dist ./dist
CMD ["pixi", "run", "--environment", "prod", "serve"]
```

## Performance Optimization

### Caching Strategies

1. **Task Inputs/Outputs**: Always specify for build tasks
2. **Lockfile**: Commit to version control
3. **Package Cache**: Shared across workspaces (configure `PIXI_CACHE_DIR`)
4. **Environment Cache**: Use detached environments for faster cleanup

### Concurrency Configuration

```toml
# In config.toml
[concurrency]
solves = 1        # Parallel solves
downloads = 12    # Parallel downloads
```

## Troubleshooting Advanced Issues

### Lockfile Conflicts

```bash
# Regenerate from scratch
rm pixi.lock
pixi lock

# Check satisfiability
pixi install --locked  # Fails if not satisfiable
```

### Dependency Resolution Issues

```bash
# Check what's available
pixi search package-name

# Try different solve strategy
# Edit pixi.toml: solve-strategy = "lowest"

# Check dependency tree
pixi tree package-name
pixi tree --invert package-name  # Reverse deps
```

### Build Issues

```bash
# Enable verbose output
pixi install -vvv

# Check system requirements
pixi info

# Test with clean environment
pixi clean
pixi install
```

## Security Best Practices

1. **Checksums**: Specify `sha256` for critical packages
2. **Channel Priority**: Use `strict` (default) to prevent dependency confusion
3. **Index Strategy**: Use `first-index` for PyPI to prevent dependency confusion
4. **Lockfiles**: Always review lockfile changes in PRs
5. **Authentication**: Use `pixi auth` for private channels, not embedded credentials
