import json

JSON_FILE = "task_tracker.json"

def initialize_json_file():
    with open(JSON_FILE, 'w') as file:
        json.dump([], file)

def load_tasks_from_json():
    try:
        with open(JSON_FILE, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        initialize_json_file()
        tasks = []
    return tasks

def import_tasks(stored_data):
    tasks = load_tasks_from_json()
    tasks.append(stored_data)
    save_tasks_to_json(tasks)

def get_all_tasks():
    tasks = load_tasks_from_json()
    return [task['title'] for task in tasks]

def get_priority(title):
    tasks = load_tasks_from_json()
    for task in tasks:
        if task['title'] == title:
            return task['priority']

def get_date(title):
    tasks = load_tasks_from_json()
    for task in tasks:
        if task['title'] == title:
            return task['date']

def get_hours(title):
    tasks = load_tasks_from_json()
    for task in tasks:
        if task['title'] == title:
            return task['hours']

def save_tasks_to_json(tasks):
    with open(JSON_FILE, 'w') as file:
        json.dump(tasks, file)
