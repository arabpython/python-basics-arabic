# بايثون العرب - الدرس 13
# الفرق بين print و return

def add_with_print(a, b):
    print(a + b)

def add_with_return(a, b):
    return a + b

add_with_print(5, 3)

total = add_with_return(5, 3)
print(total * 2)
