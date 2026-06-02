def validate_task_name(task_name):
    if not isinstance(task_name, str):
        return False
    if len(task_name.strip()) == 0:
        return False
    return True

def validate_priority(priority):
    valid_priorities = ["low", "medium", "high"]
    if not isinstance(priority, str):
        return False
    if priority.strip().lower() not in valid_priorities:
        return False
    return True

def validate_task_id(task_id, tasks):
    if not isinstance(task_id, int):
        return False
    ids = [task["id"] for task in tasks]
    if task_id not in ids:
        return False
    return True