# 486. 预测赢家.py
from typing import List


# f(i, j, 0) = max(f(i+1, j, 1) + a[i[, f(i, j-1, 1) +a[j])
# f(i, j, 1) = f(i+1, j, 0), f(i, j-1, 0)
# f(i, i, 0) = nums[i]
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i][0] = nums[i]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                left = dp[i + 1][j][1] + nums[i]
                right = dp[i][j - 1][1] + nums[j]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
        return dp[0][n - 1][0] >= dp[0][n - 1][1]


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[[nums[i], 0] for i in range(n)] for _ in range(n)]
        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap
                left = dp[i + 1][j][1] + nums[i]
                right = dp[i][j - 1][1] + nums[j]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
        return dp[0][n - 1][0] >= dp[0][n - 1][1]


def main():
    pass


if __name__ == '__main__':
    main()
