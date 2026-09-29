# Use Case Specification

## Actors

**Primary Actor:** User / Student Record Administrator

## Use Cases

| ID | Use Case | Description |
|---|---|---|
| UC-01 | Add Student | Add a new student name |
| UC-02 | Mark Attendance | Record present/absent status |
| UC-03 | View Report | Display all student records |
| UC-04 | Search Student | Display one student's details |
| UC-05 | Delete Student | Remove a student |
| UC-06 | Calculator | Perform arithmetic operations |
| UC-07 | Set Grade | Store and classify a grade |
| UC-08 | Exit | Close the application |

## Typical Search Flow

1. User selects Search Student.
2. User enters the student name.
3. System checks the dictionary.
4. If found, the system calculates attendance percentage.
5. The system displays attendance and grade.
6. If attendance is below 75%, a warning is displayed.
7. If not found, the system displays `Student not found.`
