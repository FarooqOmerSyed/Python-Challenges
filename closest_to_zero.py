def closetozero(nums):
    closest = nums[0]

    for x in nums:
        if abs(x) < abs(closest):
            closest = x

    if closest < 0 and abs(closest) in nums:
        return abs(closest)
    else:
        return closest


print(closetozero([2, -1, 1]))
