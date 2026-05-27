# بايثون العرب - الدرس 21
# رسالة اختيارية باستخدام None

def show_message(message=None):
    if message is None:
        print("لا توجد رسالة")
    else:
        print(message)

show_message()
show_message("Welcome to Python")
