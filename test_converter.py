#!/usr/bin/env python3
"""
XMind 转 Markdown 功能测试脚本
可以独立运行，无需启动 MCP 服务
"""
import sys
from pathlib import Path
from xmind_parser import XMindParser
from md_converter import MarkdownConverter


def test_conversion(xmind_path: str, output_path: str = None):
    """
    测试转换功能
    
    Args:
        xmind_path: XMind 文件路径
        output_path: 输出 Markdown 文件路径（可选）
    """
    print(f"🔍 正在读取 XMind 文件: {xmind_path}")
    
    try:
        # 解析 XMind 文件
        parser = XMindParser(xmind_path)
        xmind_data = parser.parse()
        metadata = parser.get_metadata()
        
        print("✅ XMind 文件解析成功！")
        print(f"   - 画布数量: {len(xmind_data.get('sheets', []))}")
        print(f"   - 文件大小: {metadata['file_size']} 字节")
        
        # 转换为 Markdown
        print("\n🔄 正在转换为 Markdown...")
        converter = MarkdownConverter()
        markdown_content = converter.convert(xmind_data, metadata)
        
        print("✅ Markdown 转换成功！")
        
        # 保存或输出
        if output_path:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_text(markdown_content, encoding="utf-8")
            print(f"\n💾 文件已保存到: {output_path}")
        else:
            print("\n📄 Markdown 内容预览：")
            print("=" * 60)
            print(markdown_content[:1000])
            if len(markdown_content) > 1000:
                print("\n... (内容过长，已省略)")
            print("=" * 60)
        
        return True
        
    except FileNotFoundError as e:
        print(f"❌ 错误: 文件不存在 - {e}")
        return False
    except ValueError as e:
        print(f"❌ 错误: 参数错误 - {e}")
        return False
    except Exception as e:
        print(f"❌ 错误: 转换失败 - {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法:")
        print(f"  python {sys.argv[0]} <xmind_file> [output_file]")
        print("\n示例:")
        print(f"  python {sys.argv[0]} example.xmind")
        print(f"  python {sys.argv[0]} example.xmind output.md")
        sys.exit(1)
    
    xmind_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = test_conversion(xmind_path, output_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()