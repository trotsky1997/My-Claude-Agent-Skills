# uv pip - Pip兼容接口

## 概述

`uv pip` 提供与 pip 完全兼容的命令行接口，但速度更快（10-100倍）。可以直接替换 pip 命令，无需修改工作流程。

## 基本用法

### 安装包

```bash
# 安装单个包
uv pip install requests

# 安装指定版本
uv pip install requests==2.31.0

# 安装版本范围
uv pip install "requests>=2.28.0,<3.0"

# 从requirements文件安装
uv pip install -r requirements.txt

# 可编辑安装（开发模式）
uv pip install --editable .
uv pip install -e ./local-package
```

### 卸载包

```bash
# 卸载单个包
uv pip uninstall requests

# 卸载多个包
uv pip uninstall requests pandas numpy

# 从requirements文件卸载
uv pip uninstall -r requirements.txt
```

### 列出包

```bash
# 列出所有已安装的包
uv pip list

# 列出过时的包
uv pip list --outdated

# 列出可升级的包
uv pip list --uptodate

# 显示包的详细信息
uv pip show requests
```

### 冻结依赖

```bash
# 生成requirements.txt
uv pip freeze > requirements.txt

# 只列出顶级依赖
uv pip freeze --all
```

### 检查依赖

```bash
# 检查已安装包的依赖关系
uv pip check

# 验证requirements文件
uv pip install --dry-run -r requirements.txt
```

## 高级功能

### 从不同源安装

```bash
# 从Git仓库安装
uv pip install git+https://github.com/user/repo.git
uv pip install git+https://github.com/user/repo.git@branch
uv pip install git+https://github.com/user/repo.git@tag

# 从本地文件安装
uv pip install ./package.tar.gz
uv pip install ./package.whl

# 从URL安装
uv pip install https://example.com/package.whl
```

### 使用自定义索引

```bash
# 使用自定义PyPI索引
uv pip install --index-url https://pypi.org/simple/ package-name

# 使用额外索引
uv pip install --extra-index-url https://custom-index.com/ package-name

# 使用环境变量
export UV_INDEX_URL="https://pypi.org/simple/"
uv pip install package-name
```

### 编译requirements

```bash
# 从requirements.in生成requirements.txt
uv pip compile requirements.in -o requirements.txt

# 升级所有依赖
uv pip compile requirements.in --upgrade

# 升级特定包
uv pip compile requirements.in --upgrade-package requests
```

### 缓存管理

```bash
# uv自动使用全局缓存，无需手动管理
# 缓存位置通常在 ~/.cache/uv (Linux/Mac) 或 %LOCALAPPDATA%\uv\cache (Windows)

# 清除缓存（如果需要）
# 删除 ~/.cache/uv 目录
```

## 与pip的对比

### 直接替换

所有pip命令都可以直接替换：

| pip命令 | uv命令 |
|---------|--------|
| `pip install` | `uv pip install` |
| `pip uninstall` | `uv pip uninstall` |
| `pip list` | `uv pip list` |
| `pip show` | `uv pip show` |
| `pip freeze` | `uv pip freeze` |
| `pip check` | `uv pip check` |

### 性能优势

- **安装速度**: 10-100倍更快
- **依赖解析**: 更快的依赖解析算法
- **并行下载**: 自动并行下载包
- **全局缓存**: 高效的依赖去重

## 使用场景

### 场景1: 替换现有pip工作流

```bash
# 旧方式
pip install -r requirements.txt

# 新方式（直接替换）
uv pip install -r requirements.txt
```

### 场景2: 开发环境设置

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 可编辑安装项目
uv pip install --editable .
```

### 场景3: 生产环境部署

```bash
# 使用冻结的requirements
uv pip install --requirement requirements.txt

# 不使用缓存（CI/CD）
uv pip install --no-cache -r requirements.txt
```

## 常见选项

### 全局选项

```bash
# 详细输出
uv pip install -v package-name

# 安静模式
uv pip install -q package-name

# 用户安装（不使用虚拟环境时）
uv pip install --user package-name

# 系统安装
uv pip install --system package-name
```

### 约束和覆盖

```bash
# 使用约束文件
uv pip install --constraint constraints.txt package-name

# 覆盖已安装的包
uv pip install --force-reinstall package-name

# 忽略已安装的包
uv pip install --ignore-installed package-name
```

## 最佳实践

1. **使用虚拟环境**: 即使uv pip支持系统安装，也建议使用虚拟环境
2. **使用requirements文件**: 保持依赖列表的可重现性
3. **利用速度优势**: uv pip比pip快得多，适合频繁的包管理操作
4. **使用编译功能**: `uv pip compile` 可以生成精确的依赖版本

## 故障排除

**问题**: 安装失败，提示找不到包
- **解决**: 检查索引URL，使用 `--index-url` 指定正确的PyPI镜像

**问题**: 依赖冲突
- **解决**: 使用 `uv pip check` 检查冲突，或使用 `uv pip compile` 生成兼容的依赖列表

**问题**: 安装速度慢
- **解决**: uv pip已经很快，如果仍然慢，检查网络连接或使用本地镜像
