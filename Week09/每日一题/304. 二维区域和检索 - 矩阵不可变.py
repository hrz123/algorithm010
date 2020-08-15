# 304. 二维区域和检索 - 矩阵不可变.py
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = []
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        dp = self.dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + \
                                   matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.dp:
            return 0
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[
            row2 + 1][col1] + self.dp[row1][col1]


# 以下为自我练习
class NumMatrix:
    # dp(i, j) = dp(i-1, j) +dp(i, j-1) - dp(i-1, j-1) + m[i][j]
    # 增加一维哨兵
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + \
                           matrix[i - 1][j - 1]
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] + self.dp[row1][col1] - \
               self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1]


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        self.dp = dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] - dp[i][j] + \
                                   matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - \
               self.dp[row2 + 1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
def main():
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    sol = NumMatrix(matrix)
    res = sol.sumRegion(2, 1, 4, 3)
    print(res)


if __name__ == '__main__':
    main()
