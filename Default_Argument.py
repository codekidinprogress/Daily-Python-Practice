def place_order(item, quantity=1, delivery_charge=40):
    total_price = quantity * 120 + delivery_charge
    print("Item:", item)
    print("Quantity:", quantity)
    print("Delivery Charge:", delivery_charge)
    print("Total Bill: ₹", total_price)

place_order("Pizza")

print()

place_order("Burger", 2)

print()

place_order("Pasta", 3, 60)
