# بايثون العرب - الدرس 19
# مثال عملي: معرفة المهارات التي تحتاج تعلمها

required_skills = {"Python", "HTML", "CSS", "SQL"}
my_skills = {"Python", "HTML"}

missing_skills = required_skills.difference(my_skills)

print("Missing skills:", missing_skills)
