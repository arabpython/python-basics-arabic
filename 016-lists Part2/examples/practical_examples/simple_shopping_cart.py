# بايثون العرب - الدرس 16
# مثال سلة مشتريات بسيطة

cart = []

cart.append("Laptop")
cart.append("Mouse")
cart.append("Keyboard")

print("Items count:", len(cart))

for item in cart:
    print("-", item)

cart.remove("Mouse")

print("After remove:", cart)
