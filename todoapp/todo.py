# Create todo app using kivy
# 1- Create Todo
# 2- Read Todo
# 3- Edit Todo
# 4- Delete Todo
# Todo -> tasks

class Task:
    def __init__(self ,name, date, status):
        self.name = name
        self.date = date
        self.status = status


class Todo(Task):
    tasks = []
    def __init__(self ,name="", date="", status=""):
        super().__init__(name, date, status)
        if (len(self.tasks) == 0) and (len(self.get_tasks_file())) != 0:
            for task in self.get_tasks_file():
                self.tasks.append(task)

    # Create Task
    def create_task(self, name, date, status):
        id = len(self.tasks) + 1
        task = {"id": id,"name": name, "date": date, "status": status}
        self.tasks.append(task)
        self.save_task(id, name, date, status)
    # Get Tasks
    @classmethod
    def get_tasks(cls):
        return cls.tasks
    @classmethod
    def edit_task_name(cls, id, name):
        for task in cls.tasks:
            if f"{task['id']}" == f"{id}":
                task['name'] = name
                break
        cls.clear_all_ffile()
        for task in cls.tasks:
            cls.save_task(task["id"], task["name"], task["date"], task["status"])
    @classmethod
    def delete_task(cls, id):
        for i in range(len(cls.tasks)):
            if f"{cls.tasks[i]['id']}" == f"{id}":
                cls.tasks.pop(i)
                break
        cls.clear_all_ffile()
        for task in cls.tasks:
            cls.save_task(task["id"], task["name"], task["date"], task["status"])
    @classmethod
    def edit_tasks_status(cls, id, status):
        for task in cls.tasks:
            if f"{task['id']}" == f"{id}":
                task['status'] = status
                break
        cls.clear_all_ffile()
        for task in cls.tasks:
            cls.save_task(task["id"], task["name"], task["date"], task["status"])
    @classmethod
    def save_task(cls, id, name, date, status):
        with open("tasks.txt", "a") as file:
            task = f"{id},{name},{date},{status}\n"
            file.write(task)
    @classmethod
    def get_tasks_file(cls):
        try:
            tasks = []
            with open("tasks.txt", "r") as file:
                tasks = file.readlines()
                tasks = [task.split("\n")[0] for task in tasks]
            return [{"id":task.split(",")[0],"name":task.split(",")[1],"date":task.split(",")[2],"status":task.split(",")[3]} for task in tasks]
        except Exception as ex:
            print("File doesn't exist!")
            return []
    @classmethod
    def clear_all_ffile(cls):
        with open("tasks.txt", "w") as file:
            pass
