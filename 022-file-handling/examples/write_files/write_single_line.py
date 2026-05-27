# بايثون العرب - الدرس 22
# الكتابة داخل ملف باستخدام w
# انتبه: w يمسح محتوى الملف القديم إذا كان موجودًا.

with open("data/output.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")

print("File written successfully")
