from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        def countPairs(max_dist):
            count = left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > max_dist:
                    left += 1
                count += right - left
            return count

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if countPairs(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
