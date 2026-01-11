# Advanced Pytest Patterns

Advanced patterns and techniques for complex testing scenarios.

## Testing Async Code

```python
import pytest
import asyncio

@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result == expected
```

## Testing with Context Managers

```python
def test_with_context_manager():
    with some_context() as ctx:
        result = ctx.do_something()
        assert result == expected
```

## Testing Generators

```python
def test_generator():
    gen = my_generator()
    assert next(gen) == first_value
    assert next(gen) == second_value
```

## Custom Fixtures with Teardown

```python
@pytest.fixture
def resource_with_cleanup():
    # Setup
    resource = create_resource()
    yield resource
    # Teardown (always runs)
    resource.cleanup()
```

## Fixture Parametrization

```python
@pytest.fixture(params=["option1", "option2"])
def config(request):
    return create_config(request.param)

def test_with_config(config):
    assert config is not None
```

## Testing with Temporary Files

```python
def test_with_temp_file(tmp_path):
    file_path = tmp_path / "data.json"
    file_path.write_text('{"key": "value"}')
    
    result = process_file(str(file_path))
    assert result == expected
```

## Testing Environment Variables

```python
def test_env_var(monkeypatch):
    monkeypatch.setenv("API_KEY", "test-key")
    assert os.getenv("API_KEY") == "test-key"
```

## Testing with Time

```python
from unittest.mock import patch
from datetime import datetime

@patch('mymodule.datetime')
def test_time_dependent(mock_datetime):
    mock_datetime.now.return_value = datetime(2024, 1, 1)
    result = time_dependent_function()
    assert result == expected
```

## Testing HTTP Requests

```python
import responses

@responses.activate
def test_api_call():
    responses.add(
        responses.GET,
        'https://api.example.com/data',
        json={'key': 'value'},
        status=200
    )
    result = make_api_call()
    assert result == {'key': 'value'}
```

## Testing Database Transactions

```python
@pytest.fixture
def db_transaction(db_session):
    transaction = db_session.begin()
    yield transaction
    transaction.rollback()
```

## Testing with Multiple Fixtures

```python
def test_multiple_fixtures(fixture1, fixture2, fixture3):
    result = function(fixture1, fixture2, fixture3)
    assert result == expected
```

## Conditional Test Execution

```python
import sys

@pytest.mark.skipif(
    sys.platform == "win32",
    reason="Not supported on Windows"
)
def test_unix_only():
    pass
```

## Testing Class Methods

```python
class TestMyClass:
    def test_method(self):
        obj = MyClass()
        assert obj.method() == expected
    
    @classmethod
    def test_class_method(cls):
        assert MyClass.class_method() == expected
```

## Testing Private Methods

```python
def test_private_method():
    obj = MyClass()
    # Access private method
    result = obj._private_method()
    assert result == expected
```

## Testing with Mocks and Spies

```python
from unittest.mock import Mock, MagicMock, call

def test_mock_calls():
    mock = Mock()
    function_under_test(mock)
    mock.method.assert_called_once_with(arg1, arg2)
    assert mock.method.call_count == 1

def test_spy():
    real_obj = RealObject()
    spy = MagicMock(wraps=real_obj)
    function_using_object(spy)
    spy.method.assert_called()
```

## Testing Exceptions in Context

```python
def test_exception_context():
    with pytest.raises(ValueError) as exc_info:
        function_that_raises()
    
    assert exc_info.value.args[0] == "expected message"
    assert exc_info.type == ValueError
```

## Parallel Test Execution

```bash
pip install pytest-xdist
pytest -n auto  # Use all CPUs
pytest -n 4     # Use 4 workers
```

## Test Discovery Customization

```python
# pytest_collect_file hook
def pytest_collect_file(parent, path):
    if path.ext == ".py" and path.basename.startswith("test_"):
        return pytest.Module.from_parent(parent, path=path)
```
