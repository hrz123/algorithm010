# 363. 矩形区域不超过 K 的最大数值和.py
import bisect
from typing import List


# 暴力解法
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        res = float('-inf')
        for row_start in range(m):
            for row_end in range(row_start, m):
                for col_start in range(n):
                    for col_end in range(col_start, n):
                        total = sum(matrix[i][j] for i in range(row_start,
                                                                row_end + 1)
                                    for j in range(col_start, col_end + 1))
                        if total <= k:
                            if total == k:
                                return k
                            res = max(res, total)
        return res


# 时间复杂度: O(N^2*m^2) N是列数，M是行数
# 空间复杂度: O(1)常数空间

# 固定左右边界，前缀和+二分
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        _sums = [0] * row
        for left in range(col):
            # 以left为左边界，每行的总和
            _sums[:] = [0] * row
            for right in range(left, col):
                for i in range(row):
                    _sums[i] += matrix[i][right]
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                # 初始化前缀和数组，和前缀和
                arr = [0]
                cur = 0
                for r in _sums:
                    cur += r
                    # 二分法查找
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
        return res


# 时间复杂度没变: O(N^2*m^2) N是列数，M是行数，但是系数小了
# 空间复杂度: O(m)常数空间, M是行数

# 以下为自我练习
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        res = float('-inf')
        _sum = [0] * row
        for left in range(col):
            _sum[:] = [0] * row
            for right in range(left, col):
                for i in range(row):
                    _sum[i] += matrix[i][right]
                # 初始化前缀和数组和前缀和
                arr = [0]
                cur = 0
                for r in _sum:
                    cur += r
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(res, cur - arr[loc])
                    bisect.insort(arr, cur)
        return res


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row, col = len(matrix), len(matrix[0])
        _sum = [0] * row
        res = float('-inf')
        for left in range(col):
            _sum[:] = [0] * row
            for right in range(left, col):
                for i in range(row):
                    _sum[i] += matrix[i][right]
                arr = [0]
                cur = 0
                for r in _sum:
                    cur += r
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(res, cur - arr[loc])
                    bisect.insort(arr, cur)
        return res


def main():
    sol = Solution()
    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    res = sol.maxSumSubmatrix(matrix, k)
    print(res)

    matrix = [[2, 2, -1]]
    k = 3
    res = sol.maxSumSubmatrix(matrix, k)
    print(res)


if __name__ == '__main__':
    main()
