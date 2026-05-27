# بايثون العرب - الدرس 15
# استخدام global لتعديل متغير عام

count = 0

def increase():
    global count
    count = count + 1

increase()
print(count)
