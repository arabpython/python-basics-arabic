# بايثون العرب - الدرس 22
# readlines() تقرأ كل الأسطر داخل قائمة List

with open("data/notes.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)
print(type(lines))
