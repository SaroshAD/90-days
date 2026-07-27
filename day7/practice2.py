# password checker

password = "robotics"

name= input("Enter your name : ")

while True:
    user_password = input("Enter the password: ")
    if user_password==password:
        print("Access Granted !!\n")
        break
    else:
        print("Wrong Password.")

print(f"Welcome to the lab {name} ...")




# mini ATM without user login  
def show_balance():
    print(f"Your current balance is {balance}.")
balance = 5000

while True:
    print("1.Check Balance. \n2.Deposit. \n3.Withdraw. \n4.Exit. ")
    choose=int(input("Enter the option to choose: "))

    if choose==1:
        show_balance()
    elif choose==2:
        deposit = int(input("Enter the amount to deposit: "))
        while deposit <= 0:
            deposit = int(input("Enter the correct amount to deposit: "))

        balance=balance + deposit
        show_balance()

    elif choose==3:
        withdraw = int(input("Enter the amount to withdraw: "))
        # while withdraw <= 0 or withdraw > balance:
        #     withdraw = int(input("Enter the correct amount to withdraw: "))

        while True:
            if withdraw <=0:
                withdraw=int(input("Enter amount greater than 0 :"))
            elif withdraw > balance:
                print(f"Insufficient balance. Your current balance is {balance}.")
                withdraw = int(input("Enter the amount to withdraw: "))
            else:
                break
        balance =balance - withdraw
        show_balance()

    elif choose==4:
        print("Thank You !  visit agian..")
        break

    else:
        print("Wrong option")