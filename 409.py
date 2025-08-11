class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        counts = Counter(s)
        length = 0
        odd_found = False
        
        for count in counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True
        
        if odd_found:
            length += 1
        return length
