from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))
        return sum(stack)

# Example usage (for VS Code/local testing)
if __name__ == "__main__":
    sol = Solution()
    print(sol.calPoints(["5","2","C","D","+"]))                # Output: 30
    print(sol.calPoints(["5","-2","4","C","D","9","+","+"]))   # Output: 27
    print(sol.calPoints(["1","C"]))                            # Output: 0
