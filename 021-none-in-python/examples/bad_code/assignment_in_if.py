# مثال خاطئ
# هذا الملف مقصود أن يعطي SyntaxError.
# السبب: استخدام = بدل is أو == داخل الشرط.

value = None

if value = None:
    print("لا توجد قيمة")
