# 提交到 mcp.so 的信息

## 📋 基本信息

**项目名称**：XMind to Markdown MCP Server

**包名**：`xmind-to-markdown-mcp`

**一句话描述**：
```
将 XMind 思维导图文件转换为 Markdown 格式的 MCP 服务
```

**详细描述**：
```
这是一个功能强大的 MCP Server，专门用于将 XMind 思维导图文件转换为结构化的 Markdown 文档。
支持完整保留层级结构、备注、标签等信息，并提供两种工具：文件转换和结构查看。
基于 FastMCP 框架开发，符合 MCP 协议规范，易于集成到各种 AI 客户端中。
```

---

## 🔗 链接信息

**GitHub 仓库**：
```
https://github.com/jiandong0718/mcp-center
```

**PyPI 包地址**：
```
https://pypi.org/project/xmind-to-markdown-mcp/
```

**文档地址**：
```
https://github.com/jiandong0718/mcp-center#readme
```

---

## 📦 安装方式

**使用 uvx（推荐）**：
```bash
uvx xmind-to-markdown-mcp
```

**使用 pip**：
```bash
pip install xmind-to-markdown-mcp
```

---

## ⚙️ 配置示例

### Claude Desktop
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

### Cursor IDE
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

### Cline (VS Code)
```json
{
  "xmind-to-markdown": {
    "command": "uvx",
    "args": ["xmind-to-markdown-mcp"]
  }
}
```

---

## 🛠️ 可用工具

### 1. convert_xmind_to_markdown

**功能**：将 XMind 文件转换为 Markdown 格式

**参数**：
- `xmind_path` (string, required) - XMind 文件路径
- `output_path` (string, optional) - 输出 Markdown 文件路径
- `include_metadata` (boolean, optional, default: true) - 是否包含文件元信息

**示例**：
```json
{
  "xmind_path": "/path/to/project.xmind",
  "output_path": "/path/to/output.md",
  "include_metadata": true
}
```

### 2. read_xmind_structure

**功能**：读取并返回 XMind 文件的结构化数据（JSON 格式）

**参数**：
- `xmind_path` (string, required) - XMind 文件路径

**示例**：
```json
{
  "xmind_path": "/path/to/project.xmind"
}
```

---

## 🎯 使用场景

1. **知识管理**：将思维导图笔记转换为 Markdown 便于版本管理
2. **文档生成**：快速将设计稿转化为结构化文档
3. **团队协作**：统一思维导图和文档格式
4. **自动化工作流**：集成到 CI/CD 或文档生成流程

---

## ?? 主要特性

- ✅ **完整层级保留**：准确还原思维导图的层级结构
- ✅ **中文支持**：完美支持中文文件名和内容
- ✅ **元数据包含**：可选包含文件大小、创建时间等信息
- ✅ **灵活输出**：支持自定义输出路径或默认保存
- ✅ **双工具设计**：转换和结构查看两种模式
- ✅ **标准协议**：基于 FastMCP 框架，符合 MCP 规范

---

## 📊 技术栈

- **语言**：Python 3.10+
- **框架**：FastMCP 2.0+
- **核心依赖**：
  - `fastmcp` - MCP 服务框架
  - `xmindparser` - XMind 文件解析

---

## 🏷️ 标签（Tags）

```
mcp, mcp-server, xmind, markdown, converter, ai-tools, llm, fastmcp, python, mindmap, model-context-protocol
```

---

## 📈 项目状态

- **开发状态**：Beta
- **维护状态**：活跃维护中
- **最新版本**：0.1.1
- **发布日期**：2025-01-15
- **Python 版本支持**：3.10, 3.11, 3.12, 3.13

---

## 👥 作者信息

**作者**：jiandong.liu  
**邮箱**：jiandong.yh@gmail.com  
**GitHub**：@jiandong0718

---

## 📝 许可证

MIT License

---

## 📮 提交方式

### 在 mcp.so 网站提交

1. 访问 https://mcp.so/submit
2. 填写上述信息
3. 提交审核

### 预期审核时间

通常 1-3 个工作日

---

## ✅ 提交前检查清单

- [x] PyPI 包已成功发布
- [x] GitHub 仓库已创建并包含完整代码
- [x] README.md 文档完整
- [x] LICENSE 文件已添加
- [x] 配置示例已测试
- [x] 工具描述清晰
- [x] 作者信息准确
- [x] 所有链接可访问

---

**准备就绪！现在可以提交到 mcp.so 了！** 🚀