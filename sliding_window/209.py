def minSubArrayLen(target, nums):
    n = len(nums)
    left = 0
    total = 0
    min_len = float('inf')

    for right in range(n):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return 0 if min_len == float('inf') else min_len

# Example usage
print(minSubArrayLen(7, [2,3,1,2,4,3]))  # Output: 2
print(minSubArrayLen(4, [1,4,4]))        # Output: 1
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))  # Output: 0
