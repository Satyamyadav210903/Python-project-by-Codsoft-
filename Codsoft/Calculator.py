def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Error: Cannot divide by zero.")
        return None
    return x / y

def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue

        operation = input("Choose an operation (+, -, *, /): ")

        if operation not in ['+', '-', '*', '/']:
            print("Invalid operation. Please choose a valid operation.")
            continue

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)

        if result is not None:
            print(f"Result: {result}")

        another_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if another_calculation != 'yes':
            print("Calculator closed.")
            break

if __name__ == "__main__":
    calculator()
