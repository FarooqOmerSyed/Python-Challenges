def max_subarray(nums):
    max_sum = nums[0]  # Initialize max_sum to first element
    current_sum = nums[0]  # Initialize current_sum to first element

    # Iterate from second element since we've already initialized our sums
    for i in range(1, len(nums)):
        # Check whether to start a new subarray or extend the existing one
        current_sum = max(nums[i], current_sum + nums[i])
        # Update the maximum sum if the current sum is greater
        max_sum = max(max_sum, current_sum)

    return max_sum


# Test the function
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))  # Output: 6
