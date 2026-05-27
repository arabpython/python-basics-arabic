# بايثون العرب - الدرس 11
# مثال يجمع and و or و not

age = 22
has_account = True
is_banned = False

if age >= 18 and has_account and not is_banned:
    print("يمكنك استخدام الخدمة")
else:
    print("لا يمكنك استخدام الخدمة")

is_admin = False
is_owner = True

if is_admin or is_owner:
    print("يمكنك تعديل الإعدادات")
