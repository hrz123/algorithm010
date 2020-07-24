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


# 以下为自我练习
# 子问题
# i， j走到m-1,n-1位置的最小值
# 最后返回0，0的最小值
# 定义状态数组
# f(i, j) = min(f(i+1, j), f(i, j+1)) + grid[i][j]
# 递推方程
# f(i, j) = min(f(i+1, j), f(i, j+1)) + grid[i][j]
# 初始化：
# f(m-1, n-1) = grid[m-1, n-1]
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        h, w = len(grid), len(grid[0])
        dp = grid[h - 1][:]
        for j in range(w - 2, -1, -1):
            dp[j] += dp[j + 1]

        for i in range(h - 2, -1, -1):
            dp[w - 1] += grid[i][w - 1]
            for j in range(w - 2, -1, -1):
                dp[j] = min(dp[j], dp[j + 1]) + grid[i][j]
        return dp[0]


# 定义子问题
# i， j到终点的最小值
# 状态数组
# f(i, j) = min(f(i+1, j), f(i, j+1)) + a[i][j]
# 递推方程
# f(i, j) = min(f(i+1, j), f(i, j+1)) + a[i][j]
# 初始化
# f(m-1, n-1) = a[m-1][n-1]
# 返回值
# f(0,0）
# 优化空间复杂度
# 只需要一个数组
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        h, w = len(grid), len(grid[0])

        dp = grid[h - 1][:]
        for i in range(w - 1, 0, -1):
            dp[i - 1] += dp[i]

        for i in range(h - 2, -1, -1):
            dp[w - 1] += grid[i][w - 1]
            for j in range(w - 2, -1, -1):
                dp[j] = min(dp[j], dp[j + 1]) + grid[i][j]

        return dp[0]


def main():
    sol = Solution()

    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    res = sol.minPathSum(grid)
    print(res)

    grid = [
        [1]
    ]
    res = sol.minPathSum(grid)
    print(res)


if __name__ == '__main__':
    main()
