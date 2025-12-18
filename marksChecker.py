marks = float(input("Enter your marks (out of 100): "))

if marks >= 90:
    print("Grade: A+ (Excellent!)")
elif marks >= 80:
    print("Grade: A (Very Good)")
elif marks >= 70:
    print("Grade: B (Good)")
elif marks >= 60:
    print("Grade: C (Distinction)")
elif marks >= 35:
    print("Grade: D (Pass)")
else:
    print("Grade: F (Fail)")
