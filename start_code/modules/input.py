def get_user_option():
    option = input("Select an option 1, 2, 3, 4, 5, display (m)enu or (q)uit: ")
    return option

def get_description():
    description = input("Enter task description to search for: ")
    return description

def get_duration():
    duration = int(input("Enter task duration: "))
    return duration

def get_user_import():
    user_import = input("Import previous task list? y/n")
    return user_import