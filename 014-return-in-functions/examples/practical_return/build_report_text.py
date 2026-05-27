# بايثون العرب - الدرس 14
# دالة ترجع نص تقرير بدل طباعته مباشرة

def build_report(name, score):
    return f"Student {name} scored {score}"

report = build_report("Mona", 90)

print(report)
