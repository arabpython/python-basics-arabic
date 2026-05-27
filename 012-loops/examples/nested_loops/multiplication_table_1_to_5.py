# بايثون العرب - الدرس 12
# جداول ضرب من 1 إلى 5 باستخدام Nested Loops

for number in range(1, 6):
    print("Table of", number)

    for i in range(1, 11):
        print(number, "x", i, "=", number * i)

    print("-" * 20)
