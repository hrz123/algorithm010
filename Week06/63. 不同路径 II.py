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
# f(start, j) = f(start+1, j) + f(start, j+1) if a[start,j] == 0
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


# 定义子问题
# f(start, j)
# f(start, j) = f(start +1, j) + f(start, j+1) if m(start, j) !+ 1
#         = 0                      else
# 初始化
# f(h-1, w-1) = 1
# 返回值
# f(0, 0)
# 优化空间复杂度
# 可以只使用行和列中较小的那一个，但是不太方便写代码，就用有多少列吧
# 原地改变自值即可
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[h - 1][w - 1]:
            return 0

        dp = [0] * (w - 1) + [1]
        for j in range(w - 2, -1, -1):
            if obstacleGrid[h - 1][j]:
                dp[j] = 0
            else:
                dp[j] = dp[j + 1]

        for i in range(h - 2, -1, -1):
            dp[w - 1] = 0 if obstacleGrid[i][w - 1] else dp[w - 1]
            for j in range(w - 2, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j + 1]
        return dp[0]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        h, w = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[h - 1][w - 1]:
            return 0
        dp = [1] * w
        for j in range(w - 2, -1, -1):
            dp[j] = 0 if obstacleGrid[h - 1][j] else dp[j + 1]
        for i in range(h - 2, -1, -1):
            if obstacleGrid[i][w - 1]:
                dp[w - 1] = 0
            for j in range(w - 2, -1, -1):
                if obstacleGrid[i][j]:
                    dp[j] = 0
                else:
                    dp[j] += dp[j + 1]
        return dp[0]


# f(i, j) =f(i-1, j) + f(i, j-1) if m[i][j] == 0
#          0   else
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0
        dp = [0, 1] + [0] * (n - 1)
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    dp[j + 1] = 0
                else:
                    dp[j + 1] += dp[j]
        return dp[n]


# 定义子问题
# 到达i， j f(i,j)有多少种走法
# f(i, j) = f(i-1, j) +f(i, j-1) if a[i][j] == 0  else 0
# 初始化和边界条件
# f(0, j) = 1 if 前面都是0 0 如果前面有一个1
# 有点麻烦
# 我们加一层哨兵试试
# 加一层[1, 0...0]的哨兵可以
# 返回值
# f(m, n)
# 优化复杂度
# 可以使用一维数组，从左到右原地更新
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        return dp[n - 1]


# 定义
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(n):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j] + dp[j - 1]
        return dp[n - 1]


# 滚动数组思想
def main():
    sol = Solution()

    matrix = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    res = sol.uniquePathsWithObstacles(matrix)
    print(res)

    matrix = [[1]]
    res = sol.uniquePathsWithObstacles(matrix)
    print(res)


if __name__ == '__main__':
    main()
