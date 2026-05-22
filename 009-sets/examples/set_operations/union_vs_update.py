# بايثون العرب - الدرس 09
# الفرق بين union() و update()

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

new_set = set1.union(set2)

print("set1 after union:", set1)
print("new_set:", new_set)

set1.update(set2)

print("set1 after update:", set1)
