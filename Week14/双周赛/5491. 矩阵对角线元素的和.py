# 5491. 矩阵对角线元素的和.py
from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        for i in range(n):
            s += mat[i][i]
        for i in range(n):
            s += mat[i][n - i - 1]
        if n & 1:
            s -= mat[n >> 1][n >> 1]
        return s


def main():
    pass


if __name__ == '__main__':
    main()
