# بايثون العرب - الدرس 20
# عد الطلاب الناجحين باستخدام Boolean بطريقة بسيطة

grades = [80, 45, 90, 30, 60]
passed_count = 0

for grade in grades:
    is_passed = grade >= 50
    if is_passed:
        passed_count += 1

print("Passed students:", passed_count)
