def max_area(height):
    max_area = 0
    left = 0
    right = len(height) - 1

    # Loop until the two pointers meet
    while left < right:
        # Calculate the area using the minimum height between the two pointers
        h = min(height[left], height[right])
        w = right - left
        area = h * w

        # Update max_area if a larger area is found
        max_area = max(max_area, area)

        # Move the pointer pointing to the smaller height inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))  # Output: 49
