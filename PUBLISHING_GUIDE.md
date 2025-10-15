# XMind to Markdown MCP Server - 发布指南

## 📦 已完成的准备工作

✅ 项目结构已重组为标准 Python 包格式
✅ `pyproject.toml` 配置文件已创建
✅ LICENSE (MIT) 已添加
✅ README_PYPI.md 已准备（PyPI 展示用）
✅ 打包文件已生成：
   - `xmind_to_markdown_mcp-0.1.0.tar.gz` (7.5 KB)
   - `xmind_to_markdown_mcp-0.1.0-py3-none-any.whl` (9.5 KB)

---

## 🚀 发布到 PyPI 的步骤

### 步骤 1：注册 PyPI 账号

1. 访问 https://pypi.org/account/register/
2. 填写用户名、邮箱、密码
3. 验证邮箱
4. 设置双重身份验证（2FA）
   - 下载 Microsoft Authenticator 或 Google Authenticator
   - 扫描二维码完成绑定
   - 保存恢复码

### 步骤 2：生成 API Token

1. 登录 PyPI 后，进入 Account Settings
2. 找到 "API tokens" 部分
3. 点击 "Add API token"
4. Token 名称：随意填写（如 "xmind-mcp-upload"）
5. Scope：选择 "Entire account (all projects)"
6. 点击 "Create token"
7. **重要**：立即复制并保存 token（格式：`pypi-xxxxx...`）

### 步骤 3：发布到 PyPI

在项目目录执行：

```bash
cd XmindConvertMD

# 安装 twine（如果还没安装）
./venv/bin/pip install twine

# 上传到 PyPI
./venv/bin/twine upload dist/* --username __token__ --password pypi-YOUR_TOKEN_HERE
```

**注意**：
- 将 `pypi-YOUR_TOKEN_HERE` 替换为您的实际 token
- 首次上传可能需要等待几分钟才能在 PyPI 上看到

### 步骤 4：验证发布

1. 访问 https://pypi.org/project/xmind-to-markdown-mcp/
2. 检查包信息是否正确显示
3. 测试安装：
   ```bash
   uvx xmind-to-markdown-mcp
   ```

---

## 📝 发布前的检查清单

在发布前，请确认：

- [ ] **更新作者信息**：编辑 `pyproject.toml` 中的 `authors` 部分
  ```toml
  authors = [
      {name = "您的名字", email = "your.email@example.com"}
  ]
  ```

- [ ] **更新项目 URL**：编辑 `pyproject.toml` 中的 `[project.urls]` 部分
  ```toml
  [project.urls]
  Homepage = "https://github.com/yourusername/xmind-to-markdown-mcp"
  Repository = "https://github.com/yourusername/xmind-to-markdown-mcp"
  ```

- [ ] **更新 README**：将 `README_PYPI.md` 重命名为 `README.md`
  ```bash
  mv README_PYPI.md README.md
  ```

- [ ] **测试本地安装**：
  ```bash
  ./venv/bin/pip install dist/*.whl
  xmind-to-markdown-mcp
  ```

---

## 🌐 提交到 MCP 资源库

发布到 PyPI 后，您可以将项目提交到以下 MCP 资源库：

### 1. Smithery.ai (推荐)
- 网址：https://smithery.ai/
- 提交方式：通过 GitHub 仓库自动索引
- 配置文件示例：
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

### 2. mcp.so
- 网址：https://mcp.so/
- 在 MCP Feed 页面提交您的项目
- 提供项目描述和 GitHub 链接

### 3. PulseMCP
- 网址：https://www.pulsemcp.com/
- 通过 GitHub 仓库提交

### 4. MCP 官方仓库
- 仓库：https://github.com/modelcontextprotocol/servers
- Fork 仓库，添加您的项目到 README
- 提交 Pull Request

---

## 📋 MCP 配置示例文件

为了方便用户使用，建议在 GitHub 仓库中提供配置示例：

### Claude Desktop (macOS)
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

## 🔄 版本更新流程

当需要发布新版本时：

1. **更新版本号**：编辑 `pyproject.toml`
   ```toml
   version = "0.2.0"
   ```

2. **更新 `__init__.py`**：
   ```python
   __version__ = "0.2.0"
   ```

3. **重新打包**：
   ```bash
   rm -rf dist/
   ./venv/bin/python -m build
   ```

4. **上传新版本**：
   ```bash
   ./venv/bin/twine upload dist/*
   ```

---

## 🎯 发布后的推广建议

1. **创建 GitHub 仓库**
   - 上传完整代码
   - 编写详细的 README
   - 添加使用示例和截图

2. **社交媒体宣传**
   - Twitter/X 上使用 #MCP #AI 标签
   - Reddit r/mcp 社区分享
   - 相关技术论坛发帖

3. **撰写博客文章**
   - 介绍项目背景和使用场景
   - 提供详细的使用教程
   - 分享开发经验

4. **视频演示**
   - 录制使用演示视频
   - 上传到 YouTube/B站
   - 制作 GIF 动图展示核心功能

---

## ⚠️ 注意事项

1. **包名唯一性**：PyPI 包名不能与现有包重复
2. **版本号规范**：遵循语义化版本 (Semantic Versioning)
3. **License 选择**：确保选择合适的开源许可证
4. **安全性**：不要在代码中包含敏感信息（API 密钥等）
5. **依赖管理**：确保所有依赖都在 `pyproject.toml` 中正确声明

---

## 📞 需要帮助？

如果在发布过程中遇到问题：

1. 查看 PyPI 官方文档：https://packaging.python.org/
2. MCP 官方文档：https://modelcontextprotocol.io/
3. 相关社区寻求帮助

---

## ✅ 发布完成后

发布成功后，您的 MCP Server 将：

- ✅ 在 PyPI 上可搜索和安装
- ✅ 用户可通过 `uvx xmind-to-markdown-mcp` 直接使用
- ✅ 自动出现在各大 MCP 资源库中
- ✅ 成为 MCP 生态系统的一部分

**恭喜您为 AI 工具生态系统做出贡献！** 🎉