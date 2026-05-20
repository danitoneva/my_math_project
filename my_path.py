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

print("Enter first number:")
number1 = float(input())

print("Enter second number:")
number2 = float(input())

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    print("Enter a choice: ")
    choice = float(input())

    if choice == 1:
        print(f"{number1} + {number2} = {add(number1,number2)}")

    elif choice == 2:
        print(f"{number1} - {number2} = {subtract(number1,number2)}")

    elif choice == 3:
        print(f"{number1} * {number2} = {multiply(number1,number2)}")

    elif choice == 4:
        print(f"{number1} / {number2} = {divide(number1,number2)}")

    else:
        print("Invalid choice.")