import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []

        # Initialize min heap with the smallest fractions for each denominator
        for j in range(1, n):
            heapq.heappush(heap, (arr[0] / arr[j], 0, j))

        # Pop the smallest fraction k-1 times
        for _ in range(k - 1):
            frac, i, j = heapq.heappop(heap)
            if i + 1 < j:
                heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))

        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]
