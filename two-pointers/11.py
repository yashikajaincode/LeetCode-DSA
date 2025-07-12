def maxArea(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0

    while left < right:
        # Calculate area
        width = right - left
        h = min(height[left], height[right])
        max_water = max(max_water, width * h)

        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example usage:
print(maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
print(maxArea([1,1]))               # Output: 1
