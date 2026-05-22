# بايثون العرب - الدرس 09
# الفرق بين remove() و discard()

fruits = {"apple", "banana", "cherry"}

fruits.remove("banana")
print("After remove banana:", fruits)

# discard لا يعطي خطأ إذا كان العنصر غير موجود.
fruits.discard("mango")
print("After discard mango:", fruits)
