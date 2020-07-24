# 爬楼梯组合数.py
from typing import List


class Solution:
    def climbStairs(self, n: int, steps: List[int]) -> int:
        dp = [1] + [0] * n

        for c in steps:
            for i in range(1, n + 1):
                if i >= c:
                    dp[i] += dp[i - c]
        return dp[n]


def main():
    sol = Solution()

    n = 4
    steps = [1, 2]
    res = sol.climbStairs(n, steps)
    print(res)


if __name__ == '__main__':
    main()
