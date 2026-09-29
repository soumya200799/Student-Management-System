# Implementation Details

## Language
Python 3.x

## Main Data Structure

```python
student = {}
```

Each key is a student name. The value is another dictionary containing:

- `present`: number of present days
- `total`: total attendance days
- `grade`: numeric grade

## Main Control Flow

The program uses:

```python
while True:
```

to repeatedly display the main menu until the user selects Exit.

## Attendance Calculation

For a student with at least one attendance record:

```python
percentage = (present / total) * 100
```

If no attendance has been recorded, the percentage is set to 0.

## Grade Logic

Grades are classified using descending thresholds:

- 90 or more: A
- 80 or more: B
- 70 or more: C
- 60 or more: D
- 40 or more: E
- Below 40: F

## Calculator

The calculator uses `float` values and Python arithmetic operators.

## Input Validation

The program validates:
- Student existence for student-specific operations.
- Grade range from 0 to 100.
- Main-menu and calculator choices.

The current implementation does not catch non-numeric input errors or division by zero.
