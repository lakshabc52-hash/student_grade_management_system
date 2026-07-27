# ==========================================
# Student Grade Management System
# Part 1
# ==========================================

import csv
import os
students = []
student_id = 1
FILE_NAME = " students.csv"

# -----------------------------
# Grade Function
# -----------------------------
def calculate_grade(score):

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60 :
        return "D"
    
    elif score >= 50 :
        return "E"
    
    else:
        return "F"


# -----------------------------
# Pass / Fail Function
# -----------------------------
def pass_fail(score):

    if score >= 50:
        return "Pass"
    else:
        return "Fail"
# -----------------------------
# Save Data
# -----------------------------
def save_data():

    with open(FILE_NAME, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["ID", "Name", "Score", "Grade", "Status"])

        for student in students:

            writer.writerow([
                student["id"],
                student["name"],
                student["score"],
                student["grade"],
                student["status"]
            ])


# -----------------------------
# Load Data
# -----------------------------
def load_data():

    global student_id

    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as file:

        reader = csv.DictReader(file)

        students.clear()

        highest_id = 0

        for row in reader:

            student = {

                "id": int(row["ID"]),
                "name": row["Name"],
                "score": float(row["Score"]),
                "grade": row["Grade"],
                "status": row["Status"]

            }

            students.append(student)

            if student["id"] > highest_id:
                highest_id = student["id"]

        student_id = highest_id + 1

# -----------------------------
# Add Student
# -----------------------------
def add_student():

    global student_id

    while True:

        name = input("Enter Student Name : ").strip()

        if name == "":
            print("Name cannot be empty.")

        else:
            break

    while True:

        try:

            score = float(input("Enter Student Score (0-100): "))

            if score < 0 or score > 100:
                print("Score must be between 0 and 100.")

            else:
                break

        except ValueError:
            print("Invalid score.")

    student = {
        "id": student_id,
        "name": name,
        "score": score,
        "grade": calculate_grade(score),
        "status": pass_fail(score)
    }

    students.append(student)

    student_id += 1
    
    save_data()

    print("\nStudent Added Successfully.\n")


# -----------------------------
# View All Students
# -----------------------------
def view_students():

    if len(students) == 0:
        print("\nNo Student Record Found.\n")
        return

    print("\n================ STUDENT RECORDS ================\n")

    print("{:<5} {:<20} {:<10} {:<10} {:<10}".format(
        "ID",
        "Name",
        "Score",
        "Grade",
        "Status"
    ))

    print("-" * 60)

    for student in students:

        print("{:<5} {:<20} {:<10} {:<10} {:<10}".format(

            student["id"],
            student["name"],
            student["score"],
            student["grade"],
            student["status"]
        ))

    print()
    
    
# -----------------------------
# Search Student
# -----------------------------
def search_student():

    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    name = input("Enter student name to search: ").strip().lower()

    found = False

    for student in students:

        if student["name"].lower() == name:

            print("\nStudent Found")
            print("-" * 30)
            print("ID     :", student["id"])
            print("Name   :", student["name"])
            print("Score  :", student["score"])
            print("Grade  :", student["grade"])
            print("Status :", student["status"])
            print()

            found = True
            break

    if not found:
        print("\nStudent not found.\n")


# -----------------------------
# Update Student
# -----------------------------
def update_student():

    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    try:
        student_id_input = int(input("Enter Student ID: "))

    except ValueError:
        print("Invalid ID.")
        return

    for student in students:

        if student["id"] == student_id_input:

            while True:

                try:

                    new_score = float(input("Enter New Score: "))

                    if 0 <= new_score <= 100:
                        break
                    else:
                        print("Score must be between 0 and 100.")

                except ValueError:
                    print("Invalid score.")

            student["score"] = new_score
            student["grade"] = calculate_grade(new_score)
            student["status"] = pass_fail(new_score)
            save_data()
            print("\nStudent updated successfully.\n")
            return

    print("\nStudent ID not found.\n")


# -----------------------------
# Delete Student
# -----------------------------
def delete_student():

    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    try:
        student_id_input = int(input("Enter Student ID: "))

    except ValueError:
        print("Invalid ID.")
        return

    for student in students:

        if student["id"] == student_id_input:

            students.remove(student)
            save_data()
            print("\nStudent deleted successfully.\n")
            return

    print("\nStudent ID not found.\n")    
    
    
# -----------------------------
# Class Statistics
# -----------------------------
def statistics():

    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    scores = [student["score"] for student in students]

    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print("\n========== CLASS STATISTICS ==========\n")

    print("Total Students :", len(students))
    print("Average Score  :", round(average, 2))
    print("Highest Score  :", highest)
    print("Lowest Score   :", lowest)
    print()


# -----------------------------
# Show Topper
# -----------------------------
def show_topper():

    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    topper = max(students, key=lambda student: student["score"])

    print("\n========== CLASS TOPPER ==========\n")

    print("ID     :", topper["id"])
    print("Name   :", topper["name"])
    print("Score  :", topper["score"])
    print("Grade  :", topper["grade"])
    print()


# -----------------------------
# Pass / Fail Count
# -----------------------------
def pass_fail_count():

    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    passed = 0
    failed = 0

    for student in students:

        if student["status"] == "Pass":
            passed += 1
        else:
            failed += 1

    print("\n========== RESULT SUMMARY ==========\n")

    print("Passed Students :", passed)
    print("Failed Students :", failed)
    print()


# -----------------------------
# Sort By Name
# -----------------------------
def sort_by_name():

    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    students.sort(key=lambda student: student["name"].lower())
    save_data()
    print("\nStudents Sorted By Name.\n")


# -----------------------------
# Sort By Score
# -----------------------------
def sort_by_score():

    if len(students) == 0:
        print("\nNo student records found.\n")
        return

    students.sort(key=lambda student: student["score"], reverse=True)
    save_data()
    print("\nStudents Sorted By Score.\n")    
    


# -----------------------------
# Main Menu
# -----------------------------

# -----------------------------
# Login System
# -----------------------------
def login():

    USERNAME = "admin"
    PASSWORD = "1234"

    print("\n========== LOGIN ==========\n")

    while True:

        username = input("Username : ")
        password = input("Password : ")

        if username == USERNAME and password == PASSWORD:

            print("\nLogin Successful!\n")
            break

        else:

            print("\nInvalid Username or Password.")
            print("Please try again.\n")
            

def main():
    login()
    load_data()
    
    while True:

        print("===================================")
        print(" Student Grade Management System")
        print("===================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Class Statistics")
        print("7. Show Topper")
        print("8. Pass / Fail Count")
        print("9. Sort By Name")
        print("10. Sort By Score")
        print("11. Exit")
        
        choice = input("\nEnter Choice : ")

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":
            
            search_student()

        elif choice == "4":

           update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            statistics()
            

        elif choice == "7":
            show_topper()

        elif choice == "8":
            pass_fail_count()

        elif choice == "9":
            sort_by_name()

        elif choice == "10":
            sort_by_score()

        elif choice == "11":

            confirm = input("Are you sure you want to exit? (Y/N): ")

            if confirm.lower() == "y":
                print("\nThank You For Using The System.")
                break


main()