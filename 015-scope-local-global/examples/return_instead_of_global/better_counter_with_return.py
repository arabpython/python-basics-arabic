# بايثون العرب - الدرس 15
# الأفضل غالبًا: استخدام return بدل global

def increase(number):
    return number + 1

count = 0
count = increase(count)

print(count)
