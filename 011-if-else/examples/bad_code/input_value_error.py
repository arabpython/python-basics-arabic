# مثال قد يعطي ValueError
# إذا كتب المستخدم نصًا بدل رقم، لن يستطيع int() تحويله.

age = int(input("أدخل عمرك: "))

if age >= 18:
    print("بالغ")
else:
    print("أقل من 18")
