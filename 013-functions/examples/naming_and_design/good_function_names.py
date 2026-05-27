# بايثون العرب - الدرس 13
# أسماء دوال جيدة وواضحة

def calculate_total(price, quantity):
    return price * quantity

def check_password(password):
    return password == "python123"

def print_report(title):
    print("-" * 20)
    print(title)
    print("-" * 20)

print(calculate_total(10, 3))
print(check_password("python123"))
print_report("Student Report")
