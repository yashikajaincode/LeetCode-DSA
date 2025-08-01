class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_num = max(nums)
        index = nums.index(max_num)
        for i in range(len(nums)):
            if i != index and max_num < 2 * nums[i]:
                return -1
        return index
