print("*" * 40)
print(f"{'INVOICE':^40}")
print("*" * 40)

items = []
total = 0

n = int(input("Enter number of items: "))

for i in range(n):
    print(f"\nItem {i+1}")
    name = input("Item name: ")
    qty = int(input("Quantity: "))
    price = float(input("Price per item: "))

    amount = qty * price
    total += amount
    items.append((name, qty, price, amount))

print("\n" + "-" * 40)
print(f"{'Item':<15}{'Qty':>5}{'Price':>10}{'Amount':>10}")
print("-" * 40)

for item in items:
    name, qty, price, amount = item
    print(f"{name:<15}{qty:>5}{price:>10,.2f}{amount:>10,.2f}")

print("-" * 40)
print(f"{'Total':<30}{total:>10,.2f}")
print("*" * 40)
