# بايثون العرب - الدرس 21
# البحث عن منتج داخل قائمة قواميس

def find_product(products, product_name):
    for product in products:
        if product["name"] == product_name:
            return product

    return None

products = [
    {"name": "Laptop", "price": 800},
    {"name": "Mouse", "price": 20},
]

result = find_product(products, "Keyboard")

if result is None:
    print("المنتج غير موجود")
else:
    print(result)
