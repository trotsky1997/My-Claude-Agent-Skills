#!/bin/bash
# Bash script to publish Python package to PyPI
# Usage: ./publish.sh [--test] [--token <token>]

TEST_PYPI=false
TOKEN=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --test)
            TEST_PYPI=true
            shift
            ;;
        --token)
            TOKEN="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "Running tests..."
python -m pytest tests/ -v --tb=short

if [ $? -ne 0 ]; then
    echo "Tests failed! Aborting publish."
    exit 1
fi

echo ""
echo "All tests passed! Building package..."
uv build

if [ $? -ne 0 ]; then
    echo "Build failed!"
    exit 1
fi

echo "Checking package..."
uvx twine check dist/*

if [ $? -ne 0 ]; then
    echo "Package check failed!"
    exit 1
fi

echo ""
echo "Package files:"
ls -lh dist/

if [ "$TEST_PYPI" = true ]; then
    echo ""
    echo "Publishing to Test PyPI..."
    REPO_FLAG="--repository testpypi"
else
    echo ""
    echo "Publishing to Production PyPI..."
    REPO_FLAG=""
fi

if [ -n "$TOKEN" ]; then
    export TWINE_USERNAME="__token__"
    export TWINE_PASSWORD="$TOKEN"
    uvx twine upload $REPO_FLAG dist/* --non-interactive
else
    echo "Username: __token__"
    echo "Password: (your PyPI API token)"
    if [ "$TEST_PYPI" = true ]; then
        uvx twine upload --repository testpypi dist/*
    else
        uvx twine upload dist/*
    fi
fi

if [ $? -eq 0 ]; then
    echo ""
    echo "✓ Published successfully!"
    echo ""
    echo "Install with:"
    if [ "$TEST_PYPI" = true ]; then
        echo "  pip install -i https://test.pypi.org/simple/ your-package-name"
    else
        echo "  pip install your-package-name"
    fi
else
    echo ""
    echo "✗ Publish failed!"
    exit 1
fi
