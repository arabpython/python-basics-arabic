# بايثون العرب - الدرس 14
# استخدام return مع if

def check_age(age):
    if age >= 18:
        return "Allowed"
    else:
        return "Not allowed"

print(check_age(20))
print(check_age(15))
