# بايثون العرب - الدرس 15
# تعديل نتيجة باستخدام return بدل global

def add_points(current_score, points):
    return current_score + points

score = 0
score = add_points(score, 10)
score = add_points(score, 5)

print(score)
