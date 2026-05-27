# مشروع صغير إضافي - نتيجة طالب باستخدام return

def calculate_total(scores):
    total = 0
    for score in scores:
        total += score
    return total

def calculate_average(scores):
    return calculate_total(scores) / len(scores)

def get_status(average):
    if average >= 60:
        return "Passed"

    return "Failed"

def build_report(name, scores):
    total = calculate_total(scores)
    average = calculate_average(scores)
    status = get_status(average)

    return f"Name: {name}\nTotal: {total}\nAverage: {average}\nStatus: {status}"

report = build_report("Mona", [80, 90, 70])

print(report)
