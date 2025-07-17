from typing import List
from collections import Counter
from functools import lru_cache

class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        m = len(stickers)
        sticker_counts = [Counter(sticker) for sticker in stickers]
        target_count = Counter(target)

        # Early pruning: if any char in target is not in any sticker, return -1
        available_chars = set()
        for sc in sticker_counts:
            available_chars |= set(sc.keys())
        if not set(target).issubset(available_chars):
            return -1

        @lru_cache(None)
        def dp(remain):
            if not remain:
                return 0
            remain_count = Counter(remain)
            res = float('inf')
            for sc in sticker_counts:
                if remain[0] not in sc:
                    continue
                new_remain = ''
                for c in remain_count:
                    left = remain_count[c] - sc.get(c, 0)
                    if left > 0:
                        new_remain += c * left
                res = min(res, 1 + dp(new_remain))
            return res if res != float('inf') else -1

        return dp(target)
