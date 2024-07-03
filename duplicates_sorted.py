# remove duplicates from a sorted list without using extra memory and extra list

def remove_duplicates(sorted_list):
    if not sorted_list:
        return 0

    write_index = 1

    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[write_index - 1]:
            sorted_list[write_index] = sorted_list[i]
            write_index += 1

    return write_index


nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 10]
unique_nums = remove_duplicates(nums)
print(nums[:unique_nums])
