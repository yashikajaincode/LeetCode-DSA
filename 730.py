class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[[0] * 4 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i][ord(s[i]) - ord('a')] = 1

        for size in range(2, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                for k in range(4):
                    c = chr(ord('a') + k)
                    if s[i] != c:
                        dp[i][j][k] = dp[i + 1][j][k]
                    elif s[j] != c:
                        dp[i][j][k] = dp[i][j - 1][k]
                    else:
                        if i + 1 > j - 1:
                            dp[i][j][k] = 2
                        else:
                            dp[i][j][k] = 2
                            for m in range(4):
                                dp[i][j][k] += dp[i + 1][j - 1][m]
                        dp[i][j][k] %= MOD

        return sum(dp[0][n - 1]) % MOD
