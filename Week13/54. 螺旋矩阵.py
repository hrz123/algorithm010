# 54. 螺旋矩阵.py
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        res = []
        while left <= right and top <= bottom:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])
            if left < right and top < bottom:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][col])
                for row in range(bottom - 1, top, -1):
                    res.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return res


def main():
    sol = Solution()
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    res = sol.spiralOrder(matrix)
    print(res)
    matrix = [
        [6, 9, 7]
    ]
    res = sol.spiralOrder(matrix)
    print(res)


if __name__ == '__main__':
    main()
