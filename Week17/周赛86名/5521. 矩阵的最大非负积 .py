# 5521. 矩阵的最大非负积 .py
from typing import List


# if a(i, j) > 0

# f(i, j, 0) = max(f(i - 1, j, 0) * a, f(i, j - 1, 0) * a)
# f(i, j, 1) = min(f(i - 1, j, 1) * a, f(i, j - 1, 1) * a)


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        row, col = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(col)] for _ in range(row)]
        zero_exist = False
        for hang in grid:
            for e in hang:
                if e == 0:
                    zero_exist = True
                    break

        pre = 1
        for j in range(col):
            pre *= grid[0][j]
            if pre >= 0:
                dp[0][j][0] = pre
            else:
                dp[0][j][1] = pre
        pre = 1
        for i in range(row):
            pre *= grid[i][0]
            if pre >= 0:
                dp[i][0][0] = pre
            else:
                dp[i][0][1] = pre

        for i in range(1, row):
            for j in range(1, col):
                t = grid[i][j]
                if t >= 0:
                    dp[i][j][0] = max(dp[i - 1][j][0] * t, dp[i][j - 1][0] * t)
                    dp[i][j][1] = min(dp[i - 1][j][1] * t, dp[i][j - 1][1] * t)
                else:
                    dp[i][j][0] = max(dp[i - 1][j][1] * t, dp[i][j - 1][1] * t)
                    dp[i][j][1] = min(dp[i - 1][j][0] * t, dp[i][j - 1][0] * t)
        if dp[row - 1][col - 1][0] == 0:
            if zero_exist:
                return 0
            else:
                return -1
        return dp[row - 1][col - 1][0] % mod


def main():
    sol = Solution()
    grid = [[-1, -2, -3],
            [-2, -3, -3],
            [-3, -3, -2]]
    res = sol.maxProductPath(grid)
    print(res)


if __name__ == '__main__':
    main()
