# Sequence Diagram

## Add Student

```text
User -> Application: Select 1
User -> Application: Enter student name
Application -> Student Dictionary: Check name
Student Dictionary --> Application: Exists / Not Exists
Application -> Student Dictionary: Create record
Application --> User: Student Added
```

## Mark Attendance

```text
User -> Application: Select 2
Application --> User: Display student list
User -> Application: Enter student name
Application -> Student Dictionary: Find student
User -> Application: Enter P/A
Application -> Student Dictionary: Increment total
Application -> Student Dictionary: Increment present if P
Application --> User: Attendance result
```

## Search Student

```text
User -> Application: Select 4
User -> Application: Enter student name
Application -> Student Dictionary: Find record
Application -> Application: Calculate attendance %
Application --> User: Display student report
```

## Set Grade

```text
User -> Application: Select 7
User -> Application: Enter student name
User -> Application: Enter grade
Application -> Student Dictionary: Validate and store grade
Application -> Application: Determine grade category
Application --> User: Display grade result
```
