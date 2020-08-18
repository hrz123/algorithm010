# 64. 最小路径和.py
from typing import List


# 定义子问题
# 到第i,j位置的最小数字总和
# 返回m-1,n-1位置
# 定义状态数组dp(start, j)
# 可以一层一层的推
# f(start, j) = min(f(start+1, j), f(start, j+1)) + a[start][j]
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
# start， j走到m-1,n-1位置的最小值
# 最后返回0，0的最小值
# 定义状态数组
# f(start, j) = min(f(start+1, j), f(start, j+1)) + grid[start][j]
# 递推方程
# f(start, j) = min(f(start+1, j), f(start, j+1)) + grid[start][j]
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
# start， j到终点的最小值
# 状态数组
# f(start, j) = min(f(start+1, j), f(start, j+1)) + a[start][j]
# 递推方程
# f(start, j) = min(f(start+1, j), f(start, j+1)) + a[start][j]
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


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = grid[m - 1][:]
        for j in range(n - 2, -1, -1):
            dp[j] += dp[j + 1]
        for i in range(m - 2, -1, -1):
            dp[n - 1] += grid[i][n - 1]
            for j in range(n - 2, -1, -1):
                dp[j] = min(dp[j], dp[j + 1]) + grid[i][j]
        return dp[0]


# f(i, j) = min(f(i+1, j), f(i, j+1)) + m[i][j]
# 初始化
# 我们尽量使用哨兵初始化
# 我们初始化为 [float('inf')] * (n-1) + [0, float('inf')]
# 这样最后一层经过递推方程
# 没问题
# 返回值
# 优化复杂度
# 一维数组原地
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * (n - 1) + [0, float('inf')]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[j] = min(dp[j], dp[j + 1]) + grid[i][j]
        return dp[0]


# f(i, j)为到达i， j的最小路径和
# f(i, j) = min(f(i-1, j), f(i, j-1)) + a[i][j]
# 初始化和边界条件
# f(0, 0) = a[0][0]
# 我们可以加一层全正无穷的哨兵，但是第一个位置是0，因为取的是最小值，也符合递推公式
# 返回值f(m, n)
# 优化复杂度
# 我们可以用一维数组，从左到右原地更新
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = [0] + [float('inf')] * n
        for i in range(m):
            for j in range(n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[n - 1]


# f(i, j) = min(f(i-1,j), f(i, j-1)) + a
# 初始化和边界条件
# 我们可以初始化第一列
# 也可以初始化一个哨兵
# 不初始化哨兵的话，第一行就是一个前缀和
# 返回值f(m-1, n-1）
# 优化复杂度
# 我们从左往右可以原地更新
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dp = []
        p = 0
        for num in grid[0]:
            p += num
            dp.append(p)
        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[n - 1]


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
