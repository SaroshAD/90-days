fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)
print(fruits[0])


fruits[3] = "Grapes"

print(fruits)

fruits.append("Orange")

print(fruits)
print(len(fruits))      #it lets you know how many items/elements are in the list

fruits.insert(3, "Pineapple")
print(fruits)


fruits.remove("Banana")    # removes the item by name
print(fruits)


fruits.pop(1)    # removes the item by index
print(fruits)

