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
