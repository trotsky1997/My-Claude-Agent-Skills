# Pixi Manifest Reference

Complete reference for the `pixi.toml` and `pyproject.toml` manifest files.

## Manifest Discovery

Pixi looks for manifests in this priority order:

1. `--manifest-path` (command-line argument)
2. `pixi.toml` (current directory)
3. `pyproject.toml` (current directory)
4. `pixi.toml` or `pyproject.toml` (parent directories)
5. `$PIXI_PROJECT_MANIFEST` (when in pixi shell)

## Workspace Table

### Required Fields

```toml
[project]  # or [workspace]
channels = ["conda-forge"]
platforms = ["linux-64", "osx-64", "win-64"]
```

### Optional Fields

```toml
[project]
name = "my-project"                    # Workspace name
version = "0.1.0"                      # Version (conda version spec)
authors = ["Name <email@example.com>"] # List of authors
description = "Project description"    # Short description
license = "MIT"                        # SPDX license string
license-file = "LICENSE.md"           # Relative path to license
readme = "README.md"                   # Relative path to README
homepage = "https://example.com"       # Homepage URL
repository = "https://github.com/..."  # Repository URL
documentation = "https://docs..."      # Documentation URL
```

### Channels

```toml
# Channel names (anaconda.org)
channels = ["conda-forge", "pytorch"]

# Full URLs
channels = ["https://prefix.dev/channels/conda-forge"]

# Local file system (absolute paths)
channels = ["/path/to/local/channel"]

# Priority order (for channel concatenation)
[feature.cuda]
channels = ["nvidia", { channel = "pytorch", priority = -1 }]
```

### Platforms

Available platforms: `linux-64`, `linux-arm64`, `osx-64`, `osx-arm64`, `win-64`, `win-arm64`, `noarch`, `unknown`

```toml
platforms = ["linux-64", "osx-64", "win-64"]

# Support both architectures
platforms = ["osx-64", "osx-arm64", "win-64", "win-arm64"]
```

### Channel Priority

```toml
# Strict (default): Use packages from first matching channel only
channel-priority = "strict"

# Disabled: Allow packages from any channel (not recommended)
channel-priority = "disabled"
```

### Solve Strategy

```toml
# Highest (default): Solve to highest compatible versions
solve-strategy = "highest"

# Lowest: Solve to lowest compatible versions
solve-strategy = "lowest"

# Lowest-direct: Only direct deps to lowest, transitive to highest
solve-strategy = "lowest-direct"
```

### Requires Pixi

```toml
requires-pixi = ">=0.40"           # Minimum version
requires-pixi = ">=0.40,<1.0"      # Version range
```

### Exclude Newer

```toml
exclude-newer = "2023-10-01"              # Date format
exclude-newer = "2023-10-01T00:00:00Z"    # RFC 3339 timestamp
```

## Dependencies

### Conda Dependencies

**Version operators:**
- `==` - Exact match
- `!=` - Not equal
- `<`, `<=`, `>`, `>=` - Comparison
- `~=` - Compatible release (e.g., `~=1.2.3` = `>=1.2.3,<1.3.0`)
- `*` - Wildcard
- `,` - AND
- `|` - OR

**Examples:**
```toml
[dependencies]
# Simple version
python = ">=3.11"

# Exact version
numpy = "==1.21.0"

# Version range
pandas = ">=1.0,<2.0"

# MatchSpec format
pytorch = { version = "2.0.*", channel = "pytorch" }
numpy = { version = ">=1.21", build = "py311*" }
python = { version = "3.11.0", build-number = ">=1" }

# Checksums
package = { version = "1.0.0", sha256 = "abc..." }
```

### PyPI Dependencies

**PEP 440 version specifiers:**
- `*` - Any version
- `==1.2.3` - Exact
- `>=1.2.3,<2.0` - Range
- `~=1.2.3` - Compatible

**Examples:**
```toml
[pypi-dependencies]
# Simple
requests = ">=2.25.1"

# With extras
pandas = { version = ">=1.0.0", extras = ["dataframe", "sql"] }
flask = { version = "==3.1.0", extras = ["async"] }

# Git dependencies
package = { git = "https://github.com/user/repo.git" }
package = { git = "ssh://git@github.com/user/repo.git", rev = "abc123" }
package = { git = "https://...", branch = "main" }
package = { git = "https://...", tag = "v1.0.0" }
package = { git = "https://...", subdirectory = "subdir" }

# Local path
package = { path = "./local-package", editable = true }

# Direct URL
package = { url = "https://files.pythonhosted.org/.../package.whl" }

# Custom index
package = { version = "*", index = "https://custom-index.com/simple" }
```

### Platform-Specific Dependencies

```toml
[dependencies]
cmake = "*"  # All platforms

[target.linux-64.dependencies]
glibc = "2.28"

[target.osx-arm64.dependencies]
mlx = "*"

[target.win-64.dependencies]
msmpi = "~=10.1.1"
```

### Build Dependencies

```toml
[build-dependencies]
cmake = "*"
ninja = "*"
gcc = "*"

[host-dependencies]
python = ">=3.11"
setuptools = "*"

[run-dependencies]
requests = "*"
```

## PyPI Options

```toml
[pypi-options]
# Index configuration
index-url = "https://pypi.org/simple"
extra-index-urls = ["https://custom-index.com/simple"]
find-links = [{ path = "./links" }, { url = "https://..." }]

# Build configuration
no-build-isolation = ["package1", "package2"]  # Per package
no-build-isolation = true                       # All packages
no-build = true                                 # No source builds
no-binary = ["package1"]                        # Build from source

# Resolution strategy
index-strategy = "first-index"                  # or "unsafe-first-match", "unsafe-best-match"
prerelease-mode = "allow"                       # or "disallow", "if-necessary", "explicit", "if-necessary-or-explicit"
```

## Tasks Table

### Simple Tasks

```toml
[tasks]
hello = "echo Hello World"
test = "pytest"
```

### Task with Dependencies

```toml
[tasks]
lint = "ruff check ."
fmt = "ruff format ."
build = { cmd = "cargo build", depends-on = ["fmt", "lint"] }
```

### Task with Environment Variables

```toml
[tasks]
run = { cmd = "python main.py", env = { DEBUG = "true", PORT = "8080" } }
```

### Task with Working Directory

```toml
[tasks]
build = { cmd = "npm build", cwd = "frontend" }
```

### Task with Caching

```toml
[tasks]
compile = { 
    cmd = "gcc -o output input.c", 
    inputs = ["src/*.c", "include/*.h"], 
    outputs = ["output"] 
}
```

### Task with Arguments

```toml
[tasks]
greet = { 
    cmd = "echo Hello, {{ name }}!", 
    args = [{ arg = "name", default = "World" }] 
}

build = {
    cmd = "build.sh --mode {{ mode }} --target {{ target }}",
    args = [
        { arg = "mode", default = "debug" },
        { arg = "target", default = "{{ pixi.platform }}" }
    ]
}
```

### Task with Clean Environment

```toml
[tasks]
isolated = { cmd = "python isolated.py", clean-env = true }
```

### Platform-Specific Tasks

```toml
[tasks]
clean = "rm -rf build/"

[target.win.tasks]
clean = "rmdir /s /q build"
```

### Hidden Tasks

Tasks prefixed with `_` are hidden from `pixi task list`:

```toml
[tasks]
_configure = "cmake ..."
build = { cmd = "...", depends-on = ["_configure"] }
```

## Features and Environments

### Features

Features can contain all dependency types, tasks, activation, etc.:

```toml
[feature.test.dependencies]
pytest = "*"
pytest-cov = "*"

[feature.test.tasks]
test = "pytest"

[feature.lint.dependencies]
ruff = "*"
mypy = "*"

[feature.cuda]
channels = ["nvidia"]
dependencies = { cuda = "12.1.*", cudnn = "12.0" }
pypi-dependencies = { torch = "2.0.0" }
platforms = ["linux-64"]
system-requirements = { cuda = "12.1" }
tasks = { warmup = "python warmup.py" }

[feature.cuda.target.osx-arm64.dependencies]
mlx = "*"
```

### Environments

```toml
[environments]
# Simple
default = []
test = ["test"]
dev = ["test", "lint"]

# With solve-group
prod = { features = [], solve-group = "prod" }
test-prod = { features = ["test"], solve-group = "prod" }

# Without default feature
lint = { features = ["lint"], no-default-feature = true }
```

## Activation Table

```toml
[activation]
scripts = ["setup.sh", "env.sh"]
env = { 
    MY_VAR = "value",
    PATH = "$PIXI_PROJECT_ROOT/bin:$PATH"
}

[target.win-64.activation]
scripts = ["setup.bat"]
env = { MY_VAR = "windows-value" }

[target.unix.activation.env]
PATH = "$OTHER_VAR/unix-path"

[target.win.activation.env]
PATH = "%OTHER_VAR%\\windows-path"
```

## System Requirements

```toml
[system-requirements]
linux = "5.4"                                    # Kernel version
libc = { family = "glibc", version = "2.28" }   # libc version
macos = "11.0"                                   # macOS version
cuda = "12.1"                                    # CUDA version
```

## Build Variants (Preview)

```toml
[workspace]
preview = ["pixi-build"]

[workspace.build-variants]
python = ["3.11.*", "3.12.*"]
c_compiler_version = ["11.4", "14.0"]

[workspace.target.linux-64.build-variants]
c_compiler = ["gcc"]
c_compiler_version = ["11.4", "13.0"]
```

## Package Section (Preview)

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

[package.build.config]
# Backend-specific config

[package.build-dependencies]
cmake = "*"

[package.host-dependencies]
python = ">=3.11"
setuptools = "*"

[package.run-dependencies]
requests = "*"
```

## Preview Features

Enable preview features:

```toml
[workspace]
preview = ["pixi-build"]
# or
preview = true  # Enable all preview features
```
