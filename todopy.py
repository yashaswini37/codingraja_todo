import tkinter as tk
from tkinter import ttk

tasks = []

def add_task():
    task = task_entry.get()
    priority = priority_var.get()
    due_date = due_date_entry.get()
    description = description_entry.get("1.0", tk.END).strip() if description_enabled.get() else ""
    if task and due_date:
        task_details = (task, priority, due_date, description)
        tasks.append(task_details)
        update_listbox()
        task_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        description_entry.delete("1.0", tk.END)

def remove_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_listbox()

def mark_as_completed():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        tasks[selected_task[0]] = ("✔ " + tasks[selected_task[0]][0], tasks[selected_task[0]][1], tasks[selected_task[0]][2], tasks[selected_task[0]][3])
        update_listbox()

def update_listbox():
    tasks_listbox.delete(0, tk.END)
    for task, priority, due_date, description in tasks:
        task_text = f"{task} ({priority}) - Due: {due_date}"
        if description:
            task_text += f"\nDescription: {description}"
        tasks_listbox.insert(tk.END, task_text)

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

priority_var = tk.StringVar(root)
priority_var.set("Low")  # default priority

priority_label = tk.Label(root, text="Priority:")
priority_label.pack()

priority_dropdown = ttk.Combobox(root, textvariable=priority_var, values=["Low", "Medium", "High"])
priority_dropdown.pack()

due_date_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
due_date_label.pack()

due_date_entry = tk.Entry(root, width=30)
due_date_entry.pack(pady=5)

description_enabled = tk.BooleanVar(root)
description_enabled.set(False)

description_checkbox = tk.Checkbutton(root, text="Add Description", variable=description_enabled)
description_checkbox.pack()

description_label = tk.Label(root, text="Description:")
description_label.pack()

description_entry = tk.Text(root, width=30, height=5)
description_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

mark_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed)
mark_button.pack()

tasks_listbox = tk.Listbox(root, width=50)
tasks_listbox.pack(pady=10)

update_listbox()

root.mainloop()