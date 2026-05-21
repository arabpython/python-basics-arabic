# بايثون العرب - الدرس 07
# الأنواع التسلسلية: list, tuple, range

fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = ("apple", "banana", "cherry")
numbers_range = range(6)

print(fruits_list, type(fruits_list))
print(fruits_tuple, type(fruits_tuple))
print(numbers_range, type(numbers_range))

# list قابلة للتغيير
fruits_list[0] = "orange"
print(fruits_list)

# range يستخدم غالبًا مع for
for number in numbers_range:
    print(number)
