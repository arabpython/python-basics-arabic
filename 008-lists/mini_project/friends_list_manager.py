# مشروع صغير - إدارة قائمة أصدقاء بسيطة
# الفكرة: تطبيق أغلب عمليات القوائم في برنامج واحد.

friends = ["Ali", "Omar", "Sara", "Mona", "Khaled"]

print("=" * 45)
print("Initial friends list:")
print(friends)

print("\nFirst friend:", friends[0])
print("Last friend:", friends[-1])

friends.append("Ahmed")
print("\nAfter append Ahmed:")
print(friends)

friends.insert(2, "Lina")
print("\nAfter insert Lina at index 2:")
print(friends)

friends.remove("Omar")
print("\nAfter remove Omar:")
print(friends)

removed_friend = friends.pop()
print("\nRemoved last friend:", removed_friend)
print("After pop():")
print(friends)

print("\nNumber of friends:", len(friends))
print("Is Sara in friends?", "Sara" in friends)

sorted_friends = friends.copy()
sorted_friends.sort()

print("\nOriginal friends list:")
print(friends)

print("Sorted copy:")
print(sorted_friends)

sorted_friends.reverse()
print("Reversed sorted copy:")
print(sorted_friends)

print("=" * 45)
