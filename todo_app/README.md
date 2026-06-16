# 本地 Todo List

一个轻量级本地桌面待办事项管理程序，使用 Python 3 标准库和 Tkinter 构建，优先适配 macOS，也可在 Windows/Linux 上运行。

## 功能

- 手动添加任务内容、日期、优先级和备注。
- 查看今天、全部、未完成、已完成任务。
- 标记完成/未完成、删除任务、编辑任务、刷新列表。
- 自动保存到本地 `tasks.json`。
- 启动时自动读取本地任务；如果 `tasks.json` 不存在会自动创建。
- 为后续只读扫描 Obsidian Daily Notes 预留接口。

## 安装依赖

第一版只使用 Python 标准库，不需要安装第三方依赖。

macOS 通常自带 Tkinter。如果你的 Python 环境缺少 Tkinter，请安装包含 Tk 支持的 Python 3，例如从 Python 官网或 Homebrew 安装。

```bash
python3 --version
```

## 运行程序

进入项目目录后运行：

```bash
cd todo_app
python app.py
```

如果你的系统默认 `python` 不是 Python 3，可使用：

```bash
python3 app.py
```

## 如何添加任务

1. 在顶部“任务内容”输入框填写待办事项。
2. 日期默认为今天，格式为 `YYYY-MM-DD`，可手动修改。
3. 从优先级下拉框选择：高 / 中 / 低。
4. 可在“备注”输入框补充说明。
5. 点击“添加”，任务会立即显示在表格中并自动保存。

## 如何管理任务

- 使用中间筛选按钮查看：今天、全部、未完成、已完成。
- 在表格中选择一条任务后，可点击：
  - `标记完成`
  - `标记未完成`
  - `编辑`
  - `删除`
  - `刷新`
- 双击任务行也可以打开编辑流程。

## 数据保存在哪里

任务数据保存在本目录下的：

```text
todo_app/tasks.json
```

配置文件保存在：

```text
todo_app/config.json
```

程序不会联网，不会上传用户数据。请定期自行备份 `tasks.json`。

## 数据文件损坏怎么办

如果 `tasks.json` 格式损坏，程序会显示友好提示并以空列表启动，避免直接崩溃。程序不会自动覆盖损坏文件，方便你手动修复或从备份恢复。

## 后续配置 Obsidian 目录

`config.json` 中已经预留 Obsidian 配置项：

```json
{
  "data_file": "tasks.json",
  "obsidian_daily_notes_dir": "",
  "obsidian_read_only": true
}
```

后续扩展时，可以把 `obsidian_daily_notes_dir` 设置为 Daily Notes 文件夹路径。第一版不会扫描 Obsidian，也不会修改任何 Markdown 文件。

未来计划支持只读识别 Markdown 待办格式：

```markdown
- [ ] 未完成任务
- [x] 已完成任务
```

解析后将记录来源文件、日期和行号，并与本地手动添加任务统一展示。

## 运行测试

```bash
cd todo_app
python -m unittest discover -s tests
```
