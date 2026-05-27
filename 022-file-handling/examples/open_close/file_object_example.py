# بايثون العرب - الدرس 22
# عند فتح ملف نحصل على file object نستطيع القراءة منه أو الكتابة فيه

with open("data/notes.txt", "r", encoding="utf-8") as file:
    print(file)
    print(type(file))
