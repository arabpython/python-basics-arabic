# حل تمرين 06

numbers = [5, 10, 15]
names = ["Ahmed", "Sara", "Omar"]

total = 0

for number in numbers:
    total += number

print("Total:", total)

found = False

for name in names:
    if name == "Sara":
        found = True
        break

if found:
    print("Sara is found")
else:
    print("Sara is not found")
