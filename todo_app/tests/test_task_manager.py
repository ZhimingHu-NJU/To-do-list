"""Unit tests for the local todo task manager."""

import json
import tempfile
import unittest
from pathlib import Path

from task_manager import TaskManager


class TaskManagerTest(unittest.TestCase):
    """Verify CRUD, filtering, persistence, and damaged-file handling."""

    def make_manager(self):
        temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(temp_dir.cleanup)
        return TaskManager(Path(temp_dir.name) / "tasks.json")

    def test_add_task_creates_and_persists_task(self):
        manager = self.make_manager()
        task = manager.add_task("写日报", "2026-06-16", "高", "同步项目进度")

        self.assertEqual(task.content, "写日报")
        self.assertEqual(task.priority, "高")
        self.assertTrue(manager.data_file.exists())
        data = json.loads(manager.data_file.read_text(encoding="utf-8"))
        self.assertEqual(len(data["tasks"]), 1)

    def test_update_complete_delete_and_stats(self):
        manager = self.make_manager()
        task = manager.add_task("整理收件箱", "2026-06-16", "中")

        manager.set_completed(task.id, True)
        self.assertEqual(manager.stats(), {"total": 1, "active": 0, "completed": 1})

        manager.update_task(task.id, content="整理邮件收件箱", priority="低", completed=False)
        updated = manager.get_task(task.id)
        self.assertEqual(updated.content, "整理邮件收件箱")
        self.assertEqual(updated.priority, "低")
        self.assertFalse(updated.completed)

        manager.delete_task(task.id)
        self.assertEqual(manager.stats(), {"total": 0, "active": 0, "completed": 0})

    def test_filters_today_active_and_completed(self):
        manager = self.make_manager()
        today_task = manager.add_task("今天任务", "2026-06-16", "中")
        old_task = manager.add_task("历史任务", "2026-06-15", "中")
        manager.set_completed(old_task.id, True)

        self.assertEqual([task.id for task in manager.list_tasks("today", "2026-06-16")], [today_task.id])
        self.assertEqual([task.id for task in manager.list_tasks("active")], [today_task.id])
        self.assertEqual([task.id for task in manager.list_tasks("completed")], [old_task.id])

    def test_invalid_date_and_empty_content_are_rejected(self):
        manager = self.make_manager()

        with self.assertRaises(ValueError):
            manager.add_task("", "2026-06-16", "中")
        with self.assertRaises(ValueError):
            manager.add_task("无效日期", "16-06-2026", "中")

    def test_corrupt_json_sets_friendly_error(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_file = Path(temp_dir) / "tasks.json"
            data_file.write_text("{not json", encoding="utf-8")

            manager = TaskManager(data_file)

            self.assertEqual(manager.tasks, [])
            self.assertIsNotNone(manager.last_error)
            self.assertIn("无法读取任务数据", manager.last_error)

    def test_obsidian_scan_hook_is_read_only_placeholder(self):
        manager = self.make_manager()
        self.assertEqual(manager.scan_obsidian_tasks("/tmp/nonexistent"), [])


if __name__ == "__main__":
    unittest.main()
