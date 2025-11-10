# Simple Menu-Driven Calculator

while True:
    print("\n----- Calculator Menu -----")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    choice = input("Enter your choice (1-5): ")

    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice! Please enter a number between 1 and 5.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if choice == '1':
        result = num1 + num2
        print(f"The result of addition: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of subtraction: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of multiplication: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of division: {result}")
        else:
            print("Error: Division by zero is not allowed.")
            continue
    elif choice == '5':
        result = num1 % num2
        print(f"The result of modulus: {result}")

    again = input("Do you want to perform another calculation? (yes/no): ").lower()
    if again != 'yes':
        print("Thank you for using the calculator. Goodbye!")
        break
