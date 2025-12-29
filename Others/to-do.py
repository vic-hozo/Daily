import time
#declare Task class
class Task:
    def __init__(self, name, task):
        self.name = name
        self.task = task
#string function for Task class
    def __str__(self):
        return f" {self.name} | {self.task}"
#empty tasks list
tasks = {}

#function to add task
def addTask():
    add = input("Name of task: ")
    task = input("Add a description: ")
    if add not in tasks:
        tasks[add] = Task(add, task)
    else:
        print(f"Task {add} already exists")

#function for viewing tasks
def viewTasks():
    for name, task in tasks.items():
     print(f'{name}: {task}')

#function for removing task
def removeTask():
    remove = input("Remove a task: ")
    if remove not in tasks:
        print(f"{remove} does not exist")
    else:
        tasks.pop(remove)
        print(f"{remove} has been removed")

#function for updating class
def updateTask():
    update = input("Update a task: ")
    if update not in tasks:
        print(f"{update} does not exist")
    else: #i got the task here
           result = tasks[update].task = tasks[update].task + " (Done)"
           return result

#Looping through choices until users pick 5
while True:
    print("\n---FUNCTIONS---")
    print("1. Add Task, 2. Delete Task, 3. Update Tasks, 4. View Tasks, 5. Exit")
    choice = input("Enter your choice:")
    if choice == '1':
        addTask()
    elif choice == '2':
        removeTask()
    elif choice == '3':
        updateTask()
    elif choice == '4':
        viewTasks()
    elif choice == '5':
        print("Exiting...")
        time.sleep(2)
        break