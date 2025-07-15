class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        answer = []
        low, high = 1, k + 1
        for i in range(k + 1):
            if i % 2 == 0:
                answer.append(low)
                low += 1
            else:
                answer.append(high)
                high -= 1
        for i in range(k + 2, n + 1):
            answer.append(i)
        return answer
