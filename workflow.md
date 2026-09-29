# Workflow

```text
START
  |
  v
Initialize student = {}
  |
  v
Display Main Menu
  |
  +--> 1 Add Student --------+
  |                           |
  +--> 2 Mark Attendance -----+
  |                           |
  +--> 3 View Report ---------+
  |                           |
  +--> 4 Search Student ------+
  |                           |
  +--> 5 Delete Student ------+
  |                           |
  +--> 6 Calculator ----------+
  |                           |
  +--> 7 Set Grade -----------+
  |                           |
  +--> 8 Exit --> END         |
  |                           |
  +------ Invalid Choice -----+
              |
              v
        Display Error
              |
              v
        Return to Menu
```

## Attendance Workflow

```text
Select student
      |
      v
Enter P/A
      |
      v
Increase total attendance
      |
      +---- P ----> Increase present count
      |
      +---- Other -> Mark absent
      |
      v
Return to main menu
```

## Grade Workflow

```text
Select student
      |
      v
Enter grade
      |
      v
Is grade 0-100?
   /           Yes           No
  |             |
Store grade    Error
  |
Classify A-F
  |
Return to menu
```
