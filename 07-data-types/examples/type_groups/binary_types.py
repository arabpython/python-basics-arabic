# بايثون العرب - الدرس 07
# الأنواع الثنائية: bytes, bytearray, memoryview
# هذه الأنواع متقدمة قليلًا، وتستخدم مع الملفات والبيانات الثنائية.

x = b"Hello"
y = bytearray(5)
z = memoryview(bytes(5))

print(x, type(x))
print(y, type(y))
print(z, type(z))
