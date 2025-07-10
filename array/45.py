def jump(nums):
    jumps = 0
    curr_end = 0
    farthest = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == curr_end:
            jumps += 1
            curr_end = farthest

    return jumps

# Example usage
nums = [2, 3, 1, 1, 4]
print(jump(nums))
