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
        print("Addition of {},{} is ".format(a, b), add())
    elif option == "Sub":
        print("Subtraction of {},{} ".format(a, b), sub())
    elif option == "Multiply":
        print("Multiplication of {},{} ".format(a, b), Multiply())
    elif option == 'Divide':
        print("Division of {},{} ".format(a, b), Divide())


test()
