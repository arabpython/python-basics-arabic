# بايثون العرب - الدرس 08
# مثال عملي شامل على القوائم

students = ["Ahmed", "Sara", "Omar"]

students.append("Mona")

print("قائمة الطلاب:")
print(students)

print("عدد الطلاب:")
print(len(students))

print("أول طالب:", students[0])
print("آخر طالب:", students[-1])

print("هل Sara موجودة؟", "Sara" in students)

print("طباعة الطلاب واحدًا واحدًا:")
for student in students:
    print(student)
