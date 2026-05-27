# مشروع صغير إضافي - تسجيل دخول بسيط باستخدام Boolean

correct_password = "python123"
is_banned = False

password = input("Password: ")

is_correct = password == correct_password
can_login = is_correct and not is_banned

print("=" * 45)
print("Login Check")
print("=" * 45)
print("Password correct:", is_correct)
print("User banned:", is_banned)

if can_login:
    print("تم تسجيل الدخول")
else:
    print("لا يمكن تسجيل الدخول")

print("=" * 45)
