# بايثون العرب - الدرس 12
# بحث أفضل باستخدام متغير found

names = ["Ahmed", "Sara", "Omar"]
target = "Mona"
found = False

for name in names:
    if name == target:
        found = True
        break

if found:
    print("تم العثور على الاسم")
else:
    print("الاسم غير موجود")
