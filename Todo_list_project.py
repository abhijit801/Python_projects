class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Not Completed"
        return f"{self.description} - {status}"


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print("Task added successfully.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.mark_as_completed()
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks):
                print(f"{index}. {task}")

    def menu(self):
        while True:
            user = input("""What would you like to do?
            1. Add task
            2. Mark task as completed
            3. View tasks
            4. Exit
            """)

            if user == "1":
                description = input("Enter task description: ")
                self.add_task(description)
            elif user == "2":
                index = int(input("Enter task index to mark as completed: "))
                self.mark_task_completed(index)
            elif user == "3":
                self.view_tasks()
            elif user == "4":
                break
            else:
                print("Invalid input. Please try again.")


todo_list = TodoList()
todo_list.menu()
