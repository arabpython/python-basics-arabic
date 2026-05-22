# بايثون العرب - الدرس 09
# pop() و clear() و del

fruits = {"apple", "banana", "cherry"}

removed_item = fruits.pop()

print("Removed item:", removed_item)
print("After pop:", fruits)

fruits.clear()
print("After clear:", fruits)

# del يحذف المتغير بالكامل:
# del fruits
# print(fruits)  # سيعطي NameError إذا شغلت هذا السطر.
