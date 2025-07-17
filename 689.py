from typing import List


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sum_k = [0] * (n - k + 1)
        curr = sum(nums[:k])
        sum_k[0] = curr
        for i in range(1, n - k + 1):
            curr = curr - nums[i - 1] + nums[i + k - 1]
            sum_k[i] = curr

        left = [0] * len(sum_k)
        max_idx = 0
        for i in range(len(sum_k)):
            if sum_k[i] > sum_k[max_idx]:
                max_idx = i
            left[i] = max_idx

        right = [0] * len(sum_k)
        max_idx = len(sum_k) - 1
        for i in reversed(range(len(sum_k))):
            if sum_k[i] >= sum_k[max_idx]:
                max_idx = i
            right[i] = max_idx

        max_total = 0
        res = []
        for j in range(k, len(sum_k) - k):
            i = left[j - k]
            l = right[j + k]
            total = sum_k[i] + sum_k[j] + sum_k[l]
            if total > max_total:
                max_total = total
                res = [i, j, l]
        return res
