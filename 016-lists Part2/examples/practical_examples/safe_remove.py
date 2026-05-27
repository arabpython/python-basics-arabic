# بايثون العرب - الدرس 16
# حذف عنصر بأمان بعد التحقق من وجوده

fruits = ["apple", "banana"]

item = "orange"

if item in fruits:
    fruits.remove(item)
else:
    print("العنصر غير موجود")

print(fruits)
