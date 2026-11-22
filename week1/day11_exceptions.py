def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero."


def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number. Try again.\n")
        calculator()
    else:
        print("Sum:", add(num1, num2))
        print("Difference:", subtract(num1, num2))
        print("Product:", multiply(num1, num2))
        print("Division:", divide(num1, num2))


calculator()
