# بايثون العرب - الدرس 22
# مثال عملي: قراءة أسماء الطلاب من ملف

with open("data/students.txt", "r", encoding="utf-8") as file:
    for student in file:
        print(student.strip())
