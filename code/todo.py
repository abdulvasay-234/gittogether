import json
from storage import load_tasks, save_tasks

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = load_tasks(self.filename)

    def add_task(self, title):
        task = {'title': title, 'completed': False}
        self.tasks.append(task)
        save_tasks(self.filename, self.tasks)

    def view_tasks(self):
        for idx, task in enumerate(self.tasks, 1):
            status = '✔️' if task['completed'] else '❌'
            print(f"{idx}. {task['title']} - {status}")

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
            save_tasks(self.filename, self.tasks)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
            save_tasks(self.filename, self.tasks)
