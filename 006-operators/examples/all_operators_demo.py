# بايثون العرب - الدرس 06
# تجربة عدة أنواع من العوامل في ملف واحد

x = 10
y = 3

print("Arithmetic:")
print(x + y, x - y, x * y, x / y, x % y, x ** y, x // y)

print("\nComparison:")
print(x == y, x != y, x > y, x < y)

print("\nLogical:")
print(x > 5 and y < 5)
print(x > 10 or y < 5)
print(not(x > 5))

print("\nAssignment:")
z = 5
z += 3
print("z += 3:", z)

print("\nMembership:")
nums = [1, 2, 3]
print(2 in nums)
print(5 not in nums)
