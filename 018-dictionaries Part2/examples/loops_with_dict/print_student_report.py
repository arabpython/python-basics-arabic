# بايثون العرب - الدرس 18
# طباعة تقرير من Dictionary باستخدام for

student = {
    "name": "Ahmed",
    "age": 20,
    "major": "Computer Science",
    "grade": "A"
}

print("Student Report")
print("-" * 30)

for key, value in student.items():
    print(key, ":", value)
