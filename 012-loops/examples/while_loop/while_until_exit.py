# بايثون العرب - الدرس 12
# تكرار حتى يكتب المستخدم exit

command = ""

while command != "exit":
    command = input("اكتب أمرًا أو exit للخروج: ")
    print("You typed:", command)

print("انتهى البرنامج")
