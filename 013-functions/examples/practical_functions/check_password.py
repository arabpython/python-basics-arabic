# بايثون العرب - الدرس 13
# دالة للتحقق من كلمة المرور

def check_password(password):
    if password == "python123":
        return True
    return False

print(check_password("python123"))
print(check_password("123456"))
