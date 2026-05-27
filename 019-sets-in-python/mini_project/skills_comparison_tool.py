# مشروع صغير - أداة مقارنة مهارات باستخدام Set
# الفكرة: استخدام union و intersection و difference لفهم فائدة Set.

ahmed_skills = {"Python", "HTML", "CSS"}
sara_skills = {"Python", "JavaScript", "CSS"}

print("=" * 45)
print("Skills Comparison Tool")
print("=" * 45)

print("Ahmed skills:", ahmed_skills)
print("Sara skills :", sara_skills)

all_skills = ahmed_skills.union(sara_skills)
common_skills = ahmed_skills.intersection(sara_skills)
only_ahmed = ahmed_skills.difference(sara_skills)
only_sara = sara_skills.difference(ahmed_skills)

print("\nAll skills:")
print(all_skills)

print("\nCommon skills:")
print(common_skills)

print("\nOnly Ahmed has:")
print(only_ahmed)

print("\nOnly Sara has:")
print(only_sara)

print("=" * 45)
