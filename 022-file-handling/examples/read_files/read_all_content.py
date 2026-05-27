# بايثون العرب - الدرس 22
# قراءة محتوى الملف كاملًا باستخدام read()

with open("data/notes.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
