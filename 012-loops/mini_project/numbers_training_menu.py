# مشروع صغير - تدريب على الأرقام والحلقات
# الفكرة: برنامج بسيط يستخدم for و while و break و continue.

while True:
    print("\nاختر عملية:")
    print("1 - طباعة الأرقام من 1 إلى 10")
    print("2 - طباعة الأرقام الزوجية من 2 إلى 20")
    print("3 - جدول ضرب رقم")
    print("4 - خروج")

    choice = input("اختيارك: ")

    if choice == "1":
        for i in range(1, 11):
            print(i)

    elif choice == "2":
        for i in range(2, 21, 2):
            print(i)

    elif choice == "3":
        number = int(input("أدخل الرقم: "))

        for i in range(1, 11):
            print(number, "x", i, "=", number * i)

    elif choice == "4":
        print("تم الخروج من البرنامج")
        break

    else:
        print("اختيار غير صحيح، حاول مرة أخرى")
