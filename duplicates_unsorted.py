def remove_duplicates(unsorted_list):
    if not unsorted_list:
        return 0

    write_index = 1

    for i in range(1, len(unsorted_list)):
        if unsorted_list[i] not in unsorted_list[:write_index]:
            unsorted_list[write_index] = unsorted_list[i]
            write_index += 1

    return write_index


# Example usage
my_unsorted_list = [3, 1, 1, 4, 6, 2, 4, 4, 2, 5, 5]
unique_count = remove_duplicates(my_unsorted_list)
print(my_unsorted_list[:unique_count])
