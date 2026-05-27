# حل تمرين 07

def welcome(name=None):
    if name is None:
        print("أهلا بك")
    else:
        print("أهلا بك", name)

welcome()
welcome("Ahmed")
