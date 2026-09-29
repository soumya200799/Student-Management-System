# Component Diagram

```text
+--------------------------------------------------+
|              Student Management System            |
+--------------------------------------------------+
|                                                  |
|  +-------------+     +------------------------+  |
|  | Main Menu   |---->| Student Data Dictionary|  |
|  +-------------+     +------------------------+  |
|        |                         |               |
|        +---- Add Student        |               |
|        +---- Attendance         |               |
|        +---- View Report        |               |
|        +---- Search Student     |               |
|        +---- Delete Student     |               |
|        +---- Set Grade          |               |
|        +---- Calculator         |               |
|        +---- Exit               |               |
|                                  |               |
+--------------------------------------------------+
```

## Components

### Main Menu
Controls the application loop and receives the user's choice.

### Student Data Dictionary
Stores student names and their attendance/grade records.

### Attendance Module
Updates `present` and `total` counts.

### Report/Search
Reads student records and calculates attendance percentage.

### Grade Module
Stores a score and classifies it from A to F.

### Calculator
Performs seven arithmetic operations.
