# مثال خاطئ
# هذا الملف مقصود أن يعطي TypeError.
# السبب: الدالة تحتاج إلى Argument واحد، لكننا لم نرسله.

def greet(name):
    print(f"Hello {name}")

greet()
