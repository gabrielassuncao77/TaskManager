import os

class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description

class TaskManager:
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        self.tasks.append(task)

    def removeLastTask(self):
        if self.tasks:
            self.tasks.pop()
        else:
            print("There are no tasks to remove.")
    
    def clearTaskManager(self):
        if not self.tasks:
            print('There are no tasks to be cleared.')
        else:
            self.tasks.clear()      

    def printTaskManager(self):
        if not self.tasks:
            print('There are no tasks.')
        else:
            print('There are these tasks in the manager.')
            for i, task in enumerate(self.tasks, start=1):
                print(f'{i}. {task.title}: {task.description}')

def createTask():
    title = input("Title: ")
    description = input("Description: ")
    return Task(title, description)



def main():
    manager = TaskManager()
    while True:
        print('')
        print("Welcome to the Gabriel's Task Manager, chose one of the options below:")
        print("1. Add task.")
        print("2. Show tasks.")
        print("3. Remove last task.")
        print("4. Clear Task Manager.")
        print("5. Exit Task Manager.")
        option = input()
        if option == '1':
            task = createTask()
            manager.addTask(task)
            print(f'Task add with sucess!')
        elif option == '2':
            manager.printTaskManager()
        elif option == '3':
            manager.removeLastTask()
            print(f'Task removed with sucess!')
        elif option == '4':
            manager.clearTaskManager()
        elif option == '5':
            print('Exiting...')
            break

if __name__ == '__main__':
    main()
