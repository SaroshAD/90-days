# use of for loop using range
print("Printing numbers from 0 to 4")
for i in range(5):
    print(i)


print("Printing numbers from 1 to 9")
for i in range(1, 10, 2):         #here it skips 2 units every time it prints the value of i
    print(i)


print("Printing numbers divisible by 11 from 0 to 99")
for i in range(0, 100):
    if i%11==0:
        print(i)
    