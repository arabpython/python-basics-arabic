# بايثون العرب - الدرس 21
# الفرق بين None والنص الفارغ

name1 = ""
name2 = None

print(name1 == name2)

if name1 == "":
    print("name1 نص فارغ")

if name2 is None:
    print("name2 لا يحتوي على قيمة")
