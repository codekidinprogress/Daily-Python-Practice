amount = float(input("Enter amount: "))
currency = input("Convert from (I)NR or (U)SD: ").upper()
if currency == "I":
    converted = amount / 83.0   
    print("Amount in USD: $" + str(round(converted, 2)))
elif currency == "U":
    converted = amount * 83.0
    print("Amount in INR: ₹" + str(round(converted, 2)))
else:
    print("Invalid input! Please enter 'I' or 'U'.")
