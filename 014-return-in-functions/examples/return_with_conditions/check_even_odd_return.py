# بايثون العرب - الدرس 14
# دالة ترجع نتيجة مختلفة حسب الشرط

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"

    return "Odd"

print(check_even_odd(8))
print(check_even_odd(7))
