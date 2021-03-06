# 爬楼梯steps.py
# 爬楼梯，可以走steps里面的步数
from functools import lru_cache
from typing import List


# dp
# dp(m) = sum{dp(m - step)}
# 起始条件
# dp(0) = 1
# dp(负数) = 0
class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> int:
        @lru_cache(None)
        def recur(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            return sum([recur(n - step) for step in steps])

        return recur(n)


# 循环
class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, n + 1):
            dp[i] = sum([dp[i - step] for step in steps if i >= step])

        return dp[n]


class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> int:
        dp = [1] + [0] * n

        for i in range(1, n + 1):
            dp[i] = sum(dp[i - c] if i >= c else 0 for c in steps)
        return dp[n]


def main():
    n = 3
    steps = [1, 2]

    sol = Solution()
    res = sol.climbStairs(n, steps)
    print(res)


if __name__ == '__main__':
    main()
