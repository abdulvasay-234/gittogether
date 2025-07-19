from todo import TodoList

def main():
    todo_list = TodoList()

    while True:
        print("\n--- Todo CLI ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            todo_list.view_tasks()
        elif choice == '2':
            title = input("Enter task title: ")
            todo_list.add_task(title)
        elif choice == '3':
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.mark_completed(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
