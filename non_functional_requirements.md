# Non-Functional Requirements

## Usability
- The application shall use a simple numbered menu.
- Prompts shall clearly request the required input.
- Results shall be displayed in readable text.

## Performance
- Student lookup uses a Python dictionary and is suitable for a small number of records.
- Operations should execute immediately for normal classroom-sized datasets.

## Portability
- The program should run on systems supporting Python 3.x.
- No third-party libraries are required.

## Maintainability
- Student data is grouped in a consistent dictionary structure.
- Menu options are separated using conditional branches.

## Reliability
- The program checks whether a student exists before search, attendance, deletion and grade updates.
- Grade values are checked against the 0–100 range.

## Data Persistence
- The current implementation does not persist records to a file or database.
- All records are lost when the program terminates.
