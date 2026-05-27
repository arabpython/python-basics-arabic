# مثال خاطئ
# هذا الملف مقصود أن يعطي NameError.
# المتغير message داخل الدالة، ولا يمكن استخدامه خارجها إلا إذا رجعناه.

def greet():
    message = "Hello"

greet()

print(message)
