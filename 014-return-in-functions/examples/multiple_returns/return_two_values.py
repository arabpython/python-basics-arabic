# بايثون العرب - الدرس 14
# إرجاع أكثر من قيمة

def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

sum_result, diff_result = calculate(10, 4)

print(sum_result)
print(diff_result)
