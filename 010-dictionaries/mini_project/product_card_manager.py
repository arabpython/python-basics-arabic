# مشروع صغير - بطاقة منتج باستخدام Dictionary
# الفكرة: تخزين بيانات منتج، تعديلها، إضافة معلومات، ثم عرضها بشكل منظم.

product = {
    "name": "Laptop",
    "price": 750,
    "available": True,
    "category": "Electronics"
}

print("=" * 45)
print("Initial product:")
print(product)

product["price"] = 699
product["discount"] = "10%"
product["specs"] = {
    "ram": "16GB",
    "storage": "512GB SSD"
}

print("\nProduct card:")
print("Name     :", product["name"])
print("Price    :", product["price"])
print("Available:", product.get("available", False))
print("Category :", product.get("category", "No category"))
print("RAM      :", product["specs"]["ram"])
print("Storage  :", product["specs"]["storage"])

removed_discount = product.pop("discount")

print("\nRemoved discount:", removed_discount)

print("\nAll product data:")
for key, value in product.items():
    print(key, "=>", value)

print("=" * 45)
