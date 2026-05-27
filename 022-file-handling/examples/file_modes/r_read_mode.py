# بايثون العرب - الدرس 22
# وضع r للقراءة فقط ويحتاج أن يكون الملف موجودًا

with open("data/notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
