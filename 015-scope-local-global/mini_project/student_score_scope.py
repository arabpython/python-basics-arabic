# مشروع صغير إضافي - نتيجة طالب بدون الاعتماد على global

def calculate_total(scores):
    total = 0  # Local variable
    for score in scores:
        total += score
    return total

def calculate_average(scores):
    total = calculate_total(scores)
    return total / len(scores)

site_name = "بايثون العرب"  # Global variable للقراءة فقط

def print_report(name, scores):
    average = calculate_average(scores)
    print("=" * 40)
    print(site_name)
    print("Student:", name)
    print("Average:", average)
    print("=" * 40)

print_report("Mona", [80, 90, 70])
