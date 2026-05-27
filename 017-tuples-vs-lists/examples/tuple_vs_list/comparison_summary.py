# بايثون العرب - الدرس 17
# مقارنة مختصرة بين List و Tuple

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

print("List type :", type(my_list))
print("Tuple type:", type(my_tuple))

my_list.append(4)
print("List after append:", my_list)

# Tuple لا تدعم append:
# my_tuple.append(4)
