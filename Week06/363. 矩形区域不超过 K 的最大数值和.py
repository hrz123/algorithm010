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


# 时间复杂度: O(N^2*M^2) N是列数，M是行数
# 空间复杂度: O(1)常数空间


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        res = float("-inf")
        _sum = [0] * row
        for left in range(col):
            # 以left为左边界，每行的总和
            _sum = [0] * row
            for right in range(left, col):
                for j in range(row):
                    _sum[j] += matrix[j][right]
                # 在left，right为边界下的矩阵，求不超过K的最大数值和
                arr = [0]
                cur = 0
                for tmp in _sum:
                    cur += tmp
                    # 二分法
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(cur - arr[loc], res)
                    # 把累加和加入
                    bisect.insort(arr, cur)
        return res


# 时间复杂度没变: O(N^2*M^2) N是列数，M是行数，但是系数小了
# 空间复杂度: O(M)常数空间, M是行数

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
