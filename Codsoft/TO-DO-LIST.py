import json
from datetime import datetime

def load_todo_list():
    try:
        with open("todo_list.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_todo_list(todo_list):
    with open("todo_list.json", "w") as file:
        json.dump(todo_list, file, indent=2)

def show_todo_list(todo_list):
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task['title']} - {task['due_date']}")

def add_task(todo_list):
    title = input("Enter the task title: ")
    due_date = input("Enter the due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    task = {"title": title, "due_date": due_date.strftime("%Y-%m-%d")}
    todo_list.append(task)
    save_todo_list(todo_list)
    print("Task added successfully.")

def update_task(todo_list):
    show_todo_list(todo_list)

    try:
        task_index = int(input("Enter the index of the task to update: ")) - 1
        if 0 <= task_index < len(todo_list):
            new_title = input("Enter the new task title: ")
            new_due_date = input("Enter the new due date (YYYY-MM-DD): ")

            try:
                new_due_date = datetime.strptime(new_due_date, "%Y-%m-%d").date()
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
                return

            todo_list[task_index]["title"] = new_title
            todo_list[task_index]["due_date"] = new_due_date.strftime("%Y-%m-%d")
            save_todo_list(todo_list)
            print("Task updated successfully.")
        else:
            print("Invalid task index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def main():
    todo_list = load_todo_list()

    while True:
        print("\nTo-Do List Application")
        print("1. Show To-Do List")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            show_todo_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            update_task(todo_list)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
