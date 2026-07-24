while True:
    operator = input("Enter the operation to do:")

    if operator=="quit":
          break
    elif operator!="+":
          continue
    elif operator!="-":
          continue
    elif operator!="/":
          continue
    elif operator!="*":
          print("select the correct command")
          continue

    num1 =float(input("Enter the first number:"))
    num2 =float(input("Enter the second number:"))

    if operator == "+":
            print(f"The addtion of {num1} and {num2} is {num1+num2}\n{num1} + {num2} = {num1+num2}")
        
    elif operator=="-":
            print(f"The subtraction of {num1} and {num2} is {num1-num2}\n{num1} - {num2} = {num1-num2}")
    elif operator=="/":
        if num2 == 0:
            print("It cannot be divided by zero")
        else:
            print(f"The division of {num1} and {num2} is {num1/num2}\n{num1} / {num2} = {num1/num2}")
    elif operator=="*":
            print(f"The multiplication of {num1} and {num2} is {num1*num2}\n{num1} * {num2} = {num1*num2}")
    
    
    