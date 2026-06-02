from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

tasks = []

def display_menu():
    print("\n=== Task Management System ===")
    print("1. Add a task")
    print("2. Mark task as complete")
    print("3. View pending tasks")
    print("4. Track progress")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            add_task(tasks, title, description, due_date)

        elif choice == "2":
            task_index = input("Enter task number to mark as complete: ").strip()
            mark_task_as_complete(tasks, task_index)

        elif choice == "3":
            view_pending_tasks(tasks)

        elif choice == "4":
            print(calculate_progress(tasks))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()