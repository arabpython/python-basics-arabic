# بايثون العرب - الدرس 20
# القيم غير الفارغة غالبًا تعتبر True

values = [1, "Python", [1], (1,), {"name": "Ali"}, {"Python"}]

for value in values:
    print(repr(value), "=>", bool(value))
