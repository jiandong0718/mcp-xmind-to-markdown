# XMind 转 Markdown MCP 服务

这是一个基于 Model Context Protocol (MCP) 的服务，用于将 XMind 思维导图文件转换为 Markdown 格式文档。

## 功能特性

- ✅ 解析 XMind 文件的完整层级结构
- ✅ 保留主题、子主题、备注、标签等信息
- ✅ 转换为结构清晰的 Markdown 格式
- ✅ 支持动态输入文件路径
- ✅ 可选择保存文件或直接返回内容
- ✅ 提供结构化数据查看功能

## Markdown 转换规则

转换后的 Markdown 采用以下层级结构：

```markdown
# [中心主题]

## [一级分支1]
- 子主题1.1
  - 详细内容1.1.1
  - 详细内容1.1.2
- 子主题1.2

## [一级分支2]
- 子主题2.1
  > 备注：这里是XMind中的备注内容
- 子主题2.2

---
**文件元信息**
- 文件名: example.xmind
- 文件大小: 15.32 KB
- 创建时间: 2025-01-01 10:00:00
- 修改时间: 2025-01-02 15:30:00
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 启动服务

```bash
python server.py
```

服务将通过标准输入/输出 (stdio) 与 MCP 客户端通信。

## 可用工具

### 1. convert_xmind_to_markdown

将 XMind 文件转换为 Markdown 格式。

**参数：**
- `xmind_path` (必需): XMind 文件路径
- `output_path` (可选): 输出 Markdown 文件路径，不提供则直接返回内容
- `include_metadata` (可选): 是否包含文件元信息，默认为 `true`

**使用示例：**

```json
{
  "xmind_path": "./my-mindmap.xmind",
  "output_path": "./output/mindmap.md",
  "include_metadata": true
}
```

### 2. read_xmind_structure

读取 XMind 文件的结构化数据（JSON 格式），不进行转换。

**参数：**
- `xmind_path` (必需): XMind 文件路径

**使用示例：**

```json
{
  "xmind_path": "./my-mindmap.xmind"
}
```

## 配置 MCP 客户端

如果您使用支持 MCP 的客户端（如 Claude Desktop），可以在配置文件中添加此服务：

### macOS/Linux

编辑 `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "python",
      "args": ["/Users/shansong/comate-zulu-demo/server.py"]
    }
  }
}
```

### Windows

编辑 `%APPDATA%\Claude\claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "python",
      "args": ["C:\\path\\to\\comate-zulu-demo\\server.py"]
    }
  }
}
```

## 项目结构

```
xmind-mcp-server/
├── server.py              # MCP 服务主程序
├── xmind_parser.py        # XMind 解析模块
├── md_converter.py        # Markdown 转换器
├── requirements.txt       # Python 依赖
└── README.md              # 本文档
```

## 技术栈

- **MCP SDK**: Model Context Protocol 实现
- **xmindparser**: XMind 文件解析库
- **Python 3.8+**: 运行环境

## 使用场景

1. **文档整理**: 将思维导图快速转换为文档格式
2. **知识管理**: 将 XMind 笔记导出为 Markdown 便于版本管理
3. **团队协作**: 将思维导图分享为通用的 Markdown 格式
4. **自动化流程**: 集成到 CI/CD 或文档生成流程中

## 注意事项

1. 确保 XMind 文件格式为 `.xmind`
2. 文件路径支持相对路径和绝对路径
3. 输出目录会自动创建（如果不存在）
4. 转换过程保留原始层级关系

## 许可证

MIT License