# بايثون العرب - الدرس 21
# البحث عن اسم داخل قائمة وإرجاع None إذا لم يوجد

def find_name(names, target):
    for name in names:
        if name == target:
            return name

    return None

students = ["Ali", "Sara", "Omar"]

result = find_name(students, "Mona")

if result is None:
    print("الاسم غير موجود")
else:
    print("تم العثور على الاسم:", result)
