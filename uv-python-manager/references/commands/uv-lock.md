# uv lock - 锁文件管理

## 概述

`uv lock` 用于生成和更新 `uv.lock` 文件，该文件包含所有依赖的精确版本信息，确保可重现的构建。

## 基本用法

### 生成锁文件

```bash
# 根据pyproject.toml生成锁文件
uv lock

# 如果锁文件已存在，会更新它
uv lock
```

### 更新锁文件

```bash
# 升级所有依赖到最新兼容版本
uv lock --upgrade

# 升级特定包
uv lock --upgrade-package requests

# 升级多个包
uv lock --upgrade-package requests --upgrade-package pandas
```

### 检查锁文件

```bash
# 检查锁文件是否与pyproject.toml一致
uv lock --check
```

## 高级选项

### 升级策略

```bash
# 升级所有依赖
uv lock --upgrade

# 只升级直接依赖
uv lock --upgrade-package requests

# 升级所有传递依赖
uv lock --upgrade-all
```

### 平台特定

```bash
# 为特定平台生成锁文件
uv lock --platform linux-x86_64

# 为多个平台生成
uv lock --platform linux-x86_64 --platform windows-x86_64
```

### 输出选项

```bash
# 详细输出
uv lock --verbose

# 安静模式
uv lock --quiet
```

## 工作流示例

### 示例1: 新项目

```bash
# 初始化项目
uv init my-project
cd my-project

# 添加依赖
uv add requests pandas

# 生成锁文件
uv lock

# 提交到版本控制
git add uv.lock
git commit -m "Add dependencies"
```

### 示例2: 更新依赖

```bash
# 编辑pyproject.toml更改版本约束
# 然后更新锁文件
uv lock

# 或直接升级
uv lock --upgrade
```

### 示例3: 安全更新

```bash
# 检查可用的更新
uv lock --check

# 升级特定包（安全补丁）
uv lock --upgrade-package requests

# 测试更新
uv sync
pytest
```

### 示例4: CI/CD

```bash
# 在CI中验证锁文件
uv lock --check

# 如果失败，说明需要更新锁文件
```

## 锁文件格式

### 文件结构

`uv.lock` 是TOML格式文件，包含：
- 所有依赖的精确版本
- 依赖树结构
- 平台特定信息
- 哈希验证

### 示例片段

```toml
[[package]]
name = "requests"
version = "2.31.0"
source = "registry+https://pypi.org/simple"
dependencies = [
    "certifi",
    "charset-normalizer",
    "idna",
    "urllib3",
]
```

## 与pyproject.toml的关系

### 依赖声明

`pyproject.toml` 声明依赖需求：
```toml
[project]
dependencies = [
    "requests>=2.28.0",
]
```

### 锁文件解析

`uv.lock` 包含精确版本：
```toml
[[package]]
name = "requests"
version = "2.31.0"  # 精确版本
```

## 最佳实践

1. **提交锁文件**: 总是将 `uv.lock` 提交到版本控制
2. **定期更新**: 定期运行 `uv lock --upgrade` 更新依赖
3. **测试更新**: 更新锁文件后运行测试确保兼容性
4. **团队协作**: 确保团队成员使用相同的锁文件

## 与poetry lock的对比

### Poetry方式

```bash
poetry lock
poetry lock --update
```

### uv lock方式

```bash
uv lock
uv lock --upgrade
```

功能相似，但uv lock更快。

## 故障排除

**问题**: 锁文件生成失败
- **解决**: 检查 `pyproject.toml` 语法，确保依赖名称正确

**问题**: 依赖冲突无法解析
- **解决**: 检查版本约束，可能需要放宽某些约束

**问题**: 锁文件与pyproject.toml不一致
- **解决**: 运行 `uv lock` 重新生成锁文件

**问题**: 跨平台不一致
- **解决**: 使用 `--platform` 选项为特定平台生成锁文件
