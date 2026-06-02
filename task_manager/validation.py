cat > task_manager/validation.py << 'EOF'
def validate_task_title(title):
    if len(title.strip()) == 0:
        raise ValueError("Invalid title: Title must be a non-empty string.")
    return True

def validate_task_description(description):
    if len(description.strip()) == 0:
        raise ValueError("Invalid description: Description must be a non-empty string.")
    return True

def validate_due_date(due_date):
    import re
    if len(due_date.strip()) == 0 or not re.match(r"\d{4}-\d{2}-\d{2}", due_date.strip()):
        raise ValueError("Invalid due date: Due date must be in YYYY-MM-DD format.")
    return True
EOF