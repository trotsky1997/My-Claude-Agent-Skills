# Codebase Reading Tool Checklist

Comprehensive tool checklist for efficient codebase reading and understanding.

## Code Search Tools

### Ripgrep (rg) - Fast Text Search

```bash
# Basic search (faster than grep)
rg "keyword" -n .

# Search with context (before/after lines)
rg "keyword" -n -C 5 .

# Search in specific file types
rg "keyword" -t rust
rg "keyword" -t py

# Case-insensitive search
rg "keyword" -i .

# Search for regex patterns
rg "function\s+\w+" .

# Find entry points
rg "main\(" .
rg "pub fn main" .

# Find public API
rg "pub fn" .
rg "pub struct" .

# Find TODOs and FIXMEs
rg "TODO|FIXME|XXX|HACK|BUG" -i .

# Exclude files/directories
rg "keyword" --glob '!node_modules' --glob '!*.min.js'
```

### Git Grep - Git-Optimized Search

```bash
# Search in tracked files only
git grep "keyword"

# Search with line numbers
git grep -n "keyword"

# Case-insensitive search
git grep -i "keyword"

# Search with context
git grep -C 3 "keyword"

# Search in specific paths
git grep "keyword" -- src/

# Find function definitions
git grep "^\s*def\|^\s*function\|^\s*pub fn"
```

### IDE/Editor Search

**VS Code:**
- `Ctrl+Shift+F` - Global search
- `Ctrl+P` - Quick file open
- `Ctrl+Shift+O` - Go to symbol in file
- `Ctrl+T` - Go to symbol in workspace

**Vim/Neovim:**
- `:grep` / `:vimgrep` - Search
- `:Rg` (with ripgrep plugin) - Fast search
- `CtrlP` / `Telescope` - File/symbol finder

## Git Tools

### Basic Git Commands

```bash
# View commit history
git log --oneline --all

# Visual history with graph
git log --graph --oneline --all

# View specific file history
git log --follow -- path/to/file

# View file changes in a commit
git show <commit-hash> -- path/to/file

# View all changes in a commit
git show <commit-hash>

# View diff between versions
git diff HEAD~5 HEAD
git diff <commit1> <commit2>

# Find when a line was changed
git blame -w -- path/to/file

# Search commit messages
git log --grep="keyword" --all

# Find commits that modified a file
git log -p -- path/to/file

# Find commits by author
git log --author="name"

# Find commits by date range
git log --since="2 weeks ago"
git log --until="2024-01-01"
```

### Git Archaeology

```bash
# Find when a bug was introduced (bisect)
git bisect start
git bisect bad
git bisect good <commit-hash>
# Test and mark good/bad until found

# Find commits touching specific code
git log -S "function_name" -- path/to/file

# Find file renames
git log --follow --name-status -- path/to/file

# View file at specific commit
git show <commit-hash>:path/to/file

# Compare branches
git log branch1..branch2
git diff branch1..branch2
```

## Language-Specific Tools

### Rust

```bash
# Build and test
cargo build
cargo build --release
cargo test
cargo test -- --nocapture

# Code quality
cargo clippy
cargo fmt --check
cargo fmt                    # Auto-format

# Documentation
cargo doc --open            # Generate and open docs
cargo doc --no-deps         # Docs without dependencies

# Dependency analysis
cargo tree                  # Dependency tree
cargo outdated              # Check for outdated deps
cargo audit                 # Security audit

# Performance analysis
cargo bench                 # Run benchmarks
cargo build --release --profile release-with-debug

# Search in Rust code
rg "pub fn" -t rust
rg "struct\s+\w+" -t rust
rg "impl\s+\w+" -t rust
```

### Python

```bash
# Run tests
pytest
pytest -v                   # Verbose
pytest path/to/test.py     # Specific test
pytest -k "test_name"      # Pattern matching

# Code quality
mypy .                      # Type checking
pylint .
black --check .            # Formatting check
black .                     # Auto-format

# Documentation
pydoc module_name
sphinx-build docs/ docs/_build/

# Dependency analysis
pip list
pip show package_name
pipdeptree                  # Dependency tree

# Search in Python code
rg "def\s+\w+" -t py
rg "class\s+\w+" -t py
rg "import\s+\w+" -t py
```

### JavaScript/TypeScript

```bash
# Build and test
npm test
npm run test:watch
npm run build

# Code quality
eslint .
tsc --noEmit               # Type checking
prettier --check .
prettier --write .         # Auto-format

# Dependency analysis
npm list
npm outdated
npm audit

# Search in JS/TS code
rg "function\s+\w+" -t js
rg "const\s+\w+\s*=" -t js
rg "export\s+(function|const|class)" -t js
```

### Go

```bash
# Build and test
go build
go test ./...
go test -v ./...

# Code quality
golint ./...
go vet ./...
go fmt ./...               # Auto-format

# Documentation
godoc -http=:6060          # Local docs server

# Dependency analysis
go list -m all
go mod graph

# Search in Go code
rg "func\s+\w+" -t go
rg "type\s+\w+" -t go
```

## Debugging Tools

### Debuggers

**Rust:**
- VS Code + CodeLLDB extension
- rust-gdb / rust-lldb
- `println!` / `dbg!` macros
- `log` crate for structured logging

**Python:**
- `pdb` - Built-in debugger
- `ipdb` - Enhanced pdb
- VS Code Python debugger
- `print()` statements (simple but effective)

**JavaScript/Node:**
- `node --inspect` - Node.js inspector
- VS Code JavaScript debugger
- Chrome DevTools
- `console.log()` / `debugger` statement

**Go:**
- `delve` (dlv) - Go debugger
- VS Code Go extension
- `fmt.Printf()` for simple debugging

### Profiling Tools

**Rust:**
- `perf` (Linux) - System profiler
- `flamegraph` - Flame graph generator
- `cargo flamegraph`

**Python:**
- `cProfile` - Built-in profiler
- `py-spy` - Sampling profiler
- `line_profiler` - Line-by-line profiler

**Node.js:**
- `clinic.js` - Performance profiling
- `0x` - Flame graph for Node.js

### Logging and Tracing

```bash
# Follow logs
tail -f logfile.log
tail -f -n 100 logfile.log  # Last 100 lines

# Search in logs
grep "ERROR" logfile.log
rg "ERROR|WARN" logfile.log

# Monitor file changes (useful for log watching)
watch -n 1 'tail -n 20 logfile.log'
```

## Code Analysis Tools

### Static Analysis

**General:**
- `grep` / `ripgrep` - Text search
- `find` - File search
- `tree` - Directory structure

**Language-specific:**
- Rust: `cargo clippy`, `cargo audit`
- Python: `pylint`, `mypy`, `bandit`
- JavaScript: `eslint`, `prettier`, `sonarjs`
- Go: `golint`, `go vet`, `staticcheck`

### Dependency Analysis

```bash
# Rust
cargo tree                 # Dependency tree
cargo outdated             # Outdated dependencies

# Python
pipdeptree                 # Dependency tree
pip list --outdated        # Outdated packages

# Node.js
npm list                   # Dependency tree
npm outdated               # Outdated packages

# Go
go list -m all            # All dependencies
go mod graph              # Dependency graph
```

## Quick Reference Commands

### Find Entry Points

```bash
# Web applications
rg "main\(" .
rg "router\|route\|controller\|handler" .
rg "app\.(get|post|put|delete)" .

# CLI applications
rg "^main\(" .
rg "CLI\|Command\|Args" .

# Libraries
rg "^pub fn" .
rg "^pub struct" .
rg "^pub mod" .
```

### Find Function Definitions

```bash
# Rust
rg "^pub fn\s+\w+" -t rust
rg "^fn\s+\w+" -t rust

# Python
rg "^def\s+\w+" -t py
rg "^async def\s+\w+" -t py

# JavaScript
rg "^function\s+\w+" -t js
rg "^const\s+\w+\s*=\s*(function|\(\))" -t js

# Go
rg "^func\s+\w+" -t go
```

### Find Class/Struct Definitions

```bash
# Rust
rg "^pub struct\s+\w+" -t rust
rg "^pub enum\s+\w+" -t rust

# Python
rg "^class\s+\w+" -t py

# JavaScript
rg "^class\s+\w+" -t js

# Go
rg "^type\s+\w+\s+(struct|interface)" -t go
```

### Find TODOs and Technical Debt

```bash
# Find all TODOs
rg "TODO|FIXME|XXX|HACK|BUG|NOTE" -i .

# Find with context
rg "TODO|FIXME" -i -C 3 .

# Count by file
rg "TODO|FIXME" -i --count .
```

## Tool Setup (10 minutes)

### Essential Tools to Install

1. **ripgrep (rg)** - Fast text search
   - `brew install ripgrep` (macOS)
   - `apt install ripgrep` (Ubuntu)
   - `cargo install ripgrep` (Rust)

2. **fd** - Fast file finder (alternative to find)
   - `brew install fd` (macOS)
   - `apt install fd-find` (Ubuntu)
   - `cargo install fd-find` (Rust)

3. **bat** - Better cat (syntax highlighting)
   - `brew install bat` (macOS)
   - `apt install bat` (Ubuntu)
   - `cargo install bat` (Rust)

4. **jq** - JSON processor
   - `brew install jq` (macOS)
   - `apt install jq` (Ubuntu)

5. **tree** - Directory tree view
   - `brew install tree` (macOS)
   - `apt install tree` (Ubuntu)

### Editor/IDE Extensions

**VS Code:**
- GitLens - Enhanced Git capabilities
- Error Lens - Inline error highlighting
- CodeLLDB / Python / Go extensions

**Vim/Neovim:**
- fzf / Telescope - Fuzzy finder
- ripgrep integration
- LSP support (rust-analyzer, pylsp, gopls)

## Efficiency Tips

1. **Use aliases:**
   ```bash
   alias ggl='git log --oneline --graph --all'
   alias ggb='git blame -w'
   alias rgg='rg --type rust'
   ```

2. **Create helper scripts:**
   ```bash
   # find-entry.sh
   rg "main\(" . && rg "router\|route" . && rg "pub fn" .
   ```

3. **Use fuzzy finders:**
   - `fzf` - General fuzzy finder
   - `Telescope` (Neovim)
   - VS Code Quick Open (`Ctrl+P`)

4. **Learn keyboard shortcuts:**
   - Your editor's "go to definition"
   - "find references"
   - "go to symbol"
