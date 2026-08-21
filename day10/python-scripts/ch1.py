sensor_values = [45, 12, 78, 23, 9, 56, 31]

sensor_values.append(100)
print(sensor_values)

sensor_values.pop()
print(sensor_values)

sensor_values.sort()
print("Final sensor values:", sensor_values)

high_values = [n for n in sensor_values if n > 40]
print("High values:", high_values)

sensor_tuple = tuple(n for n in sensor_values)

print("Sensor tuple:", sensor_tuple)