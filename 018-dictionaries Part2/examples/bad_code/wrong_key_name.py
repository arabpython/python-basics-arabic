# مثال خاطئ
# هذا الملف مقصود أن يعطي KeyError.
# المفتاح الصحيح هو user_name وليس username.

user = {
    "user_name": "arabpython",
    "email": "info@example.com"
}

print(user["username"])
