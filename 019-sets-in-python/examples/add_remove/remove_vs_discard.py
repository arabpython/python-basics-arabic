# بايثون العرب - الدرس 19
# الفرق بين remove و discard

fruits = {"apple", "banana", "orange"}

fruits.discard("mango")
print("After discard missing item:", fruits)

# السطر التالي يعطي KeyError إذا شغلته:
# fruits.remove("mango")
