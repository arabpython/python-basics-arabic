# بايثون العرب - الدرس 17
# دالة ترجع أكثر من قيمة

def get_scores_stats(scores):
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores)
    return total, average, highest

stats = get_scores_stats([80, 90, 70])

print(stats)

total, average, highest = stats

print("Total:", total)
print("Average:", average)
print("Highest:", highest)
