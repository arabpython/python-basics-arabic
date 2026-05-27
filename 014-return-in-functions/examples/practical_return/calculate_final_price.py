# بايثون العرب - الدرس 14
# حساب السعر النهائي باستخدام return

def calculate_total(price, quantity):
    return price * quantity

def add_shipping(total, shipping):
    return total + shipping

total = calculate_total(10, 3)
final_total = add_shipping(total, 5)

print(final_total)
