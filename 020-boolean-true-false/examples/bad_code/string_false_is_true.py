# مثال تعليمي مهم
# النص "False" ليس False، بل نص غير فارغ لذلك bool("False") تساوي True.

value = "False"

print(bool(value))

if value:
    print("هذا النص غير فارغ، لذلك يعتبر True")
