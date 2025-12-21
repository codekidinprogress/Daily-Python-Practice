balance = 1000  

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    balance += amount
    print("Updated Balance:", balance)

def withdraw():
    global balance
    amount = int(input("Enter withdraw amount: "))
    if amount <= balance:
        balance -= amount
        print("Updated Balance:", balance)
    else:
        print("Insufficient balance")

deposit()
withdraw()
