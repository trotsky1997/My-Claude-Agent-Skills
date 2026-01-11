---
name: pytest-testing
description: Comprehensive guide for writing and running pytest tests in Python projects. Use when (1) Setting up pytest for a new project, (2) Writing test files and test cases, (3) Using fixtures, mocks, and parametrization, (4) Improving test coverage, (5) Debugging test failures, (6) Organizing test structure, or any Python testing tasks with pytest.
metadata:
  short-description: Write and run pytest tests for Python projects
---

# Pytest Testing Guide

Comprehensive guide for writing effective pytest tests in Python projects.

## Quick Start

### Installation

```bash
pip install pytest pytest-cov
# Or with uv
uv pip install pytest pytest-cov
```

### Basic Test Structure

```python
# tests/test_example.py
def test_addition():
    assert 1 + 1 == 2

def test_string_concatenation():
    assert "hello" + " " + "world" == "hello world"
```

### Running Tests

```bash
pytest                    # Run all tests
pytest tests/             # Run tests in directory
pytest tests/test_models.py::TestClass::test_method  # Run specific test
pytest -v                # Verbose output
pytest --cov=package     # With coverage
```

## Test Organization

### File Structure

```
project/
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Shared fixtures
│   ├── test_models.py       # Model tests
│   ├── test_api.py          # API tests
│   └── test_cli.py          # CLI tests
└── pytest.ini              # Configuration
```

### Naming Conventions

- Test files: `test_*.py` or `*_test.py`
- Test classes: `Test*`
- Test functions: `test_*`

## Fixtures

Fixtures provide reusable test data and setup/teardown logic.

### Basic Fixture

```python
# conftest.py
import pytest

@pytest.fixture
def sample_data():
    """Create sample test data"""
    return {"key": "value"}

# test_file.py
def test_something(sample_data):
    assert sample_data["key"] == "value"
```

### Fixture Scopes

- `function` (default): Each test function
- `class`: Each test class
- `module`: Each test module
- `session`: Entire test session

```python
@pytest.fixture(scope="session")
def expensive_setup():
    """Run once per test session"""
    return expensive_operation()
```

### Built-in Fixtures

- `tmp_path`: Temporary directory (Path object)
- `capsys`: Capture stdout/stderr
- `monkeypatch`: Temporarily modify environment
- `request`: Access test context

### Fixture with Dependencies

```python
@pytest.fixture
def sample_file(tmp_path):
    """Create temporary file"""
    file_path = tmp_path / "test.txt"
    file_path.write_text("test content")
    return str(file_path)
```

## Assertions

Pytest uses Python's `assert` statement with detailed failure information.

```python
def test_assertions():
    # Basic
    assert 1 + 1 == 2
    
    # Membership
    assert "test" in "this is a test"
    
    # Type checking
    assert isinstance([1, 2, 3], list)
    
    # Exception testing
    with pytest.raises(ValueError):
        int("not a number")
    
    # Exception message matching
    with pytest.raises(ValueError, match="invalid"):
        raise ValueError("invalid input")
```

## Parametrized Tests

Run the same test with multiple inputs:

```python
@pytest.mark.parametrize("input,expected", [
    ("hello", 5),
    ("world", 5),
    ("", 0),
])
def test_string_length(input, expected):
    assert len(input) == expected
```

## Mocking and Patching

Use `unittest.mock` to isolate code under test:

```python
from unittest.mock import patch, MagicMock

def test_with_mock(capsys):
    with patch('sys.argv', ['script', 'arg1']):
        main()
        captured = capsys.readouterr()
        assert "expected" in captured.out

def test_mock_object():
    mock_obj = MagicMock()
    mock_obj.method.return_value = "result"
    assert mock_obj.method() == "result"
    mock_obj.method.assert_called_once()
```

## Test Coverage

### Running Coverage

```bash
pytest --cov=package_name --cov-report=term-missing
pytest --cov=package_name --cov-report=html
```

### Configuration (pytest.ini)

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --cov=package_name
    --cov-report=term-missing
    --cov-report=html
```

## Best Practices

### 1. Test Independence

Each test should be independent and not rely on execution order:

```python
# Good
def test_create():
    obj = create_object()
    assert obj is not None

# Bad - depends on global state
global_obj = None
def test_create():
    global global_obj
    global_obj = create_object()
```

### 2. Use Fixtures, Not Globals

```python
# Good
@pytest.fixture
def sample_data():
    return {"key": "value"}

def test_something(sample_data):
    assert sample_data["key"] == "value"
```

### 3. Test Edge Cases

Test both happy paths and edge cases:

```python
def test_normal_case():
    result = function("normal input")
    assert result == expected

def test_empty_input():
    result = function("")
    assert result == default

def test_none_input():
    with pytest.raises(ValueError):
        function(None)
```

### 4. Descriptive Test Names

Use clear, descriptive names:

```python
# Good
def test_find_user_by_email_returns_user():
    pass

# Bad
def test1():
    pass
```

### 5. Test Documentation

Add docstrings to explain test purpose:

```python
def test_find_by_name_fuzzy():
    """Test fuzzy name search finds partial matches"""
    # test code
```

## Common Patterns

### Testing CLI Commands

```python
from unittest.mock import patch

def test_cli_command(capsys):
    with patch('sys.argv', ['script', 'command', 'arg']):
        main()
        captured = capsys.readouterr()
        assert "expected output" in captured.out
```

### Testing Exceptions

```python
def test_invalid_input():
    with pytest.raises(ValueError) as exc_info:
        function("invalid")
    assert "error message" in str(exc_info.value)
```

### Testing File Operations

```python
def test_file_operations(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("content")
    assert file_path.read_text() == "content"
```

### Testing with Database

```python
@pytest.fixture
def db_session():
    # Setup database
    session = create_session()
    yield session
    # Teardown
    session.close()
```

## Advanced Features

### Markers

```python
@pytest.mark.slow
def test_expensive_operation():
    pass

# Run only fast tests
pytest -m "not slow"
```

### Skipping Tests

```python
@pytest.mark.skip(reason="Not implemented yet")
def test_future_feature():
    pass

@pytest.mark.skipif(sys.version_info < (3, 8), reason="Requires Python 3.8+")
def test_python38_feature():
    pass
```

### Expected Failures

```python
@pytest.mark.xfail(reason="Known bug, fixing")
def test_known_bug():
    assert False
```

## Debugging Tests

### Run with Output

```bash
pytest -s              # Show print statements
pytest -v              # Verbose output
pytest --pdb           # Drop into debugger on failure
pytest --tb=short      # Shorter traceback
```

### Run Last Failed

```bash
pytest --lf            # Run last failed tests
pytest --ff            # Run failed first, then others
```

## Configuration Examples

### pytest.ini

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    -v
    --strict-markers
    --tb=short
    --cov=package_name
    --cov-report=term-missing
    --cov-report=html

markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### pyproject.toml

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
addopts = "-v --tb=short"
```

## Common Issues and Solutions

### Import Errors

Ensure test directory is in Python path or use `-e` install:

```bash
pip install -e .
```

### Fixture Not Found

Check fixture is defined in `conftest.py` or same test file.

### Coverage Not Working

Ensure `pytest-cov` is installed and package name is correct.

### Tests Not Running

Check file naming (`test_*.py`) and function naming (`test_*`).

## Integration with CI/CD

### GitHub Actions Example

```yaml
- name: Run tests
  run: |
    pip install pytest pytest-cov
    pytest --cov=package --cov-report=xml
```

## References

- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)
- See `references/advanced-patterns.md` for complex testing scenarios
- See `references/coverage-improvement.md` for coverage optimization strategies
