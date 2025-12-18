age = int(input("Enter your age: "))

months = age * 12
weeks = age * 52
days = age * 365

# Store in tuple
age_tuple = (months, weeks, days)

print("\n⏳ Your Age in Units ⏳")
print(f"Months: {age_tuple[0]}")
print(f"Weeks: {age_tuple[1]}")
print(f"Days: {age_tuple[2]}")
