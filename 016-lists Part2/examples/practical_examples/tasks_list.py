# بايثون العرب - الدرس 16
# مثال تطبيقي: قائمة مهام بسيطة

tasks = []

tasks.append("تعلم القوائم")
tasks.append("حل تمارين بايثون")
tasks.append("مراجعة الدرس")

print("عدد المهام:", len(tasks))

for task in tasks:
    print("-", task)
