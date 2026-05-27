# بايثون العرب - الدرس 15
# تقليل الاعتماد على المتغيرات العامة

def calculate_final_price(price, tax):
    return price + tax

price = 100
tax = 5

final_price = calculate_final_price(price, tax)

print(final_price)
