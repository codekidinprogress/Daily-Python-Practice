speed = float(input("Enter speed: "))
unit = input("Convert from (K)m/h or (M)ph: ").upper()
if unit == "K":
    converted = float(speed) / 1.609  
    print("Speed in mph: " + str(converted))
elif unit == "M":
    converted = float(speed) * 1.609
    print("Speed in km/h: " + str(converted))
else:
    print("Invalid input! Please enter 'K' or 'M'.")
