# مثال تعليمي
# هذا لا يعطي خطأ، لكنه لا يغير المتغير العام كما يتوقع المبتدئ.

count = 0

def increase():
    count = 1
    print("Inside:", count)

increase()
print("Outside:", count)
