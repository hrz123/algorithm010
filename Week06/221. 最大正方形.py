# 221. 最大正方形.py
from typing import List


# 定义子问题
# 到i, j位置的最大正方形面积的边长，返回m-1, n-1,必须包含i，j
# 定义状态数组
# dp[i][j] i 0..m-1 j 0..n-1
# 递推方程
# f(i, j) = min{f(i-1, j), f(i, j-1)} if f(i-1, j) != f(i, j-1)
# f(i, j) = f(i, j-1) + 1 if a[i-f(i, j-1)][j-f(i, j-1)] else 0
# 可以只要一层
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        dp = [int(c) for c in matrix[0]]
        ans = max(dp)

        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            dp[0] = int(matrix[i][0])
            ans = max(ans, dp[0])
            for j in range(1, n):
                if matrix[i][j] == '1':
                    if dp[j] != dp[j - 1]:
                        dp[j] = min(dp[j], dp[j - 1]) + 1
                    else:
                        length = dp[j - 1]
                        previ = i - length
                        prevj = j - length
                        dp[j] = (length + 1) if matrix[previ][
                                                    prevj] == '1' else length
                else:
                    dp[j] = 0
                ans = max(ans, dp[j])
        return ans * ans


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for _ in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                                       dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])

        return maxSide * maxSide


# 以下为自我练习
# 定义子问题，以i， j为右下角的正方形的最大边长
# 定义状态数组
# dp(i, j)
# 递推方程
# f(i, j) = min(f(i-1, j), f(i, j-1), f(i-1, j-1)) + 1 if (i, j)位置为1
#         = 0   else
# 返回值
# 取每一步中的最大值，再平方
# 优化空间复杂度
# 可以只使用一个数组，长度为矩阵的宽或高
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        h, w = len(matrix), len(matrix[0])
        dp = [int(e) for e in matrix[0]]
        dp_ = [0] * w
        max_side = any(dp)

        for i in range(1, h):
            dp_[0] = int(matrix[i][0])
            max_side = max(max_side, dp_[0])
            for j in range(1, w):
                if int(matrix[i][j]):
                    dp_[j] = min(dp[j], dp_[j - 1], dp[j - 1]) + 1
                    max_side = max(max_side, dp_[j])
                else:
                    dp_[j] = 0
            dp, dp_ = dp_, dp
        return max_side * max_side


def main():
    sol = Solution()

    matrix = [["0", "0", "0", "1"],
              ["1", "1", "0", "1"],
              ["1", "1", "1", "1"],
              ["0", "1", "1", "1"],
              ["0", "1", "1", "1"]]
    res = sol.maximalSquare(matrix)
    print(res)

    matrix = [
        ["1"]
    ]
    res = sol.maximalSquare(matrix)
    print(res)


if __name__ == '__main__':
    main()
