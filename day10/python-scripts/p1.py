robot=["Robo", 4, 12.5, True]
print(robot)
print(robot[0])
print(robot[-1])
print(robot[3])
robot[1] = 6
print(robot)

robot.append("ESP32")
print(robot)
robot.pop()
print(robot)

robot.pop(1)
print(robot)