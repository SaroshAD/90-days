def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    else:
        return a / b

def calculator():

    while True:

        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        

        choice = input("Enter choice (1/2/3/4/5): ")
        if choice == '5':
                    print("Exiting the calculator.")
                    break
        elif choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="5":
          print("select the correct command")
          continue
        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            print(f"{num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"{num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"{num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            if result is not None:
                print(f"{num1} / {num2} = {result}")



calculator()