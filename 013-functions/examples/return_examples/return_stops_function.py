# بايثون العرب - الدرس 13
# return توقف تنفيذ الدالة وترجع القيمة

def check_number(number):
    if number > 0:
        return "Positive"

    return "Zero or Negative"

print(check_number(10))
print(check_number(-5))
