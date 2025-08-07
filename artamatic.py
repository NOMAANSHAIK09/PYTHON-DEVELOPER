# Taking input from the user
num1 = int(input("Enter first number: "))
operator = input("Enter operation (+, -, *, /): ")
num2 = int(input("Enter second number: "))

# Performing arithmetic operation
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operator"

# Showing the result
print("Result:", result)
