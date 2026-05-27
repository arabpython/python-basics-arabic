# بايثون العرب - الدرس 17
# الفرق العملي بين List و Tuple

names_list = ["Ali", "Sara", "Omar"]
names_list[0] = "Ahmed"
print("List:", names_list)

names_tuple = ("Ali", "Sara", "Omar")
print("Tuple:", names_tuple)

# السطر التالي يعطي TypeError إذا شغلته:
# names_tuple[0] = "Ahmed"
