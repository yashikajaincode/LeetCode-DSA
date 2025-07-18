from typing import List

class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        intervals = []
        result = []
        max_height = 0

        for left, size in positions:
            right = left + size
            base_height = 0

            for l, r, h in intervals:
                if l < right and r > left:  # overlapping range
                    base_height = max(base_height, h)

            new_height = base_height + size
            intervals.append((left, right, new_height))
            max_height = max(max_height, new_height)
            result.append(max_height)

        return result
