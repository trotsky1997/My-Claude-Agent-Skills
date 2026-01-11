# uv sync - 同步依赖

## 概述

`uv sync` 用于根据 `pyproject.toml` 和 `uv.lock` 同步虚拟环境，确保安装的包与锁文件一致。

## 基本用法

### 基本同步

```bash
# 同步所有依赖
uv sync

# 同步并安装项目本身
uv sync --install-project
```

### 同步特定组

```bash
# 同步开发依赖
uv sync --dev

# 同步所有可选依赖组
uv sync --all-groups

# 同步特定组
uv sync --group test --group lint
```

## 高级选项

### 虚拟环境控制

```bash
# 不使用虚拟环境（系统安装）
uv sync --system

# 指定虚拟环境路径
uv sync --venv /path/to/venv

# 重新创建虚拟环境
uv sync --reinstall
```

### 锁定文件选项

```bash
# 使用冻结的锁文件（不更新）
uv sync --frozen

# 如果锁文件过期，更新它
uv sync --upgrade

# 只更新特定包
uv sync --upgrade-package requests
```

### 安装选项

```bash
# 不同步，只检查
uv sync --dry-run

# 不安装项目本身
uv sync --no-install-project

# 可编辑安装项目
uv sync --editable
```

## 工作流示例

### 示例1: 新环境设置

```bash
# 克隆项目
git clone <repo>
cd <repo>

# 同步依赖（自动创建虚拟环境）
uv sync

# 运行项目
uv run python main.py
```

### 示例2: 更新依赖

```bash
# 编辑pyproject.toml添加新依赖
# 然后同步
uv sync

# 或使用uv add（会自动sync）
uv add new-package
```

### 示例3: 生产环境部署

```bash
# 使用冻结的锁文件（确保版本一致）
uv sync --frozen

# 不安装开发依赖
uv sync --frozen --no-dev
```

### 示例4: 开发环境

```bash
# 同步所有依赖包括开发依赖
uv sync --all-groups

# 可编辑安装项目
uv sync --editable
```

## 与锁文件的关系

### 锁文件作用

`uv.lock` 文件确保：
- 精确的版本号
- 可重现的构建
- 跨平台一致性

### 同步流程

1. 读取 `pyproject.toml` 获取依赖声明
2. 读取 `uv.lock` 获取精确版本
3. 检查虚拟环境状态
4. 安装/更新/移除包以匹配锁文件

### 锁文件过期

如果 `pyproject.toml` 更改但 `uv.lock` 未更新：

```bash
# uv sync会提示需要更新锁文件
uv sync  # 可能会失败

# 更新锁文件
uv lock

# 然后同步
uv sync
```

## 性能优化

### 增量同步

uv sync只安装/更新需要更改的包，不会重新安装所有包。

### 并行安装

多个包会并行安装，提高速度。

### 缓存利用

uv使用全局缓存，相同版本的包不会重复下载。

## 最佳实践

1. **提交锁文件**: 总是将 `uv.lock` 提交到版本控制
2. **使用--frozen**: 在生产环境使用 `--frozen` 确保版本一致
3. **定期同步**: 定期运行 `uv sync` 保持环境最新
4. **分组管理**: 使用依赖组组织不同类型的依赖

## 与poetry install的对比

### Poetry方式

```bash
poetry install
```

### uv sync方式

```bash
uv sync
```

两者功能相似，但uv sync更快。

## 故障排除

**问题**: 同步失败，锁文件过期
- **解决**: 运行 `uv lock` 更新锁文件，然后 `uv sync`

**问题**: 依赖冲突
- **解决**: 检查 `pyproject.toml` 中的版本约束，运行 `uv lock` 重新解析

**问题**: 虚拟环境损坏
- **解决**: 删除 `.venv` 目录，运行 `uv sync` 重新创建

**问题**: 同步很慢
- **解决**: 检查网络连接，确保使用uv的缓存机制
