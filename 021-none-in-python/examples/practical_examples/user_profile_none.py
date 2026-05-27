# بايثون العرب - الدرس 21
# استخدام None مع بيانات مستخدم لم تكتمل بعد

user = {
    "name": "Ahmed",
    "email": None
}

if user["email"] is None:
    print("البريد الإلكتروني غير مضاف")
else:
    print("Email:", user["email"])
