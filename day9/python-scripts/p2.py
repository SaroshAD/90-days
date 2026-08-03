shop_list = []
n = int(input("How many items do you want to add to the list? "))
i = 0
def add_item():

    global i
    while i < n:

        shop_list.append(input("Enter the item to add: "))
        i+=1
        print("Adding item to the list")
    print("Your shopping list is: ", shop_list)


add_item()