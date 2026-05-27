# بايثون العرب - الدرس 19
# difference() للعناصر الموجودة في المجموعة الأولى وليست في الثانية

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "JavaScript"}

only_frontend = frontend.difference(backend)

print(only_frontend)
