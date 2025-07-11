def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n

    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]

    return answer

# Example usage:
if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    nums2 = [-1, 1, 0, -3, 3]
    print(productExceptSelf(nums1))  # Output: [24, 12, 8, 6]
    print(productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]
