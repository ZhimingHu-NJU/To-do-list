"""Tkinter desktop entry point for the local Todo List application."""

from __future__ import annotations

import json
import tkinter as tk
from datetime import date
from pathlib import Path
from tkinter import messagebox, simpledialog, ttk

from task_manager import Task, TaskManager

APP_DIR = Path(__file__).resolve().parent
CONFIG_FILE = APP_DIR / "config.json"


def load_config() -> dict:
    """Load app configuration with safe defaults."""

    defaults = {"data_file": "tasks.json", "obsidian_daily_notes_dir": "", "obsidian_read_only": True}
    if not CONFIG_FILE.exists():
        CONFIG_FILE.write_text(json.dumps(defaults, ensure_ascii=False, indent=2), encoding="utf-8")
        return defaults
    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        return {**defaults, **data}
    except json.JSONDecodeError:
        messagebox.showwarning("配置提示", "config.json 格式有误，已使用默认配置启动。")
        return defaults


class TodoApp(tk.Tk):
    """Main desktop window."""

    def __init__(self) -> None:
        super().__init__()
        self.title("本地 Todo List")
        self.geometry("980x620")
        self.minsize(820, 520)

        config = load_config()
        data_file = APP_DIR / config["data_file"]
        self.manager = TaskManager(data_file)
        self.current_filter = tk.StringVar(value="today")
        self.selected_task_id: str | None = None

        self._build_widgets()
        if self.manager.last_error:
            messagebox.showwarning("数据提示", self.manager.last_error)
        self.refresh_tasks()

    def _build_widgets(self) -> None:
        """Create all visible Tkinter widgets."""

        top = ttk.LabelFrame(self, text="添加任务")
        top.pack(fill="x", padx=12, pady=8)

        ttk.Label(top, text="任务内容").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        self.content_var = tk.StringVar()
        ttk.Entry(top, textvariable=self.content_var, width=42).grid(row=0, column=1, padx=6, pady=6, sticky="ew")

        ttk.Label(top, text="日期").grid(row=0, column=2, padx=6, pady=6, sticky="w")
        self.date_var = tk.StringVar(value=date.today().isoformat())
        ttk.Entry(top, textvariable=self.date_var, width=14).grid(row=0, column=3, padx=6, pady=6)

        ttk.Label(top, text="优先级").grid(row=0, column=4, padx=6, pady=6, sticky="w")
        self.priority_var = tk.StringVar(value="中")
        ttk.Combobox(top, textvariable=self.priority_var, values=["高", "中", "低"], width=8, state="readonly").grid(row=0, column=5, padx=6, pady=6)

        ttk.Label(top, text="备注").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        self.note_var = tk.StringVar()
        ttk.Entry(top, textvariable=self.note_var).grid(row=1, column=1, columnspan=4, padx=6, pady=6, sticky="ew")
        ttk.Button(top, text="添加", command=self.add_task).grid(row=1, column=5, padx=6, pady=6, sticky="ew")
        top.columnconfigure(1, weight=2)
        top.columnconfigure(4, weight=1)

        filters = ttk.Frame(self)
        filters.pack(fill="x", padx=12, pady=4)
        for label, value in [("今天", "today"), ("全部", "all"), ("未完成", "active"), ("已完成", "completed")]:
            ttk.Radiobutton(filters, text=label, value=value, variable=self.current_filter, command=self.refresh_tasks).pack(side="left", padx=4)
        ttk.Button(filters, text="标记完成", command=lambda: self.set_selected_completed(True)).pack(side="right", padx=4)
        ttk.Button(filters, text="标记未完成", command=lambda: self.set_selected_completed(False)).pack(side="right", padx=4)
        ttk.Button(filters, text="编辑", command=self.edit_selected_task).pack(side="right", padx=4)
        ttk.Button(filters, text="删除", command=self.delete_selected_task).pack(side="right", padx=4)
        ttk.Button(filters, text="刷新", command=self.refresh_tasks).pack(side="right", padx=4)

        columns = ("status", "date", "priority", "content", "note")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", selectmode="browse")
        headings = {"status": "状态", "date": "日期", "priority": "优先级", "content": "任务内容", "note": "备注"}
        widths = {"status": 90, "date": 110, "priority": 80, "content": 420, "note": 260}
        for column in columns:
            self.tree.heading(column, text=headings[column])
            self.tree.column(column, width=widths[column], anchor="w")
        self.tree.pack(fill="both", expand=True, padx=12, pady=8)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        self.tree.bind("<Double-1>", lambda _event: self.edit_selected_task())

        self.status_var = tk.StringVar()
        ttk.Label(self, textvariable=self.status_var, anchor="w").pack(fill="x", padx=12, pady=(0, 8))

    def add_task(self) -> None:
        """Add a task from the input area."""

        try:
            self.manager.add_task(self.content_var.get(), self.date_var.get(), self.priority_var.get(), self.note_var.get())
        except ValueError as exc:
            messagebox.showerror("无法添加任务", str(exc))
            return
        self.content_var.set("")
        self.note_var.set("")
        self.refresh_tasks()

    def refresh_tasks(self) -> None:
        """Reload the task table and status bar."""

        self.tree.delete(*self.tree.get_children())
        for task in self.manager.list_tasks(self.current_filter.get()):
            self.tree.insert("", "end", iid=task.id, values=self._task_values(task))
        stats = self.manager.stats()
        self.status_var.set(f"共有 {stats['total']} 个任务｜未完成 {stats['active']} 个｜已完成 {stats['completed']} 个")

    def on_select(self, _event: tk.Event) -> None:
        """Remember selected task id for action buttons."""

        selection = self.tree.selection()
        self.selected_task_id = selection[0] if selection else None

    def set_selected_completed(self, completed: bool) -> None:
        """Toggle completion for the selected row."""

        task_id = self._require_selection()
        if not task_id:
            return
        self.manager.set_completed(task_id, completed)
        self.refresh_tasks()

    def delete_selected_task(self) -> None:
        """Delete the selected row after confirmation."""

        task_id = self._require_selection()
        if not task_id:
            return
        if messagebox.askyesno("确认删除", "确定要删除选中的任务吗？"):
            self.manager.delete_task(task_id)
            self.selected_task_id = None
            self.refresh_tasks()

    def edit_selected_task(self) -> None:
        """Edit selected task content, date, priority, and note with simple dialogs."""

        task_id = self._require_selection()
        if not task_id:
            return
        task = self.manager.get_task(task_id)
        content = simpledialog.askstring("编辑任务", "任务内容：", initialvalue=task.content, parent=self)
        if content is None:
            return
        task_date = simpledialog.askstring("编辑任务", "日期（YYYY-MM-DD）：", initialvalue=task.task_date, parent=self)
        if task_date is None:
            return
        priority = simpledialog.askstring("编辑任务", "优先级（高/中/低）：", initialvalue=task.priority, parent=self)
        if priority is None:
            return
        note = simpledialog.askstring("编辑任务", "备注：", initialvalue=task.note, parent=self)
        if note is None:
            return
        try:
            self.manager.update_task(task_id, content=content, task_date=task_date, priority=priority, note=note)
        except ValueError as exc:
            messagebox.showerror("无法编辑任务", str(exc))
            return
        self.refresh_tasks()

    def _require_selection(self) -> str | None:
        if not self.selected_task_id:
            messagebox.showinfo("请选择任务", "请先在表格中选择一个任务。")
            return None
        return self.selected_task_id

    @staticmethod
    def _task_values(task: Task) -> tuple[str, str, str, str, str]:
        status = "已完成" if task.completed else "未完成"
        return status, task.task_date, task.priority, task.content, task.note


if __name__ == "__main__":
    TodoApp().mainloop()
