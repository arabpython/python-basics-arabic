# مشروع صغير إضافي - أداة بحث بسيطة داخل قائمة أسماء

names = ["Ahmed", "Sara", "Omar", "Mona", "Khaled"]

target = input("اكتب الاسم الذي تريد البحث عنه: ")

found = False

for name in names:
    if name == target:
        found = True
        break

if found:
    print("تم العثور على الاسم")
else:
    print("الاسم غير موجود")
