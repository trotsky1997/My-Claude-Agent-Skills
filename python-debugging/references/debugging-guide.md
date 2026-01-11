# Python Debugging Guide

## Debugging Strategies

### 1. Function Entry Debugging

Set breakpoints at function entries to inspect parameters and initial state.

```bash
# Find function entries
python scripts/smart_breakpoint_suggester.py script.py --only functions

# Insert at function entry
python scripts/insert_breakpoint.py script.py --line 10 --method pdb
```

### 2. Loop Debugging

Debug loops by setting breakpoints or conditional breakpoints.

```bash
# Only pause on specific iteration
python scripts/conditional_breakpoint.py script.py --line 15 --condition "i == 10"
```

### 3. Error Condition Debugging

Set conditional breakpoints for error-prone conditions.

```bash
# Only pause when error condition occurs
python scripts/conditional_breakpoint.py script.py --line 20 --condition "divisor == 0"
```

### 4. Performance Debugging

Use Python's cProfile to identify performance bottlenecks.

```python
import cProfile
import pstats

profiler = cProfile.Profile()
profiler.enable()

# Your code here

profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)
```

## Best Practices

1. **Use smart suggestions first** - Let AI find optimal breakpoint locations
2. **Clean up breakpoints** - Always remove breakpoints after debugging
3. **Use conditional breakpoints** - Avoid unnecessary pauses in loops
4. **Combine tools** - Use suggestions + breakpoint insertion + auto debug
5. **Record debugging sessions** - Keep notes for complex bugs

## Common Scenarios

### Scenario: Debug Divide by Zero

```bash
# 1. Find division operation
python scripts/smart_breakpoint_suggester.py script.py --only assignments

# 2. Insert conditional breakpoint
python scripts/conditional_breakpoint.py script.py --line 18 --condition "b == 0"

# 3. Run debugging
python script.py
# Pauses only when b == 0

# 4. Clean up
python scripts/insert_breakpoint.py script.py --remove-all
```

### Scenario: Debug Loop Performance

```bash
# 1. Get loop suggestions
python scripts/smart_breakpoint_suggester.py script.py --only loops

# 2. Insert breakpoint at loop start
python scripts/insert_breakpoint.py script.py --line 15 --method pdb

# 3. Run and check variables
python script.py
# (Pdb) p i
# (Pdb) p items[i]
```

### Scenario: Debug Function Call Chain

```bash
# 1. Get all function suggestions
python scripts/smart_breakpoint_suggester.py script.py --only functions --max 10

# 2. Insert breakpoints at multiple functions
python scripts/insert_breakpoint.py script.py --line 10 --method pdb
python scripts/insert_breakpoint.py script.py --line 25 --method pdb

# 3. Use call stack commands
python script.py
# (Pdb) w  # Show call stack
# (Pdb) u  # Move up stack
# (Pdb) d  # Move down stack
```
