print(
    """
    Please select operation:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    """
)

operation = int(input("Enter operation: "))

if operation not in [1, 2, 3, 4]:
    print("Invalid operation")
    exit()
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if operation == 1:
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == 2:
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == 3:
    print(f"{num1} * {num2} = {num1 * num2}")
else:
    print(f"{num1} / {num2} = {num1 / num2}")