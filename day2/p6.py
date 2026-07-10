name = input("What is your name?\n")
weight =input('what do you weigh? (in pounds)\t')

print(type(weight))
weight = int(weight)
print(type(weight))

print(name,'weight is ',weight, 'pounds')

kg = weight * 0.45

print(type(kg))

print(name, 'weight in kg is ', kg, 'kilograms')


print("\n\n")


# This below is a formatted string
f_string = f"{name}'s weight is {kg} kilograms"
print(f_string)

print(f"{name}'s weight is {kg} kilograms")

# this below is to fing length of string

length = len(f_string)

print(length)

print(f_string.capitalize())

print(f_string.upper())


# for using "\" in the print code

# print('C:\Users\Sarosh\python')

print(r'C:\Users\Sarosh\python')


# use of modulo operator

print("The student %s weight is %s kilograms" %(name,kg))