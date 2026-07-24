name = input("What is your name?")
weight =input('what do you weigh? (in pounds)')

print(type(weight))
weight = int(weight)
print(type(weight))

print(name,'weight is ',weight, 'pounds')

kg = weight * 0.45

print(type(kg))

print(name, 'weight in kg is ', kg, 'kilograms')