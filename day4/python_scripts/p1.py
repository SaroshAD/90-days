# simple login using if else statement

user= "ADMIN"
pas= "0123"
username = input("Enter username: ")
password = input("Enter password: ")

if username == user and password == pas:
    print("Login successful")
else:
    print("Login failed")



# in this code we will use elif statement to check the username and password one by one

username = input("Enter username: ")

if username == user:
    password = input("Enter password: ")
    if password == pas:
        print("Login successful")
    else:
        print("Login failed")
elif username != user:
    print("wrong username")
