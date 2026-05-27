# مشروع صغير - تقرير طالب باستخدام الدوال
# الفكرة: تقسيم البرنامج إلى دوال صغيرة بدل كتابة كل شيء في مكان واحد.

def print_line():
    print("-" * 40)

def calculate_total(scores):
    total = 0

    for score in scores:
        total += score

    return total

def calculate_average(scores):
    total = calculate_total(scores)
    return total / len(scores)

def get_level(average):
    if average >= 90:
        return "ممتاز"
    elif average >= 80:
        return "جيد جدًا"
    elif average >= 70:
        return "جيد"
    else:
        return "تحتاج إلى تحسين"

def print_student_report(name, scores):
    total = calculate_total(scores)
    average = calculate_average(scores)
    level = get_level(average)

    print_line()
    print("Student Report")
    print_line()
    print(f"Name   : {name}")
    print(f"Scores : {scores}")
    print(f"Total  : {total}")
    print(f"Average: {average}")
    print(f"Level  : {level}")
    print_line()

student_name = "Mona"
student_scores = [85, 90, 80]

print_student_report(student_name, student_scores)
