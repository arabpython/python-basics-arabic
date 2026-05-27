# بايثون العرب - الدرس 15
# نفس اسم المتغير داخل وخارج الدالة لا يعني أنهما نفس المتغير

name = "Ali"

def show_name():
    name = "Omar"
    print("Inside function:", name)

show_name()
print("Outside function:", name)
