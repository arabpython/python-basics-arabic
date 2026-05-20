# تمرين 06
# قبل تشغيل الكود، توقع نوع كل قيمة.

values = [
    "10",
    10,
    10.0,
    ["Python"],
    ("Python",),
    {"course": "Python"},
    {"Python"},
    False
]

for value in values:
    print(type(value))
