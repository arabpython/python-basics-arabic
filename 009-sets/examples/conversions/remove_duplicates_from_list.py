# بايثون العرب - الدرس 09
# حذف القيم المكررة من قائمة باستخدام set()

names = ["Ali", "Omar", "Ali", "Sara", "Omar"]

unique_names = set(names)

print(unique_names)

# تحويل النتيجة إلى list مرة أخرى:
unique_names_list = list(unique_names)

print(unique_names_list)

# ملاحظة: الترتيب قد يتغير لأن Set غير مرتبة.
