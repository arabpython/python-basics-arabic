# مشروع صغير - إدارة بيانات طالب باستخدام Dictionary
# الفكرة: إنشاء قاموس، الوصول للقيم، التعديل، الإضافة، الحذف، و items().

student = {
    "name": "Ahmed",
    "age": 20,
    "major": "Computer Science",
    "grade": "B"
}

print("=" * 45)
print("Initial Student Data")
print("=" * 45)

for key, value in student.items():
    print(key, ":", value)

student["grade"] = "A"
student["city"] = "Amman"
removed_age = student.pop("age")

print("\nRemoved age:", removed_age)

print("\nUpdated Student Data")
print("=" * 45)

for key, value in student.items():
    print(key, ":", value)

print("\nSafe access examples:")
print("Email:", student.get("email", "No email found"))
print("City :", student.get("city", "No city found"))

print("=" * 45)
