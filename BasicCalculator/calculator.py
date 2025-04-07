#Basic calculator

#Ask the user to input the first number
num1 = float(input("Enter first number:"))

#Ask the user to input the second number
num2 = float(input("Enter second number:"))

#Ask the user to input the operator
operation = input("Enter operator (+, -, *, /):")

#Perform the calculation based on the operator
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero.")     
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")               