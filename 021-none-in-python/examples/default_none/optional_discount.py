# بايثون العرب - الدرس 21
# مثال عملي: خصم اختياري باستخدام None

def calculate_price(price, discount=None):
    if discount is None:
        return price

    return price - discount

print(calculate_price(100))
print(calculate_price(100, 20))
