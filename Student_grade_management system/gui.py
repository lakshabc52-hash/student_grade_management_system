import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv
import os

root = tk.Tk()

root.title("Student Grade Management System")

root.geometry("900x600")

root.resizable(False, False)

root.configure(bg="#f0f8ff")

heading = tk.Label(
    root,
    text="Student Grade Management System",
    font=("Arial", 20, "bold"),
    bg="#f0f8ff",
    fg="darkblue"
)

heading.pack(pady=20)

students = []
student_id = 1
FILE_NAME = "students.csv"

# ==============================
# Input Frame
# ==============================

input_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
input_frame.pack(pady=20, padx=20, fill="x")

# Name
name_label = tk.Label(
    input_frame,
    text="Student Name",
    font=("Arial", 12),
    bg="white"
)
name_label.grid(row=0, column=0, padx=10, pady=15, sticky="w")

name_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=30
)
name_entry.grid(row=0, column=1, padx=10)

# Score
score_label = tk.Label(
    input_frame,
    text="Student Score",
    font=("Arial", 12),
    bg="white"
)
score_label.grid(row=0, column=2, padx=10)

score_entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    width=15
)
score_entry.grid(row=0, column=3, padx=10)

# ==============================
# Grade Function
# ==============================

def calculate_grade(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# ==============================
# Pass / Fail
# ==============================

def pass_fail(score):

    if score >= 50:
        return "Pass"
    else:
        return "Fail"
    
# ==============================
# Add Student Function
# ==============================

def add_student():

    global student_id

    name = name_entry.get().strip()
    score = score_entry.get().strip()

    if name == "" or score == "":
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        score = float(score)
    except ValueError:
        messagebox.showerror("Error", "Invalid Score.")
        return

    if score < 0 or score > 100:
        messagebox.showerror("Error", "Score must be between 0 and 100.")
        return

    grade = calculate_grade(score)
    status = pass_fail(score)

    student_table.insert(
        "",
        tk.END,
        values=(student_id, name, score, grade, status)
    )

    student_id += 1

    name_entry.delete(0, tk.END)
    score_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Student Added Successfully!")    

# Add Button
add_btn = tk.Button(
    input_frame,
    text="Add Student",
    font=("Arial", 11, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=add_student
)

add_btn.grid(row=0, column=4, padx=20)

# ==============================
# Student Table
# ==============================

table_frame = tk.Frame(root)
table_frame.pack(padx=20, pady=10, fill="both", expand=True)

columns = ("ID", "Name", "Score", "Grade", "Status")

student_table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=15
)

# Column Headings
student_table.heading("ID", text="ID")
student_table.heading("Name", text="Student Name")
student_table.heading("Score", text="Score")
student_table.heading("Grade", text="Grade")
student_table.heading("Status", text="Status")

# Column Width
student_table.column("ID", width=60, anchor="center")
student_table.column("Name", width=250, anchor="center")
student_table.column("Score", width=100, anchor="center")
student_table.column("Grade", width=100, anchor="center")
student_table.column("Status", width=120, anchor="center")

# Scrollbar
scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=student_table.yview
)

student_table.configure(yscrollcommand=scrollbar.set)

student_table.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
