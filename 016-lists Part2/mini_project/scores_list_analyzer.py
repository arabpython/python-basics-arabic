# مشروع صغير إضافي - تحليل قائمة درجات

scores = [70, 95, 80, 60, 90, 85]

total = 0

for score in scores:
    total += score

average = total / len(scores)

scores_sorted = scores.copy()
scores_sorted.sort(reverse=True)

top_three = scores_sorted[:3]

print("=" * 45)
print("Scores:", scores)
print("Total:", total)
print("Average:", average)
print("Top three:", top_three)
print("Highest:", scores_sorted[0])
print("Lowest:", scores_sorted[-1])
print("=" * 45)
