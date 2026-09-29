# System Architecture

The application follows a simple single-process console architecture.

```text
User
 |
 v
+---------------------+
| Console Input/Output|
+----------+----------+
           |
           v
+---------------------+
| Application Control |
|     app.py          |
+----------+----------+
           |
           v
+---------------------+
| Student Dictionary  |
| In-Memory Storage   |
+---------------------+
```

## Architecture Characteristics

- Single Python application.
- No external services.
- No database.
- No network communication.
- No external Python packages.
- Data exists only during the program session.

## Processing Flow

1. Start application.
2. Create empty student dictionary.
3. Display main menu.
4. Accept user choice.
5. Execute selected operation.
6. Return to main menu.
7. Exit when option 8 is selected.
