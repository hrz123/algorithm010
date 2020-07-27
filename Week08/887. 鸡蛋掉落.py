# 887. 鸡蛋掉落.py
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        _dp = [0] * (N + 1)
        for _ in range(K - 1):
            for j in range(1, N + 1):
                _dp[j] = 1 + min(max(dp[k - 1], _dp[j - k])
                                 for k in range(1, j + 1))
            dp, _dp = _dp, dp
        return dp[N]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[float('inf')] * (N + 1) for _ in range(K + 1)]
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j],
                                   1 + max(dp[i - 1][k - 1], dp[i][j - k]))
        return dp[K][N]


# 时间复杂度：O(kn^2)
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def dfs(i, j):
            if i == 1:
                return j
            if j == 0:
                return 0
            if j == 1:
                return 1
            if (i, j) in d:
                return d[i, j]
            lo, hi = 0, j
            while lo < hi:
                mid = lo + ((hi - lo) >> 1)
                left, right = dfs(i - 1, mid - 1), dfs(i, j - mid)
                if left < right:
                    lo = mid + 1
                else:
                    hi = mid
            res = 1 + max(dfs(i - 1, lo - 1), dfs(i, j - lo))
            d[i, j] = res
            return res

        d = {}
        return dfs(K, N)


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[float('inf')] * (N + 1) for _ in range(K + 1)]
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N + 1):
            dp[1][j] = j

        for i in range(2, K + 1):
            k = 1
            for j in range(2, N + 1):
                while k < j + 1 and dp[i][j - k] > dp[i - 1][k - 1]:
                    k += 1
                dp[i][j] = 1 + dp[i - 1][k - 1]
        return dp[K][N]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = range(N + 1)
        for i in range(2, K + 1):
            k = 1
            ndp = [0, 1] + [float('inf')] * (N - 1)
            for j in range(2, N + 1):
                while k < j + 1 and ndp[j - k] > dp[k - 1]:
                    k += 1
                ndp[j] = 1 + dp[k - 1]
            dp = ndp
        return dp[N]


# 以下为自我练习
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = range(N + 1)
        for i in range(2, K + 1):
            ndp = [0, 1] + [0] * (N - 1)
            k = 1
            for j in range(2, N + 1):
                while k < j + 1 and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = 1 + dp[k - 1]
            dp = ndp
        return dp[N]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = list(range(N + 1))
        ndp = [0, 1] + [0] * (N - 1)
        for i in range(2, K + 1):
            k = 1
            for j in range(2, N + 1):
                while k < j + 1 and dp[k - 1] < ndp[j - k]:
                    k += 1
                ndp[j] = 1 + dp[k - 1]
            dp, ndp = ndp, dp
        return dp[N]


def main():
    sol = Solution()

    K = 4
    N = 5000
    res = sol.superEggDrop(K, N)
    print(res)


if __name__ == '__main__':
    main()
