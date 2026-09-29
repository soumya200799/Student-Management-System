# Student Management System

## Project Overview

The **Student Management System** is a Python-based, menu-driven console application developed to manage basic student academic information.

The project allows a user to add students, record attendance, view reports, search for individual students, delete student records, perform basic calculations, and assign grades.

The project is designed as a practical application of Python programming concepts such as **dictionaries, loops, conditional statements, functions of input/output, arithmetic operators, and data validation**.

This project follows the VITyarthi *Build Your Own Project* requirements by providing functional modules, a clear user workflow, documentation, testing information, and an organized GitHub-ready project structure.

## Problem Statement

Managing student names, attendance, and grades manually can be time-consuming and difficult to maintain. A simple computerized system can make these tasks easier by providing a structured way to enter, update, search, and display student information.

The proposed system provides a console-based solution for maintaining basic student academic records during a program session.

## Objectives

- Add and maintain student names.
- Record student attendance.
- Calculate and display attendance percentage.
- Warn when attendance is below 75%.
- View a summary report of students.
- Search for individual student records.
- Delete student records.
- Store and classify student grades.
- Provide a basic calculator.
- Demonstrate practical Python programming concepts.

## Features

### 1. Add Student
Adds a new student name to the system and creates an initial record:

- Present attendance = 0
- Total attendance = 0
- Grade = 0.0

### 2. Mark Attendance
Records whether a student is present or absent.

- `P` increases the present count.
- Every attendance entry increases the total count.

### 3. View Report
Displays:

- Student name
- Number of present days
- Total attendance days
- Grade

### 4. Search Student
Displays an individual student's:

- Name
- Present days
- Total attendance
- Attendance percentage
- Grade

A warning is displayed when attendance is below 75%.

### 5. Delete Student
Removes an existing student from the system.

### 6. Calculator
Supports:

- Addition
- Subtraction
- Multiplication
- Division
- Exponentiation
- Modulus
- Floor division

### 7. Set Grade
Accepts a grade from 0 to 100 and classifies it as:

| Score | Grade | Description |
|---:|:---:|---|
| 90–100 | A | Excellent |
| 80–89.99 | B | Good |
| 70–79.99 | C | Can do better |
| 60–69.99 | D | Efforts needed |
| 40–59.99 | E | Please work on your grades |
| 0–39.99 | F | Fail |

## Technologies / Tools Used

- **Programming Language:** Python 3.x
- **Data Structure:** Python Dictionary
- **Interface:** Command Line / Console
- **Version Control:** Git / GitHub
- **External Libraries:** None

## Student Data Structure

The application stores student information in a nested Python dictionary:

```python
student = {
    "Student Name": {
        "present": 0,
        "total": 0,
        "grade": 0.0
    }
}
```

## Attendance Calculation

The attendance percentage is calculated as:

```text
Attendance Percentage = (Present Days / Total Attendance Days) × 100
```

If no attendance has been recorded, the percentage is displayed as 0%.

## Installation

### Prerequisites

Install Python 3.x on your computer.

Check the installation with:

```bash
python --version
```

or:

```bash
python3 --version
```

### Clone the Repository

```bash
git clone <your-github-repository-url>
cd student_management_system
```

### Run the Application

```bash
python app.py
```

## How to Use

After starting the program, the following main menu is displayed:

```text
==Main Menu==
1. Add the name of the student
2. Mark Attendance
3. View Report
4. Search Student
5. Delete Student
6. Calculator
7. Set Grade
8. Exit
```

Enter the number corresponding to the required operation.

## Example Workflow

1. Select `1` and add a student.
2. Select `2` and record attendance.
3. Select `7` and enter the student's grade.
4. Select `3` to view the overall report.
5. Select `4` to view an individual student's attendance percentage.
6. Select `5` if a student needs to be removed.
7. Select `8` to exit.

## Testing

The project includes a `testing.md` file containing functional test cases for:

- Adding students
- Duplicate student detection
- Attendance
- Reports
- Student search
- Student deletion
- Grade validation
- Grade classification
- Calculator operations
- Invalid choices
- Exit operation

Run the application and execute the test cases manually through the console.

## Project Structure

```text
student_management_system/
│
├── .gitignore
├── README.md
├── app.py
├── statement.md
├── functional_requirements.md
├── non_functional_requirements.md
├── system_architecture.md
├── workflow.md
├── use_case.md
├── component_diagram.md
├── sequence_diagram.md
├── design_decisions.md
├── implementation_details.md
└── testing.md
```

## Design and Documentation

The project documentation includes:

- Problem Statement
- Objectives
- Functional Requirements
- Non-Functional Requirements
- System Architecture
- Workflow
- Use Case
- Component Diagram
- Sequence Diagram
- Design Decisions
- Implementation Details
- Testing

These artefacts support the VITyarthi project documentation requirements.

## Limitations

The current implementation stores data only in memory. Therefore, all student information is lost when the application is closed.

The current version also does not include:

- Database storage
- Login/authentication
- Graphical user interface
- Automatic file backup
- Advanced exception handling

## Future Enhancements

Possible future improvements include:

- Save student data in CSV/JSON/database storage.
- Add a graphical user interface.
- Add login and role-based access.
- Add automatic attendance reports.
- Add subject-wise grades.
- Add student ID/roll number.
- Export reports to PDF or Excel.
- Add stronger input and exception handling.
- Add automated unit tests.

## Conclusion

The Student Management System demonstrates how basic Python programming concepts can be combined to solve a practical student-record management problem. It provides a clear menu-driven workflow and implements student management, attendance, grading, reporting, searching, deletion, and calculator operations.

## References

- VITyarthi – Build Your Own Project: General Project Instructions & Submission Guidelines.
- Python 3.x documentation and standard language concepts.
