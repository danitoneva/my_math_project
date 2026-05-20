def add(number1,number2):
    return number1 + number2

def subtract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1 * number2    

def divide(number1,number2):
    try:
        return number1 / number2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."

