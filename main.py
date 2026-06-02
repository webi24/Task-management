from task_utils import add_task, mark_task_complete, view_pending_tasks, track_progress

def display_menu():
    print("\n" + "="*45)
    print("       TASK MANAGEMENT SYSTEM")
    print("="*45)
    print("  1. Add a new task")
    print("  2. Mark a task as complete")
    print("  3. View pending tasks")
    print("  4. Track progress")
    print("  5. View all tasks")
    print("  6. Exit")
    print("="*45)

def view_all_tasks(tasks):
    if not tasks:
        print("No tasks found. Start by adding a task!")
        return
    print(f"\n{'='*50}")
    print(f"  ALL TASKS ({len(tasks)} task(s))")
    print(f"{'='*50}")
    for task in tasks:
        status = "✔ Done" if task["completed"] else "○ Pending"
        print(f"  {task['id']:<5} {status:<12} {task['priority'].capitalize():<10} {task['name']}")
    print(f"{'='*50}\n")

def main():
    tasks = []
    print("\nWelcome to the Task Management System!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == "1":
            task_name = input("Enter task name: ").strip()
            priority = input("Enter priority (low / medium / high) [default: medium]: ").strip()
            if priority == "":
                priority = "medium"
            add_task(tasks, task_name, priority)
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
            else:
                view_all_tasks(tasks)
                try:
                    task_id = int(input("Enter task ID to mark complete: ").strip())
                    mark_task_complete(tasks, task_id)
                except ValueError:
                    print("Error: Please enter a valid numeric ID.")
        elif choice == "3":
            view_pending_tasks(tasks)
        elif choice == "4":
            track_progress(tasks)
        elif choice == "5":
            view_all_tasks(tasks)
        elif choice == "6":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 6.")

if __name__ == "__main__":
    main()