## Step-1: `todo.py`
```
# Create a TodoList class that manages tasks with add, view, complete, and delete functionalities.
# Store tasks as a list of dictionaries with 'title' and 'completed' keys.
# Load tasks from a JSON file on initialization and save changes on every operation.
```
## Step-2: Storage.py
```
# Write functions to load tasks from a JSON file and save tasks to a JSON file.
# If the file doesn't exist, return an empty list.
```
## Step-3: app.py
```
# Write a command-line interface to interact with the TodoList class.
# The options should allow users to view tasks, add tasks, mark tasks completed, delete tasks, or exit the app.
# Use input prompts for user choices and handle invalid inputs gracefully.
```

## Step-4 test/test_todo.py (Optional)
```
# Write unit tests for the TodoList class methods: add_task, mark_completed, and delete_task.
# Use the unittest framework.
# Each test should validate the expected behavior of the corresponding method.
```
