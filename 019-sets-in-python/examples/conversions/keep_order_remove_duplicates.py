# بايثون العرب - الدرس 19
# طريقة تحافظ على الترتيب أثناء إزالة التكرار
# هذه إضافة تدريبية مفيدة لأن set قد لا يحافظ على الترتيب.

names = ["Ali", "Sara", "Ali", "Omar", "Sara"]
unique_names = []

for name in names:
    if name not in unique_names:
        unique_names.append(name)

print(unique_names)
