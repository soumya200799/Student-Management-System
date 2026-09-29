# Design Decisions

## 1. Console Interface
A console application was selected because it is simple to implement and suitable for a beginner Python project.

## 2. Dictionary-Based Storage
A dictionary was selected because student names can be used as keys for direct lookup.

## 3. Nested Student Records
Each student has a nested dictionary containing attendance and grade fields. This keeps related information together.

## 4. Menu-Driven Design
A numbered menu makes the available operations clear and allows repeated use without restarting the program.

## 5. In-Memory Storage
The current project intentionally avoids database or file storage to keep the implementation simple and focused on Python fundamentals.

## 6. Separate Functional Options
Adding students, attendance, reporting, searching, deleting, calculating and grading are represented as separate menu choices.

## 7. Grade Thresholds
The grade thresholds directly follow the rules implemented in `app.py`.
