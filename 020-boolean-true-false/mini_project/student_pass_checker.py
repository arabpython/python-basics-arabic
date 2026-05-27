# مشروع صغير - فحص نجاح الطالب باستخدام Boolean
# الفكرة: تخزين نتائج المقارنات في متغيرات Boolean ثم استخدامها داخل if.

student_name = "Mona"
grade = 75
attendance = 80

is_grade_passed = grade >= 50
is_attendance_good = attendance >= 70
is_passed = is_grade_passed and is_attendance_good

print("=" * 45)
print("Student Pass Checker")
print("=" * 45)
print("Name:", student_name)
print("Grade:", grade)
print("Attendance:", attendance)
print("Grade passed:", is_grade_passed)
print("Attendance good:", is_attendance_good)

if is_passed:
    print("Result: الطالب ناجح")
else:
    print("Result: الطالب راسب أو يحتاج مراجعة")

print("=" * 45)
