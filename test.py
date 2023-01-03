import os

# option = input("Enter Input")
option = os.environ['Select_One']

# a = int(input("Enter first Value")
a = int(os.environ['First_Value'])

# b = int(input("Enter Second Value")
b = int(os.environ['Second_Value'])


def add():
    return a+b


def sub():
    return a-b


def test():
    if option == 'Add':
        print(add())
    else:
        print(sub())


test()
