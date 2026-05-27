# مثال خاطئ
# هذا الملف مقصود أن يعطي NameError.
# المتغير name محلي داخل الدالة ولا يعيش خارجها.

def greet():
    name = "Ahmed"

greet()

print(name)
