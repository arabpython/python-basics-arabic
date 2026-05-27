# بايثون العرب - الدرس 17
# تحويل Tuple إلى List ثم تعديلها ثم إرجاعها إلى Tuple

colors = ("red", "green", "blue")

colors_list = list(colors)
colors_list[0] = "black"

colors = tuple(colors_list)

print(colors)
