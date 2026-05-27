# بايثون العرب - الدرس 13
# استخدام القيمة الراجعة لاحقًا

def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(15, 4)
discounted_total = total - 5

print("Total:", total)
print("After discount:", discounted_total)
