import json 

tasks_list = []

# function to print the welcome message
def main():
    print("Welcome to the task tracker")
    while True: 
        print("Here are the options")
        print("1. Add task")
        print("2. Delete task")
        print("3. Update task")
        print("4. Mark task in progress or done")
        print("5. List all tasks that are done")
        print("6. List all tasks that are not done")
        print("6. List all tasks that are in progress")

        try:
            action = int(input("Please choose one: "))  # convert to int
            if 1 <= action <= 7:
                break       
            print("\n")
            print("Invalid option. Please choose a valid number from option above.")

        except ValueError:
            print("\n")
            print("Invalid input. Please enter a number.")


    # dictionary (hashmap in java)
    options = {
        1: add_task,
        2: delete_task,
        3: update_task,
        4: list_task_in_progress,
        5: list_task_done,
        6: list_task_not_done,
    }

    # call the selected function
    options[action]()


# function check valid ID that is already existed in the tasks list
def valid_id(id, task_list):
    for task in task_list:
        # if the id is already taken, invalid id
        if task["id"] == id:
            return False  
    return True

# function add task
def add_task(): 
    global tasks_list
    tasks_list = read_file()
    #get user input for the task detail
    id = int(input("Please enter the ID of the task: "))

    while not valid_id(id, tasks_list): 
        print("The ID is already taken.")
        id = int(input("Please enter the ID of the task: "))


    task = input("What is the task? ")
    description = input("What is the best description for this task? ")
    status = input("What is the status of the task? Finished? In progress? Not done? ")
    create_at = input("What date is today? ")

    # create a task dictionary
    new_task = {
        "id": id,
        "task": task,
        "description": description,
        "status": status,
        "create_at": create_at,
    }

    tasks_list.append(new_task)
    write_file(tasks_list)

    print(f"Task with ID '{id}' added successfully to the tracker.")

# function delete task
def delete_task():
    global tasks_list
    tasks_list = read_file()

    while True:
        print("Which task do you want to delete?")
        task_found = False
        try: 
            id = int(input("Please enter the ID: "))
            # check if the ID is in the list
            for task in tasks_list: 
                if task["id"] == id:
                    task_found = True
                    tasks_list.remove(task)
                    print(f"Task with '{id}' is deleted successfully from the tracker.")
                    write_file(tasks_list)      # save the updated list
                    return  # return here to exit the function
            if not task_found:
                print("The ID you selected is not in the list. Please choose again.")
        except ValueError:
            print("Invalid input. Please enter a valid number for the task ID.")

# function update task
def update_task():
    global tasks_list
    tasks_list = read_file()
    task_found = None      # type dictionary

    # check if valid id
    while True: 
        try:
            id = int(input("Please enter the ID of the task you want to update: "))
            for task in tasks_list:
                if task["id"] == id:
                    task_found = task
                    break

            if task_found:
                print(f"Here is the task with id {id}: ")
                print(f"Task Name: {task_found["task"]}")
                print(f"Description: {task_found["description"]}")
                print(f"Status: {task_found["status"]}")
                break   # exit the loop when see a valid ID
            
            print(f"Task with id {id} not found.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # ask the user which category they want to update
    print("\nWhat would you like to update?")
    print("1. Task Name")
    print("2. Description")
    print("3. Status (Finished, In Progress, Not Done)")

    while True:
        try:
            choice = int(input("Enter your choice from 1 to 3: "))
            if choice in [1,2,3]:
                break
            print("Invalid option. Please enter a number from 1 to 3.")
        except ValueError:
            print("Invalid input. Pleaser enter a number.")

    # update the selected field in task_found
    if choice == 1:
        task_found["task"] = input("Enter new task name: ")
    elif choice == 2:
        task_found["description"] = input("Enter new description: ")
    elif choice == 3:
        task_found["status"] = input("Enter new status (Finished, In Progress, Not Done): ")

    # After updating the task, save the updated tasks_list to the file
    write_file(tasks_list)
    print(f"Task with id '{id}' has been updated successfully.")


# function list task
def list_task_done():
    global tasks_list
    tasks_list = read_file()
    done_task = []
    for task in tasks_list:
        if task["status"].lower() == "done" or task["status"].lower() == "finished":
            done_task.append(task)

    if not done_task:
        print("No tasks are marked as done.")
    else:
        print("\n===== Finished Tasks =====")
        for task in done_task:
            print_task(task)

    print("---------------------------")
    
def list_task_not_done():
    pass
def list_task_in_progress():
    pass

# function that mark the task that is done 
def mark_done():
    pass

# function that mark the task that is in progress
def mark_in_progress():
    pass
def read_file():
    global tasks_list
    # Read current tasks from the file (if exists)
    try: 
        with open("task.json", "r") as file: 
            tasks_list = json.load(file)        # load the content into a Python list
    except FileNotFoundError:
        tasks_list = []     # create an empty list if the file does not exist
    return tasks_list

def write_file(tasks_list):
    # write th e update to the task.json list
    with open("task.json", "w") as file:
        json.dump(tasks_list, file, indent=4)   # write the updated list back to the file with indent for readability

def print_task(task):
    global tasks_list
    tasks_list = read_file()

    print(f"ID: {task["id"]}")
    print(f"Task Name: {task["task"]}")
    print(f"Description: {task["description"]}")
    print(f"Status: {task["status"]}")
    
    write_file(tasks_list)

# run the program to test 
if __name__ == "__main__":
    main()
