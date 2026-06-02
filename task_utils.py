from validation import validate_task_name, validate_priority, validate_task_id

def add_task(tasks, task_name, priority="medium"):
    if not validate_task_name(task_name):
        print("Error: Invalid task name. Task name must be a non-empty string.")
        return None
    if not validate_priority(priority):
        print("Error: Invalid priority. Choose from 'low', 'medium', or 'high'.")
        return None
    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {
        "id": new_id,
        "name": task_name.strip(),
        "priority": priority.strip().lower(),
        "completed": False,
    }
    tasks.append(new_task)
    print(f"Task '{new_task['name']}' added successfully with ID {new_id}.")
    return tasks

def mark_task_complete(tasks, task_id):
    if not validate_task_id(task_id, tasks):
        print(f"Error: Task with ID {task_id} does not exist.")
        return None
    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print(f"Task '{task['name']}' is already marked as complete.")
            else:
                task["completed"] = True
                print(f"Task '{task['name']}' marked as complete.")
            break
    return tasks

def view_pending_tasks(tasks):
    pending = [task for task in tasks if not task["completed"]]
    if not pending:
        print("No pending tasks! Great job staying on top of things.")
    else:
        print(f"\n{'='*45}")
        print(f"  PENDING TASKS ({len(pending)} task(s))")
        print(f"{'='*45}")
        print(f"  {'ID':<5} {'Priority':<10} {'Task Name'}")
        print(f"  {'-'*40}")
        for task in pending:
            print(f"  {task['id']:<5} {task['priority'].capitalize():<10} {task['name']}")
        print(f"{'='*45}\n")
    return pending

def track_progress(tasks):
    total = len(tasks)
    completed = sum(1 for task in tasks if task["completed"])
    pending = total - completed
    percentage = (completed / total * 100) if total > 0 else 0
    print(f"\n{'='*45}")
    print(f"  TASK PROGRESS REPORT")
    print(f"{'='*45}")
    print(f"  Total Tasks   : {total}")
    print(f"  Completed     : {completed}")
    print(f"  Pending       : {pending}")
    filled = int(percentage / 5)
    bar = "█" * filled + "░" * (20 - filled)
    print(f"  [{bar}] {percentage:.1f}%")
    print(f"{'='*45}\n")
    return {"total": total, "completed": completed, "pending": pending, "percentage": round(percentage, 1)}