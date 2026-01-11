# uv tool - 工具管理

## 概述

`uv tool` 用于安装和管理Python工具（类似pipx），可以在隔离环境中运行工具，无需激活虚拟环境。

## 基本用法

### 安装工具

```bash
# 安装工具
uv tool install black

# 安装特定版本
uv tool install "black==23.0.0"

# 安装多个工具
uv tool install black ruff mypy
```

### 运行工具

```bash
# 运行已安装的工具
uv tool run black .

# 运行并传递参数
uv tool run ruff check --fix

# 临时安装并运行（不持久化）
uv tool run --with black black .
```

### 列出工具

```bash
# 列出所有已安装的工具
uv tool list

# 显示工具信息
uv tool show black
```

### 卸载工具

```bash
# 卸载工具
uv tool uninstall black

# 卸载多个工具
uv tool uninstall black ruff
```

## 高级选项

### 版本管理

```bash
# 安装特定版本
uv tool install "black==23.0.0"

# 升级工具
uv tool install --upgrade black

# 升级所有工具
uv tool install --upgrade-all
```

### 从不同源安装

```bash
# 从Git仓库安装
uv tool install git+https://github.com/user/tool.git

# 从本地路径安装
uv tool install ./local-tool

# 从URL安装
uv tool install https://example.com/tool.whl
```

### 运行选项

```bash
# 使用特定Python版本
uv tool run --python 3.12 black .

# 传递环境变量
uv tool run --env VAR=value tool-name

# 在指定目录运行
uv tool run --cwd /path/to/dir tool-name
```

## 工作流示例

### 示例1: 代码格式化工具

```bash
# 安装格式化工具
uv tool install black ruff

# 格式化代码
uv tool run black .
uv tool run ruff check --fix
```

### 示例2: 开发工具链

```bash
# 安装开发工具
uv tool install pytest black mypy ruff

# 运行测试
uv tool run pytest

# 类型检查
uv tool run mypy .

# 代码检查
uv tool run ruff check .
```

### 示例3: 临时使用工具

```bash
# 不安装，直接运行
uv tool run --with requests python -c "import requests; print(requests.__version__)"

# 或使用uvx（如果可用）
uvx requests python -c "import requests; print(requests.__version__)"
```

## 工具存储

### 存储位置

uv tool将工具安装在：
- **macOS/Linux**: `~/.local/share/uv/tools/`
- **Windows**: `%LOCALAPPDATA%\uv\tools\`

### 环境隔离

每个工具都在独立的虚拟环境中运行，互不干扰。

## 与pipx的对比

### pipx方式

```bash
pipx install black
pipx run black .
```

### uv tool方式

```bash
uv tool install black
uv tool run black .
```

功能相似，但uv tool更快。

## 常用工具

### 代码格式化

```bash
uv tool install black
uv tool install ruff  # 也支持格式化
```

### 类型检查

```bash
uv tool install mypy
uv tool install pyright
```

### 测试工具

```bash
uv tool install pytest
uv tool install pytest-cov
```

### 构建工具

```bash
uv tool install build
uv tool install twine
```

## 最佳实践

1. **工具隔离**: 使用uv tool而不是全局安装，保持系统Python干净
2. **版本固定**: 对于CI/CD，固定工具版本
3. **定期更新**: 定期更新工具以获取新功能和修复
4. **文档化**: 在项目文档中记录使用的工具

## 故障排除

**问题**: 工具安装失败
- **解决**: 检查工具名称是否正确，网络连接是否正常

**问题**: 工具运行失败
- **解决**: 检查工具是否正确安装，使用 `uv tool list` 查看

**问题**: 找不到工具
- **解决**: 确保工具已安装，使用 `uv tool list` 查看已安装的工具
