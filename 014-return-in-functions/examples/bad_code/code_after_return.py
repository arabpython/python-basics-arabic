# مثال تعليمي
# الكود بعد return في نفس المسار لن يعمل.

def test():
    return "Done"
    print("This line will not run")

print(test())
