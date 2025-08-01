from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        license_count = Counter(c.lower() for c in licensePlate if c.isalpha())
        res = None

        for word in words:
            word_count = Counter(word)
            if all(word_count[c] >= license_count[c] for c in license_count):
                if res is None or len(word) < len(res):
                    res = word

        return res
