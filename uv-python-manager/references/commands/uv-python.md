# uv python - Python版本管理

## 概述

`uv python` 用于安装、管理和切换Python版本。它类似于pyenv，但速度更快，并且与uv的其他功能深度集成。

## 基本用法

### 安装Python版本

```bash
# 安装单个版本
uv python install 3.12

# 安装多个版本
uv python install 3.10 3.11 3.12

# 安装特定补丁版本
uv python install 3.12.0

# 安装PyPy
uv python install pypy@3.10
uv python install pypy@3.11

# 安装预发布版本
uv python install 3.13.0a1
```

### 列出已安装版本

```bash
# 列出所有已安装的Python版本
uv python list

# 列出所有可用版本
uv python list --all-versions
```

### 固定项目Python版本

```bash
# 为当前项目固定Python版本
uv python pin 3.12

# 固定到特定补丁版本
uv python pin 3.12.0

# 这会创建.python-version文件
```

### 查找Python

```bash
# 查找特定版本
uv python find 3.12

# 查找所有可用版本
uv python find --all
```

## 高级功能

### 自动下载

uv python会在需要时自动下载Python版本：

```bash
# 如果3.12未安装，会自动下载
uv venv --python 3.12

# 如果3.12.0未安装，会自动下载
uv run --python 3.12.0 -- python script.py
```

### 版本选择

```bash
# 使用已安装的版本
uv python install 3.12

# 使用系统Python
uv python install system

# 使用特定路径的Python
uv python install /usr/bin/python3.12
```

### 卸载Python版本

```bash
# 卸载特定版本
uv python uninstall 3.12

# 卸载多个版本
uv python uninstall 3.10 3.11
```

## 工作流示例

### 示例1: 多版本开发

```bash
# 安装多个Python版本
uv python install 3.10 3.11 3.12

# 为每个版本创建测试环境
uv venv --python 3.10 venv-310
uv venv --python 3.11 venv-311
uv venv --python 3.12 venv-312

# 测试兼容性
source venv-310/bin/activate && pytest
source venv-311/bin/activate && pytest
source venv-312/bin/activate && pytest
```

### 示例2: 项目版本固定

```bash
# 在项目根目录
cd my-project

# 固定Python版本
uv python pin 3.12

# 这会创建.python-version文件
# 后续操作会自动使用该版本
uv venv  # 使用3.12
uv run python script.py  # 使用3.12
```

### 示例3: CI/CD环境

```bash
# 在CI脚本中
uv python install 3.10 3.11 3.12

# 测试多个版本
for version in 3.10 3.11 3.12; do
    uv venv --python $version test-env
    source test-env/bin/activate
    pytest
    deactivate
done
```

## Python版本存储

### 存储位置

uv python将Python版本存储在：
- **macOS/Linux**: `~/.local/share/uv/python/`
- **Windows**: `%LOCALAPPDATA%\uv\python\`

### 版本管理

```bash
# 查看存储位置
uv python list

# 清理未使用的版本（手动删除目录）
# 或使用系统工具清理
```

## 与.python-version文件集成

### 自动检测

当项目中有`.python-version`文件时，uv会自动使用该版本：

```bash
# 创建.python-version文件
echo "3.12.0" > .python-version

# 后续命令自动使用该版本
uv venv  # 使用3.12.0
uv run python script.py  # 使用3.12.0
```

### 版本格式

`.python-version`文件支持多种格式：
```
3.12
3.12.0
pypy@3.10
system
```

## 性能优化

### 缓存机制

uv python会缓存下载的Python安装包，后续安装相同版本会更快。

### 并行安装

可以同时安装多个Python版本，uv会并行处理。

## 与pyenv的对比

### 相似之处

- 都支持安装多个Python版本
- 都支持版本切换
- 都支持.python-version文件

### uv python的优势

- **速度更快**: 安装和切换版本更快
- **自动下载**: 无需手动下载Python安装包
- **深度集成**: 与uv的其他功能无缝集成
- **跨平台**: Windows、macOS、Linux统一体验

## 最佳实践

1. **固定项目版本**: 使用 `uv python pin` 确保团队使用相同版本
2. **提交.python-version**: 将.python-version文件提交到版本控制
3. **定期更新**: 定期更新Python版本以获取安全补丁
4. **测试多版本**: 在CI/CD中测试多个Python版本兼容性

## 故障排除

**问题**: Python版本安装失败
- **解决**: 检查网络连接，确保有足够的磁盘空间

**问题**: 找不到Python版本
- **解决**: 使用 `uv python list` 查看已安装版本，或使用 `uv python install` 安装

**问题**: 版本不匹配
- **解决**: 使用 `uv python pin` 固定版本，确保.python-version文件存在
