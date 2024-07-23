

from todos_methods import Todo_methods

todo_list = Todo_methods()
def greeting(name):
    print(f"Hello, {name}! Welcome Back to your to-do list.")

username = input("Enter your username : ")
greeting(username)

while username != "":
    print("\n1. Add Task ")
    print("2. View all tasks ")
    print("3. Delete Task")
    print("4. Update Task status ")
    print("5. Make changes in Task ")
    print("6. Exit the application ")
    choices = input("What do you want to do : ")

    match choices:
        case '1':
            task = input("Enter Yout Task : ")
            response = todo_list.add_task(username, task, False)
            if response:
                print("Task added successfully.")
            else: print("Facing some error while adding task")
        case '2':
            response = todo_list.show_List(username)
            for task in response:
                print(f"\n Task : {task["task"]}\n Completed : {task["completed"]}\n")
        case '3':
            res = todo_list.show_List(username)
            index = 1
            for task in res:
                print(f"\n{index}. Task : {task["task"]}\n Completed : {task["completed"]}")
                index += 1
            task_index = int(input("Enter the number of task to Delete : "))
            print(todo_list.delete_task(username, task_index))
            
        case '4':
            res = todo_list.show_List(username)
            index = 1
            for task in res:
                print(f"\n{index}. Task : {task["task"]}\n Completed : {task["completed"]}")
                index += 1
            task_index = int(input("Enter the number of task to update status : "))
            print(todo_list.update_status(username, task_index, True))
        case '6':
            username = ""
            

            
       

        
    
        
