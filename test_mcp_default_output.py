#!/usr/bin/env python3
"""
测试 MCP 服务的默认输出功能
"""
import asyncio
from server import convert_xmind_to_markdown


async def test_default_output():
    """测试不指定 output_path 时的默认行为"""
    print("🧪 测试 MCP 默认输出功能...\n")
    
    # 测试参数：不指定 output_path
    arguments = {
        "xmind_path": "/Users/shansong/Documents/work/other/新一口价-毛利结算.xmind",
        "include_metadata": True
    }
    
    print(f"📋 测试参数:")
    print(f"   - xmind_path: {arguments['xmind_path']}")
    print(f"   - output_path: 未指定（使用默认）")
    print(f"   - include_metadata: {arguments['include_metadata']}\n")
    
    # 调用转换函数
    result = await convert_xmind_to_markdown(arguments)
    
    # 打印结果
    print("📤 MCP 服务返回结果:")
    print("=" * 60)
    for content in result:
        print(content.text)
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_default_output())