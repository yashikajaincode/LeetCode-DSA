from collections import Counter

class Solution:
    def numRabbits(self, answers: list[int]) -> int:
        count = Counter(answers)
        total = 0
        for x, freq in count.items():
            group_size = x + 1
            groups = (freq + x) // group_size
            total += groups * group_size
        return total
