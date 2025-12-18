weight = input("Enter your weight: ")
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = float(weight)/0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = float(weight) * 0.45
    print("Weight in Kgs: " + str(converted))