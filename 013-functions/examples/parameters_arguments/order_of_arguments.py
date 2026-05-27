# بايثون العرب - الدرس 13
# ترتيب Arguments مهم عند استخدام أكثر من Parameter

def student_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

student_info("Ali", 20)

# لو عكست الترتيب سيختلف المعنى:
student_info(20, "Ali")
