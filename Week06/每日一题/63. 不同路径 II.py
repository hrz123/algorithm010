# 63. 不同路径 II.py
from functools import lru_cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = {(0, 0): 0} if obstacleGrid[0][0] == 1 else {(0, 0): 1}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if obstacleGrid[i][j] == 1:
                memo[(i, j)] = 0
            else:
                if i > 0 and j > 0:
                    memo[(i, j)] = dp(i - 1, j) + dp(i, j - 1)
                elif i > 0:
                    memo[(i, j)] = dp(i - 1, j)
                else:
                    memo[(i, j)] = dp(i, j - 1)
            return memo[(i, j)]

        return dp(m - 1, n - 1)


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        @lru_cache(None)
        def dp(i, j):
            if not i and not j:
                return 1 - obstacleGrid[0][0]

            if obstacleGrid[i][j] == 1:
                return 0
            else:
                if i >= 1 and j >= 1:
                    return dp(i - 1, j) + dp(i, j - 1)
                elif i >= 1:
                    return dp(i - 1, j)
                else:
                    return dp(i, j - 1)

        return dp(m - 1, n - 1)


def main():
    obstacleGrid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]

    sol = Solution()
    res = sol.uniquePathsWithObstacles(obstacleGrid)
    print(res)


if __name__ == '__main__':
    main()
