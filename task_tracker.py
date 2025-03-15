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

    # create a task dictionary
    new_task = {
        "id": id,
        "task": task,
        "description": description,
        "status": status
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
    pass
# function list task
def list_task_done():
    pass
def list_task_not_done():
    pass
def list_task_in_progress():
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

# run the program to test
if __name__ == "__main__":
    main()