# CLI Calculator Project
# Name: Carlie Tsai

def calculate(num1, num2, operator, decimal_mode=True, remainder_mode=False):
    """Performs a calculation based on the given operator and modes."""
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error: Division by zero"
            if remainder_mode:
                return f"Quotient: {num1 // num2}, Remainder: {num1 % num2}"
            return num1 / num2 if decimal_mode else num1 // num2
        elif operator == "^":
            return num1 ** num2
        else:
            return "Error: Invalid operator"
    except Exception as e:
        return f"Error: {e}"


def get_number(prompt):
    """Get a numeric input from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("Welcome to CLI Calculator ")
    last_result = None

    while True:
        # Ask if user wants to reuse the last result
        if last_result is not None:
            use_last = input("Use last result as the first number? (y/n): ").strip().lower()
            num1 = last_result if use_last == "y" else get_number("Enter first number: ")
        else:
            num1 = get_number("Enter first number: ")

        num2 = get_number("Enter second number: ")
        operator = input("Enter operator (+, -, *, /, ^): ").strip()

        # Ask division preferences
        decimal_choice = True
        remainder_choice = False
        if operator == "/":
            decimal_choice = input("Show decimal result? (y/n): ").strip().lower() == "y"
            remainder_choice = input("Show remainder (integer division)? (y/n): ").strip().lower() == "y"

        # Perform calculation
        result = calculate(num1, num2, operator, decimal_choice, remainder_choice)
        print(f"\n -> Calculation: {num1} {operator} {num2} = {result}")

        # Save result if numeric
        if isinstance(result, (int, float)):
            last_result = result
            try:
                with open("last_result.txt", "w") as f:
                    f.write(str(result))
            except IOError:
                print("Warning: Could not save last result to file.")

        # Ask if user wants to continue
        cont = input("\nDo you want to continue? (y/n): ").strip().lower()
        if cont != "y":
            print("\nThanks for using CLI Calculator.")
            break


if __name__ == "__main__":
    main()
