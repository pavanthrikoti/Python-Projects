import json
import os

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task_description):
    tasks.append({"description": task_description, "completed": False})
    print(f"Task '{task_description}' added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{idx}. [{status}] {task['description']}")

def complete_task(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index-1]["completed"] = True
        print(f"Task '{tasks[index-1]['description']}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(tasks, index):
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index-1)
        print(f"Task '{removed_task['description']}' removed.")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            task_description = input("Enter task description: ")
            if task_description.strip():
                add_task(tasks, task_description)
                save_tasks(tasks)
            else:
                print("Task description cannot be empty.")
                
        elif choice == "2":
            view_tasks(tasks)
            
        elif choice == "3":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to mark as complete: "))
                complete_task(tasks, index)
                save_tasks(tasks)
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "4":
            view_tasks(tasks)
            try:
                index = int(input("Enter task number to remove: "))
                remove_task(tasks, index)
                save_tasks(tasks)
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()