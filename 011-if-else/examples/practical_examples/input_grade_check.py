# بايثون العرب - الدرس 11
# تقييم الدرجة باستخدام input()

grade = int(input("أدخل درجتك: "))

if grade >= 90:
    print("ممتاز")
elif grade >= 80:
    print("جيد جدًا")
elif grade >= 70:
    print("جيد")
else:
    print("تحتاج إلى تحسين")
