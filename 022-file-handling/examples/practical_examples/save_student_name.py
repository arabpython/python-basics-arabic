# بايثون العرب - الدرس 22
# مثال عملي: حفظ اسم طالب داخل ملف
# لتسهيل التشغيل بدون إدخال، استخدمنا قيمة جاهزة.

student_name = "Huda"

with open("data/students.txt", "a", encoding="utf-8") as file:
    file.write(student_name + "\n")

print("Student saved successfully")
