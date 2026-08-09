numbers = [10, 20, 30, 40, 50, 60]

for num in numbers:
    if num == 40:
        break
    print(num)

print("\n\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

for i in numbers:
    if i==4:
        continue
    print(i)

print("\n\n")
numbers_1 = [12, 5, 8, 20, 3, 15, 7]

for x in numbers_1:
    if x > 15:
        break
    print(x)


print("\n\n")

sensor_values = [25, 28, 31, 35, 42, 90, 38, 40]

for value in sensor_values:
    if value > 50:
        print("Object detected! Stopping the loop.")
        break
    print("Sensor value:", value)