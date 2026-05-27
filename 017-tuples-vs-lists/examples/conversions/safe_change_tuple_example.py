# بايثون العرب - الدرس 17
# تعديل Tuple بطريقة غير مباشرة عبر التحويل إلى List

days = ("Saturday", "Sunday", "Monday")

days_list = list(days)
days_list.append("Tuesday")

days = tuple(days_list)

print(days)
