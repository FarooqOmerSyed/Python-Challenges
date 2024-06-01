def moveZeroes(list1):
    zero_count = 0

    for i in range(len(list1)):
        if list1[i] != 0:
            list1[i], list1[zero_count] = list1[zero_count], list1[i]
            zero_count += 1


# Test the function
nums = [0, 1, 0, 3, 12, 0, 4, 5, 0]
moveZeroes(nums)
print(nums)