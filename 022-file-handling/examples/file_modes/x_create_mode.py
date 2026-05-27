# بايثون العرب - الدرس 22
# وضع x ينشئ ملفًا جديدًا ويعطي خطأ إذا كان موجودًا
# غيّر اسم الملف إذا أردت تجربة الملف أكثر من مرة.

with open("data/create_mode_demo.txt", "x", encoding="utf-8") as file:
    file.write("Created with x mode")

print("File created")
