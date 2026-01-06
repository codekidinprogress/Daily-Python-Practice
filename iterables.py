students = ["Amit", "Riya", "Karan", "Sneha"]

marks = (78, 85, 69, 92)

student_data = {
    "Amit": 78,
    "Riya": 85,
    "Karan": 69,
    "Sneha": 92
}

course = "Python"

print("Course:", course)
print("\nStudent Details:")

for name, mark in student_data.items():
    print(name, "scored", mark)

total = 0
for m in marks:
    total += m

average = total / len(marks)
print("\nAverage Marks:", average)

print("\nCharacters in course name:")
for ch in course:
    print(ch, end=" ")
