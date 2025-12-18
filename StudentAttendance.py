students = {}

try:
    with open("attendance.txt", "r") as file:
        for line in file:
            roll, name, status = line.strip().split(",")
            students[roll] = [name, status]
except FileNotFoundError:
    pass

while True:
    print("\n--- Student Attendance System ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. View Attendance")
    print("4. Save & Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Roll No: ")
        name = input("Name: ")
        students[roll] = [name, "Not Marked"]
        print("Student added!")

    elif choice == "2":
        roll = input("Roll No: ")
        if roll in students:
            status = input("P for Present, A for Absent: ").upper()
            students[roll][1] = "Present" if status == "P" else "Absent"
        else:
            print("Student not found")

    elif choice == "3":
        for roll in students:
            print(f"{roll} | {students[roll][0]} | {students[roll][1]}")

    elif choice == "4":
        with open("attendance.txt", "w") as file:
            for roll in students:
                file.write(f"{roll},{students[roll][0]},{students[roll][1]}\n")
        print("Data saved. Exiting...")
        break

    else:
        print("Invalid choice")
