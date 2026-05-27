# بايثون العرب - الدرس 15
# إنشاء متغير محلي بنفس اسم العام لا يغير المتغير العام

count = 0

def increase():
    count = 1
    print("Inside function:", count)

increase()
print("Outside function:", count)
