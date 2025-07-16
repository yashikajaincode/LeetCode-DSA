from typing import List
from itertools import permutations
import math

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def helper(nums):
            if len(nums) == 1:
                return math.isclose(nums[0], 24, rel_tol=1e-6)
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i != j:
                        remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
                        for op in ops:
                            if op == '+' or op == '*':
                                if i > j:  # skip duplicates for commutative ops
                                    continue
                            if op == '+':
                                result = nums[i] + nums[j]
                            elif op == '-':
                                result = nums[i] - nums[j]
                            elif op == '*':
                                result = nums[i] * nums[j]
                            elif op == '/':
                                if nums[j] == 0:
                                    continue
                                result = nums[i] / nums[j]
                            if helper(remaining + [result]):
                                return True
            return False

        ops = ['+', '-', '*', '/']
        for perm in permutations(cards):
            if helper(list(perm)):
                return True
        return False

# Example usage (for VS Code/local testing)
if __name__ == "__main__":
    sol = Solution()
    print(sol.judgePoint24([4, 1, 8, 7]))  # True
    print(sol.judgePoint24([1, 2, 1, 2]))  # False
