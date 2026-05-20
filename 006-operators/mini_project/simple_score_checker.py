# مشروع صغير - فحص درجة طالب
# الفكرة: استخدام العوامل الحسابية والمقارنة والمنطقية والعضوية في برنامج واحد.

student_name = "Mona"
score_1 = 80
score_2 = 90
score_3 = 70

total = score_1 + score_2 + score_3
average = total / 3

passed = average >= 60
excellent = average >= 85
allowed_grades = ["A", "B", "C", "D", "F"]

grade = "B"

print("=" * 40)
print(f"Student: {student_name}")
print(f"Total  : {total}")
print(f"Average: {average}")
print(f"Passed : {passed}")
print(f"Excellent: {excellent}")
print(f"Grade is valid: {grade in allowed_grades}")
print("=" * 40)

if passed and grade in allowed_grades:
    print("Result can be saved.")
else:
    print("Please check the result.")
