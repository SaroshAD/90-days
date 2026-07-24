import random
m = int(input("Enter the starting number: "))
n = int(input("Enter the ending number:"))
guess = random.randint(m, n)
attempts=0
while True:
    

    guess_num = int(input(f"Guess a number between {m} to {n} :"))
    attempts+=1
    if guess > guess_num:
        print("Too low . Try Again|")
    elif guess < guess_num:
        print("too HIgh . Try again")
    else:
        print(f"Congratulations You Won in {attempts} attempts..")
        break