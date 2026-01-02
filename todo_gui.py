import tkinter as tk
from tkinter import messagebox
import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(" | ")
                if len(parts) == 2:
                    task, status = parts
                    tasks.append({"task": task, "done": status=="Done"})
    return tasks

def save_tasks():
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        for t in tasks:
            status = "Done" if t["done"] else "Pending"
            file.write(f"{t['task']} | {status}\n")

def refresh_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        status = "✔" if t["done"] else "✖"
        listbox.insert(tk.END, f"{t['task']} [{status}]")

def add_task():
    task = task_entry.get()
    if task:
        tasks.append({"task": task, "done": False})
        task_entry.delete(0, tk.END)
        refresh_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Enter a task!")

def mark_done():
    try:
        index = listbox.curselection()[0]
        tasks[index]["done"] = True
        refresh_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task!")

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        refresh_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task!")

# Initialize tasks
tasks = load_tasks()

# Create window
root = tk.Tk()
root.title("To-Do List App")

# Input field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

tk.Button(button_frame, text="Add Task", width=12, command=add_task).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Mark Done", width=12, command=mark_done).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Task", width=12, command=delete_task).grid(row=0, column=2, padx=5)

# Listbox
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)
refresh_listbox()

# Run app
root.mainloop()
def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["done"] else "✖"
        print(f"{i}. {t['task']} [{status}]")

def main()  :
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