def findCloseToZero(nums):
    absolute_nums = list(map(abs, nums))
    closestToZero = min(absolute_nums)
    if closestToZero == 0:
        closestToZero += 1

    return closestToZero


nums = [-4, -2, 1, 4, 8]
nums2 = [2, -1, 1]
print(findCloseToZero(nums))
print(findCloseToZero(nums2))