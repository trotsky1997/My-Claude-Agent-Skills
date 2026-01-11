# Pixi Commands Reference

Complete reference for all Pixi CLI commands.

## Workspace Management

### `pixi init`

Create a new Pixi workspace.

```bash
pixi init [project-name]
pixi init --format pyproject
pixi init --channel conda-forge --channel pytorch
pixi init --platform linux-64 --platform osx-64
```

### `pixi add`

Add dependencies to the workspace.

```bash
# Conda packages
pixi add python
pixi add python ">=3.11"
pixi add numpy pandas matplotlib

# PyPI packages
pixi add --pypi requests
pixi add --pypi "flask[async]==3.1.0"

# Feature-specific
pixi add --feature test pytest
pixi add --feature dev ipython

# Platform-specific
pixi add --platform linux-64 glibc
pixi add --platform osx-arm64 mlx

# Build dependencies
pixi add --build cmake ninja
pixi add --host python setuptools

# Channel specification
pixi add pytorch --channel pytorch
pixi add pytorch::pytorch  # Shorthand

# MatchSpec format
pixi add "pytorch=2.0.*=cuda*"
pixi add "numpy[version='>=1.21',build='py311*']"
```

### `pixi remove`

Remove dependencies from the workspace.

```bash
pixi remove numpy
pixi remove --feature test pytest
pixi remove --platform linux-64 glibc
pixi remove --build cmake
pixi remove --host setuptools
```

### `pixi update`

Update dependencies within their constraints.

```bash
pixi update                    # Update all
pixi update numpy             # Update specific package
pixi update --environment test # Update specific environment
pixi update --all             # Update all environments
```

### `pixi upgrade`

Upgrade dependencies to latest versions (ignores pins).

```bash
pixi upgrade                   # Upgrade all
pixi upgrade numpy            # Upgrade specific package
pixi upgrade --environment test
```

### `pixi lock`

Generate or update the lockfile without installing.

```bash
pixi lock
pixi lock --environment test
pixi lock --all
```

### `pixi install`

Install the environment.

```bash
pixi install                   # Install default environment
pixi install --environment test
pixi install --frozen          # Use lockfile as-is
pixi install --locked          # Only if lockfile matches
pixi install --all             # Install all environments
```

### `pixi reinstall`

Force reinstall the environment.

```bash
pixi reinstall
pixi reinstall --environment test
```

## Running Commands

### `pixi run`

Run a task or command in the environment.

```bash
pixi run python script.py
pixi run pytest
pixi run --environment test pytest
pixi run --clean-env python isolated.py
pixi run task-name arg1 arg2
```

### `pixi shell`

Activate a shell in the environment.

```bash
pixi shell
pixi shell --environment test
pixi shell --frozen
pixi shell --locked
```

### `pixi shell-hook`

Print environment activation script.

```bash
pixi shell-hook
pixi shell-hook --environment test
eval "$(pixi shell-hook)"  # Use in shell config
```

### `pixi exec`

Run a command in a temporary environment.

```bash
pixi exec python --version
pixi exec --spec "python=3.12" python --version
pixi exec --spec "python>=3.11" pytest
```

## Task Management

### `pixi task add`

Add a task to the manifest.

```bash
pixi task add build "cargo build"
pixi task add test "pytest" --depends-on build
pixi task add lint "ruff check ." --feature dev
pixi task add run "python main.py" --cwd scripts
pixi task add compile "gcc -o output input.c" --inputs "*.c" --outputs "output"
```

### `pixi task remove`

Remove a task from the manifest.

```bash
pixi task remove build
pixi task remove --feature dev lint
```

### `pixi task list`

List all tasks.

```bash
pixi task list
pixi task list --environment test
```

## Environment Management

### `pixi list`

List installed packages.

```bash
pixi list                      # All packages
pixi list --environment test
pixi list --explicit          # Only explicitly installed
pixi list numpy               # Specific package
```

### `pixi tree`

Show dependency tree.

```bash
pixi tree                      # Full tree
pixi tree --environment test
pixi tree numpy               # Tree for specific package
pixi tree --invert numpy      # Reverse dependencies
pixi tree --depth 2           # Limit depth
```

### `pixi clean`

Remove environments and cache.

```bash
pixi clean                     # Remove all environments
pixi clean --environment test # Remove specific environment
pixi clean cache              # Clear package cache
```

### `pixi info`

Show workspace and system information.

```bash
pixi info                      # Basic info
pixi info -v                   # Verbose
pixi info -vv                  # More verbose
pixi info -vvv                 # Show config locations
```

## Global Tools

### `pixi global install`

Install global CLI tools.

```bash
pixi global install gh
pixi global install gh nvim ipython btop
pixi global install --channel pytorch pytorch
```

### `pixi global uninstall`

Uninstall global tools.

```bash
pixi global uninstall gh
```

### `pixi global add`

Add packages to existing global environment.

```bash
pixi global add nvim ripgrep
```

### `pixi global update`

Update global environments.

```bash
pixi global update             # Update all
pixi global update gh          # Update specific tool
```

### `pixi global list`

List global installations.

```bash
pixi global list
```

### `pixi global sync`

Sync global environments with manifest.

```bash
pixi global sync
```

### `pixi global edit`

Edit the global manifest.

```bash
pixi global edit
```

### `pixi global tree`

Show dependency tree for global environment.

```bash
pixi global tree gh
```

### `pixi global expose`

Expose executables from global environment.

```bash
pixi global expose gh
```

### `pixi global shortcut`

Manage shortcuts for global tools.

```bash
pixi global shortcut add gh g
pixi global shortcut remove g
```

## Workspace Commands

### `pixi workspace channel add`

Add channel to workspace.

```bash
pixi workspace channel add pytorch
pixi workspace channel add https://prefix.dev/channels/custom
```

### `pixi workspace channel remove`

Remove channel from workspace.

```bash
pixi workspace channel remove pytorch
```

### `pixi workspace platform add`

Add platform to workspace.

```bash
pixi workspace platform add osx-arm64
```

### `pixi workspace platform remove`

Remove platform from workspace.

```bash
pixi workspace platform remove osx-arm64
```

### `pixi workspace environment add`

Add environment to workspace.

```bash
pixi workspace environment add test --feature test
pixi workspace environment add prod --solve-group prod
```

### `pixi workspace environment remove`

Remove environment from workspace.

```bash
pixi workspace environment remove test
```

## Configuration

### `pixi config`

Manage Pixi configuration.

```bash
pixi config list               # List all config
pixi config list --local       # Project config
pixi config list --global      # Global config

pixi config set pinning-strategy semver
pixi config set shell.change-ps1 false
pixi config set --local concurrency.solves 1

pixi config get pinning-strategy
pixi config unset pinning-strategy

pixi config edit               # Edit config file
pixi config edit --local
pixi config edit --global

pixi config append pypi-config.extra-index-urls "https://custom"
pixi config prepend pypi-config.extra-index-urls "https://first"
```

## Authentication

### `pixi auth login`

Login to private channels.

```bash
pixi auth login
pixi auth login --channel prefix-dev
pixi auth login --channel https://prefix.dev/channels/private
```

### `pixi auth logout`

Logout from channels.

```bash
pixi auth logout
pixi auth logout --channel prefix-dev
```

## Search

### `pixi search`

Search for packages.

```bash
pixi search numpy
pixi search --channel pytorch torch
```

## Completion

### `pixi completion`

Generate shell completion scripts.

```bash
pixi completion --shell bash
pixi completion --shell zsh
pixi completion --shell fish
pixi completion --shell powershell
pixi completion --shell nushell
```

Usage:
```bash
# Bash
eval "$(pixi completion --shell bash)"

# Zsh
eval "$(pixi completion --shell zsh)"

# Fish
pixi completion --shell fish | source
```

## Build (Preview)

### `pixi build`

Build a conda package.

```bash
pixi build
pixi build --output ./output
```

## Import

### `pixi import`

Import environment from other formats.

```bash
pixi import requirements.txt
pixi import environment.yml
pixi import poetry.lock
```

## Self Update

### `pixi self-update`

Update Pixi itself.

```bash
pixi self-update               # Update to latest
pixi self-update --version 0.40.0  # Specific version
```

## Help

### `pixi help`

Show help information.

```bash
pixi help
pixi help add
pixi help run
```
