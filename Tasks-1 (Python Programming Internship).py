'''
Task - 1

'''
tasks = []

def addTask():
    task = input("Add your Task: ")
    tasks.append(task)
    print(f"Task '{task}' added into the list.")
    
def listTasks():
    if not tasks:
        print("There are no task Currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")
    
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete🗑️: "))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"task #{taskToDelete} was not found.")
    except:
        print("❌Invalid Input❌")

if __name__ == "__main__":
    
    print("Welcome to the To DO List App :")
    while True:
        print("\n")
        print("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️")
        print("Please Select one of the following options")
        print("▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️▪️")
        print("1. Add New Task")
        print("2. Delete Task")
        print("3. List Task")
        print("4. Quit")
        
        choice = input("Select any Number: ")
        
        if(choice == "1"):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            listTasks()
        elif(choice == "4"):
            break
        else:
            print("❌Invalid input❌")
           
    print("Thank You, Good Bye👋🏻")