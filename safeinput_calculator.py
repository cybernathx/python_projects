def result_display(result):
    print(f"The result is: {result}")

def process():
    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /, %): ")
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")
        return

    if operation == "+":
            result = first_number + second_number
            result_display(result)
    elif operation == "-":
            result = first_number - second_number
            result_display(result)
    elif operation == "*":
            result = first_number * second_number
            result_display(result)
    elif operation == "/":
        try:
            if second_number == 0:
                raise ValueError("Cannot divide by zero.")
            result = first_number / second_number
            result_display(result)
        except ValueError as ve:
            print(f"Value error: {ve}")
    elif operation == "%":
        try:
            if second_number == 0:
                raise ValueError("Cannot perform modulus by zero.")
            result = first_number % second_number
            result_display(result)
        except ValueError as ve:
            print(f"Value error: {ve}")
    else:
        print("Invalid operation. Please enter one of the following: +, -, *, /, %.")

    decision = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
    if decision == "yes":
        print("Starting a new calculation...")
        return True
    elif decision == "no":
        print("Thank you for using the calculator. Goodbye!")
        return False
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")


while True:
    if not process():
        break