# بايثون العرب - الدرس 14
# يمكن الاستغناء عن else أحيانًا بعد return

def check_age(age):
    if age >= 18:
        return "Allowed"

    return "Not allowed"

print(check_age(20))
print(check_age(15))
