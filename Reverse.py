def reverse_value(value):
    if value.isdigit():
        num = int(value)
        rev = 0
        while num > 0:
            digit = num % 10
            rev = rev * 10 + digit
            num //= 10
        return rev
    else:
        return value[::-1]

user_input = input("Enter any number or string:")
print("Reversed value:", reverse_value(user_input))
