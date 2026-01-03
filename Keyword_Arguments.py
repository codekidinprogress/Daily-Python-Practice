def shopping_cart(**items):
    total = 0
    print("Items Purchased:")
    for item, price in items.items():
        print(item, "₹", price)
        total += price
    print("Total Bill: ₹", total)

shopping_cart(shoes=2500, watch=1800, bag=1200)
