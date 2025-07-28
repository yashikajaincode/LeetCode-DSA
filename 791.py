class Solution:
    def customSortString(self, order: str, s: str) -> str:
        from collections import Counter

        count = Counter(s)
        result = []

        for ch in order:
            if ch in count:
                result.append(ch * count[ch])
                del count[ch]

        for ch in count:
            result.append(ch * count[ch])

        return ''.join(result)
