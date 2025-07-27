import os

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks,1):
            print(f"{i}. {task}\n")

def add_task(tasks, new_tasks):
    tasks.append(new_tasks)
    print("Task Added successfully")

def mark_done(tasks,index,mark_done):
    if 1 <= index <=len(tasks):
        tasks[index-1] = mark_done
        print("Task marked done successfully")
    else:
        print("invalid Task index. ")


def delete_task(tasks,index):
    if 1 <= index <=len(tasks):
        delete_task = tasks.pop(index-1)
        print(f"Task '{delete_task}' deleted successfully")
    else:
        print("Invalid Task Index. ")     
     
def save_task(file_path, tasks):
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(f"{tasks}\n")


def load_tasks_from_file(file_path):
    task=[]
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            task = file.read().splitlines()
    return task


def main():
    file_path = "todo_list.txt"
    tasks = load_tasks_from_file(file_path)
    while True:
        print("\n==== TO DO LIST ==== ")
        print("1. show task")
        print("2. add task")
        print("3. mark as done")
        print("4. delete task")
        print("5. exit")
        choice = input("Enter your choice (1-5): ")
        if choice=="1":
            show_tasks(tasks)
        elif choice=="2":
            new_task = input("Enter the task to  add: ")
            add_task(tasks,new_task)
        elif choice=="3":
            index = int(input("Enter the task index to marked"))
            mark_done = input("Enter the task marked done : ")
            mark_done(tasks,index,mark_done)
        elif choice=="4":
            index = int(input("Enter thge task index to delete: "))
            delete_task(tasks,index)
        elif choice=="5":
            save_task(tasks)
            print("tasks saved. exiting.. ")
            break
        else:
            print("Invalid choice. Please try again ")

if __name__ == "__main__":
    main()