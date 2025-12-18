print("===== Simple Billing App =====")

prices = []

while True:
    user_input = input("Enter price: ")

    # stop taking prices
    if user_input == "":
        confirm = input("Finish billing? (y/n): ").lower()
        if confirm == "y":
            break
        else:
            continue

    # add price
    price = float(user_input)
    prices.append(price)
    print("Added ✓")

# show summary
print("\n===== BILL SUMMARY =====")
print("Items:", prices)
print("Total Items:", len(prices))
print("Total Amount:", sum(prices))
