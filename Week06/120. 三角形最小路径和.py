# 120. 三角形最小路径和.py
from typing import List


# 1. brute-force, 递归，n层：r or r: 2^n

# 2.DP
# a.重复性（分治） problem(start, j) = min(sub(start+1, j), sub(start+1, j+1)) + a[start, j]
# b.定义状态数组：f(start, j)
# c.DP方程：f(start, j) = min(f(start+1, j), f(start+1, j+1)) + a[start, j]
#   初始状态： f(n-1, j) = a[n-1, j]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j],
                                      triangle[i + 1][j + 1])
        return triangle[0][0]


# 改变参数数组，不建议在工业级代码中使用

# 不改变原数组，并且使用O(N)空间
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[n - 1][:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


# 以下为自我练习
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        n = len(triangle)
        dp = triangle[n - 1][:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


# 子问题
# 定义状态数组：f(start, j) = min(f(start+1, j), f(start+1, j+1)) + a[start,j]
# 返回f(0, 0)
# 递推方程
# f(start, j) = min(f(start+1, j), f(start+1, j+1)) + a[start,j]
# 初始状态
# f(n-1, j) = a[n-1, j]
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[n - 1][:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


# 定义子问题
# 到这一层的所有结点的最小路径和
# 定义状态数组f(start,j) start 0..h-1 j 0..w-1
# 递推方程
# f(start, j) = min(f(start+1, j), f(start+1, j+1)) + a[start][j]
# 初始化
# f(h-1, j) = a(h-1, j)
# 返回值f(0,0）
# 优化空间复杂度
# 可以只使用最后一层，从左往右递推可以原地改变值
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[n - 1][:]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[n - 1][:]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


# 定义子问题
# i,j到下的最小路径和
# f(i, j) = min(f(i+1, j), f(i+1, j+1)) +a[i][j]
# 初始化
# 初始化为最后一层的值
# 返回值f(0, 0)
# 优化复杂度
# 从左到右原地更新
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = triangle[n - 1][:]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


# f(i, j)定义为i, j的最小路径和
# f(i,j) = min(f(i+1, j), f(i+1, j+1)) +a[i][j]
# 初始化
# 最后一层就是自己，可以用自身初始化
# 返回值f(0, 0)
# 优化复杂度
# 可以用一维数组，从左到右原地更新
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


def main():
    sol = Solution()
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    res = sol.minimumTotal(triangle)
    print(res)

    triangle = [[1], [2, 3]]
    res = sol.minimumTotal(triangle)
    print(res)


if __name__ == '__main__':
    main()
