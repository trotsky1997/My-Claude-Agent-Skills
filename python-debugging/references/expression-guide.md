# Expression Usage Guide for Agents

Comprehensive guide for agents to use Python expressions in debugger for hypothesis testing, state inspection, and debugging.

## Overview

In pdb/ipdb, agents can execute **any Python expression** directly. This enables:
- Testing calculations before execution
- Modifying variables to test scenarios
- Calling functions with different parameters
- Evaluating conditions and boolean logic
- Importing modules and using their functions

## Basic Expression Types

### 1. Arithmetic Operations

```python
(Pdb) x + y
30

(Pdb) x * y
200

(Pdb) x / y
0.5

(Pdb) 2 ** 8
256

(Pdb) x % y
10
```

### 2. Variable Access and Modification

```python
# View variable
(Pdb) x
10

# Modify variable (enables testing different scenarios)
(Pdb) x = 100
(Pdb) x
100

# Test with modified value
(Pdb) calculate(x, y)
```

### 3. List Operations

```python
(Pdb) numbers
[1, 2, 3, 4, 5]

(Pdb) sum(numbers)
15

(Pdb) max(numbers)
5

(Pdb) [n * 2 for n in numbers]
[2, 4, 6, 8, 10]

(Pdb) [n for n in numbers if n > 3]
[4, 5]

(Pdb) numbers[0:3]
[1, 2, 3]
```

### 4. Dictionary Operations

```python
(Pdb) data
{'name': 'Python', 'version': 3.12}

(Pdb) data['name']
'Python'

(Pdb) data.keys()
dict_keys(['name', 'version'])

(Pdb) {k: v for k, v in data.items()}
{'name': 'Python', 'version': 3.12}

(Pdb) 'name' in data
True
```

### 5. String Operations

```python
(Pdb) text
'Hello World'

(Pdb) text.upper()
'HELLO WORLD'

(Pdb) text.lower()
'hello world'

(Pdb) len(text)
11

(Pdb) f"Message: {text}"
'Message: Hello World'

(Pdb) text.replace(' ', '_')
'Hello_World'
```

### 6. Function Calls

```python
# Built-in functions
(Pdb) abs(-10)
10

(Pdb) round(3.14159, 2)
3.14

(Pdb) len([1, 2, 3])
3

# Import and use modules
(Pdb) import math
(Pdb) math.sqrt(16)
4.0

(Pdb) import os
(Pdb) os.getcwd()
'/path/to/directory'

# Call functions from current scope
(Pdb) calculate('add', 5, 3)
8

(Pdb) process_numbers([1, 2, 3])
{'sum': 6, 'count': 3}
```

### 7. Conditional Expressions

```python
(Pdb) "positive" if x > 0 else "negative"
'positive'

(Pdb) x > 5 and x < 20
True

(Pdb) x if x > y else y
20

(Pdb) x > 0 and y > 0
True
```

### 8. Lambda Functions

```python
(Pdb) f = lambda x: x * 2
(Pdb) f(5)
10

(Pdb) list(map(lambda x: x**2, [1, 2, 3]))
[1, 4, 9]

(Pdb) sorted([3, 1, 2], key=lambda x: -x)
[3, 2, 1]
```

## Agent Debugging Scenarios

### Scenario 1: Test Calculation Before Execution

**When:** Agent suspects calculation might fail

```python
# Agent tests division before executing
(Pdb) a
10.0
(Pdb) b
2.0
(Pdb) a / b
5.0  # Safe to proceed

# Agent tests edge case
(Pdb) b = 0
(Pdb) a / b
*** ZeroDivisionError: division by zero
# Agent identifies issue and adds check
```

### Scenario 2: Test Hypothesis with Modified Values

**When:** Agent wants to test if different values cause issue

```python
# Original values
(Pdb) x
10
(Pdb) y
20

# Agent tests with different values
(Pdb) x = 100
(Pdb) calculate(x, y)  # Test with x=100

(Pdb) x = -10
(Pdb) abs(x)  # Test with negative value

(Pdb) x = 0
(Pdb) x + y  # Test with zero
```

### Scenario 3: Inspect Complex Data Structures

**When:** Agent needs to understand data structure

```python
(Pdb) items
[10, 20, 30, 40, 50]

(Pdb) len(items)
5

(Pdb) sum(items)
150

(Pdb) sum(items) / len(items)
30.0

(Pdb) [n for n in items if n > 25]
[30, 40, 50]

(Pdb) max(items)
50
```

### Scenario 4: Test Function with Different Parameters

**When:** Agent wants to verify function behavior

```python
# Agent tests function with different operations
(Pdb) calculate('add', 5, 3)
8

(Pdb) calculate('multiply', 4, 7)
28

(Pdb) calculate('divide', 10, 2)
5.0

# Agent tests error case
(Pdb) calculate('divide', 10, 0)
*** ZeroDivisionError: division by zero
```

### Scenario 5: Evaluate Conditions

**When:** Agent needs to check if condition is true

```python
(Pdb) count
105

(Pdb) count > 100
True  # Condition is met

(Pdb) x > 0 and y < 50
True

(Pdb) divisor == 0
True  # This is the problem!

(Pdb) "error" if divisor == 0 else "ok"
'error'
```

## Advanced Expression Patterns

### Multi-line Expressions

```python
(Pdb) result = (
...     x * 2
...     + y * 3
...     + 10
... )
(Pdb) result
90
```

### List Comprehensions

```python
(Pdb) [x**2 for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

(Pdb) [n for n in numbers if n % 2 == 0]
[2, 4]
```

### Generator Expressions

```python
(Pdb) sum(x**2 for x in range(10))
285

(Pdb) max(n * 2 for n in numbers)
10
```

### Exception Handling

```python
(Pdb) try:
...     result = 10 / 0
... except ZeroDivisionError as e:
...     print(f"Error: {e}")
...
Error: division by zero
```

## Expression vs Commands

| Feature | Command (`p`) | Expression (direct) |
|---------|---------------|---------------------|
| View variable | `p x` | `x` |
| Calculate | `p x + y` | `x + y` |
| Call function | `p func()` | `func()` |
| Modify variable | ❌ Not supported | ✅ `x = 10` |
| Import module | ❌ Not supported | ✅ `import os` |
| Define function | ❌ Not supported | ✅ `def f(): ...` |
| List comprehension | ❌ Not supported | ✅ `[x*2 for x in items]` |

**Recommendation:** Use expressions directly for maximum flexibility.

## Best Practices for Agents

1. **Test calculations before execution** - Verify operations won't fail
2. **Modify variables to test scenarios** - Change values to test edge cases
3. **Use expressions for hypothesis testing** - Evaluate conditions directly
4. **Import modules as needed** - Access additional functionality
5. **Use comprehensions for data analysis** - Filter and transform data structures

## Common Agent Workflows

### Workflow: Debug Division Error

```python
# Agent identifies error at division
(Pdb) a
10
(Pdb) b
0  # Problem found!

# Agent tests fix
(Pdb) a / b if b != 0 else None
None

# Agent tests with valid value
(Pdb) b = 2
(Pdb) a / b
5.0
```

### Workflow: Test Loop Condition

```python
# Agent checks loop variable
(Pdb) i
10
(Pdb) items[i]  # Test if index is valid
20

# Agent tests condition
(Pdb) i < len(items)
True

# Agent tests edge case
(Pdb) i = len(items)
(Pdb) items[i]
*** IndexError: list index out of range
```

### Workflow: Analyze Data Structure

```python
# Agent inspects data
(Pdb) data
{'count': 105, 'items': [1, 2, 3]}

# Agent analyzes
(Pdb) data['count'] > 100
True

(Pdb) len(data['items'])
3

(Pdb) sum(data['items'])
6
```

## Summary

Expressions turn the debugger into a **full Python REPL**, enabling agents to:

✅ Execute any Python expression
✅ Modify variables to test scenarios
✅ Call functions with different parameters
✅ Import modules and use their functions
✅ Test hypotheses and conditions
✅ Analyze complex data structures
✅ Test fixes before implementing them

**This is a powerful capability for autonomous debugging!**
