#!/usr/bin/env python3
"""
智能断点建议工具 - AI 分析代码，建议最佳断点位置
"""
import sys
import os
import ast
import argparse
from pathlib import Path
from typing import List, Tuple, Set


class BreakpointSuggester:
    """智能断点建议器"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        self.suggestions: List[Tuple[int, str, str]] = []
    
    def read_file(self) -> str:
        """读取文件内容"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    def parse_code(self) -> ast.Module:
        """解析代码为 AST"""
        code = self.read_file()
        return ast.parse(code)
    
    def analyze_function_definitions(self, tree: ast.Module) -> List[Tuple[int, str]]:
        """分析函数定义，建议在函数入口设置断点"""
        suggestions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                # 跳过私有函数和特殊方法（可选）
                if node.name.startswith('_') and not node.name.startswith('__'):
                    continue
                
                # 函数定义行
                line = node.lineno
                # 函数第一行可执行代码（跳过 docstring）
                first_stmt_line = line + 1
                
                # 如果有文档字符串，跳过它
                if (node.body and 
                    isinstance(node.body[0], ast.Expr) and 
                    isinstance(node.body[0].value, ast.Constant) and
                    isinstance(node.body[0].value.value, str)):
                    first_stmt_line = node.body[0].lineno + 1 if node.body else line + 2
                elif node.body:
                    first_stmt_line = node.body[0].lineno
                
                suggestions.append((
                    first_stmt_line,
                    f"Function entry: {node.name}()",
                    "函数入口 - 可以查看函数参数"
                ))
        
        return suggestions
    
    def analyze_loops(self, tree: ast.Module) -> List[Tuple[int, str]]:
        """分析循环，建议在循环开始设置断点"""
        suggestions = []
        
        for node in ast.walk(tree):
            if isinstance(node, (ast.For, ast.While)):
                # 循环的第一行
                line = node.lineno
                suggestions.append((
                    line,
                    f"Loop start: {'for' if isinstance(node, ast.For) else 'while'}",
                    "循环开始 - 可以查看循环变量"
                ))
        return suggestions
    
    def analyze_conditionals(self, tree: ast.Module) -> List[Tuple[int, str]]:
        """分析条件语句，建议在分支处设置断点"""
        suggestions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                # if 语句行
                line = node.lineno
                suggestions.append((
                    line,
                    "Conditional branch",
                    "条件分支 - 可以测试条件表达式"
                ))
                
                # else/elif 分支
                if node.orelse:
                    orelse_node = node.orelse[0]
                    if isinstance(orelse_node, ast.If):
                        suggestions.append((
                            orelse_node.lineno,
                            "Elif branch",
                            "Elif 分支"
                        ))
                    else:
                        suggestions.append((
                            orelse_node.lineno if hasattr(orelse_node, 'lineno') else line + 1,
                            "Else branch",
                            "Else 分支"
                        ))
        
        return suggestions
    
    def analyze_exceptions(self, tree: ast.Module) -> List[Tuple[int, str]]:
        """分析异常处理，建议在 try/except 处设置断点"""
        suggestions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Try):
                # try 块开始
                suggestions.append((
                    node.lineno,
                    "Try block start",
                    "异常捕获开始 - 可以监控异常"
                ))
                
                # except 块
                for handler in node.handlers:
                    suggestions.append((
                        handler.lineno,
                        f"Except handler: {handler.type.id if handler.type else 'all'}",
                        "异常处理 - 可以在异常时暂停"
                    ))
        
        return suggestions
    
    def analyze_return_statements(self, tree: ast.Module) -> List[Tuple[int, str]]:
        """分析返回语句，建议在返回前设置断点"""
        suggestions = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Return):
                suggestions.append((
                    node.lineno,
                    "Return statement",
                    "返回语句 - 可以查看返回值"
                ))
        
        return suggestions
    
    def analyze_variable_assignments(self, tree: ast.Module) -> List[Tuple[int, str]]:
        """分析关键变量赋值（用户输入、计算结果等）"""
        suggestions = []
        important_patterns = [
            'result', 'output', 'data', 'response', 'error', 
            'status', 'value', 'total', 'sum', 'count'
        ]
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                # 检查是否赋值给重要变量
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_name = target.id.lower()
                        if any(pattern in var_name for pattern in important_patterns):
                            suggestions.append((
                                node.lineno,
                                f"Variable assignment: {target.id}",
                                "关键变量赋值 - 可以查看计算结果"
                            ))
                            break
        
        return suggestions
    
    def suggest_breakpoints(self, options: Set[str] = None) -> List[Tuple[int, str, str]]:
        """生成断点建议"""
        if options is None:
            options = {'functions', 'loops', 'conditionals', 'exceptions', 'returns', 'assignments'}
        
        tree = self.parse_code()
        all_suggestions = []
        
        if 'functions' in options:
            all_suggestions.extend(self.analyze_function_definitions(tree))
        
        if 'loops' in options:
            all_suggestions.extend(self.analyze_loops(tree))
        
        if 'conditionals' in options:
            all_suggestions.extend(self.analyze_conditionals(tree))
        
        if 'exceptions' in options:
            all_suggestions.extend(self.analyze_exceptions(tree))
        
        if 'returns' in options:
            all_suggestions.extend(self.analyze_return_statements(tree))
        
        if 'assignments' in options:
            all_suggestions.extend(self.analyze_variable_assignments(tree))
        
        # 去重（同一行的建议合并）
        seen_lines = set()
        unique_suggestions = []
        for line, title, reason in sorted(all_suggestions, key=lambda x: x[0]):
            if line not in seen_lines:
                seen_lines.add(line)
                unique_suggestions.append((line, title, reason))
        
        self.suggestions = unique_suggestions
        return unique_suggestions
    
    def print_suggestions(self, max_suggestions: int = 10):
        """打印断点建议"""
        if not self.suggestions:
            print("ℹ️  No breakpoint suggestions found")
            return
        
        print(f"💡 Found {len(self.suggestions)} breakpoint suggestion(s):\n")
        
        for i, (line, title, reason) in enumerate(self.suggestions[:max_suggestions], 1):
            print(f"{i:2d}. Line {line:4d}: {title}")
            print(f"    └─ {reason}\n")
        
        if len(self.suggestions) > max_suggestions:
            print(f"... and {len(self.suggestions) - max_suggestions} more suggestions")
            print("(Use --max to see more)")


def main():
    parser = argparse.ArgumentParser(
        description='Smart breakpoint suggester - AI analyzes code and suggests breakpoint locations',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Get all suggestions
  python smart_breakpoint_suggester.py demo.py
  
  # Only suggest function entries
  python smart_breakpoint_suggester.py demo.py --only functions
  
  # Suggest functions and loops
  python smart_breakpoint_suggester.py demo.py --only functions loops
  
  # Limit suggestions
  python smart_breakpoint_suggester.py demo.py --max 5
        """
    )
    
    parser.add_argument('file', help='Python file to analyze')
    parser.add_argument('--only', nargs='+',
                       choices=['functions', 'loops', 'conditionals', 'exceptions', 'returns', 'assignments'],
                       help='Only suggest specific types of breakpoints')
    parser.add_argument('--exclude', nargs='+',
                       choices=['functions', 'loops', 'conditionals', 'exceptions', 'returns', 'assignments'],
                       help='Exclude specific types of suggestions')
    parser.add_argument('--max', type=int, default=10,
                       help='Maximum number of suggestions to show (default: 10)')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"❌ Error: File not found: {args.file}")
        return 1
    
    try:
        suggester = BreakpointSuggester(args.file)
        
        # 确定要分析的选项
        all_options = {'functions', 'loops', 'conditionals', 'exceptions', 'returns', 'assignments'}
        
        if args.only:
            options = set(args.only)
        elif args.exclude:
            options = all_options - set(args.exclude)
        else:
            options = all_options
        
        # 生成建议
        suggester.suggest_breakpoints(options)
        
        # 打印建议
        suggester.print_suggestions(args.max)
        
        return 0
        
    except SyntaxError as e:
        print(f"❌ Syntax error in {args.file}: {e}")
        return 1
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
