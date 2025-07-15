class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last = {int(x): i for i, x in enumerate(digits)}
        
        for i, x in enumerate(digits):
            for d in range(9, int(x), -1):
                if last.get(d, -1) > i:
                    digits[i], digits[last[d]] = digits[last[d]], digits[i]
                    return int("".join(digits))
        return num
