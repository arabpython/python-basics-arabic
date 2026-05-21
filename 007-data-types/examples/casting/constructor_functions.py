# بايثون العرب - الدرس 07
# تحديد نوع البيانات يدويًا باستخدام Constructor Functions

values = [
    str(10),
    int("20"),
    float(5),
    complex(1, 2),
    list("abc"),
    tuple([1, 2]),
    set([1, 2, 2]),
    dict(name="A", age=20),
    bool(1),
    bytes(5),
    bytearray(5),
    memoryview(bytes(5))
]

for value in values:
    print(value, "->", type(value))
