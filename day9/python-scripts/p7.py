# kwargs

def student_info(**kwargs):
    for key, value, in kwargs.items():
        print(f"{key}: {value}")
def count_settings(**kwargs):
    count = 0
    for key, value in kwargs.items():
        count += 1
    return count

def robot_config(**kwargs):
    print("\nRobot Configuration:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name = "Sarosh Adurkar", branch = "Mechatronics", year = 4)


print(count_settings(speed=100, direction="forward", mode="auto"))


robot_config(speed=100, direction="forward", mode="autonomous")





def robot_status(**kwargs):
    print("\nRobot Status:")
    for key, value in kwargs.items():
        print(f"{key}= {value}")


robot_status(
    speed=120,
    direction="forward",
    battery=85,
    mode="autonomous"
)