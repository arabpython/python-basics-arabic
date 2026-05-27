# مثال تعليمي مهم
# استخدام w بالخطأ يمسح المحتوى القديم.

with open("data/warning_w_mode.txt", "w", encoding="utf-8") as file:
    file.write("First content\n")

with open("data/warning_w_mode.txt", "w", encoding="utf-8") as file:
    file.write("Second content only\n")

with open("data/warning_w_mode.txt", "r", encoding="utf-8") as file:
    print(file.read())

# لو كنت تريد الإضافة، استخدم a بدل w.
