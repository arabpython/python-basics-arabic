# مشروع صغير - آلة حاسبة باستخدام return
# الفكرة: كل دالة ترجع النتيجة بدل طباعتها مباشرة.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b

x = 10
y = 5

print("=" * 40)
print("Calculator Results")
print("=" * 40)

sum_result = add(x, y)
diff_result = subtract(x, y)
mul_result = multiply(x, y)
div_result = divide(x, y)

print("Add      :", sum_result)
print("Subtract :", diff_result)
print("Multiply :", mul_result)
print("Divide   :", div_result)

final_score = sum_result + mul_result
print("Final score from two results:", final_score)

print("=" * 40)
