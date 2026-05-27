# مثال خاطئ
# هذا الملف مقصود أن يعطي FileNotFoundError.
# وضع r يحتاج أن يكون الملف موجودًا.

with open("data/missing_file.txt", "r", encoding="utf-8") as file:
    print(file.read())
