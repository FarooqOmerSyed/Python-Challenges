def flatten_list(my_list):
    result = []

    def flatten(lst):
        for item in lst:
            if isinstance(item, list):
                flatten(item)
            else:
                result.append(item)

    flatten(my_list)
    return result


# Example
nested_list = [[1, 2, [3]], 4, [5, 6]]
flattened_list = flatten_list(nested_list)
print(flattened_list)
