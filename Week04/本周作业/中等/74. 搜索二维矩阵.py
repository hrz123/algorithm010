# 74. 搜索二维矩阵.py
from typing import List


# 标准的二分查找
# 单调
# 存在上下界
# 能够通过索引访问
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row * col - 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            # 注意这里是除以col
            r, c = divmod(mid, col)
            if target == matrix[r][c]:
                return True
            if target < matrix[r][c]:
                right = mid - 1
            else:
                left = mid + 1
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = row * col - 1

        while left <= right:
            mid = left + ((right - left) >> 1)
            r, c = divmod(mid, col)
            if matrix[r][c] == target:
                return True
            if target < matrix[r][c]:
                right = mid - 1
            else:
                left = mid + 1
        return False


def main():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    target = 3

    # matrix = [
    #     [1, 3, 5, 7],
    #     [10, 11, 16, 20],
    #     [23, 30, 34, 50]
    # ]
    # target = 13
    matrix = [[1, 3]]
    target = 3

    sol = Solution()
    res = sol.searchMatrix(matrix, target)
    print(res)


if __name__ == '__main__':
    main()
