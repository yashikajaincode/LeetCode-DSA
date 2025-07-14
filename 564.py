class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set()

        # Edge cases like 100..001 and 999..999
        candidates.add(str(10**length + 1))
        candidates.add(str(10**(length - 1) - 1))

        prefix = int(n[:(length + 1) // 2])
        for i in [-1, 0, 1]:
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidate = new_prefix + new_prefix[::-1]
            else:
                candidate = new_prefix + new_prefix[:-1][::-1]
            candidates.add(candidate)

        candidates.discard(n)

        def diff(x):
            return abs(int(x) - int(n)), int(x)

        return min(candidates, key=diff)
