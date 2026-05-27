# بايثون العرب - الدرس 18
# استخدام get() مع قيمة افتراضية

user = {
    "name": "Ali",
    "city": "Sanaa"
}

print(user.get("age", "العمر غير موجود"))
print(user.get("email", "البريد غير موجود"))
