import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_freq = max(count.values())
        
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        # Max heap by frequency
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        
        res = []
        prev_freq, prev_char = 0, ''
        
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            res.append(char)
            
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))
            
            prev_freq, prev_char = freq + 1, char  # use one occurrence
        
        return ''.join(res)
