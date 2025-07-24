from collections import Counter
from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sorted_arr = sorted(arr)
        count1 = Counter()
        count2 = Counter()
        chunks = 0

        for i in range(len(arr)):
            count1[arr[i]] += 1
            count2[sorted_arr[i]] += 1
            if count1 == count2:
                chunks += 1

        return chunks
