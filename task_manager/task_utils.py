cat > task_manager/task_utils.py << 'EOF'
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

def add_task(tasks, title, description, due_date):
    try:
        validate_task_title(title)
        validate_task_description(description)
        validate_due_date(due_date)
    except ValueError as e:
        print(f"Error: {e}")
        return None
    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")
    return tasks

def mark_task_as_complete(tasks, task_index):
    try:
        index = int(task_index) - 1
        if index < 0 or index >= len(tasks):
            print("Error: Task not found.")
            return None
        tasks[index]["completed"] = True
        print("Task marked as complete!")
        return tasks
    except (ValueError, IndexError):
        print("Error: Invalid task number.")
        return None

def view_pending_tasks(tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks!")
    else:
        print("\n--- Pending Tasks ---")
        for task in pending:
            print(f"  Title      : {task['title']}")
            print(f"  Description: {task['description']}")
            print(f"  Due Date   : {task['due_date']}")
            print()
    return pending

def calculate_progress(tasks):
    total = len(tasks)
    if total == 0:
        return 0
    completed = sum(1 for task in tasks if task["completed"])
    percentage = (completed / total) * 100
    return percentage
EOF