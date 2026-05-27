# مشروع صغير إضافي - التحقق من تسجيل الدخول

correct_username = "admin"
correct_password = "python123"

username = input("Username: ")
password = input("Password: ")

if username == correct_username and password == correct_password:
    print("تم تسجيل الدخول بنجاح")
else:
    print("اسم المستخدم أو كلمة المرور غير صحيحة")
