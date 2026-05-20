# بايثون العرب - الدرس 06
# الفرق بين == و is

list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print(list_a == list_b)  # True: نفس القيم
print(list_a is list_b)  # False: ليسا نفس الكائن
print(list_a is list_c)  # True: نفس الكائن في الذاكرة
