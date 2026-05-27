# بايثون العرب - الدرس 21
# استخدام None كقيمة افتراضية

def welcome(name=None):
    if name is None:
        print("أهلا بك")
    else:
        print("أهلا بك", name)

welcome()
welcome("Ahmed")
