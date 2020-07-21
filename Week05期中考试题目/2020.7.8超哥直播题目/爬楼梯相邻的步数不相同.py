# 爬楼梯不相同.py
from functools import lru_cache
from typing import List


# 爬楼梯，可以走steps里面的步数，相邻两步不相同
class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> int:
        @lru_cache(None)
        def recur(n, cur_step):
            if n < 0:
                return 0
            if n == 0:
                return 1
            return sum([recur(n - step, step) for step in steps if step !=
                        cur_step])

        return recur(n, 0)


# 循环
# dp[i][j]表示走到i步，且到这步走了steps[j]步
# 那么dp[i][j] = sum(dp[i - steps[j]][k]) k != j
# 起始条件是
# dp[steps[j]][j] = 1, j从0到ns - 1
# dp[负数][j] = 0
class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> int:
        ns = len(steps)
        dp = [[0 for _ in range(ns)] for _ in range(n + 1)]

        for i in range(n + 1):
            for j in range(ns):
                dp[i][j] = 1 if i == steps[j] else \
                    sum(dp[i - steps[j]][k] for k in range(ns)
                        if k != j and i >= steps[j])

        return sum(dp[n])


def main():
    n = 5
    steps = [1, 2, 3]

    sol = Solution()
    res = sol.climbStairs(n, steps)
    print(res)


if __name__ == '__main__':
    main()
