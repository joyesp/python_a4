while True:
    print("STUDENT RECORD SYSTEM")
    print("1 - Add Student Record")
    print("2 - View Saved Records")
    print("3 - Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip()

        try:
            grade = float(input("Enter student grade: "))
        except ValueError:
            print("Invalid input! Grade must be a number.")
            continue

        try:
            with open("students.txt", "a") as file:
                file.write(f"{name},{grade}\n")
            print("Record saved successfully!")
        except Exception as e:
            print("Error saving record:", e)

    elif choice == "2":
        try:
            with open("students.txt", "r") as file:
                records = file.readlines()

            if not records:
                print("No records found yet.")
            else:
                print("\n--- Saved Records ---")
                for record in records:
                    name, grade = record.strip().split(",")
                    print(f"{name} = {grade}")

        except FileNotFoundError:
            print("No records found yet.")


    elif choice == "3":
        print("Program terminated. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1, 2, or 3.")