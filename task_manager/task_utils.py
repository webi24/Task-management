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

def mark_task_as_complete(tasks, title):
    for task in tasks:
        if task["title"].lower() == title.strip().lower():
            task["completed"] = True
            print(f"Task '{task['title']}' marked as complete.")
            return tasks
    print(f"Error: Task '{title}' not found.")
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
        print("No tasks available.")
        return 0
    completed = sum(1 for task in tasks if task["completed"])
    percentage = (completed / total) * 100
    print(f"\n--- Progress ---")
    print(f"Total Tasks : {total}")
    print(f"Completed   : {completed}")
    print(f"Pending     : {total - completed}")
    print(f"Progress    : {percentage:.1f}%")
    return percentage
