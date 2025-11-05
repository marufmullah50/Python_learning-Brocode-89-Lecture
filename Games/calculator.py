#python Calculator
operation = input("Choose a operation (+, -, *, /): ")
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: "))  
if operation  == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
else:
    result ="Invalid operation"
    print("Invalid operation")
print(f"The result of num1 and num2 {operation} is: {result}")