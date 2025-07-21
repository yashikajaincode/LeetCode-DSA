class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def is_self_dividing(n):
            for digit in str(n):
                if digit == '0' or n % int(digit) != 0:
                    return False
            return True
        
        return [i for i in range(left, right + 1) if is_self_dividing(i)]
