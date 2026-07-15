from datetime import datetime

def userChoice(tasks,choice):

    if choice == 1:
        task_name = input("Enter task name: ")
        deadline = input("Enter deadline (DD-MM-YYYY): ")
        add_task(tasks, task_name, deadline)
    elif choice == 2:
        if not tasks:
            print("No tasks available\n")
            return
        
        display_tasks(tasks)
        task_number = int(input("Enter task number to be deleted: "))
        delete_task(tasks, task_number)
    elif choice == 3:
        display_tasks(tasks)
    elif choice == 4:
        return "Exiting Application..."
    else:
        print("Invalid Choice\n")


def validate_date(deadline):
    
    try:
        deadline_date = datetime.strptime(deadline, "%d-%m-%Y").date()
        return deadline_date

    except ValueError:
        """exception occured, print an error message"""
        print("Invalid Date format! Try Again\n")

def add_task(tasks, task_name, deadline):
    deadline_date = validate_date(deadline) 

    tasks.append({"task": task_name, "deadline": deadline_date})
    print(f"Task '{task_name}' added successfully\n")


def delete_task(tasks, task_number):

    task_index = task_number -1

    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"{removed_task['task']} removed successfully\n")
    else:
        print("Invalid Task number!\n")


def display_tasks(tasks):
    if not tasks:
        print("No tasks available\n")
        return
    
    index = 0
    print("\nYour Tasks:")
    for task in tasks:
        formatted_deadline = task['deadline'].strftime("%d-%m-%Y")
        print(f"{index+1}. {task['task']} - Deadline: {formatted_deadline}")
        index += 1
    print()


if __name__ == "__main__":

    
    print("""Welcome to to-do list Appplication""")

    tasks = []   
    while True:
        print("choose one operation")
        print("1. Add a Task")
        print("2. Delete a Task")
        print("3. Display all tasks")
        print("4. Exit")

        choice = int(input("Enter your choice: ").strip())
        value = userChoice(tasks, choice)

        if value == "Exiting Application...":
            print(value)
            break