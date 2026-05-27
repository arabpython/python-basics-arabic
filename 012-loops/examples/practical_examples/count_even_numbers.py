# بايثون العرب - الدرس 12
# عد الأرقام الزوجية داخل قائمة

numbers = [1, 2, 3, 4, 5, 6]
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print("Even numbers count:", even_count)
