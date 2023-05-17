import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero!"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Invalid input!"

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Invalid input!"

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    if x >= 0:
        return math.factorial(x)
    else:
        return "Invalid input!"

def absolute_value(x):
    return abs(x)

def calculate():
    print("Scientific Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")
    print("12. Absolute Value")

    choice = input("Enter operation number (1-12): ")

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))
    elif choice in ['6', '7', '8', '9', '11', '12']:
        num = float(input("Enter the number: "))

        if choice == '6':
            print("Result:", square_root(num))
        elif choice == '7':
            base = float(input("Enter the base: "))
            print("Result:", logarithm(num, base))
        elif choice == '8':
            print("Result:", sine(num))
        elif choice == '9':
            print("Result:", cosine(num))
        elif choice == '11':
            print("Result:", factorial(int(num)))
        elif choice == '12':
            print("Result:", absolute_value(num))
    elif choice == '10':
        angle = float(input("Enter the angle in degrees: "))
        print("Result:", tangent(angle))
    else:
        print("Invalid choice!")

calculate()
