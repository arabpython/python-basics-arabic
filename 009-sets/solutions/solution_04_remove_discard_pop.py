# حل تمرين 04

fruits = {"apple", "banana", "cherry", "orange"}

fruits.remove("banana")
fruits.discard("mango")

removed_item = fruits.pop()

print("Removed by pop:", removed_item)
print("Current set:", fruits)
