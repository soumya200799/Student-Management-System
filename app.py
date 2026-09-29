# Student Management System

student = {}

while True:
    print("\n==Main Menu==")
    print("1. Add the name of the student")
    print("2. Mark Attendance")
    print("3. View Report")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Calculator")
    print("7. Set Grade")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in student:
            print(name, "Already Exists.")
        else:
            student[name] = {"present": 0, "total": 0, "grade": 0.0}
            print(name, "Added.")

    elif choice == "2":
        print("Students:", list(student.keys()))
        name = input("Enter student name: ")

        if name in student:
            status = input("Is the student present today? (P/A): ")
            student[name]["total"] += 1
            if status == "P":
                student[name]["present"] += 1
                print(f"Attendance for {name} marked as PRESENT.")
            else:
                print(f"Attendance for {name} marked as ABSENT.")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\nName\tPresent\tTotal\tGrade")
        for name, record in student.items():
            print(
                f"{name}\t{record['present']}\t"
                f"{record['total']}\t{record['grade']:.2f}"
            )

    elif choice == "4":
        name = input("Enter student name to search: ")

        if name in student:
            record = student[name]
            if record["total"] > 0:
                percentage = (record["present"] / record["total"]) * 100
            else:
                percentage = 0

            print("Name:", name)
            print("Present:", record["present"])
            print("Total:", record["total"])
            print("Percentage:", f"{percentage:.2f}%")
            print("Grade:", f"{record['grade']:.2f}")

            if percentage < 75:
                print("Warning: Attendance is below 75%!")
        else:
            print("Student not found.")

    elif choice == "5":
        print("Students:", list(student.keys()))
        name = input("Enter student name to delete: ")

        if name in student:
            del student[name]
            print(name, "Deleted Successfully.")
        else:
            print("Student not found.")

    elif choice == "6":
        print("\na. Add")
        print("b. Subtract")
        print("c. Multiply")
        print("d. Divide")
        print("e. Exponentiation")
        print("f. Modulus")
        print("g. Floor Division")
        sub_choice = input("Enter choice: ")

        if sub_choice in ("a", "b", "c", "d", "e", "f", "g"):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if sub_choice == "a":
                print("Result:", num1 + num2)
            elif sub_choice == "b":
                print("Result:", num1 - num2)
            elif sub_choice == "c":
                print("Result:", num1 * num2)
            elif sub_choice == "d":
                print("Result:", num1 / num2)
            elif sub_choice == "e":
                print("Result:", num1 ** num2)
            elif sub_choice == "f":
                print("Result:", num1 % num2)
            elif sub_choice == "g":
                print("Result:", num1 // num2)
        else:
            print("Invalid choice.")

    elif choice == "7":
        name = input("Enter student: ")
        if name in student:
            grade = float(input("Enter student's grade (0-100): "))
            if 0 <= grade <= 100:
                student[name]["grade"] = grade
                print("Grade set for", name, ":", f"{grade:.2f}")

                if grade >= 90:
                    print("Grade: A, Excellent")
                elif grade >= 80:
                    print("Grade: B, Good")
                elif grade >= 70:
                    print("Grade: C, Can do better")
                elif grade >= 60:
                    print("Grade: D, Efforts needed")
                elif grade >= 40:
                    print("Grade: E, Please work on your grades")
                else:
                    print("Grade: F, Fail")
            else:
                print("Grade must be between 0 and 100.")
        else:
            print("Student not found.")

    elif choice == "8":
        print("Exiting application")
        break

    else:
        print("Invalid choice. Please try again.")
