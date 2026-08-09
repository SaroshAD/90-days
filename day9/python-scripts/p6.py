def add_numbers(*args):
    sum = 0
    for num in args:
        sum+=num

    return sum

print(add_numbers(10, 20, 30))

print("\n\n")

print(add_numbers(5, 10, 15, 20))





def find_largest(*args):
    largest = args[0]
    for i in args:
        if i > largest:
            largest = i
    return largest


print(find_largest(10, 45, 23, 67, 12))