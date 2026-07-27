[READ.md](https://github.com/user-attachments/files/30425271/READ.md)[Uploading READ# Student Grade Management System

A simple Python console-based application to manage student records. This project allows users to add, update, delete, search, and view student records while automatically calculating grades and pass/fail status. Student data is stored permanently using a CSV file.

---

## Features

- Add Student
- View All Students
- Search Student by Name
- Update Student Score
- Delete Student Record
- Calculate Grades Automatically
- Pass/Fail Status
- Class Statistics
- Show Class Topper
- Count Passed and Failed Students
- Sort Students by Name
- Sort Students by Score
- Save Data in CSV File
- Load Data Automatically on Startup

---

## Technologies Used

- Python 3
- CSV Module
- OS Module

---

## Project Structure

```
Student-Grade-Management-System/
│
├── main.py
├── students.csv
└── README.md
```

---

## Grade Criteria

| Score | Grade |
|--------|-------|
| 90 - 100 | A |
| 80 - 89 | B |
| 70 - 79 | C |
| 60 - 69 | D |
| 59 - 50 | E |
| Below 50 | F |

---

## Pass / Fail Criteria

- Score **50 or above** → Pass
- Score **Below 50** → Fail

---

## Menu Options

```
1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Class Statistics
7. Show Topper
8. Pass / Fail Count
9. Sort By Name
10. Sort By Score
11. Exit
```

---

## How to Run

1. Install Python 3.
2. Download or clone this project.
3. Open the project folder.
4. Run the program using:

```bash
python main.py
```

---

## Data Storage

Student records are saved in **students.csv**.

Each record contains:

- Student ID
- Student Name
- Score
- Grade
- Pass/Fail Status

The data is automatically loaded when the program starts.

---

## Sample Output

```
===================================
 Student Grade Management System
===================================

1. Add Student
2. View All Students
3. Search Student
4. Update Student
5. Delete Student
6. Class Statistics
7. Show Topper
8. Pass / Fail Count
9. Sort By Name
10. Sort By Score
11. Exit

Enter Choice:
```

---

## Future Improvements

- Login System
- GPA Calculator
- Multiple Subjects
- Student Attendance
- Export Reports
- Graphical User Interface (GUI)
- Database Integration (MySQL/SQLite)




.md…]()
