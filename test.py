import os

# option = input("Enter Input")
option = os.environ['Select_One']



# a = int(input("Enter first Value")
a = int(os.environ['First_Value'])

# b = int(input("Enter Second Value")
b = int(os.environ['Second_Value'])

file1 = os.environ("data.json")
print(type(file1))
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
        print("Subtraction of {},{} is ".format(a, b), sub())
    elif option == "Multiply":
        print("Multiplication of {},{} is ".format(a, b), Multiply())
    elif option == 'Divide':
        print("Division of {},{} is ".format(a, b), Divide())


test()
