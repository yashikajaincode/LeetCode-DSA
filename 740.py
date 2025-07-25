from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        from collections import Counter

        count = Counter(nums)
        max_num = max(nums)
        dp = [0] * (max_num + 1)

        for i in range(len(dp)):
            dp[i] = count[i] * i

        for i in range(2, len(dp)):
            dp[i] = max(dp[i - 1], dp[i - 2] + dp[i])

        return dp[-1]
