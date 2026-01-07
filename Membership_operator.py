students = {
    "CS101": {"name": "Aarav", "year": 1},
    "CS102": {"name": "Diya", "year": 2},
    "CS103": {"name": "Rahul", "year": 3}
}

library_users = ["CS101", "CS103"]
portal_users = ["CS101", "CS102", "CS103"]
exam_hall_users = ["CS102", "CS103"]

print("\n🎓 WELCOME TO COLLEGE ACCESS SYSTEM")

student_id = input("Enter your Student ID: ").upper()

if student_id not in students:
    print("Invalid ID. ")
    exit()

print(f"\nWelcome {students[student_id]['name']}")

while True:
    print("\nSelect Service:")
    print("1. Library Access")
    print("2. Online Portal Access")
    print("3. Exam Hall Entry")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        if student_id in library_users:
            print("Library Access Granted")
        else:
            print("Library Access Denied")

    elif choice == "2":
        if student_id in portal_users:
            print("Online Portal Access Granted")
        else:
            print("Online Portal Access Denied")

    elif choice == "3":
        if student_id in exam_hall_users:
            print("Exam Hall Entry Allowed")
        else:
            print("Exam Hall Entry Not Allowed")

    elif choice == "4":
        print("Logged out successfully")
        break

    else:
        print("Invalid choice. Try again.")
