# بايثون العرب - الدرس 14
# Early return للتحقق من الأخطاء أولًا

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b

print(divide(10, 2))
print(divide(10, 0))
