# بايثون العرب - الدرس 22
# استخدام with أفضل لأنها تغلق الملف تلقائيًا

with open("data/notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

# لا نحتاج إلى file.close()
