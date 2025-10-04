# toDoApp.py

tasks=[]

def addTask(task):
    tasks.append(task)
    print("Task added!")

def showTasks():
    if len(tasks)==0:
        print("No tasks yet")
    else:
        for i in range (len(tasks)):
            print(i+1,".",tasks[i])

def removeTask(tasknumber):
    tasks.pop(tasknumber) 
    print("Task Removed!!")

def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice =="1":
            task = input("Enter Task: ")
            addTask(task)
        elif choice == "2":
            showTasks()
        elif choice == "3":
            listNumber = int(input("Enter task number to remove: "))
            removeTask(listNumber)   
        elif choice=="4":
            break
        else:
            print("Wrong choice!!")
main()
