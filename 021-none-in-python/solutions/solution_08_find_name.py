# حل تمرين 08

def find_name(names, target):
    for name in names:
        if name == target:
            return name

    return None

names = ["Ali", "Sara", "Omar"]
target = "Mona"

result = find_name(names, target)

if result is None:
    print("الاسم غير موجود")
else:
    print("تم العثور على الاسم:", result)
