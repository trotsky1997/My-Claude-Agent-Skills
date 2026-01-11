# uv venv - 虚拟环境管理

## 概述

`uv venv` 用于创建和管理Python虚拟环境。它比传统的 `python -m venv` 更快，并且与现有虚拟环境工具完全兼容。

## 基本用法

### 创建虚拟环境

```bash
# 在当前目录创建 .venv
uv venv

# 指定虚拟环境名称
uv venv myenv
uv venv .venv

# 指定Python版本
uv venv --python 3.12
uv venv --python 3.11.5

# 指定Python解释器路径
uv venv --python /usr/bin/python3.12
```

### 激活虚拟环境

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
.venv\Scripts\activate.bat
```

### 停用虚拟环境

```bash
deactivate
```

### 删除虚拟环境

```bash
# macOS/Linux
rm -rf .venv

# Windows
rmdir /s .venv
```

## 高级选项

### Python版本选择

```bash
# 使用已安装的Python版本
uv venv --python 3.12

# 自动下载并安装Python版本
uv venv --python 3.12.0

# 使用PyPy
uv venv --python pypy@3.10

# 使用系统Python
uv venv --python system
```

### 虚拟环境位置

```bash
# 当前目录
uv venv

# 指定路径
uv venv /path/to/venv

# 使用环境变量
export UV_VENV_DIR="/custom/path"
uv venv
```

### 种子包（Seed Packages）

```bash
# 不安装pip（最小环境）
uv venv --no-seed

# 安装pip和setuptools（默认）
uv venv --seed

# 指定种子包
uv venv --seed-package pip --seed-package wheel
```

### 系统站点包

```bash
# 允许访问系统站点包
uv venv --system-site-packages
```

## 工作流示例

### 示例1: 新项目设置

```bash
# 创建项目目录
mkdir my-project
cd my-project

# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate  # Windows

# 安装依赖
uv pip install requests pandas
```

### 示例2: 多Python版本测试

```bash
# 为Python 3.10创建环境
uv venv --python 3.10 venv-310

# 为Python 3.11创建环境
uv venv --python 3.11 venv-311

# 为Python 3.12创建环境
uv venv --python 3.12 venv-312

# 测试不同版本
source venv-310/bin/activate && python --version
source venv-311/bin/activate && python --version
source venv-312/bin/activate && python --version
```

### 示例3: 使用.python-version文件

```bash
# 在项目根目录创建.python-version
echo "3.12.0" > .python-version

# 创建虚拟环境时会自动使用该版本
uv venv
```

## 与标准venv的对比

### 兼容性

uv venv创建的虚拟环境与标准Python venv完全兼容：
- 可以正常激活和停用
- 可以使用pip、setuptools等标准工具
- 可以被其他工具识别

### 性能优势

- **创建速度**: 比 `python -m venv` 快得多
- **自动Python安装**: 如果Python版本不存在，会自动下载安装
- **更好的错误信息**: 更清晰的错误提示

## 集成使用

### 与uv项目管理集成

```bash
# 在uv项目中，虚拟环境会自动管理
uv init my-project
cd my-project

# uv会自动创建和管理.venv
uv sync  # 自动创建虚拟环境并安装依赖
```

### 与IDE集成

uv venv创建的虚拟环境可以被所有主流IDE识别：
- VS Code
- PyCharm
- Vim/Neovim
- Emacs

只需在IDE中选择虚拟环境的Python解释器路径。

## 最佳实践

1. **使用.venv作为默认名称**: 这是Python社区的标准约定
2. **将.venv添加到.gitignore**: 不要提交虚拟环境到版本控制
3. **使用.python-version文件**: 在项目中固定Python版本
4. **定期更新**: 定期重新创建虚拟环境以获取最新的pip和setuptools

## 故障排除

**问题**: 虚拟环境创建失败
- **解决**: 检查Python版本是否可用，使用 `uv python list` 查看已安装版本

**问题**: 激活后找不到命令
- **解决**: 确保使用正确的激活脚本路径，检查虚拟环境是否完整创建

**问题**: 虚拟环境太大
- **解决**: 使用 `--no-seed` 创建最小环境，或使用 `--system-site-packages` 共享系统包
