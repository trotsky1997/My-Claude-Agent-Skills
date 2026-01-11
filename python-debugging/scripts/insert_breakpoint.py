#!/usr/bin/env python3
"""
断点插入工具 - AI 可以直接使用
可以在 Python 代码的任意位置插入/移除断点

使用方法:
    python insert_breakpoint.py <file.py> --line 10 --method ipdb
    python insert_breakpoint.py <file.py> --line 10 --remove
    python insert_breakpoint.py <file.py> --list
"""
import sys
import os
import argparse
import re
from pathlib import Path
from typing import Optional


class BreakpointManager:
    """断点管理器"""
    
    BREAKPOINT_MARKERS = {
        'pdb': 'import pdb; pdb.set_trace()  # AI breakpoint',
        'ipdb': 'import ipdb; ipdb.set_trace()  # AI breakpoint',
        'debugpy': 'import debugpy; debugpy.breakpoint()  # AI breakpoint',
    }
    
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
    
    def has_breakpoint_at_line(self, lines: list[str], line_num: int) -> bool:
        """检查指定行是否有断点"""
        # 转换为 0-based 索引
        idx = line_num - 1
        if idx < 0 or idx >= len(lines):
            return False
        
        line = lines[idx]
        # 检查是否有断点标记
        markers = [
            'pdb.set_trace()',
            'ipdb.set_trace()',
            'debugpy.breakpoint()',
        ]
        return any(marker in line for marker in markers)
    
    def insert_breakpoint(self, line_num: int, method: str = 'ipdb') -> bool:
        """在指定行插入断点"""
        if method not in self.BREAKPOINT_MARKERS:
            raise ValueError(f"Unknown method: {method}. Choose from: {list(self.BREAKPOINT_MARKERS.keys())}")
        
        lines = self.read_file()
        
        # 转换为 0-based 索引
        idx = line_num - 1
        if idx < 0 or idx >= len(lines):
            raise ValueError(f"Line number {line_num} is out of range (1-{len(lines)})")
        
        # 检查是否已有断点
        if self.has_breakpoint_at_line(lines, line_num):
            print(f"⚠️  Breakpoint already exists at line {line_num}")
            return False
        
        # 获取当前行的缩进
        current_line = lines[idx]
        leading_whitespace = len(current_line) - len(current_line.lstrip())
        indent = current_line[:leading_whitespace]
        
        # 创建断点语句
        breakpoint_line = indent + self.BREAKPOINT_MARKERS[method] + '\n'
        
        # 在指定行之前插入断点
        lines.insert(idx, breakpoint_line)
        
        # 写回文件
        self.write_file(lines)
        
        print(f"✅ Inserted {method} breakpoint at line {line_num} (now line {idx + 1})")
        return True
    
    def remove_breakpoint(self, line_num: int) -> bool:
        """移除指定行的断点"""
        lines = self.read_file()
        
        # 转换为 0-based 索引
        idx = line_num - 1
        if idx < 0 or idx >= len(lines):
            raise ValueError(f"Line number {line_num} is out of range (1-{len(lines)})")
        
        # 检查是否有断点
        if not self.has_breakpoint_at_line(lines, line_num):
            print(f"⚠️  No breakpoint found at line {line_num}")
            return False
        
        # 移除断点行
        lines.pop(idx)
        
        # 写回文件
        self.write_file(lines)
        
        print(f"✅ Removed breakpoint at line {line_num}")
        return True
    
    def list_breakpoints(self) -> list[tuple[int, str]]:
        """列出所有断点"""
        lines = self.read_file()
        breakpoints = []
        
        for i, line in enumerate(lines, 1):
            if 'pdb.set_trace()' in line:
                breakpoints.append((i, 'pdb'))
            elif 'ipdb.set_trace()' in line:
                breakpoints.append((i, 'ipdb'))
            elif 'debugpy.breakpoint()' in line:
                breakpoints.append((i, 'debugpy'))
        
        return breakpoints
    
    def remove_all_breakpoints(self) -> int:
        """移除所有断点"""
        lines = self.read_file()
        original_count = len(lines)
        
        # 过滤掉包含断点的行
        filtered_lines = [
            line for line in lines
            if not any(marker in line for marker in [
                'pdb.set_trace()',
                'ipdb.set_trace()',
                'debugpy.breakpoint()',
            ])
        ]
        
        removed_count = original_count - len(filtered_lines)
        
        if removed_count > 0:
            self.write_file(filtered_lines)
            print(f"✅ Removed {removed_count} breakpoint(s)")
        else:
            print("ℹ️  No breakpoints found")
        
        return removed_count


def main():
    parser = argparse.ArgumentParser(
        description='Insert/Remove breakpoints in Python code',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Insert ipdb breakpoint at line 10
  python insert_breakpoint.py my_script.py --line 10 --method ipdb
  
  # Insert pdb breakpoint at line 20
  python insert_breakpoint.py my_script.py --line 20 --method pdb
  
  # Remove breakpoint at line 10
  python insert_breakpoint.py my_script.py --line 10 --remove
  
  # List all breakpoints
  python insert_breakpoint.py my_script.py --list
  
  # Remove all breakpoints
  python insert_breakpoint.py my_script.py --remove-all
        """
    )
    
    parser.add_argument('file', help='Python file to modify')
    parser.add_argument('--line', type=int, help='Line number to insert/remove breakpoint (1-based)')
    parser.add_argument('--method', choices=['pdb', 'ipdb', 'debugpy'],
                       default='ipdb', help='Debugger method (default: ipdb)')
    parser.add_argument('--remove', action='store_true',
                       help='Remove breakpoint instead of inserting')
    parser.add_argument('--list', action='store_true',
                       help='List all breakpoints in the file')
    parser.add_argument('--remove-all', action='store_true',
                       help='Remove all breakpoints in the file')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.file):
        print(f"❌ Error: File not found: {args.file}")
        return 1
    
    try:
        manager = BreakpointManager(args.file)
        
        if args.list:
            # 列出所有断点
            breakpoints = manager.list_breakpoints()
            if breakpoints:
                print(f"📍 Found {len(breakpoints)} breakpoint(s):")
                for line_num, method in breakpoints:
                    print(f"  Line {line_num}: {method}")
            else:
                print("ℹ️  No breakpoints found")
            return 0
        
        if args.remove_all:
            # 移除所有断点
            removed = manager.remove_all_breakpoints()
            return 0
        
        if args.line is None:
            parser.print_help()
            return 1
        
        if args.remove:
            # 移除断点
            manager.remove_breakpoint(args.line)
        else:
            # 插入断点
            manager.insert_breakpoint(args.line, args.method)
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return 1


if __name__ == '__main__':
    sys.exit(main())
