# match_case_calculator.py
# A simple calculator using match-case statements (Python 3.10+)

# Prompt for User Input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation Using Match Case
match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero is not allowed."
    case _:
        result = "Error: Invalid operation."

# Output the Result
print(f"The result is: {result}")
