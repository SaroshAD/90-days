marks = [45, 67, 82, 91, 56]
print("Original scores:")

for score in marks:
    print(score)

print("Adding 5 to each score")

for score in marks:
    print(score + 5)


numbers = [10, 15, 20, 25, 30]


print("Use a for loop to print only numbers greater than 20.\n\n")
for num in numbers:

    if num > 20:
        print(num)


numbers = [3, 7, 10, 14, 19, 22]

for i in numbers:
    if i % 2 == 0:
        print(i, "is an even number")
    else:
        print(i, "is an odd number")