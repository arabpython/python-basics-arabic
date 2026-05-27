# بايثون العرب - الدرس 12
# الفرق بين break و continue

print("break example:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("\ncontinue example:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
