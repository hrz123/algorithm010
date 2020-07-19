# 312. 戳气球.py
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] +
                                   dp[k][j] +
                                   nums[i] * nums[j] * nums[k])
        return dp[0][n - 1]


def main():
    sol = Solution()

    nums = [3, 1, 5, 8]
    res = sol.maxCoins(nums)
    print(res)


if __name__ == '__main__':
    main()
