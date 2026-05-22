# بايثون العرب - الدرس 09
# add() و update()

fruits = {"apple", "banana", "cherry"}

fruits.add("orange")
print("After add:", fruits)

tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print("After update with set:", fruits)

my_list = ["kiwi", "grape"]
fruits.update(my_list)
print("After update with list:", fruits)
