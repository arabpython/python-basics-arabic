# بايثون العرب - الدرس 13
# تقسيم البرنامج إلى دوال صغيرة

def print_line():
    print("-" * 30)

def print_title(title):
    print_line()
    print(title)
    print_line()

def calculate_total(scores):
    total = 0
    for score in scores:
        total += score
    return total

scores = [80, 90, 70]

print_title("Scores Report")
print("Total:", calculate_total(scores))
