# uv init - 初始化项目

## 概述

`uv init` 用于创建新的Python项目，自动生成项目结构和配置文件。

## 基本用法

### 创建新项目

```bash
# 在当前目录初始化项目
uv init

# 创建新目录并初始化
uv init my-project

# 创建嵌套目录
uv init path/to/my-project
```

### 项目类型

```bash
# 标准项目（默认）
uv init my-project

# 工作区项目
uv init --workspace my-workspace

# 库项目
uv init --lib my-library

# 应用程序项目
uv init --app my-app
```

## 生成的文件

### 标准项目结构

```
my-project/
├── pyproject.toml      # 项目配置
├── README.md           # 项目说明
└── src/                # 源代码目录（可选）
    └── my_project/
        └── __init__.py
```

### pyproject.toml示例

```toml
[project]
name = "my-project"
version = "0.1.0"
description = ""
readme = "README.md"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## 高级选项

### 指定Python版本

```bash
# 设置最低Python版本
uv init --python 3.12 my-project

# 在pyproject.toml中设置requires-python
```

### 添加初始依赖

```bash
# 初始化时添加依赖
uv init --dependency requests --dependency click my-project

# 添加开发依赖
uv init --dev-dependency pytest --dev-dependency black my-project
```

### 工作区配置

```bash
# 创建工作区
uv init --workspace my-workspace

# 工作区结构
my-workspace/
├── pyproject.toml      # 工作区配置
└── packages/            # 子项目目录
```

### 源代码布局

```bash
# 使用src布局（默认）
uv init --src my-project

# 不使用src布局
uv init --no-src my-project
```

## 工作流示例

### 示例1: 创建CLI工具

```bash
# 创建项目
uv init my-cli-tool

# 添加依赖
cd my-cli-tool
uv add click rich

# 创建CLI入口
# src/my_cli_tool/cli.py
```

### 示例2: 创建库项目

```bash
# 创建库项目
uv init --lib my-library

# 添加依赖
cd my-library
uv add requests

# 开发依赖
uv add --dev pytest black mypy
```

### 示例3: 创建工作区

```bash
# 创建工作区
uv init --workspace my-monorepo

# 添加子项目
cd my-monorepo
uv init --package package-a
uv init --package package-b
```

## 项目配置

### pyproject.toml结构

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My project description"
readme = "README.md"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "you@example.com"}
]
requires-python = ">=3.11"
dependencies = [
    "requests>=2.28.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "black",
]

[project.scripts]
my-cli = "my_project.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### 自定义配置

初始化后可以手动编辑 `pyproject.toml` 添加：
- 项目URLs
- 分类器
- 关键词
- 入口点
- 等等

## 与现有项目集成

### 在现有目录初始化

```bash
# 在已有代码的目录中
cd existing-project
uv init

# 会创建pyproject.toml，不会覆盖现有文件
```

### 从requirements.txt迁移

```bash
# 初始化项目
uv init my-project

# 从requirements.txt添加依赖
cd my-project
uv add $(cat ../requirements.txt)
```

## 最佳实践

1. **使用描述性名称**: 项目名称应该清晰描述项目用途
2. **设置Python版本**: 明确指定最低Python版本要求
3. **添加README**: 初始化后立即编写项目说明
4. **配置许可证**: 在pyproject.toml中设置许可证信息

## 故障排除

**问题**: 初始化失败
- **解决**: 检查目录权限，确保有写入权限

**问题**: 项目名称冲突
- **解决**: 使用不同的项目名称，或删除现有目录

**问题**: 依赖添加失败
- **解决**: 初始化后使用 `uv add` 单独添加依赖
