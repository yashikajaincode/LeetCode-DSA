class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask |= (1 << i)
            found_prefixes = {num & mask for num in nums}
            candidate = max_xor | (1 << i)
            if any((candidate ^ p) in found_prefixes for p in found_prefixes):
                max_xor = candidate
        return max_xor
