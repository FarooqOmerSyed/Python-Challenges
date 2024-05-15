def convert_add(*my_string):
    my_list = [int(x) for x in my_string]
    sum_it = sum(my_list)
    return sum_it


print(convert_add('1', '2', '3', '4'))