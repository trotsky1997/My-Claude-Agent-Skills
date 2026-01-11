# PowerShell script to publish Python package to PyPI
# Usage: .\publish.ps1 [--test] [--token <token>]

param(
    [switch]$Test,
    [string]$Token = ""
)

Write-Host "Running tests..." -ForegroundColor Cyan
python -m pytest tests/ -v --tb=short

if ($LASTEXITCODE -ne 0) {
    Write-Host "Tests failed! Aborting publish." -ForegroundColor Red
    exit 1
}

Write-Host "`nAll tests passed! Building package..." -ForegroundColor Green
uv build

if ($LASTEXITCODE -ne 0) {
    Write-Host "Build failed!" -ForegroundColor Red
    exit 1
}

Write-Host "Checking package..." -ForegroundColor Cyan
uvx twine check dist/*

if ($LASTEXITCODE -ne 0) {
    Write-Host "Package check failed!" -ForegroundColor Red
    exit 1
}

Write-Host "`nPackage files:" -ForegroundColor Green
Get-ChildItem dist | Format-Table Name, Length -AutoSize

if ($Test) {
    Write-Host "`nPublishing to Test PyPI..." -ForegroundColor Cyan
    $repository = "--repository testpypi"
} else {
    Write-Host "`nPublishing to Production PyPI..." -ForegroundColor Cyan
    $repository = ""
}

if ($Token) {
    $env:TWINE_USERNAME = "__token__"
    $env:TWINE_PASSWORD = $Token
    uvx twine upload $repository dist/* --non-interactive
} else {
    Write-Host "Username: __token__" -ForegroundColor Yellow
    Write-Host "Password: (your PyPI API token)" -ForegroundColor Yellow
    if ($Test) {
        uvx twine upload --repository testpypi dist/*
    } else {
        uvx twine upload dist/*
    }
}

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✓ Published successfully!" -ForegroundColor Green
    Write-Host "`nInstall with:" -ForegroundColor Cyan
    if ($Test) {
        Write-Host "  pip install -i https://test.pypi.org/simple/ your-package-name" -ForegroundColor White
    } else {
        Write-Host "  pip install your-package-name" -ForegroundColor White
    }
} else {
    Write-Host "`n✗ Publish failed!" -ForegroundColor Red
    exit 1
}
