class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zeta(x):
            res = 0
            while x > 0:
                x //= 5
                res += x
            return res

        def left_bound(k):
            low, high = 0, 5 * (k + 1)
            while low < high:
                mid = (low + high) // 2
                if zeta(mid) < k:
                    low = mid + 1
                else:
                    high = mid
            return low

        def right_bound(k):
            low, high = 0, 5 * (k + 1)
            while low < high:
                mid = (low + high) // 2
                if zeta(mid) <= k:
                    low = mid + 1
                else:
                    high = mid
            return low

        return right_bound(k) - left_bound(k)
