# 64. 最小路径和.py
from typing import List


# 定义子问题
# 到第i,j位置的最小数字总和
# 返回m-1,n-1位置
# 定义状态数组dp(i, j)
# 可以一层一层的推
# f(i, j) = min(f(i+1, j), f(i, j+1)) + a[i][j]
# 递推方程
# 初始状态
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])

        dp = grid[m - 1][:]
        for i in range(n - 2, -1, -1):
            dp[i] += dp[i + 1]

        for i in range(m - 2, -1, -1):
            dp[n - 1] += grid[i][n - 1]
            for j in range(n - 2, -1, -1):
                dp[j] = min(dp[j], dp[j + 1]) + grid[i][j]

        return dp[0]


def main():
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    sol = Solution()
    res = sol.minPathSum(grid)
    print(res)


if __name__ == '__main__':
    main()
