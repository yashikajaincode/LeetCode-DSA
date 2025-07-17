class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        times = -(-len(b) // len(a))  # ceil division
        for i in range(3):
            if b in a * (times + i):
                return times + i
        return -1
