# MCP 资源库提交模板

本文档提供了向各大 MCP 资源库提交项目的标准化信息。

---

## 📋 项目基本信息

**项目名称**：XMind to Markdown MCP Server

**包名**：`xmind-to-markdown-mcp`

**简短描述**：将 XMind 思维导图文件转换为 Markdown 格式的 MCP 服务

**详细描述**：
这是一个功能强大的 MCP Server，专门用于将 XMind 思维导图文件转换为结构化的 Markdown 文档。支持完整保留层级结构、备注、标签等信息，并提供两种工具：文件转换和结构查看。

**分类标签**：
- File Processing
- Document Conversion
- Productivity Tools
- Markdown
- XMind

**关键词**：
`mcp`, `xmind`, `markdown`, `converter`, `mindmap`, `ai-tools`, `llm`, `fastmcp`

---

## 🔗 链接信息

**PyPI 包地址**：
```
https://pypi.org/project/xmind-to-markdown-mcp/
```

**GitHub 仓库**：
```
https://github.com/yourusername/xmind-to-markdown-mcp
```

**文档地址**：
```
https://github.com/yourusername/xmind-to-markdown-mcp#readme
```

**问题追踪**：
```
https://github.com/yourusername/xmind-to-markdown-mcp/issues
```

---

## 📦 安装方式

### 使用 uvx（推荐）
```bash
uvx xmind-to-markdown-mcp
```

### 使用 pip
```bash
pip install xmind-to-markdown-mcp
```

---

## ⚙️ 配置示例

### 基础配置（STDIO）
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

### Claude Desktop 配置
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

## 🛠️ 可用工具

### 1. convert_xmind_to_markdown

**功能**：将 XMind 文件转换为 Markdown 格式

**参数**：
```json
{
  "xmind_path": "string (required) - XMind 文件路径",
  "output_path": "string (optional) - 输出 Markdown 文件路径",
  "include_metadata": "boolean (optional, default: true) - 是否包含文件元信息"
}
```

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
```json
{
  "xmind_path": "string (required) - XMind 文件路径"
}
```

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

## 📸 截图/演示

### 转换效果示例

**输入**：XMind 思维导图
```
新一口价-毛利结算
├── 后台设置
│   ├── 新增一口价规则
│   ├── 渠道范围
│   └── 生效时间
└── ...
```

**输出**：Markdown 文档
```markdown
# 新一口价-毛利结算

## 后台设置
- 新增一口价规则
- 渠道范围
- 生效时间
...
```

---

## 🌟 特色功能

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

## 📈 项目状态

- **开发状态**：Beta
- **维护状态**：活跃维护中
- **最新版本**：0.1.0
- **发布日期**：2025-01-15
- **Python 版本支持**：3.10, 3.11, 3.12, 3.13

---

## 👥 作者信息

**作者**：Your Name
**邮箱**：your.email@example.com
**GitHub**：@yourusername

---

## 📝 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🔗 相关链接

- [FastMCP 官方文档](https://gofastmcp.com/)
- [MCP 协议规范](https://modelcontextprotocol.io/)
- [xmindparser 项目](https://github.com/tobyqin/xmindparser)

---

## 📮 联系方式

- **GitHub Issues**：https://github.com/yourusername/xmind-to-markdown-mcp/issues
- **Email**：your.email@example.com
- **Twitter/X**：@yourusername

---

## 🎉 提交清单

在提交到各大 MCP 资源库前，请确认：

- [ ] PyPI 包已成功发布
- [ ] GitHub 仓库已创建并包含完整代码
- [ ] README.md 文档完整且格式正确
- [ ] LICENSE 文件已添加
- [ ] 配置示例已测试可用
- [ ] 工具描述清晰准确
- [ ] 截图/演示材料已准备
- [ ] 作者信息已更新
- [ ] 所有链接可正常访问

---

## 📤 提交方式

### Smithery.ai
1. 确保 GitHub 仓库公开
2. 添加 `mcp-server` topic 到仓库
3. 等待自动索引（通常 24 小时内）

### mcp.so
1. 访问 https://mcp.so/submit
2. 填写项目信息
3. 提交审核

### PulseMCP
1. Fork https://github.com/pulsemcp/servers
2. 添加项目到 README
3. 提交 Pull Request

### MCP 官方仓库
1. Fork https://github.com/modelcontextprotocol/servers
2. 在 `src/` 目录添加项目
3. 更新 README
4. 提交 Pull Request

---

**祝您的 MCP Server 发布顺利！** 🚀