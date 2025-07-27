class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0', '1', '2', '5', '6', '8', '9'}
        rotated = {'2', '5', '6', '9'}
        count = 0

        for num in range(1, n + 1):
            s = str(num)
            if all(ch in valid for ch in s) and any(ch in rotated for ch in s):
                count += 1

        return count
