# بايثون العرب - الدرس 13
# دالة لحساب المتوسط

def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)

grades = [80, 90, 70]

print(calculate_average(grades))
