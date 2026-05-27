# بايثون العرب - الدرس 18
# فحص وجود مفتاح باستخدام in

user = {
    "name": "Ali",
    "email": "ali@example.com"
}

if "email" in user:
    print("البريد موجود")
else:
    print("البريد غير موجود")

if "phone" in user:
    print("الهاتف موجود")
else:
    print("الهاتف غير موجود")
