"""Task storage and business logic for the Tkinter Todo List app.

The module intentionally uses only Python's standard library so the desktop app
can run on a fresh macOS Python 3 installation.  It owns local JSON persistence,
CRUD operations, filtering, and extension hooks for future read-only Obsidian
Markdown imports.
"""

from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

VALID_PRIORITIES = {"高", "中", "低"}
VALID_FILTERS = {"today", "all", "completed", "active"}


@dataclass
class Task:
    """A single todo item stored in ``tasks.json``.

    ``source`` is reserved for future integrations.  Manually created tasks use
    ``local``.  Future Obsidian tasks can use ``obsidian`` plus source metadata
    without changing the GUI-facing schema.
    """

    id: str
    content: str
    task_date: str
    priority: str = "中"
    note: str = ""
    completed: bool = False
    created_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))
    source: str = "local"
    source_file: Optional[str] = None
    source_line: Optional[int] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        """Create a task from JSON data while tolerating older/missing fields."""

        today = date.today().isoformat()
        return cls(
            id=str(data.get("id") or uuid.uuid4()),
            content=str(data.get("content") or ""),
            task_date=str(data.get("task_date") or today),
            priority=str(data.get("priority") or "中"),
            note=str(data.get("note") or ""),
            completed=bool(data.get("completed", False)),
            created_at=str(data.get("created_at") or datetime.now().isoformat(timespec="seconds")),
            updated_at=str(data.get("updated_at") or datetime.now().isoformat(timespec="seconds")),
            source=str(data.get("source") or "local"),
            source_file=data.get("source_file"),
            source_line=data.get("source_line"),
        )


class TaskManager:
    """Manage todo items and persist them to a local JSON file."""

    def __init__(self, data_file: str | Path = "tasks.json") -> None:
        self.data_file = Path(data_file)
        self.tasks: List[Task] = []
        self.last_error: Optional[str] = None
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from disk, creating an empty file when necessary.

        Corrupt JSON is not overwritten automatically.  Instead, the app keeps an
        empty in-memory task list and records ``last_error`` for the GUI/CLI to
        display as a friendly warning.
        """

        self.last_error = None
        if not self.data_file.exists():
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            self.save_tasks()
            return

        try:
            raw = json.loads(self.data_file.read_text(encoding="utf-8"))
            items = raw.get("tasks", raw) if isinstance(raw, dict) else raw
            if not isinstance(items, list):
                raise ValueError("tasks.json must contain a list or an object with a 'tasks' list")
            self.tasks = [Task.from_dict(item) for item in items if isinstance(item, dict)]
        except (json.JSONDecodeError, OSError, ValueError) as exc:
            self.tasks = []
            self.last_error = f"无法读取任务数据：{exc}。请检查 {self.data_file}。"

    def save_tasks(self) -> None:
        """Persist all tasks to disk in a readable JSON format."""

        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        payload = {"tasks": [asdict(task) for task in self.tasks]}
        self.data_file.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def add_task(self, content: str, task_date: Optional[str] = None, priority: str = "中", note: str = "") -> Task:
        """Add a new local task and save immediately."""

        content = content.strip()
        if not content:
            raise ValueError("任务内容不能为空")
        clean_date = self._normalize_date(task_date or date.today().isoformat())
        clean_priority = priority if priority in VALID_PRIORITIES else "中"
        task = Task(id=str(uuid.uuid4()), content=content, task_date=clean_date, priority=clean_priority, note=note.strip())
        self.tasks.append(task)
        self.save_tasks()
        return task

    def update_task(self, task_id: str, **changes: Any) -> Task:
        """Edit fields on a task and save immediately."""

        task = self.get_task(task_id)
        if "content" in changes:
            content = str(changes["content"]).strip()
            if not content:
                raise ValueError("任务内容不能为空")
            task.content = content
        if "task_date" in changes:
            task.task_date = self._normalize_date(str(changes["task_date"]))
        if "priority" in changes:
            priority = str(changes["priority"])
            task.priority = priority if priority in VALID_PRIORITIES else task.priority
        if "note" in changes:
            task.note = str(changes["note"]).strip()
        if "completed" in changes:
            task.completed = bool(changes["completed"])
        task.updated_at = datetime.now().isoformat(timespec="seconds")
        self.save_tasks()
        return task

    def set_completed(self, task_id: str, completed: bool = True) -> Task:
        """Mark a task completed or active."""

        return self.update_task(task_id, completed=completed)

    def delete_task(self, task_id: str) -> None:
        """Delete a task by id and save immediately."""

        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) == original_count:
            raise KeyError(f"未找到任务：{task_id}")
        self.save_tasks()

    def get_task(self, task_id: str) -> Task:
        """Return a task by id or raise ``KeyError``."""

        for task in self.tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"未找到任务：{task_id}")

    def list_tasks(self, filter_name: str = "all", target_date: Optional[str] = None) -> List[Task]:
        """List tasks using one of the GUI filters."""

        if filter_name not in VALID_FILTERS:
            filter_name = "all"
        tasks: Iterable[Task] = self.tasks
        if filter_name == "today":
            day = target_date or date.today().isoformat()
            tasks = (task for task in tasks if task.task_date == day)
        elif filter_name == "completed":
            tasks = (task for task in tasks if task.completed)
        elif filter_name == "active":
            tasks = (task for task in tasks if not task.completed)
        return sorted(tasks, key=lambda task: (task.task_date, self._priority_order(task.priority), task.created_at))

    def stats(self) -> Dict[str, int]:
        """Return total, active, and completed task counts."""

        completed = sum(1 for task in self.tasks if task.completed)
        total = len(self.tasks)
        return {"total": total, "active": total - completed, "completed": completed}

    def scan_obsidian_tasks(self, notes_dir: str | Path) -> List[Task]:
        """Future extension hook for read-only Obsidian Markdown scanning.

        The first version deliberately does not parse files yet.  Keeping this
        method here documents the contract: future implementations should read
        Markdown files, create ``Task`` objects with ``source='obsidian'``, and
        must never write back to the original notes.
        """

        _ = Path(notes_dir)
        return []

    @staticmethod
    def _normalize_date(value: str) -> str:
        """Validate and normalize dates to YYYY-MM-DD."""

        try:
            return datetime.strptime(value.strip(), "%Y-%m-%d").date().isoformat()
        except ValueError as exc:
            raise ValueError("日期格式必须为 YYYY-MM-DD") from exc

    @staticmethod
    def _priority_order(priority: str) -> int:
        return {"高": 0, "中": 1, "低": 2}.get(priority, 3)
