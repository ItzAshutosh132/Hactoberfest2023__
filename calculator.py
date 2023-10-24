# Define functions for each operation
function add(a, b):
    return a + b

function subtract(a, b):
    return a - b

function multiply(a, b):
    return a * b

function divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b

# Main calculator loop
while True:
    # Display menu to the user
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Get user input for the operation choice
    choice = input("Enter choice (1/2/3/4/5): ")

    if choice == "5":
        print("Calculator exiting. Goodbye!")
        break

    # Get user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = add(num1, num2)
        print("Result: ", result)
    elif choice == "2":
        result = subtract(num1, num2)
        print("Result: ", result)
    elif choice == "3":
        result = multiply(num1, num2)
        print("Result: ", result)
    elif choice == "4":
        result = divide(num1, num2)
        print("Result: ", result)
    else:
        print("Invalid input. Please enter a valid choice (1/2/3/4/5).")
