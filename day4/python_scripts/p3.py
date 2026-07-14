
# This program takes an integer input from the user and checks if it is divisible by 3, 5, or both. If the number is divisible by both 3 and 5, it prints "FizzBuzz". If it is only divisible by 3, it prints "Fizz". If it is only divisible by 5, it prints "Buzz". If the number is not divisible by either, it simply prints the number itself.
num = int(input("Enter a number: "))

if num% 15 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")  
else:
    print(num)


# here we are using a range of numbers from 1 to 31 to check the fizzbuzz for each as same as above code but here we are using a for loop to check the fizzbuzz for each number in the range of 1 to 31
for n in range(1, 31):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")  
    else:
        print(n)