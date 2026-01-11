# uv build - 构建项目

## 概述

`uv build` 用于构建Python项目的分发包（wheel和sdist），用于发布到PyPI或本地分发。

## 基本用法

### 构建分发包

```bash
# 构建wheel和sdist
uv build

# 只构建wheel
uv build --wheel

# 只构建sdist（源代码分发）
uv build --sdist
```

### 输出位置

```bash
# 默认输出到dist/目录
uv build

# 指定输出目录
uv build --out-dir ./build
```

## 高级选项

### 构建配置

```bash
# 使用特定构建后端
uv build --backend hatchling

# 清理构建目录
uv build --clean

# 不运行构建钩子
uv build --no-build-isolation
```

### 发布选项

```bash
# 构建并验证
uv build --check

# 详细输出
uv build --verbose
```

## 工作流示例

### 示例1: 本地构建

```bash
# 构建分发包
uv build

# 查看生成的文件
ls dist/
# my-project-0.1.0-py3-none-any.whl
# my-project-0.1.0.tar.gz
```

### 示例2: 测试安装

```bash
# 构建
uv build

# 测试安装wheel
uv pip install dist/my-project-0.1.0-py3-none-any.whl

# 或测试sdist
uv pip install dist/my-project-0.1.0.tar.gz
```

### 示例3: 发布准备

```bash
# 构建
uv build

# 检查构建产物
uv build --check

# 上传到PyPI（使用uv publish或twine）
uv publish
```

## 构建配置

### pyproject.toml配置

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-project"
version = "0.1.0"
description = "My project"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "requests",
]

[project.scripts]
my-cli = "my_project.cli:main"
```

### 支持的构建后端

- hatchling（推荐）
- setuptools
- poetry-core
- flit
- pdm-backend

## 构建产物

### Wheel文件

`.whl` 文件是预构建的分发包：
- 安装更快
- 包含编译的扩展
- 平台特定

### Sdist文件

`.tar.gz` 文件是源代码分发：
- 包含所有源代码
- 需要构建
- 平台无关

## 最佳实践

1. **测试构建**: 构建后测试安装确保正常
2. **版本管理**: 使用语义化版本号
3. **包含必要文件**: 确保所有必要文件都包含在分发包中
4. **验证构建**: 使用 `--check` 验证构建产物

## 与标准构建工具的对比

### 传统方式

```bash
python -m build
# 或
python setup.py sdist bdist_wheel
```

### uv build方式

```bash
uv build
```

功能相似，但uv build更快且更简单。

## 故障排除

**问题**: 构建失败
- **解决**: 检查 `pyproject.toml` 配置，确保构建后端正确配置

**问题**: 缺少文件
- **解决**: 检查 `MANIFEST.in` 或构建后端配置，确保包含所有必要文件

**问题**: 版本错误
- **解决**: 检查 `pyproject.toml` 中的版本号格式
