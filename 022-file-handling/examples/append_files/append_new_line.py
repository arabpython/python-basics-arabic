# بايثون العرب - الدرس 22
# الإضافة إلى نهاية الملف باستخدام a

with open("data/output.txt", "a", encoding="utf-8") as file:
    file.write("\nNew line added")

print("Line appended successfully")
