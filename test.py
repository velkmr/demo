import os

# option = input("Enter Input")
option = os.environ['Select_One']

# a = int(input("Enter first Value")
a = os.environ['First_Value']

# b = int(input("Enter Second Value")
b = os.environ['Second_Value']


def add():
    return a+b


def sub():
    return a-b


def test():
    if option == 'A':
        print(add())
    else:
        print(sub())


test()
