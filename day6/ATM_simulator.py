# Simple ATM simulator 


pin = 2244
balance = 1500

attempt = 0
logged_in = False

while attempt < 3 :
    user_pin = int(input("Enter the pin:"))
    if user_pin==pin:
        logged_in = True
        print("Welcome!")
        break
    elif user_pin!=pin:
        attempt+=1
        print("Wrong PIN !")
        if attempt==3:
            print("You have entered wrong pin 3 times! \n please contact the bank.")

while logged_in:
    print("1.Check Balance \n2.Deposit cash \n3.Withdarw cash \n4.Exit")
    choice=int(input("Choose the option: "))
    if choice==1:
        print(f"Your balance is {balance} rupees. ")
    elif choice==2:
        deposit = abs(int(input("Enter the amount to deposit:")))
        balance =  deposit+balance
        print(f"Your updated balance is {balance} rupees. ")

    elif choice==3:
        while True:
            withdraw =abs(int(input("Enter the amount to Withdraw")))

            if withdraw > balance:
                print("withdraw failed ! Due to insufficient balance.\nEnter the correct amount.")
            else:
                balance = balance-withdraw
                print(f"Your updated balance is {balance} rupees. ")
                break

    elif choice==4:
        print("Thank You! Visit again.")
        break

    else:
        print("Enter the correct option: ")
