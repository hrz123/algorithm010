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


# 迭代的写法
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0

        dp = [1] * n
        j = 0
        while j < n:
            if obstacleGrid[0][j] == 1:
                break
            j += 1
        while j < n:
            dp[j] = 0
            j += 1

        for i in range(1, m):
            dp_ = [0] * n
            dp_[0] = dp[0] if obstacleGrid[i][0] == 0 else 0
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp_[j] = 0
                else:
                    dp_[j] = dp_[j - 1] + dp[j]
            dp = dp_

        return dp[n - 1]


# 思路是给左面和上面各加一个障碍边，这样不用对边界做判断。
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 列、行
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        # 最后一个位置永远是0
        # 起始位置的路径数为1
        dp = [1] + [0] * m
        for i in range(n):
            for j in range(m):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        return dp[m - 1]


def main():
    obstacleGrid = [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]

    sol = Solution()
    res = sol.uniquePathsWithObstacles(obstacleGrid)
    print(res)


if __name__ == '__main__':
    main()
