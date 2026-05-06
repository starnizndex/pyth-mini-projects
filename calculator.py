

while True:
    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /) or 'C' to quit: ")

    if operation == "C":
        print("Calculator closed.")
        break

    if operation == "+":
        print(f"Result: {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Error!")
    else:
        print("Invalid operation")