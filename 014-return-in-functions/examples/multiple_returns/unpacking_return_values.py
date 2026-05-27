# بايثون العرب - الدرس 14
# تفكيك القيم الراجعة في متغيرات

def get_user():
    name = "Ahmed"
    age = 20
    city = "Amman"
    return name, age, city

user_name, user_age, user_city = get_user()

print(user_name)
print(user_age)
print(user_city)
