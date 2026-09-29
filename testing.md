# Testing

## Test Environment

- Python 3.x
- Console/terminal
- No external dependencies

## Functional Test Cases

| Test ID | Feature | Test Input | Expected Result |
|---|---|---|---|
| T01 | Add student | `1`, `Rahul` | Rahul is added |
| T02 | Duplicate student | Add Rahul again | Already Exists message |
| T03 | Attendance present | `2`, Rahul, `P` | Total +1 and Present +1 |
| T04 | Attendance absent | `2`, Rahul, `A` | Total +1, Present unchanged |
| T05 | View report | `3` | Student records are displayed |
| T06 | Search existing | `4`, Rahul | Student details and percentage shown |
| T07 | Search missing | `4`, Amit | Student not found |
| T08 | Delete existing | `5`, Rahul | Student is deleted |
| T09 | Delete missing | `5`, Amit | Student not found |
| T10 | Grade valid | `7`, Rahul, `85` | Grade B is displayed |
| T11 | Grade invalid | `7`, Rahul, `105` | Range error is displayed |
| T12 | Calculator addition | `6`, `a`, `10`, `5` | Result 15 |
| T13 | Calculator subtraction | `6`, `b`, `10`, `5` | Result 5 |
| T14 | Calculator multiplication | `6`, `c`, `10`, `5` | Result 50 |
| T15 | Calculator division | `6`, `d`, `10`, `5` | Result 2 |
| T16 | Calculator exponentiation | `6`, `e`, `2`, `3` | Result 8 |
| T17 | Calculator modulus | `6`, `f`, `10`, `3` | Result 1 |
| T18 | Calculator floor division | `6`, `g`, `10`, `3` | Result 3 |
| T19 | Exit | `8` | Application exits |

## Edge Cases

- Search for a student before any student has been added.
- Search a student with zero attendance.
- Enter grade 0.
- Enter grade 100.
- Enter a grade below 0 or above 100.
- Enter an invalid menu option.
- Attempt calculator division by zero.

## Current Limitations

The current code does not explicitly handle:
- Non-numeric input where `float()` is required.
- Division/modulus/floor-division by zero.
- Case-insensitive attendance input (`p` is treated as absent).
