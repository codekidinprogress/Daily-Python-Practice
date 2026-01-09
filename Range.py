for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()
print()

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
print()

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

for i in range(1, 6):
    for j in range(i):
        print(i, end="")
    print()
print()

n = 5
for i in range(n):
    for space in range(n - i - 1):
        print(" ", end="")
    for star in range(2 * i + 1):
        print("*", end="")
    print()
