# scientific_calculator.py

import math


def display_menu():
    """Display the menu of available operations."""
    print("\nScientific Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponential")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Trigonometric Functions")
    print("9. Exit")


def get_number(prompt):
    """Prompt the user to enter a number and validate the input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference between x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the quotient of x and y. Handle division by zero."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


def exponential(x, y):
    """Return x raised to the power of y."""
    return math.pow(x, y)


def square_root(x):
    """Return the square root of x. Handle negative input."""
    if x < 0:
        return "Error: Square root of negative number is not allowed."
    return math.sqrt(x)


def logarithm(x, base=10):
    """Return the logarithm of x with a given base. Default is base 10."""
    if x <= 0:
        return "Error: Logarithm of non-positive number is not allowed."
    return math.log(x, base)


def trigonometric_functions(x, function):
    """Return the result of a trigonometric function."""
    x_rad = math.radians(x)
    if function == 'sin':
        return math.sin(x_rad)
    elif function == 'cos':
        return math.cos(x_rad)
    elif function == 'tan':
        return math.tan(x_rad)
    else:
        return "Error: Invalid trigonometric function."


def perform_operation(choice):
    """Perform the selected operation based on user choice."""
    if choice in ('1', '2', '3', '4'):
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    elif choice == '5':
        num1 = get_number("Enter the base number: ")
        num2 = get_number("Enter the exponent: ")
        print(f"Result: {exponential(num1, num2)}")
    elif choice == '6':
        num = get_number("Enter the number: ")
        print(f"Result: {square_root(num)}")
    elif choice == '7':
        num = get_number("Enter the number: ")
        base = get_number("Enter the base (default is 10): ") or 10
        print(f"Result: {logarithm(num, base)}")
    elif choice == '8':
        angle = get_number("Enter the angle in degrees: ")
        function = input("Enter the trigonometric function (sin, cos, tan): ").strip().lower()
        print(f"Result: {trigonometric_functions(angle, function)}")
    elif choice == '9':
        print("Exiting the calculator. Goodbye!")


def main():
    """Main function to run the calculator."""
    while True:
        display_menu()
        choice = input("Choose an operation: ")
        if choice == '9':
            perform_operation(choice)
            break
        elif choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
            perform_operation(choice)
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
