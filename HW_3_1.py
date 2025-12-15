number1 = int(input("Enter a number: "))
operation = input("Enter an operation: ").strip()
number2 = int(input("Enter another number: "))

match operation:
    case "+":
        result = number1 + number2
        print(f"{number1} + {number2} = {result}")

    case "-":
        result = number1 - number2
        print(f"{number1} - {number2} = {result}")

    case "*":
        result = number1 * number2
        print(f"{number1} * {number2} = {result}")

    case "/":
        if number2 == 0:
            print("You can't divide by zero")
        else:
            result = number1 / number2
            print(f"{number1} / {number2} = {result}")

    case _:
        print("Unknown operation")
