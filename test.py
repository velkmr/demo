import os

# option = input("Enter Input")
option = os.environ['Select_One']

# a = int(input("Enter first Value")
a = int(os.environ['First_Value'])

# b = int(input("Enter Second Value")
b = int(os.environ['Second_Value'])


def add():
    return a + b


def sub():
    return a - b


def Multiply():
    return a * b


def Divide():
    return a / b


def test():
    if option == 'Add':
        print(add())
    elif option == "Sub":
        print(sub())
    elif option == "Multiply":
        print(Multiply())
    elif option == 'Divide':
        print(Divide())


test()
