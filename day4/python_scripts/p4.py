# this is a practice file    

# 1. Even or Odd

p = int(input("Enter a number: "))

if p % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. Positive , Negative and zero

q = int(input("Enter a number: "))

if q>0:
    print("the number is positive")
elif q<0:
    print("the number is negative")
else:
    print("the number is zero")


# 3. voting eligibility


age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote")
else: 
    print("You are not eligible to vote")


# 4. largest of three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("the lrgest number is :", num1)
elif num2 >= num1 and num2 >= num3:
    print(" the lagest number is :", num2)
else:
    print("the largest number is :", num3)




# 5. simple calculator using if else statement


a = int(input("Enter the first number:"))
oper = input("Enter the operator (+, -, *, /): ")
b = int(input("Enter the second number:"))

if oper == "+":
    print (" thesum of the given number  is :", a+b)
elif oper =="-":
    print("the subtraction of the given number is :", a-b)
elif oper == "*":
    print("the multiplication of the given number is :", a*b)
elif oper == "/":
    if b != 0:
        print("the division of the given number is :", a/b)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operator. Please use +, -, *, or /.")



# 6 . check whether it is a leap year or not

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("It is a leap year.")
else:
    print("It is not a leap year.")