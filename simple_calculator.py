# Basic Calculator Program

# Get inputs from the user
num1 = float(input("34: "))
num2 = float(input("62: "))
operation = input("(*): ")

# Perform the operation and display the result
if operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
