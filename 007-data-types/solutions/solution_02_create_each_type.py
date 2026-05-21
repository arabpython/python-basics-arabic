# حل تمرين 02

text_value = "Python"
integer_value = 10
float_value = 10.5
list_value = ["apple", "banana"]
tuple_value = ("apple", "banana")
dict_value = {"name": "Ali", "age": 25}
set_value = {"python", "beginner"}
bool_value = True

values = [
    text_value,
    integer_value,
    float_value,
    list_value,
    tuple_value,
    dict_value,
    set_value,
    bool_value
]

for value in values:
    print(value, "->", type(value))
