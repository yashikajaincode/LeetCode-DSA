def threeSum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    n = len(nums)

    for i in range(n - 2):
        # Skip duplicate values for i
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1
        while left < right:
            s = nums[i] + nums[left] + nums[right]
            if s == 0:
                res.append([nums[i], nums[left], nums[right]])
                # Skip duplicates for left and right
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                # Move pointers inward
                left += 1
                right -= 1
            elif s < 0:
                left += 1
            else:
                right -= 1

    return res

# Example usage:
print(threeSum([-1,0,1,2,-1,-4]))  # [[-1, -1, 2], [-1, 0, 1]]
print(threeSum([0,1,1]))           # []
print(threeSum([0,0,0]))           # [[0, 0, 0]]
