# 在 Cursor 中使用 XMind 转 Markdown MCP 服务

## 📋 前置要求

- ✅ Cursor IDE 已安装
- ✅ Python 3.10+ 已安装
- ✅ 项目依赖已安装（虚拟环境 `venv` 已配置）

## 🔧 配置步骤

### 1. 找到 Cursor MCP 配置文件

Cursor 的 MCP 配置文件位置：

**macOS:**
```
~/Library/Application Support/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

**Windows:**
```
%APPDATA%\Cursor\User\globalStorage\saoudrizwan.claude-dev\settings\cline_mcp_settings.json
```

**Linux:**
```
~/.config/Cursor/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json
```

### 2. 编辑配置文件

打开配置文件，添加以下配置：

```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "/Users/shansong/comate-zulu-demo/XmindConvertMD/venv/bin/python",
      "args": ["/Users/shansong/comate-zulu-demo/XmindConvertMD/server.py"],
      "env": {}
    }
  }
}
```

**⚠️ 注意：** 请将路径替换为您的实际项目路径。

### 3. 重启 Cursor

保存配置文件后，完全退出并重新启动 Cursor IDE。

### 4. 验证 MCP 服务

在 Cursor 的 AI 对话中，尝试以下命令：

```
请使用 xmind-to-markdown 服务，将这个文件转换为 Markdown：
/Users/shansong/Documents/work/other/新一口价-毛利结算.xmind
```

## 🧪 测试用例

### 测试 1：使用默认输出路径

```
请帮我转换这个 XMind 文件：
/Users/shansong/Documents/work/other/新一口价-毛利结算.xmind
```

**预期结果：** 文件保存到 `XmindConvertMD/output/新一口价-毛利结算.md`

### 测试 2：指定输出路径

```
请将这个 XMind 文件转换为 Markdown，并保存到原文件同目录：
输入：/Users/shansong/Documents/work/other/新一口价-毛利结算.xmind
输出：/Users/shansong/Documents/work/other/新一口价-毛利结算.md
```

**预期结果：** 文件保存到指定位置

### 测试 3：查看 XMind 结构

```
请帮我查看这个 XMind 文件的结构：
/Users/shansong/Documents/work/other/新一口价-毛利结算.xmind
```

**预期结果：** 返回 JSON 格式的文件结构

## 🔍 故障排查

### 问题 1：Cursor 找不到 MCP 服务

**解决方案：**
1. 确认配置文件路径正确
2. 检查 Python 虚拟环境路径是否正确
3. 完全重启 Cursor（不是重新加载窗口）

### 问题 2：服务启动失败

**解决方案：**
1. 在终端手动测试服务：
   ```bash
   cd /Users/shansong/comate-zulu-demo/XmindConvertMD
   ./venv/bin/python server.py
   ```
2. 检查依赖是否安装完整：
   ```bash
   ./venv/bin/pip list | grep -E "fastmcp|xmindparser"
   ```

### 问题 3：权限问题

**解决方案：**
```bash
chmod +x /Users/shansong/comate-zulu-demo/XmindConvertMD/server.py
chmod +x /Users/shansong/comate-zulu-demo/XmindConvertMD/venv/bin/python
```

## ?? 可用工具

### 1. convert_xmind_to_markdown

**参数：**
- `xmind_path` (必需): XMind 文件路径
- `output_path` (可选): 输出 Markdown 文件路径
- `include_metadata` (可选): 是否包含元信息，默认 true

### 2. read_xmind_structure

**参数：**
- `xmind_path` (必需): XMind 文件路径

## 💡 使用技巧

1. **批量转换：** 可以在一次对话中转换多个文件
2. **路径灵活：** 支持相对路径和绝对路径
3. **自动命名：** 不指定输出路径时，自动使用原文件名
4. **中文支持：** 完美支持中文文件名和内容

## 🎯 下一步

配置完成后，您可以：
1. 在 Cursor 中自然地请求转换 XMind 文件
2. AI 会自动调用 MCP 服务完成转换
3. 转换结果会保存到指定位置
4. AI 会向您报告转换状态和文件位置