# بايثون العرب - الدرس 22
# فتح ملف بالطريقة التقليدية ثم إغلاقه باستخدام close()

file = open("data/notes.txt", "r", encoding="utf-8")

content = file.read()
print(content)

file.close()
