def two_sum(values, target):
    seen = {}
    for i, num in enumerate(values):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


nums = [2, 7, 11, 15]
print(two_sum(nums, 9))