# Todo App 开发原则

本目录包含一个使用 Python 标准库和 Tkinter 构建的本地桌面 Todo List。

## 维护要求

- 优先保持 macOS 本地可运行：入口命令应保持为 `python app.py`。
- 第一版不依赖第三方库；新增依赖前请确认确有必要，并在 README 中说明。
- 所有用户任务数据只保存在本地 JSON 文件中，不联网、不上传。
- 不要删除或覆盖用户已有的 `tasks.json` 数据；需要迁移时应先备份或兼容读取。
- Obsidian 集成必须保持只读：只能扫描和展示 Markdown 待办，不得修改原始笔记文件。
- 业务逻辑应优先放在 `task_manager.py`，界面逻辑放在 `app.py`，便于测试和后续扩展。
- 修改后至少运行 `python -m unittest discover -s tests`。
