# بايثون العرب - الدرس 16
# remove() و pop()

fruits = ["apple", "banana", "orange"]

fruits.remove("banana")
print("After remove:", fruits)

last_item = fruits.pop()
print("Last item:", last_item)
print("After pop:", fruits)

fruits = ["apple", "banana", "orange"]
fruits.pop(1)
print("After pop(1):", fruits)
