# printing multiplicaation table  of 9

num = 9

for i in range(1, 11):
    print(f"{num} X {i} = {num*i}")


#  printing numbers in reverse from 20 

count = 20

while True:
    print(count)
    count-=1
    if count==-1:
        break


# ask the user ro enter the number until they enter 0 then stop
while True:
    number = int(input("Enter the number: "))
    if number==0:
        print("You have entered zero")
        break