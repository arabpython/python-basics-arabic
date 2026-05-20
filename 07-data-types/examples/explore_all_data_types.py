# بايثون العرب - الدرس 07
# استكشاف عدة أنواع بيانات باستخدام حلقة و type()

variables = [
    "Hello World",        # str
    20,                   # int
    20.5,                 # float
    1j,                   # complex
    ["apple", "banana"],  # list
    ("apple", "banana"),  # tuple
    range(6),             # range
    {"name": "John"},     # dict
    {"apple", "banana"},  # set
    frozenset({"apple"}), # frozenset
    True,                 # bool
    b"Hello",             # bytes
    bytearray(5),         # bytearray
    memoryview(bytes(5))  # memoryview
]

for value in variables:
    print(f"{value} -> {type(value)}")
