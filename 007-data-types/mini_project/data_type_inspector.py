# مشروع صغير - مستكشف أنواع البيانات
# الفكرة: برنامج يطبع القيمة ونوعها ووصفًا بسيطًا لها.

items = [
    "Arab Python",
    2026,
    3.14,
    ["Python", "HTML", "CSS"],
    ("beginner", "course"),
    {"site": "بايثون العرب", "url": "arabpython.com"},
    {"python", "learning", "arabic"},
    True
]

for item in items:
    print("=" * 45)
    print("Value:", item)
    print("Type :", type(item))

    if isinstance(item, str):
        print("Note : This is text.")
    elif isinstance(item, int):
        print("Note : This is an integer number.")
    elif isinstance(item, float):
        print("Note : This is a decimal number.")
    elif isinstance(item, list):
        print("Note : This is a mutable sequence.")
    elif isinstance(item, tuple):
        print("Note : This is an immutable sequence.")
    elif isinstance(item, dict):
        print("Note : This stores key-value pairs.")
    elif isinstance(item, set):
        print("Note : This stores unique values.")
    elif isinstance(item, bool):
        print("Note : This is True or False.")
