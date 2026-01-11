# uv publish - 发布到PyPI

## 概述

`uv publish` 用于将构建的分发包发布到PyPI（Python Package Index）或其他索引服务器。

## 基本用法

### 发布到PyPI

```bash
# 构建并发布
uv publish

# 只发布（需要先构建）
uv publish --no-build

# 发布到测试PyPI
uv publish --repository testpypi
```

### 指定文件

```bash
# 发布特定文件
uv publish dist/my-project-0.1.0-py3-none-any.whl

# 发布多个文件
uv publish dist/*.whl dist/*.tar.gz
```

## 高级选项

### 仓库配置

```bash
# 发布到特定仓库
uv publish --repository pypi

# 发布到测试仓库
uv publish --repository testpypi

# 使用自定义仓库
uv publish --repository https://custom-pypi.com/
```

### 认证

```bash
# 使用API token（推荐）
export UV_PUBLISH_TOKEN="pypi-..."

# 使用用户名密码
uv publish --username your-username --password your-password

# 从配置文件读取
# 在pyproject.toml中配置
```

### 发布选项

```bash
# 跳过现有版本检查
uv publish --skip-existing

# 只发布wheel
uv publish --wheel-only

# 只发布sdist
uv publish --sdist-only
```

## 配置

### pyproject.toml配置

```toml
[tool.uv.publish]
repository = "pypi"  # 或 "testpypi"
username = "your-username"  # 可选，建议使用token
```

### 环境变量

```bash
# PyPI API token
export UV_PUBLISH_TOKEN="pypi-..."

# 测试PyPI token
export UV_PUBLISH_TEST_TOKEN="pypi-..."

# 仓库URL
export UV_PUBLISH_REPOSITORY="https://pypi.org/"
```

## 工作流示例

### 示例1: 首次发布

```bash
# 1. 构建
uv build

# 2. 检查构建产物
ls dist/

# 3. 测试安装
uv pip install dist/my-project-0.1.0-py3-none-any.whl

# 4. 发布到测试PyPI
uv publish --repository testpypi

# 5. 测试从测试PyPI安装
uv pip install --index-url https://test.pypi.org/simple/ my-project

# 6. 发布到正式PyPI
uv publish
```

### 示例2: 更新版本

```bash
# 1. 更新版本号（在pyproject.toml中）
# version = "0.2.0"

# 2. 更新锁文件
uv lock

# 3. 构建
uv build

# 4. 发布
uv publish
```

### 示例3: 使用CI/CD

```yaml
# GitHub Actions示例
- name: Publish to PyPI
  env:
    UV_PUBLISH_TOKEN: ${{ secrets.PYPI_API_TOKEN }}
  run: |
    uv build
    uv publish
```

## 认证方式

### API Token（推荐）

1. 在PyPI创建API token
2. 设置环境变量：
   ```bash
   export UV_PUBLISH_TOKEN="pypi-..."
   ```
3. 发布：
   ```bash
   uv publish
   ```

### 用户名密码

```bash
uv publish --username your-username --password your-password
```

**注意**: 不推荐，建议使用API token。

### 配置文件

在 `~/.pypirc` 或 `pyproject.toml` 中配置：

```toml
[tool.uv.publish]
repository = "pypi"
username = "your-username"
password = "your-password"  # 或使用环境变量
```

## 最佳实践

1. **使用测试PyPI**: 首次发布前先在测试PyPI测试
2. **使用API token**: 比用户名密码更安全
3. **版本管理**: 遵循语义化版本规范
4. **测试安装**: 发布后测试从PyPI安装
5. **文档更新**: 确保README和文档是最新的

## 与twine的对比

### 传统方式

```bash
python -m build
twine upload dist/*
```

### uv publish方式

```bash
uv build
uv publish
```

功能相似，但uv publish更简单且更快。

## 故障排除

**问题**: 认证失败
- **解决**: 检查token是否正确，确保有发布权限

**问题**: 版本已存在
- **解决**: 更新版本号，或使用 `--skip-existing`（不推荐）

**问题**: 上传失败
- **解决**: 检查网络连接，确保PyPI可访问

**问题**: 文件太大
- **解决**: 检查分发包大小，PyPI有大小限制
