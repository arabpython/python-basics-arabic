# مثال خاطئ
# هذا الملف مقصود أن يعطي SyntaxError.
# السبب: استخدام = بدل == داخل الشرط.

password = "123"

if password = "123":
    print("Correct password")
