#!/usr/bin/env python3
"""
条件断点工具 - 只在满足条件时暂停
"""
import sys
import os
import ast
import argparse
from pathlib import Path
from typing import Optional


class ConditionalBreakpointManager:
    """条件断点管理器"""
    
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
    
    def read_file(self) -> list[str]:
        """读取文件内容"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            return f.readlines()
    
    def write_file(self, lines: list[str]):
        """写入文件内容"""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    
    def validate_condition(self, condition: str) -> bool:
        """验证条件表达式是否有效"""
        try:
            ast.parse(condition, mode='eval')
            return True
        except SyntaxError:
            return False
    
    def insert_conditional_breakpoint(
        self, 
        line_num: int, 
        condition: str,
        method: str = 'pdb'
    ) -> bool:
        """插入条件断点"""
        if not self.validate_condition(condition):
            raise ValueError(f"Invalid condition: {condition}")
        
        lines = self.read_file()
        idx = line_num - 1
        
        if idx < 0 or idx >= len(lines):
            raise ValueError(f"Line number {line_num} is out of range")
        
        # 获取缩进
        current_line = lines[idx]
        leading_whitespace = len(current_line) - len(current_line.lstrip())
        indent = current_line[:leading_whitespace]
        
        # 生成条件断点代码
        if method == 'pdb':
            breakpoint_code = f"if {condition}:\n{indent}    import pdb; pdb.set_trace()  # Conditional breakpoint: {condition}\n"
        elif method == 'ipdb':
            breakpoint_code = f"if {condition}:\n{indent}    import ipdb; ipdb.set_trace()  # Conditional breakpoint: {condition}\n"
        else:
            breakpoint_code = f"if {condition}:\n{indent}    import debugpy; debugpy.breakpoint()  # Conditional breakpoint: {condition}\n"
        
        # 插入条件断点
        lines.insert(idx, breakpoint_code)
        self.write_file(lines)
        
        print(f"✅ Inserted conditional breakpoint at line {line_num}")
        print(f"   Condition: {condition}")
        print(f"   Method: {method}")
        return True
    
    def list_conditional_breakpoints(self) -> list[tuple[int, str, str]]:
        """列出所有条件断点"""
        lines = self.read_file()
        breakpoints = []
        
        for i, line in enumerate(lines, 1):
            if 'Conditional breakpoint:' in line:
                # 提取条件
                condition = line.split('Conditional breakpoint:')[-1].strip()
                # 检查上一行是否是 if 语句
                if i > 1 and lines[i-2].strip().startswith('if '):
                    condition_line = lines[i-2].strip()
                    condition = condition_line.replace('if ', '').replace(':', '').strip()
                
                # 确定方法
                if 'pdb.set_trace()' in line:
                    method = 'pdb'
                elif 'ipdb.set_trace()' in line:
                    method = 'ipdb'
                elif 'debugpy.breakpoint()' in line:
                    method = 'debugpy'
                else:
                    method = 'unknown'
                
                breakpoints.append((i, condition, method))
        
        return breakpoints


def main():
    parser = argparse.ArgumentParser(
        description='Insert conditional breakpoints in Python code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Insert conditional breakpoint: only pause when x > 100
  python conditional_breakpoint.py demo.py --line 10 --condition "x > 100"
  
  # Only pause on 10th iteration
  python conditional_breakpoint.py demo.py --line 20 --condition "i == 10"
  
  # Only pause when value changes
  python conditional_breakpoint.py demo.py --line 15 --condition "old_value != new_value"
  
  # List all conditional breakpoints
  python conditional_breakpoint.py demo.py --list
        """
    )
    
    parser.add_argument('file', help='Python file to modify')
    parser.add_argument('--line', type=int, help='Line number to insert breakpoint')
    parser.add_argument('--condition', type=str, help='Condition expression (e.g., "x > 100")')
    parser.add_argument('--method', choices=['pdb', 'ipdb', 'debugpy'],
                       default='pdb', help='Debugger method')
    parser.add_argument('--list', action='store_true',
                       help='List all conditional breakpoints')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"❌ Error: File not found: {args.file}")
        return 1
    
    try:
        manager = ConditionalBreakpointManager(args.file)
        
        if args.list:
            breakpoints = manager.list_conditional_breakpoints()
            if breakpoints:
                print(f"📍 Found {len(breakpoints)} conditional breakpoint(s):")
                for line_num, condition, method in breakpoints:
                    print(f"  Line {line_num}: {condition} ({method})")
            else:
                print("ℹ️  No conditional breakpoints found")
            return 0
        
        if args.line is None or args.condition is None:
            parser.print_help()
            return 1
        
        manager.insert_conditional_breakpoint(args.line, args.condition, args.method)
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
