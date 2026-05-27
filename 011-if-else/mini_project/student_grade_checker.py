# مشروع صغير - تقييم درجة طالب
# الفكرة: استخدام if و elif و else لتحديد مستوى الطالب.

student_name = "Mona"
grade = 86
is_active = True

print("=" * 45)
print(f"Student: {student_name}")
print(f"Grade  : {grade}")

if grade >= 90:
    level = "ممتاز"
elif grade >= 80:
    level = "جيد جدًا"
elif grade >= 70:
    level = "جيد"
else:
    level = "تحتاج إلى تحسين"

print(f"Level  : {level}")

if grade >= 70 and is_active:
    print("Status : يمكن اعتماد النتيجة")
else:
    print("Status : راجع بيانات الطالب")

print("=" * 45)
