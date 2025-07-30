class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        def count(bound):
            res = cur = 0
            for num in nums:
                if num <= bound:
                    cur += 1
                else:
                    cur = 0
                res += cur
            return res

        return count(right) - count(left - 1)
