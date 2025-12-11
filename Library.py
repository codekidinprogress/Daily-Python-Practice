library = {}   

while True:
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. View All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    try:
        choice = int(choice)
    except:
        print("Please enter a valid number!")
        continue

    if choice == 1:
        book = input("Enter book name: ").strip()

        if book in library:
            print("Book already exists!")
            continue

        library[book] = "Available"
        print(f"'{book}' added successfully!")

    elif choice == 2:
        if not library:
            print("No books in the library.")
            continue

        print("\n=== Library Books ===")
        for book, status in library.items():
            print(f"{book} → {status}")

    elif choice == 3:
        name = input("Enter book name to search: ").strip()

        found = False
        for book in library:
            if book.lower() == name.lower():
                print(f"{book} is {library[book]}")
                found = True
                break

        if not found:
            print("Book not found!")

    elif choice == 4:
        book = input("Enter book name to issue: ").strip()

        if book not in library:
            print("Book not found!")
            continue

        if library[book] == "Issued":
            print("Book is already issued.")
            continue

        library[book] = "Issued"
        print(f"You issued '{book}' successfully!")

    elif choice == 5:
        book = input("Enter book name to return: ").strip()

        if book not in library:
            print("This book doesn't belong to this library!")
            continue

        if library[book] == "Available":
            print("Book was not issued.")
            continue

        library[book] = "Available"
        print(f"'{book}' returned successfully!")

    elif choice == 6:
        print("Exiting program… Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
