# مشروع صغير - بيانات ملف شخصي ثابتة باستخدام Tuple
# الفكرة: استخدام Tuple للبيانات التي لا نريد تعديلها مباشرة.

profile = ("Mona", 22, "Amman", "Python")

name, age, city, skill = profile

print("=" * 45)
print("Fixed Profile")
print("=" * 45)
print("Name :", name)
print("Age  :", age)
print("City :", city)
print("Skill:", skill)

print("\nOriginal tuple:")
print(profile)

# إذا احتجنا تعديلًا مؤقتًا:
profile_list = list(profile)
profile_list[3] = "Python & Data"
updated_profile = tuple(profile_list)

print("\nUpdated copy:")
print(updated_profile)
print("=" * 45)
