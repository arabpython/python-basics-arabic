# بايثون العرب - الدرس 16
# استخراج أعلى الدرجات باستخدام sort و slicing

scores = [70, 95, 80, 60, 90]

scores.sort(reverse=True)

top_three = scores[:3]

print(top_three)
