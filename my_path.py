def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b    

def divide(a,b):
    if b == 0:
        print("Error: Division by zero is not allowed.")
    return a / b

print("Enter first number:")
a = float(input())

print("Enter second number:")
b = float(input())

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

print("Enter a choice: ")
choice = float(input())

if choice == 1:
    print(f"{a} + {b} = {add(a,b)}")

elif choice == 2:
    print(f"{a} - {b} = {add(a,b)}")

elif choice == 3:
    print(f"{a} * {b} = {add(a,b)}")

elif choice == 4:
    print(f"{a} / {b} = {add(a,b)}")

else:
    print("Invalid choice.")