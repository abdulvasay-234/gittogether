import unittest
from todo import TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo = TodoList(filename='test_tasks.json')

    def test_add_task(self):
        self.todo.add_task("Test Task")
        self.assertEqual(len(self.todo.tasks), 1)
        self.assertEqual(self.todo.tasks[0]['title'], "Test Task")

    def test_mark_completed(self):
        self.todo.add_task("Complete Task")
        self.todo.mark_completed(0)
        self.assertTrue(self.todo.tasks[0]['completed'])

    def test_delete_task(self):
        self.todo.add_task("Delete Task")
        self.todo.delete_task(0)
        self.assertEqual(len(self.todo.tasks), 0)

if __name__ == '__main__':
    unittest.main()
