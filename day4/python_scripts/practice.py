# practice code for asking user username and passwrod upto 3 times

USERNAME = "admin"
PASSWORD = "password123"

logged_in = False
for i in range(3):
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")

    
    if input_username == USERNAME and input_password == PASSWORD:
            print("Login successful!")
            logged_in = True
            break
    else:
        print("Invalid username or password. Please try again.")

        if i < 2:
             print(f"You have {2 - i} attempts left.")

if not logged_in:
     print("Maximum attempts reached. Access denied.\n Account locked. Please contact the administrator.")


#------------------------------------------------------------------------------------------



# practice for asking user a num and giving output as a table of that number upto 10


num = int(input("Enter a number: "))

print(f"Multiplication table for {num}:")

for i in range(1, 11):
    result = num * i
    print(f"{num} x {i} = {result}")

print("Thank You")


# ---------------------------------------------------------



# printing the square numbers


m=int(input("ENter the number to start the aquare numbers from:"))

n =int(input("Enter the number to end the square numbers at:"))



for i in range(m, n + 1):
     square = i ** 2
     print(f"the square of {i} = {square }")
     
print("Thank You")
