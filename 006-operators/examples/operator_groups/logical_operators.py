# بايثون العرب - الدرس 06
# العوامل المنطقية Logical Operators

age = 25

print(age > 18 and age < 30)
print(age > 30 or age < 20)
print(not(age > 18))

has_account = True
is_active = False

print("Can login:", has_account and is_active)
print("Needs activation:", has_account and not is_active)
