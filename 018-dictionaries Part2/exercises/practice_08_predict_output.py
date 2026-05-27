# تمرين 08
# قبل تشغيل الكود، توقع الناتج.

student = {
    "name": "Mona",
    "grade": "B"
}

student["grade"] = "A"
student["age"] = 21
removed = student.pop("age")

print(student["name"])
print(student.get("city", "No city"))
print(removed)
print(len(student))
print(student)
