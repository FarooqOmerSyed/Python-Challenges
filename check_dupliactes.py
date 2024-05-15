def check_duplicates(list1):
    for item in list1:
        if item == item:
            return f"{item} is duplicated"
        else:
            return f"no duplicates found"


my_fruits = ["apple", "pear", "orange", "apple", "banana"]

print(check_duplicates(my_fruits))