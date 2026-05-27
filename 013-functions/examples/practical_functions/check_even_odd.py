# بايثون العرب - الدرس 13
# دالة لفحص الرقم الزوجي والفردي

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(10))
print(check_even_odd(7))
