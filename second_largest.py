def second_largest(my_list):
    sorted_list = sorted(my_list)
    return sorted_list[-2]


print(second_largest([8, 1, 3, 6, 2, 4, 5, 7]))