# 63. 不同路径 II.py
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        obstacleGrid[m - 1][n - 1] = 0 if obstacleGrid[m - 1][n - 1] else 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    if i == m - 1:
                        obstacleGrid[i][j] = obstacleGrid[i][j + 1]
                    elif j == n - 1:
                        obstacleGrid[i][j] = obstacleGrid[i + 1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i + 1][j] + \
                                             obstacleGrid[i][j + 1]

        return obstacleGrid[0][0]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])

        dp = [0] * n
        dp[0] = 1
        for row in obstacleGrid:
            for j in range(n):
                if row[j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j - 1]
        return dp[n - 1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[h - 1][w - 1]:
            return 0

        dp = [0] * w
        dp[w - 1] = 1
        for i in range(h - 1, -1, -1):
            for j in range(w - 1, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                elif j != w - 1:
                    dp[j] += dp[j + 1]

        return dp[0]


# 子问题
# 定义状态数组
# f(i, j) = f(i+1, j) + f(i, j+1) if a[i,j] == 0
#         = 0                     else
# 递推方程
# 初始化
# f(m-1, n-1) = 1
# 返回值
# f(0, 0)
# 优化空间，可以使用m,n中较小值为长度的数组，但是写起来不方便
# 可以用全部是0只有结尾是1的数组初始化
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[h - 1][w - 1]:
            return 0
        dp = [0] * (w - 1) + [1]
        for i in range(h - 1, -1, -1):
            if obstacleGrid[i][w - 1]:
                dp[w - 1] = 0
            for j in range(w - 2, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j + 1]
        return dp[0]


def main():
    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    # matrix = [[1]]
    sol = Solution()
    res = sol.uniquePathsWithObstacles(matrix)
    print(res)


if __name__ == '__main__':
    main()
