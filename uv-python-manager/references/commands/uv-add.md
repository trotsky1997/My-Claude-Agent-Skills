# uv add - 添加依赖

## 概述

`uv add` 用于向项目添加依赖包，自动更新 `pyproject.toml` 和 `uv.lock` 文件。

## 基本用法

### 添加依赖

```bash
# 添加单个依赖
uv add requests

# 添加多个依赖
uv add requests pandas numpy

# 添加指定版本
uv add "requests>=2.28.0"
uv add "django>=4.0,<5.0"

# 添加开发依赖
uv add --dev pytest
uv add -d black ruff

# 添加可选依赖组
uv add --group test pytest pytest-cov
uv add --group lint black ruff mypy
```

### 版本约束

```bash
# 精确版本
uv add "requests==2.31.0"

# 版本范围
uv add "requests>=2.28.0,<3.0"

# 兼容版本
uv add "django~=4.2.0"

# 预发布版本
uv add "package>=1.0.0a1"
```

### 从不同源添加

```bash
# 从Git仓库添加
uv add git+https://github.com/user/repo.git

# 从本地路径添加
uv add ./local-package
uv add ../other-project

# 从URL添加
uv add https://example.com/package.whl
```

## 高级选项

### 依赖组管理

```bash
# 添加到特定组
uv add --group dev pytest

# 添加到多个组
uv add --group dev,test pytest-cov

# 列出所有组
# 查看pyproject.toml中的[project.optional-dependencies]
```

### 可编辑安装

```bash
# 添加本地包为可编辑依赖
uv add --editable ./local-package

# 或使用-e简写
uv add -e ./local-package
```

### 更新选项

```bash
# 升级已存在的包
uv add --upgrade requests

# 升级所有依赖
uv add --upgrade-all

# 只升级特定包
uv add --upgrade-package requests
```

### 同步选项

```bash
# 添加后不同步（不安装）
uv add --no-sync requests

# 添加后同步（默认）
uv add requests  # 自动同步
```

## 工作流示例

### 示例1: 新项目依赖管理

```bash
# 初始化项目
uv init my-project
cd my-project

# 添加生产依赖
uv add requests pandas

# 添加开发依赖
uv add --dev pytest black

# 添加测试依赖组
uv add --group test pytest-cov
```

### 示例2: 版本升级

```bash
# 升级单个包
uv add --upgrade requests

# 升级到特定版本
uv add "requests>=2.31.0"

# 升级所有依赖
uv add --upgrade-all
```

### 示例3: 本地开发

```bash
# 添加本地包
uv add --editable ./shared-library

# 添加Git依赖
uv add git+https://github.com/user/package.git@main
```

## 与pyproject.toml的关系

### 自动更新

`uv add` 会自动更新 `pyproject.toml`:

```toml
[project]
dependencies = [
    "requests>=2.28.0",
    "pandas",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
]
test = [
    "pytest-cov",
]
```

### 手动编辑

也可以手动编辑 `pyproject.toml`，然后运行：
```bash
uv sync  # 同步依赖
```

## 依赖解析

### 自动解析

uv会自动解析依赖树，处理版本冲突：

```bash
# 如果包A需要requests>=2.0，包B需要requests<2.0
# uv会尝试找到兼容的版本组合
uv add package-a package-b
```

### 冲突处理

如果无法解析冲突，uv会报错并提示解决方案。

## 最佳实践

1. **使用版本约束**: 总是使用版本约束，避免意外升级
2. **分组管理**: 使用依赖组组织不同类型的依赖
3. **定期更新**: 定期运行 `uv add --upgrade-all` 更新依赖
4. **提交锁文件**: 将 `uv.lock` 提交到版本控制

## 与pip install的对比

### 传统方式

```bash
pip install requests
# 需要手动更新requirements.txt
pip freeze > requirements.txt
```

### uv add方式

```bash
uv add requests
# 自动更新pyproject.toml和uv.lock
```

## 故障排除

**问题**: 依赖冲突
- **解决**: 检查版本约束，使用 `uv add --upgrade` 尝试升级

**问题**: 添加失败
- **解决**: 检查包名是否正确，网络连接是否正常

**问题**: 锁文件不同步
- **解决**: 运行 `uv sync` 同步锁文件
