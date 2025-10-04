import math

def calculator():
    print("Welcome to the calculator!")
    while True:
        print("\nAvailable operations: +, -, *, /, ^ (power), sqrt (square root), exit")
        op = input("Enter operation: ").strip()
        if op == "exit":
            print("Exiting calculator.")
            break
        if op == "sqrt":
            try:
                num = float(input("Enter a number: "))
                result = math.sqrt(num)
                print(f"√{num} = {result}")
            except ValueError:
                print("Error: please enter a valid number.")
            continue
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Error: please enter valid numbers.")
            continue
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                print("Error: division by zero.")
                continue
            result = num1 / num2
        elif op == "^":
            result = num1 ** num2
        else:
            print("Error: unknown operation.")
            continue
        print(f"Result: {result}")
if __name__ == "__main__":
    calculator()