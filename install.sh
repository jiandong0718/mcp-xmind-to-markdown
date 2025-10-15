#!/bin/bash
# XMind 转 Markdown MCP 服务安装脚本

echo "🚀 开始安装 XMind 转 Markdown MCP 服务..."

# 检查 Python 版本
echo "📌 检查 Python 版本..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   当前 Python 版本: $python_version"

# 安装依赖
echo "📦 安装 Python 依赖..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ 依赖安装成功！"
else
    echo "❌ 依赖安装失败，请检查错误信息"
    exit 1
fi

# 添加执行权限
echo "🔧 设置执行权限..."
chmod +x server.py
chmod +x test_converter.py

echo ""
echo "✅ 安装完成！"
echo ""
echo "📖 使用方法："
echo "   1. 启动 MCP 服务: python3 server.py"
echo "   2. 测试转换功能: python3 test_converter.py <xmind文件路径> [输出路径]"
echo ""
echo "📝 配置 MCP 客户端："
echo "   参考 mcp_config_example.json 文件，将配置添加到您的 MCP 客户端"
echo ""