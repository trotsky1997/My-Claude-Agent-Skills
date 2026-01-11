# Test Coverage Improvement Guide

Strategies and techniques for improving test coverage in Python projects.

## Understanding Coverage

### Coverage Types

- **Line Coverage**: Percentage of lines executed
- **Branch Coverage**: Percentage of branches taken
- **Function Coverage**: Percentage of functions called
- **Statement Coverage**: Percentage of statements executed

### Running Coverage Reports

```bash
# Terminal report
pytest --cov=package_name --cov-report=term-missing

# HTML report (detailed)
pytest --cov=package_name --cov-report=html
# Open htmlcov/index.html

# XML report (for CI/CD)
pytest --cov=package_name --cov-report=xml
```

## Coverage Configuration

### pytest.ini

```ini
[pytest]
addopts = 
    --cov=package_name
    --cov-report=term-missing
    --cov-report=html
    --cov-branch          # Include branch coverage
```

### .coveragerc

```ini
[run]
source = package_name
omit = 
    */tests/*
    */venv/*
    */__pycache__/*

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
```

## Improving Coverage

### 1. Identify Uncovered Code

```bash
# Generate report
pytest --cov=package_name --cov-report=term-missing

# Look for "Missing" column
# Example output:
# Name              Stmts   Miss  Cover   Missing
# package/module.py    100     20    80%   45-50, 60-65
```

### 2. Test Edge Cases

```python
# Original code
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Tests needed
def test_divide_normal():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_negative():
    assert divide(-10, 2) == -5
```

### 3. Test Error Paths

```python
def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        read_file("nonexistent.txt")

def test_invalid_input():
    with pytest.raises(ValueError):
        process_input(None)
```

### 4. Test All Return Paths

```python
def function(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

# Test all branches
def test_positive():
    assert function(1) == "positive"

def test_negative():
    assert function(-1) == "negative"

def test_zero():
    assert function(0) == "zero"
```

### 5. Test CLI Commands

```python
from unittest.mock import patch

def test_cli_success(capsys):
    with patch('sys.argv', ['script', 'command']):
        main()
        captured = capsys.readouterr()
        assert "success" in captured.out

def test_cli_error(capsys):
    with patch('sys.argv', ['script', 'invalid']):
        with pytest.raises(SystemExit):
            main()
```

### 6. Test Module Entry Points

```python
# test __main__.py
def test_main_module():
    import subprocess
    result = subprocess.run(
        ['python', '-m', 'package'],
        capture_output=True
    )
    assert result.returncode == 0
```

## Coverage Goals

### Realistic Targets

- **Core modules**: 90-100%
- **Business logic**: 80-90%
- **CLI/UI**: 70-80%
- **Utilities**: 60-70%

### What to Exclude

- `__init__.py` files (often just imports)
- Exception classes (if simple)
- Deprecated code
- Third-party integrations (mock instead)

## Common Coverage Issues

### Issue: Import Error Handling

```python
# Code
try:
    from optional_module import feature
except ImportError:
    feature = None

# Test
def test_with_optional_module():
    # Test when module exists
    pass

def test_without_optional_module(monkeypatch):
    # Test when module missing
    monkeypatch.setattr('sys.modules', {})
    # Test fallback behavior
```

### Issue: Conditional Imports

```python
# Test both paths
def test_with_feature():
    # When feature available
    pass

def test_without_feature(monkeypatch):
    monkeypatch.delattr('package.feature')
    # When feature unavailable
    pass
```

### Issue: Exception Handling

```python
def function():
    try:
        risky_operation()
    except SpecificError:
        handle_error()
    except Exception:
        handle_generic_error()

# Test all exception paths
def test_specific_error():
    with patch('risky_operation', side_effect=SpecificError()):
        function()  # Should call handle_error()

def test_generic_error():
    with patch('risky_operation', side_effect=Exception()):
        function()  # Should call handle_generic_error()
```

## Coverage Tools

### Coverage.py

```bash
# Install
pip install coverage

# Run
coverage run -m pytest
coverage report
coverage html
```

### pytest-cov

```bash
# Install
pip install pytest-cov

# Run
pytest --cov=package_name --cov-report=html
```

## Best Practices

### 1. Focus on Quality, Not Just Percentage

High coverage with poor tests is worse than lower coverage with good tests.

### 2. Test Behavior, Not Implementation

```python
# Good - tests behavior
def test_user_creation():
    user = create_user("test@example.com")
    assert user.email == "test@example.com"

# Bad - tests implementation details
def test_user_creation():
    user = create_user("test@example.com")
    assert user._id is not None  # Implementation detail
```

### 3. Use Coverage to Find Gaps, Not as Goal

Coverage reports help identify untested code, but 100% coverage doesn't mean bug-free code.

### 4. Test Error Cases

Many uncovered lines are error handling paths. Make sure to test them.

### 5. Review Coverage Regularly

Run coverage reports regularly and address gaps incrementally.

## Example: Improving Coverage

### Before (60% coverage)

```python
# module.py
def process_data(data):
    if not data:
        return None
    return data.upper()

# test_module.py
def test_process_data():
    assert process_data("hello") == "HELLO"
```

### After (100% coverage)

```python
# test_module.py
def test_process_data():
    assert process_data("hello") == "HELLO"

def test_process_data_empty():
    assert process_data("") is None

def test_process_data_none():
    assert process_data(None) is None
```
