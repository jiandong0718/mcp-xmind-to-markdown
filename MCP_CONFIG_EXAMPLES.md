# MCP 客户端配置示例

本文档提供了在各种 MCP 客户端中配置 `xmind-to-markdown-mcp` 的详细示例。

---

## 📱 Claude Desktop

### macOS

配置文件位置：
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

配置内容：
```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "uvx",
      "args": ["xmind-to-markdown-mcp"]
    }
  }
}
```

### Windows

配置文件位置：
```
%APPDATA%\Claude\claude_desktop_config.json
```

配置内容：
```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "uvx",
      "args": ["xmind-to-markdown-mcp"]
    }
  }
}
```

---

## 💻 Cursor IDE

配置文件位置：
```
.vscode/settings.json (项目级)
或
~/Library/Application Support/Cursor/User/settings.json (全局，macOS)
%APPDATA%\Cursor\User\settings.json (全局，Windows)
```

配置内容：
```json
{
  "mcp.servers": {
    "xmind-to-markdown": {
      "command": "uvx",
      "args": ["xmind-to-markdown-mcp"]
    }
  }
}
```

---

## 🔧 Cline (VS Code Extension)

在 Cline 的 MCP 设置中添加：

```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "uvx",
      "args": ["xmind-to-markdown-mcp"]
    }
  }
}
```

---

## 🍒 Cherry Studio

### STDIO 模式（推荐）

```json
{
  "name": "xmind-to-markdown",
  "type": "stdio",
  "command": "uvx",
  "args": ["xmind-to-markdown-mcp"]
}
```

### SSE 模式（远程服务）

如果您部署了 SSE 服务：

```json
{
  "name": "xmind-to-markdown",
  "type": "sse",
  "url": "http://your-server:8000/sse"
}
```

---

## 🌐 Comate

配置文件位置：
```
.comate/mcp.json
```

配置内容：
```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "uvx",
      "args": ["xmind-to-markdown-mcp"]
    }
  }
}
```

---

## 🐍 Python 代码中使用

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def use_xmind_mcp():
    server_params = StdioServerParameters(
        command="uvx",
        args=["xmind-to-markdown-mcp"]
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # 调用工具
            result = await session.call_tool(
                "convert_xmind_to_markdown",
                {
                    "xmind_path": "/path/to/file.xmind",
                    "include_metadata": True
                }
            )
            
            print(result)
```

---

## ?? 使用示例

### 示例 1：转换 XMind 文件

在 AI 对话中：
```
请帮我将这个 XMind 文件转换为 Markdown：
/Users/username/Documents/project-plan.xmind
```

### 示例 2：指定输出路径

```
请将 project-plan.xmind 转换为 Markdown，
并保存到 /Users/username/Documents/output/plan.md
```

### 示例 3：查看 XMind 结构

```
请帮我查看这个 XMind 文件的结构：
/Users/username/Documents/project-plan.xmind
```

---

## 🔍 故障排查

### 问题 1：命令找不到

**错误信息**：`command not found: uvx`

**解决方案**：
```bash
# 安装 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或使用 pip
pip install uv
```

### 问题 2：包找不到

**错误信息**：`Package xmind-to-markdown-mcp not found`

**解决方案**：
1. 确认包已发布到 PyPI
2. 尝试手动安装：`uvx xmind-to-markdown-mcp`
3. 检查网络连接

### 问题 3：权限问题

**错误信息**：`Permission denied`

**解决方案**：
```bash
# 确保有执行权限
chmod +x $(which uvx)
```

---

## 💡 高级配置

### 使用虚拟环境

```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "/path/to/venv/bin/python",
      "args": ["-m", "xmind_to_markdown"]
    }
  }
}
```

### 自定义环境变量

```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "uvx",
      "args": ["xmind-to-markdown-mcp"],
      "env": {
        "PYTHONPATH": "/custom/path",
        "LOG_LEVEL": "DEBUG"
      }
    }
  }
}
```

---

## 📚 相关资源

- PyPI 包页面：https://pypi.org/project/xmind-to-markdown-mcp/
- GitHub 仓库：https://github.com/yourusername/xmind-to-markdown-mcp
- MCP 官方文档：https://modelcontextprotocol.io/
- FastMCP 文档：https://gofastmcp.com/

---

## 🤝 获取帮助

如果配置遇到问题：

1. 查看 [QUICKSTART.md](QUICKSTART.md)
2. 查看 [故障排查](#故障排查) 部分
3. 在 GitHub 提交 Issue
4. 加入相关社区讨论