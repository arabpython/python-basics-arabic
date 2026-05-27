# بايثون العرب - الدرس 18
# الفرق بين الأقواس [] و get()

user = {
    "name": "Ali"
}

print(user.get("age", "No age found"))

# السطر التالي يعطي KeyError إذا شغلته:
# print(user["age"])
