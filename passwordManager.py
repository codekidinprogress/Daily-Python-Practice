passwords = {}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            site, user, pwd = line.strip().split("|")
            passwords[site] = (user, pwd)
except FileNotFoundError:
    pass

while True:
    print("\n--- PASSWORD MANAGER ---")
    print("1. Add Password")
    print("2. View All Passwords")
    print("3. Search Password")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter website name: ")
        username = input("Enter username: ")
        password = input("Enter password: ")

        passwords[site] = (username, password)
        print("Password saved successfully!")

    elif choice == "2":
        if not passwords:
            print("No passwords stored.")
        else:
            print("\nSaved Passwords:")
            for site in passwords:
                print("Website:", site)
                print("Username:", passwords[site][0])
                print("Password:", passwords[site][1])
                print("-" * 20)

    elif choice == "3":
        site = input("Enter website to search: ")
        if site in passwords:
            print("Username:", passwords[site][0])
            print("Password:", passwords[site][1])
        else:
            print("No password found for this website.")

    elif choice == "4":
        with open("passwords.txt", "w") as file:
            for site in passwords:
                file.write(site + "|" + passwords[site][0] + 
                           "|" + passwords[site][1] + "\n")
        print("Passwords saved. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
