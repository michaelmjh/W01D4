# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    return get_tasks_by_status(list, False)

## Get a list of completed tasks
def get_completed_tasks(list):
    return get_tasks_by_status(list, True)

## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    task_list = []
    for task in list:
        if task["time_taken"] >= time:
            task_list.append(task)
    return task_list

## Find a task with a given description
def get_task_with_description(list, description):
    for task in list:
        if task["description"] == description:
            return task

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    task_list = []
    for task in list:
        if task["completed"] == status:
            task_list.append(task)
    return task_list

def mark_task_complete(task):
    task["completed"] = True

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)

def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

def print_list(list):
    for task in list:
        print_task(task)

def print_menu():
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")
