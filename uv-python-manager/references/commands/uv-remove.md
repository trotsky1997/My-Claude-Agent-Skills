# uv remove - 移除依赖

## 概述

`uv remove` 用于从项目中移除依赖包，自动更新 `pyproject.toml` 和 `uv.lock` 文件。

## 基本用法

### 移除依赖

```bash
# 移除单个依赖
uv remove requests

# 移除多个依赖
uv remove requests pandas numpy

# 移除开发依赖
uv remove --dev pytest

# 移除可选依赖组中的包
uv remove --group test pytest-cov
```

### 移除依赖组

```bash
# 移除整个依赖组（需要手动编辑pyproject.toml）
# uv remove不支持直接移除组，需要手动删除
```

## 高级选项

### 同步控制

```bash
# 移除后不同步（不卸载）
uv remove --no-sync requests

# 移除后同步（默认，会卸载包）
uv remove requests  # 自动同步并卸载
```

### 从所有组移除

```bash
# 如果包在多个组中，需要分别移除
uv remove --group dev package-name
uv remove --group test package-name
uv remove package-name  # 从主依赖移除
```

## 工作流示例

### 示例1: 清理未使用的依赖

```bash
# 查看项目依赖
uv pip list

# 移除不再需要的包
uv remove old-package

# 同步环境
uv sync
```

### 示例2: 重构依赖组

```bash
# 从dev组移除
uv remove --dev old-tool

# 添加到新组
uv add --group lint new-tool
```

### 示例3: 降级依赖

```bash
# 移除当前版本
uv remove package-name

# 添加旧版本
uv add "package-name<2.0"
```

## 与pyproject.toml的关系

### 自动更新

`uv remove` 会自动更新 `pyproject.toml`:

**移除前:**
```toml
[project]
dependencies = [
    "requests",
    "pandas",
]
```

**移除后:**
```bash
uv remove requests
```

```toml
[project]
dependencies = [
    "pandas",
]
```

### 手动编辑

也可以手动编辑 `pyproject.toml` 删除依赖，然后运行：
```bash
uv sync  # 同步更改
```

## 依赖清理

### 自动清理

移除依赖后，uv会自动：
1. 更新 `pyproject.toml`
2. 更新 `uv.lock`
3. 从虚拟环境卸载包（如果使用 `--sync`）

### 孤立依赖

如果其他包依赖被移除的包，uv会：
- 检查依赖树
- 如果不再需要，也会移除
- 如果需要，会保留（因为其他包依赖）

## 最佳实践

1. **检查依赖树**: 移除前检查是否有其他包依赖它
2. **测试移除**: 移除后运行测试确保没有破坏功能
3. **提交更改**: 将 `pyproject.toml` 和 `uv.lock` 的更改提交到版本控制
4. **文档更新**: 更新项目文档说明依赖变更

## 与pip uninstall的对比

### 传统方式

```bash
pip uninstall requests
# 需要手动更新requirements.txt
```

### uv remove方式

```bash
uv remove requests
# 自动更新pyproject.toml和uv.lock
```

## 故障排除

**问题**: 移除失败，提示被其他包依赖
- **解决**: 检查依赖树，可能需要先移除依赖它的包

**问题**: 包仍在虚拟环境中
- **解决**: 运行 `uv sync` 同步环境，或手动 `uv pip uninstall`

**问题**: pyproject.toml未更新
- **解决**: 检查是否有语法错误，确保在正确的项目目录中
