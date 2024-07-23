import json

class Todo_methods:
    def show_List(self, username):
        try:
            with open("todo_list.txt", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []
        if username in data:
            return data[username]        
    def save_list(self, data):
        with open("todo_list.txt", "w") as file:
            json.dump(data, file, indent=4)
    
    def add_task(self, username, task, completed=False):
        try:
            with open("todo_list.txt", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        except json.JSONDecodeError:
            data = {}

        if username in data:
            data[username].append(
                {
                    "task": task, 
                    "completed": completed
                }
                )
        else:
            data[username] = [
                {
                    "task": task, 
                    "completed": completed
                }
                ]
        self.save_list(data)
        return True
            
    def update_task(self, username, old_task, new_task, completed=False):
        try:
            with open("todo_list.txt", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return {}
        if username in data:
            for task_data in data[username]:
                if task_data.get("task") == old_task:
                    task_data["task"] = new_task
                    task_data["completed"] = completed
                    break
                else: print("This task isn't in the list")
        self.save_list(data)
    def delete_task(self, username, index_value):
        try:
            with open("todo_list.txt", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return {}
        
        if username in data:
            task_found = False
            index = 1
            for task_data in data[username]:
                if index == index_value:
                    data[username].remove(task_data)
                    task_found = True
                    break
                index += 1
            if not task_found:
                return "Task not found in the list"
        else:
            return "User not found"

        self.save_list(data)
        return "Task deleted successfully"
    
    def update_status(self, username, task_index, completed):
        try: 
            with open("todo_list.txt", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return {}
        
        if username in data:
            if 0 < task_index <= len(data[username]):
                data[username][task_index - 1]["completed"] = completed
                self.save_list(data)
                return "Status updated successfully"   
            else: print("This task isn't in the list")
        



        
        
                    
my_list = Todo_methods()


# my_list.add_task("zaheer khan", "update linked bfore EOD", False) 
# my_list.add_task("vishal", "watching netflix in evening", False)

# my_list.add_task("rana", "play pubg", False)

# my_list.update_task("rana", "play pubg", "watching reels", False)

# print(my_list.delete_task("rana", "watching reels"))

# my_list.update_status("zaheer khan", "watching reels", True)

# print(my_list.show_List("vishal"))


                