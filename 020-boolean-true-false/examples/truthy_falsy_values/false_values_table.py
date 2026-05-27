# بايثون العرب - الدرس 20
# قيم تعتبر False في Python

values = [0, "", [], (), {}, set(), None, False]

for value in values:
    print(repr(value), "=>", bool(value))
