

def print_name(*arg):
    print("inside print_name")
    print(type(arg))
    print(len(arg))
    for v in arg:
        print(v)


# print_name()
print_name("Akshara","bhanu","prakash")


