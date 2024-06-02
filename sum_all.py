def sum_all(*args):
    result = 0
    for arg in args:
        result += sum(arg) if isinstance(arg, (list, tuple)) else arg

    return result


my_tuple = (1, 2, 3, 4, 5)
my_list = [1, 2, 3, 4]

print(sum_all(my_tuple))
print(sum_all(my_list))