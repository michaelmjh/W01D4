from time import time
from modules.task_list import *
from modules.output import *
from modules.input import *

user_input = get_user_import()
if user_input == "y":
    from data.task_list import *
else:
    tasks = []

while (True):

    print_menu()
    option = get_user_option()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        description = get_description()
        task = get_task_with_description(tasks, description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        time = get_duration()
        print_list(get_tasks_taking_at_least(tasks, time))
    elif option == '6':
        description = get_description()
        print(get_task_with_description(tasks, description))
    elif option == '7':
        description = get_description()
        time_taken = get_duration()
        task = create_task(description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")

    