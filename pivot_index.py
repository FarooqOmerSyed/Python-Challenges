def pivotIndex(nums):
    left, right = 0, sum(nums)
    for i, x in enumerate(nums):
        right -= x
        if left == right:
            return i
        left += x
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))