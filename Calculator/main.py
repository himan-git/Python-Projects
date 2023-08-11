import os
from logo_art import logo
print(logo)

def add(num1,num2):
    return num1 + num2

def multiply(num1 , num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def subtract(num1, num2):
    return num2 - num1

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """ Performs add, subtract, multiply, divide """
    num1 = float(input("Enter the first number:  "))
    for symbol in operations:
        print(symbol)

    should_continue = False

    while not should_continue:
        operator = input("Enter the operation you want to perform from the above list:  ")
        num2 = float(input("Enter the seccod number:  "))
        cal_func = operations[operator]
        answer = cal_func(num1, num2)
        print(f"{num1} {operator} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start new calculations;  ") == 'y':
            num1 = answer
        else:
            os.system("clear")
            calculator()

calculator()
