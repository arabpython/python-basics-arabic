# بايثون العرب - الدرس 14
# استخدام ناتج الدالة في عملية أخرى

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(10, 3)
final_total = total + 5

print(final_total)
