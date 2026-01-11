# Debugger Commands Reference

## pdb / ipdb Commands

### Execution Control

| Command | Description | Example |
|---------|-------------|---------|
| `n` (next) | Execute next line | `n` |
| `s` (step) | Step into function | `s` |
| `c` (continue) | Continue to next breakpoint | `c` |
| `u` (up) | Move up call stack | `u` |
| `d` (down) | Move down call stack | `d` |
| `q` (quit) | Quit debugger | `q` |

### Inspection

| Command | Description | Example |
|---------|-------------|---------|
| `p <var>` | Print variable | `p x` |
| `pp <var>` | Pretty print | `pp locals()` |
| `l` (list) | Show code | `l` |
| `w` (where) | Show call stack | `w` |
| `ll` | Show more code | `ll` |

### Expressions

You can execute any Python expression directly:

```python
# View variables
(Pdb) x
(Pdb) y

# Calculate expressions
(Pdb) x + y
(Pdb) len(items)

# Modify variables
(Pdb) x = 100

# Call functions
(Pdb) calculate(x, y)

# Import modules
(Pdb) import math
(Pdb) math.sqrt(16)
```

## Common Patterns

### Pattern: Inspect Function Arguments

```python
(Pdb) p operation  # Function parameter
(Pdb) p a
(Pdb) p b
(Pdb) pp locals()  # All local variables
```

### Pattern: Test Expressions

```python
# Test calculation before executing
(Pdb) a / b
# If error, fix condition

# Test different values
(Pdb) x = 100
(Pdb) x + y
```

### Pattern: Explore Call Stack

```python
(Pdb) w  # Show full stack
(Pdb) u  # Go to caller
(Pdb) p caller_var
(Pdb) d  # Return to current frame
```
