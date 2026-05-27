# بايثون العرب - الدرس 15
# إرجاع قيمة من الدالة بدل محاولة استخدام متغير محلي خارجها

def build_message(name):
    message = f"Hello {name}"
    return message

result = build_message("Mona")

print(result)
