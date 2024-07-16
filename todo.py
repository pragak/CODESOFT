from operations import *
import os

print("Welcome to our task manager!")

while True:
    print("Task TO-DO")
    print("1. Add a task\n2.update a task\n3.Delete a task")
    choice=input("Enter your choice [1,2,3]:")
    if choice in ["1","2","3"]:
        if choice=="1":
            add_task(input("Enter task :"))
            view_task()
        elif choice=="2":
            try:
                view_task()
                update_task(int(input("Enter task id to be marked done:")))
                view_task()
            except:
                print("Invalid task")
        elif choice=="3":
            try:
                view_task()
                delete_task(int(input("Enter task id to be deleted:")))
                view_task()
            except:
                print("Invalid task id")
    else:
        print("invalid choice")
    
    cont=input("Do you want to continue[yes/no]")
    if cont=="yes" or cont=="Yes":
        os.system("cls||clear")
    else:
        print("Have A Great day!\nKeep using")
        exit()