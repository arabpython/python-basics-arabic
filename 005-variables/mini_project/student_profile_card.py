# مشروع صغير - بطاقة بيانات طالب
# الفكرة: استخدام المتغيرات و f-strings لطباعة بطاقة منظمة.

student_name = "Mona"
student_age = 22
student_city = "Cairo"
course_name = "Python Basics"
site_name = "بايثون العرب"

print("=" * 40)
print("Student Profile Card")
print("=" * 40)
print(f"Name  : {student_name}")
print(f"Age   : {student_age}")
print(f"City  : {student_city}")
print(f"Course: {course_name}")
print(f"Site  : {site_name}")
print("=" * 40)
print(f"Welcome {student_name} to {site_name}!")
