from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        count = defaultdict(int)
        first_index = {}
        last_index = {}
        degree = 0

        for i, num in enumerate(nums):
            count[num] += 1
            if num not in first_index:
                first_index[num] = i
            last_index[num] = i
            degree = max(degree, count[num])

        min_length = float('inf')
        for num in count:
            if count[num] == degree:
                min_length = min(min_length, last_index[num] - first_index[num] + 1)

        return min_length
