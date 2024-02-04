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

# save tasks to a json file
def save_tasks_to_json(tasks):
    with open(JSON_FILE, 'w') as file:
        json.dump(tasks, file, indent = 2)

# import data from the form to the json file
def import_tasks(stored_data):
    tasks = load_tasks_from_json()
    # append each task dictionary to the tasks list
    for task_dict in stored_data:
        tasks.append(task_dict)

    save_tasks_to_json(tasks)

def get_all_tasks():
    tasks = load_tasks_from_json()
    return [task_data['title'] for task_data in tasks]

# def get_priority(title):
#     tasks = load_tasks_from_json()
#     for task_data in tasks:
#         if task_data['title'] == title:
#             return task['priority']

def get_date(title):
    tasks = load_tasks_from_json()
    for task_data in tasks:
        if task_data['title'] == title:
            return task_data['date']

def get_hours(title):
    tasks = load_tasks_from_json()
    for task_data in tasks:
        if task_data['title'] == title:
            return task_data['hours']