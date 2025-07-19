import random

class Solution:

    def __init__(self, n: int, blacklist: list[int]):
        self.bound = n - len(blacklist)
        self.mapping = {}
        black_set = set(blacklist)
        
        # Map blacklisted numbers in range [0, bound) to whitelisted numbers >= bound
        available = iter(x for x in range(self.bound, n) if x not in black_set)
        
        for b in blacklist:
            if b < self.bound:
                self.mapping[b] = next(available)

    def pick(self) -> int:
        x = random.randint(0, self.bound - 1)
        return self.mapping.get(x, x)
