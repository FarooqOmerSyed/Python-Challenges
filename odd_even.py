def odd_even(nums):
    max_even = []
    max_odd = []
    for num in nums:
        if num % 2 == 0:
            max_even.append(num)

        else:
            max_odd.append(num)

    return max(max_even) - min(max_odd)


print(odd_even([1, 2, 4, 6]))