# بايثون العرب - الدرس 07
# أنواع المجموعات set و frozenset

fruits = {"apple", "banana", "cherry", "apple"}
frozen_fruits = frozenset({"apple", "banana", "cherry"})

print(fruits)
print(type(fruits))

print(frozen_fruits)
print(type(frozen_fruits))

fruits.add("orange")
print(fruits)

# السطر التالي سيعطي خطأ لأن frozenset غير قابلة للتغيير:
# frozen_fruits.add("orange")
