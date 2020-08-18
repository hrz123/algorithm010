from collections import deque


class Solution:
    def minDays(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            if not i & 1:
                dp[i] = min(dp[i], dp[i >> 1] + 1)
            if not i % 3:
                dp[i] = min(dp[i], dp[i // 3] + 1)
        return dp[n]


# 爆内存
class Solution:
    import functools
    @functools.lru_cache(None)
    def minDays(self, n: int) -> int:
        if n <= 1:
            return n
        res = self.minDays(n - 1) + 1
        if n % 3 == 0:
            res = min(res, self.minDays(n // 3) + 1)
        if not n & 1:
            res = min(res, self.minDays(n >> 1) + 1)
        return res


# 最坏O(n)的，但是可能变成log(n)的
class Solution:
    def minDays(self, n: int) -> int:
        q = deque([n])
        d = dict()
        d[n] = 0
        while 0 not in d:
            v = q.popleft()
            if v % 3 == 0 and v // 3 not in d:
                d[v // 3] = d[v] + 1
                q.append(v // 3)
            if v % 2 == 0 and v // 2 not in d:
                d[v // 2] = d[v] + 1
                q.append(v // 2)
            if v - 1 not in d:
                d[v - 1] = d[v] + 1
                q.append(v - 1)
        return d[0]


def main():
    sol = Solution()
    res = sol.minDays(1000000)
    print(res)


if __name__ == '__main__':
    main()
