# بايثون العرب - الدرس 14
# إرجاع أكثر من قيمة يعني عمليًا إرجاع Tuple

def calculate(a, b):
    return a + b, a - b

result = calculate(10, 4)

print(result)
print(type(result))
