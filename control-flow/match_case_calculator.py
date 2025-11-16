# Prompt for user input
num1 = float(input("Enter the first number: ")) #storing 1st number
num2 = float(input("Enter the second number: "))#storing 1st number
operation = input("Choose the operation (+, -, *, /): ")#storing the operation

# Perform the calculation using match case
match operation:
      case '+':
        result = num1 + num2
        print(f"The result is {result}.")
      case '-':
        result = num1 - num2
        print(f"The result is {result}.")
      case '*':
        result = num1 * num2
        print(f"The result is {result}.")
      case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
      case _:
            print("Invalid operation. Please choose one of +, -, *, or /.")