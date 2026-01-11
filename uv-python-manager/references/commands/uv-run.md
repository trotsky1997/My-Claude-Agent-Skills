# uv run - 运行Python脚本

## 概述

`uv run` 用于运行Python脚本，自动处理依赖管理和虚拟环境。它可以运行带有内联依赖声明的脚本，无需手动管理虚拟环境。

## 基本用法

### 运行脚本

```bash
# 运行Python脚本
uv run script.py

# 运行模块
uv run -m mymodule

# 运行命令
uv run python -c "print('Hello')"
```

### 指定Python版本

```bash
# 使用特定Python版本
uv run --python 3.12 script.py

# 使用PyPy
uv run --python pypy@3.10 script.py
```

### 传递参数

```bash
# 传递参数给脚本
uv run script.py arg1 arg2

# 使用--分隔参数
uv run -- python script.py --help
```

## 内联依赖声明

### 基本语法

在脚本顶部使用特殊注释声明依赖：

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "requests>=2.28.0",
#   "click>=8.0",
# ]
# ///
import requests
import click

@click.command()
def main():
    click.echo("Hello from uv script!")

if __name__ == "__main__":
    main()
```

### 完整示例

```python
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.28.0",
#     "click>=8.0",
#     "rich>=13.0.0",
# ]
# ///
import requests
import click
from rich.console import Console

console = Console()

@click.command()
@click.argument('url')
def fetch(url):
    """Fetch content from URL."""
    response = requests.get(url)
    console.print(f"Status: {response.status_code}")

if __name__ == "__main__":
    fetch()
```

运行：
```bash
uv run script.py https://example.com
```

## 高级选项

### 环境变量

```bash
# 设置环境变量
uv run --env VAR=value script.py

# 从.env文件加载
uv run --env-file .env script.py

# 多个环境变量
uv run --env VAR1=value1 --env VAR2=value2 script.py
```

### 工作目录

```bash
# 在指定目录运行
uv run --cwd /path/to/dir script.py
```

### 虚拟环境控制

```bash
# 不使用虚拟环境（使用系统Python）
uv run --no-project script.py

# 使用特定虚拟环境
uv run --venv /path/to/venv script.py
```

### 输出控制

```bash
# 安静模式
uv run --quiet script.py

# 详细输出
uv run --verbose script.py
```

## 工作流示例

### 示例1: 一次性脚本

```python
# fetch_data.py
# /// script
# dependencies = ["requests"]
# ///
import requests
data = requests.get("https://api.example.com/data").json()
print(data)
```

```bash
# 直接运行，无需安装依赖
uv run fetch_data.py
```

### 示例2: CLI工具

```python
# cli_tool.py
# /// script
# dependencies = ["click", "rich"]
# ///
import click
from rich.console import Console

console = Console()

@click.group()
def cli():
    pass

@cli.command()
def hello():
    console.print("[green]Hello![/green]")

if __name__ == "__main__":
    cli()
```

```bash
uv run cli_tool.py hello
```

### 示例3: 数据处理脚本

```python
# process.py
# /// script
# dependencies = ["pandas", "numpy"]
# ///
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")
result = df.groupby("category").sum()
print(result)
```

```bash
uv run process.py
```

## 与项目集成

### 在uv项目中使用

如果脚本在uv项目中，会自动使用项目的依赖：

```bash
# 在uv项目中
uv init my-project
cd my-project

# 运行脚本，自动使用项目依赖
uv run script.py
```

### 混合使用

可以同时使用项目依赖和内联依赖：

```python
# script.py
# /// script
# dependencies = ["extra-package"]  # 额外依赖
# ///
# 项目依赖 + extra-package 都会被安装
```

## 性能优化

### 缓存机制

uv run会缓存虚拟环境和依赖，相同脚本的后续运行会更快。

### 并行安装

多个依赖会并行安装，提高速度。

## 与标准Python的对比

### 传统方式

```bash
# 需要手动创建虚拟环境
python -m venv .venv
source .venv/bin/activate
pip install requests click
python script.py
deactivate
```

### uv run方式

```bash
# 一行命令完成所有操作
uv run script.py
```

## 最佳实践

1. **使用内联依赖**: 对于一次性脚本，使用内联依赖声明
2. **固定Python版本**: 在脚本中声明 `requires-python`
3. **版本约束**: 使用版本约束确保兼容性
4. **文档化**: 在脚本注释中说明依赖用途

## 故障排除

**问题**: 依赖安装失败
- **解决**: 检查依赖名称和版本是否正确，确保网络连接正常

**问题**: Python版本不匹配
- **解决**: 在脚本中声明 `requires-python`，或使用 `--python` 选项

**问题**: 脚本找不到模块
- **解决**: 确保依赖已正确声明，检查脚本的导入语句
