import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    """Load tasks from file"""
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            for line in file:
                # Each line: task | status
                parts = line.strip().split(" | ")
                if len(parts) == 2:
                    task, status = parts
                    tasks.append({"task": task, "done": status=="Done"})
    return tasks

def save_tasks(tasks):
    """Save tasks to file"""
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for t in tasks:
            status = "Done" if t["done"] else "Pending"
            file.write(f"{t['task']} | {status}\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
    else:
        print("\n--- TO-DO LIST ---")
        for i, t in enumerate(tasks, start=1):
            status = "✔" if t["done"] else "✖"
            print(f"{i}. {t['task']} [{status}]")

def main():
    tasks = load_tasks()
    print("Welcome to CLI To-Do List App!")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == "1":
            task = input("Enter new task: ")
            tasks.append({"task": task, "done": False})
            save_tasks(tasks)
            print(f"Task '{task}' added.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            display_tasks(tasks)
            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks[num-1]["done"] = True
                    save_tasks(tasks)
                    print(f"Task '{tasks[num-1]['task']}' marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            display_tasks(tasks)
            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num-1)
                    save_tasks(tasks)
                    print(f"Task '{removed['task']}' deleted.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
