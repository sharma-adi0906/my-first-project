shopping_list = ["Milk", "eggs", "bread", "jam", "coffee"]

item_to_find = "jam"
found_at = None

#index in range (6)

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break

print("item found at = {}".format(found_at + 1))