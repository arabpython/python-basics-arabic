# بايثون العرب - الدرس 17
# إرجاع أكثر من قيمة من دالة باستخدام Tuple

def get_user():
    return "Ahmed", 25

user = get_user()
print(user)
print(type(user))

name, age = get_user()
print(name)
print(age)
