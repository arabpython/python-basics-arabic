# مثال خاطئ
# هذا الملف قد يعطي FileExistsError إذا شغلته بعد إنشاء الملف أول مرة.
# وضع x لا يقبل أن يكون الملف موجودًا مسبقًا.

with open("data/create_mode_demo.txt", "x", encoding="utf-8") as file:
    file.write("New file")
