# حل تمرين 04

colors = ("red", "green", "blue")

colors_list = list(colors)
colors_list[0] = "black"
colors = tuple(colors_list)

print(colors)
