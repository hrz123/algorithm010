# 120. 三角形最小路径和.py
from typing import List


# 1. brute-force, 递归，n层：left or right: 2^n

# 2.DP
# a.重复性（分治） problem(i, j) = min(sub(i+1, j), sub(i+1, j+1)) + a[i, j]
# b.定义状态数组：f(i, j)
# c.DP方程：f(i, j) = min(f(i+1, j), f(i+1, j+1)) + a[i, j]
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


def main():
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    triangle = [[1], [2, 3]]
    sol = Solution()
    res = sol.minimumTotal(triangle)
    print(res)


if __name__ == '__main__':
    main()
