# مشروع صغير إضافي - تنظيف قائمة من التكرار باستخدام Set

names = ["Ali", "Sara", "Ali", "Omar", "Sara", "Mona", "Ali"]

print("=" * 45)
print("Duplicate Cleaner Tool")
print("=" * 45)

print("Original names:")
print(names)

unique_names_set = set(names)
unique_names_list = list(unique_names_set)

print("\nUnique names as set:")
print(unique_names_set)

print("\nUnique names as list:")
print(unique_names_list)

print("\nIf you need to keep order, use this method:")

ordered_unique_names = []

for name in names:
    if name not in ordered_unique_names:
        ordered_unique_names.append(name)

print(ordered_unique_names)

print("=" * 45)
