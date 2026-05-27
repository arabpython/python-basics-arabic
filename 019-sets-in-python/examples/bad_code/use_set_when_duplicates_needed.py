# مثال تعليمي
# إذا كنت تحتاج معرفة عدد التكرارات، لا تستخدم set مباشرة.

votes = ["Ali", "Ali", "Sara", "Omar", "Ali"]

unique_votes = set(votes)

print(unique_votes)

# set أزالت التكرار، وهذا ليس مناسبًا إذا كنت تريد عد الأصوات.
