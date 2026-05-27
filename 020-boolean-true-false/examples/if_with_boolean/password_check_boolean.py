# بايثون العرب - الدرس 20
# التحقق من كلمة المرور باستخدام Boolean

password = "python123"

is_correct = password == "python123"

print(is_correct)

if is_correct:
    print("تم تسجيل الدخول")
else:
    print("كلمة المرور غير صحيحة")
