# this is the simple BMI calculator

print("Welcome to the BMI calculator\n\n")


name = input("what is your name?\n")

weight = float(input("What do you weigh? (in kilos)\n"))

height = float(input("What is your height ? (in meters)\n"))

height2 = height * height

bmi = weight / (height**2)

bmi2 = weight/height2

print(f"{name}'s BMI range is {bmi}\n")


print(f"{name}'s BMI range is {bmi2}")




