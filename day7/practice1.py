# revrse the number

number = int(input("Enter the numnber to reverse it : "))
reverse= 0
while number > 0:

    last_digit = number % 10
    reverse= reverse*10 + last_digit
    number=number // 10

print(reverse)




# Finding how manuy odd or even numbers are there in the given nu,mber

number = int(input("Enter the numnber : "))
even_counts = 0
odd_counts = 0
while number >  0:
    last_digit = number % 10
    if last_digit % 2 !=0:
        odd_counts+=1
    else:
        even_counts+=1
    number=number // 10

print(f"Count of odd numbers = {odd_counts}\nCount of enen numbers = {even_counts}")

# finding the largest number 

num1=int(input("Entert the first number: "))
num2=int(input("Entert the second number: "))
num3=int(input("Entert the third number: "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3} .")
elif num2>num1 and num2 > num3:
    print(f"{num2} is greater than {num1} and {num3}. ")
else:
    print(f"\n\n{num3} is grater than {num1} and {num2} .")


# writing the table from the given input number


num=int(input("Enter the number to print the table:"))

print(f"The below is the table of {num}.\n\n")

for i  in range (1, 11):
    print(f"{num} X {i} = {num * i}")




# sum of all digit from given input number

num_a = int(input("Enter the number     :"))
num_b=num_a
number_sum=0

while num_a > 0:
    last_digit=num_a % 10
    number_sum = number_sum + last_digit
    num_a = num_a//10

print(f"The sum of all digits in {num_b} is {number_sum}.")