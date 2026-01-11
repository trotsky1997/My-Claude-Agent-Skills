#!/usr/bin/env python3
"""
自动调试助手 - AI 自动帮你调试代码
"""
import sys
import os
import subprocess
import argparse
from pathlib import Path
import sys
from pathlib import Path

# Add scripts directory to path for imports
scripts_dir = Path(__file__).parent
if str(scripts_dir) not in sys.path:
    sys.path.insert(0, str(scripts_dir))

from smart_breakpoint_suggester import BreakpointSuggester
from insert_breakpoint import BreakpointManager


class AutoDebugAssistant:
    """自动调试助手"""
    
    def __init__(self, script_path: str):
        self.script_path = Path(script_path)
        if not self.script_path.exists():
            raise FileNotFoundError(f"Script not found: {script_path}")
    
    def auto_debug(self, focus: str = 'functions', max_breakpoints: int = 3):
        """自动调试流程"""
        print("🤖 自动调试助手启动...\n")
        
        # 1. 智能建议断点
        print("📊 步骤 1: 分析代码，寻找最佳断点位置...")
        suggester = BreakpointSuggester(str(self.script_path))
        options = {focus} if focus in ['functions', 'loops', 'conditionals', 'exceptions'] else {'functions'}
        suggestions = suggester.suggest_breakpoints(options)
        
        if not suggestions:
            print("ℹ️  没有找到建议的断点位置")
            return
        
        # 显示建议
        print(f"\n💡 找到 {len(suggestions)} 个建议，选择前 {max_breakpoints} 个:")
        for i, (line, title, reason) in enumerate(suggestions[:max_breakpoints], 1):
            print(f"  {i}. Line {line}: {title}")
        
        # 2. 插入断点
        print(f"\n📍 步骤 2: 插入 {max_breakpoints} 个断点...")
        manager = BreakpointManager(str(self.script_path))
        
        # 检测可用的调试器
        try:
            import ipdb
            debugger_method = 'ipdb'
        except ImportError:
            debugger_method = 'pdb'
            print("  ℹ️  ipdb 未安装，使用 pdb")
        
        inserted = []
        for line, title, reason in suggestions[:max_breakpoints]:
            try:
                manager.insert_breakpoint(line, debugger_method)
                inserted.append(line)
                print(f"  ✅ Line {line}: {title}")
            except Exception as e:
                print(f"  ⚠️  Line {line}: 插入失败 - {e}")
        
        if not inserted:
            print("  ❌ 没有成功插入任何断点")
            return
        
        # 3. 运行调试
        print(f"\n🚀 步骤 3: 运行调试 (已插入 {len(inserted)} 个断点)...")
        print("=" * 60)
        print("程序将在断点处暂停，你可以：")
        print("  - 查看变量: p <变量名>")
        print("  - 单步执行: n (next), s (step)")
        print("  - 继续执行: c (continue)")
        print("  - 退出调试: q (quit)")
        print("=" * 60 + "\n")
        
        try:
            subprocess.run([sys.executable, str(self.script_path)])
        except KeyboardInterrupt:
            print("\n⚠️  调试被中断")
        
        # 4. 清理断点
        print(f"\n🧹 步骤 4: 清理断点...")
        removed = manager.remove_all_breakpoints()
        print(f"  ✅ 已清理 {removed} 个断点")
        
        print("\n✅ 自动调试完成！")
    
    def quick_debug(self, line: int):
        """快速调试 - 在指定行插入断点并运行"""
        print(f"⚡ 快速调试: Line {line}\n")
        
        # 检测可用的调试器
        try:
            import ipdb
            debugger_method = 'ipdb'
        except ImportError:
            debugger_method = 'pdb'
        
        manager = BreakpointManager(str(self.script_path))
        manager.insert_breakpoint(line, debugger_method)
        
        print("🚀 运行调试...\n")
        subprocess.run([sys.executable, str(self.script_path)])
        
        print("\n🧹 清理断点...")
        manager.remove_all_breakpoints()
        print("✅ 完成！")


def main():
    parser = argparse.ArgumentParser(
        description='Auto Debug Assistant - AI helps you debug automatically',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Auto debug with smart suggestions
  python auto_debug_assistant.py demo.py
  
  # Focus on functions only
  python auto_debug_assistant.py demo.py --focus functions
  
  # Quick debug at specific line
  python auto_debug_assistant.py demo.py --quick 10
  
  # Auto debug with more breakpoints
  python auto_debug_assistant.py demo.py --max-breakpoints 5
        """
    )
    
    parser.add_argument('script', help='Python script to debug')
    parser.add_argument('--focus', choices=['functions', 'loops', 'conditionals', 'exceptions'],
                       default='functions', help='Focus on specific code structures')
    parser.add_argument('--max-breakpoints', type=int, default=3,
                       help='Maximum number of breakpoints to insert (default: 3)')
    parser.add_argument('--quick', type=int, metavar='LINE',
                       help='Quick debug at specific line')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.script):
        print(f"❌ Error: Script not found: {args.script}")
        return 1
    
    try:
        assistant = AutoDebugAssistant(args.script)
        
        if args.quick:
            assistant.quick_debug(args.quick)
        else:
            assistant.auto_debug(args.focus, args.max_breakpoints)
        
        return 0
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
