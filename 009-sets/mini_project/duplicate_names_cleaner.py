# مشروع صغير - تنظيف قائمة أسماء من التكرار
# الفكرة: استخدام set لحذف التكرار، ثم تنفيذ عمليات بسيطة على المجموعة.

names = ["Ali", "Omar", "Ali", "Sara", "Omar", "Mona", "Sara"]

print("=" * 45)
print("Original names list:")
print(names)

unique_names = set(names)

print("\nUnique names as set:")
print(unique_names)

unique_names.add("Khaled")
unique_names.discard("Unknown")

print("\nAfter add Khaled and discard Unknown:")
print(unique_names)

new_names = {"Lina", "Ali", "Ahmed"}

print("\nUnion with new_names:")
print(unique_names.union(new_names))

print("\nCommon names with new_names:")
print(unique_names.intersection(new_names))

print("\nDifferent names:")
print(unique_names.symmetric_difference(new_names))

print("\nBack to list:")
print(list(unique_names))

print("=" * 45)
