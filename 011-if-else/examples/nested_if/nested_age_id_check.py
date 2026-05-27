# بايثون العرب - الدرس 11
# الشروط المتداخلة Nested if

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("يمكنك الدخول")
    else:
        print("تحتاج إلى بطاقة هوية")
else:
    print("العمر غير مناسب")
