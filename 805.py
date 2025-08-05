class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        from functools import lru_cache
        
        n = len(nums)
        total_sum = sum(nums)
        nums.sort()
        
        @lru_cache(None)
        def dfs(k, target, i):
            if k == 0:
                return target == 0
            if i >= n or k < 0 or target < 0:
                return False
            if dfs(k - 1, target - nums[i], i + 1):
                return True
            return dfs(k, target, i + 1)
        
        for k in range(1, n // 2 + 1):
            if (total_sum * k) % n == 0:
                target = (total_sum * k) // n
                if dfs(k, target, 0):
                    return True
        return False
