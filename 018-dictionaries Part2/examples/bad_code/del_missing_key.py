# مثال خاطئ
# هذا الملف مقصود أن يعطي KeyError.
# لا تستخدم del مع مفتاح غير موجود إلا بعد التحقق.

student = {
    "name": "Ahmed"
}

del student["age"]
