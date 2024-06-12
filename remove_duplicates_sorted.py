def remove_duplicates_sorted_list(arr):
    if len(arr) == 0:
        return 0

    write_index = 1

    for i in range(1, len(arr)):
        if arr[i] != arr[write_index - 1]:
            arr[write_index] = arr[i]
            write_index += 1

    return write_index, arr[:write_index]

# Sorted list with duplicates
sorted_list = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8]

print("Original sorted list with duplicates:", sorted_list)

new_length, result = remove_duplicates_sorted_list(sorted_list)

print("List after removing duplicates:", result)
print("Length of list after removing duplicates:", new_length)
