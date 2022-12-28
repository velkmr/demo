option = input("Enter Input")
a = int(input("Enter First Value"))
b = int(input("Enter Second value"))


def add():
    print(a + b)


def sub():
    print(a - b)


def test():
    if option == 'A':
        add()
    else:
        sub()


test()
