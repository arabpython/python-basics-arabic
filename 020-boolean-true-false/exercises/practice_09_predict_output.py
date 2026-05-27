# تمرين 09
# قبل تشغيل الكود، توقع الناتج.

value = ""
items = [1, 2]
is_admin = False
is_owner = True

print(bool(value))
print(bool(items))

if is_admin or is_owner:
    print("Allowed")

if not value:
    print("Empty value")
