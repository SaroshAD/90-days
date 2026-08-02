def square(a):
    return a**2

a=int(input("Enter a number: "))

result = square(a)
print(f"The square of {a} is {result}")





def circle_area(radius):
    pi = 3.14159
    return pi * radius**2

radius = float(input("Enter the radius of the circle: "))
area = circle_area(radius)
print(f"The area of the circle with radius {radius} is {area}")