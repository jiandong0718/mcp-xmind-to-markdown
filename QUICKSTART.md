# 快速开始指南

## 一、安装依赖

### 方法 1：使用安装脚本（推荐）

```bash
./install.sh
```

### 方法 2：手动安装

```bash
pip3 install -r requirements.txt
```

## 二、测试功能

在启动 MCP 服务之前，可以先使用测试脚本验证转换功能：

```bash
# 仅输出到终端（预览）
python3 test_converter.py /path/to/your/file.xmind

# 保存到文件
python3 test_converter.py /path/to/your/file.xmind output.md
```

## 三、启动 MCP 服务

```bash
python3 server.py
```

服务将通过 stdio 与 MCP 客户端通信。

## 四、配置 MCP 客户端

### Claude Desktop（macOS）

1. 打开配置文件：
```bash
open ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

2. 添加服务配置：
```json
{
  "mcpServers": {
    "xmind-to-markdown": {
      "command": "python3",
      "args": ["/Users/shansong/comate-zulu-demo/server.py"]
    }
  }
}
```

3. 重启 Claude Desktop

### 其他 MCP 客户端

参考 `mcp_config_example.json` 文件，根据您的客户端文档进行配置。

## 五、使用工具

### 工具 1：convert_xmind_to_markdown

**功能**：将 XMind 文件转换为 Markdown

**参数示例**：
```json
{
  "xmind_path": "./example.xmind",
  "output_path": "./output/example.md",
  "include_metadata": true
}
```

**使用场景**：
- 将思维导图导出为文档
- 批量转换 XMind 文件
- 集成到自动化流程

### 工具 2：read_xmind_structure

**功能**：查看 XMind 文件的结构化数据（JSON 格式）

**参数示例**：
```json
{
  "xmind_path": "./example.xmind"
}
```

**使用场景**：
- 调试和分析思维导图结构
- 提取特定信息
- 验证文件完整性

## 六、常见问题

### Q1: 提示找不到模块？
**A**: 确保已安装所有依赖：
```bash
pip3 install -r requirements.txt
```

### Q2: 文件路径错误？
**A**: 
- 使用绝对路径：`/Users/username/file.xmind`
- 或相对于工作目录的路径：`./file.xmind`

### Q3: 转换结果不符合预期？
**A**: 
- 使用 `read_xmind_structure` 查看原始结构
- 检查 XMind 文件是否完整
- 确认文件格式为 `.xmind`

### Q4: MCP 服务无法连接？
**A**:
- 检查配置文件中的路径是否正确
- 确认 Python 环境可用
- 查看客户端日志获取详细错误信息

## 七、示例工作流

### 场景 1：单个文件转换

```bash
# 测试转换
python3 test_converter.py my-mindmap.xmind preview.md

# 查看结果
cat preview.md
```

### 场景 2：通过 MCP 客户端使用

1. 在 Claude Desktop 中输入：
```
请帮我将 ./project-plan.xmind 转换为 Markdown，保存到 ./docs/plan.md
```

2. 系统会自动调用 `convert_xmind_to_markdown` 工具

3. 查看转换结果

### 场景 3：批量转换（需要脚本）

创建批量转换脚本：
```bash
#!/bin/bash
for file in *.xmind; do
    python3 test_converter.py "$file" "output/${file%.xmind}.md"
done
```

## 八、进阶使用

### 自定义转换逻辑

编辑 `md_converter.py`，修改 `MarkdownConverter` 类的方法：
- `_convert_root_topic`: 调整中心主题格式
- `_convert_branch`: 修改分支主题样式
- `_convert_list_item`: 自定义列表项格式

### 扩展功能

可以在 `server.py` 中添加新工具，例如：
- 批量转换工具
- 格式验证工具
- 导出为其他格式（HTML、PDF 等）

## 需要帮助？

- 查看完整文档：`README.md`
- 查看代码注释了解实现细节
- 提交 Issue 报告问题