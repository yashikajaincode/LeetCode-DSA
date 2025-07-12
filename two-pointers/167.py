def twoSum(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

# Example usage:
print(twoSum([2, 7, 11, 15], 9))    # [1, 2]
print(twoSum([2, 3, 4], 6))         # [1, 3]
print(twoSum([-1, 0], -1))          # [1, 2]
