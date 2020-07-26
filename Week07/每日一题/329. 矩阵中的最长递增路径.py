# 329. 矩阵中的最长递增路径.py
import itertools
from typing import List


# 第一遍解法
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        res = 1
        h, w = len(matrix), len(matrix[0])

        # 因为是递增，所以不用判断是否访问过
        # 这里使用记忆化搜索
        memo = {}

        def dfs(i, j, pre):
            if (i, j) in memo:
                return memo[(i, j)]
            # 设定初始值，防止周围都比该值小，未进入递归
            memo[(i, j)] = 1
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w \
                        and matrix[_i][_j] > pre:
                    memo[(i, j)] = max(memo[i, j],
                                       1 + dfs(_i, _j, matrix[_i][_j]))
            return memo[(i, j)]

        for i in range(h):
            for j in range(w):
                res = max(res, dfs(i, j, matrix[i][j]))
        return res


# 执行用时击败了94%
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        h, w = len(matrix), len(matrix[0])

        # 因为是递增，所以不用判断是否访问过
        # 这里使用记忆化搜索
        memo = [[0] * w for _ in range(h)]

        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            cur = matrix[i][j]
            # 设定初始值，防止周围都比该值小，未进入递归
            memo[i][j] = 1
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w \
                        and matrix[_i][_j] > cur:
                    memo[i][j] = max(memo[i][j], 1 + dfs(_i, _j))
            return memo[i][j]

        return max(dfs(i, j) for i in range(h) for j in range(w))


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        h, w = len(matrix), len(matrix[0])

        # 因为是递增，所以不用判断是否访问过
        # 这里使用记忆化搜索
        memo = [[0] * w for _ in range(h)]

        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            cur = matrix[i][j]
            # 设定初始值，防止周围都比该值小，未进入递归
            memo[i][j] = 1
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w \
                        and matrix[_i][_j] > cur:
                    memo[i][j] = max(memo[i][j], 1 + dfs(_i, _j))
            return memo[i][j]

        return max(dfs(i, j) for i, j in itertools.product(range(h), range(w)))


# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         if not matrix or not matrix[0]:
#             return 0
#
#         row = len(matrix)
#         col = len(matrix[0])
#         lookup = [[0] * col for _ in range(row)]
#
#         def dfs(i, j):
#             if lookup[i][j] != 0:
#                 return lookup[i][j]
#             # 方法一
#             res = 1
#             for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
#                 tmp_i = x + i
#                 tmp_j = y + j
#                 if 0 <= tmp_i < row and 0 <= tmp_j < col and \
#                         matrix[tmp_i][tmp_j] > matrix[i][j]:
#                     res = max(res, 1 + dfs(tmp_i, tmp_j))
#             lookup[i][j] = max(res, lookup[i][j])
#             # 方法二
#             # val = matrix[i][j]
#             # lookup[i][j] = 1 + max(
#             #     dfs(i + 1, j) if 0 <= i + 1 < row and 0 <= j < pre and matrix[i + 1][j] > val else 0,
#             #     dfs(i - 1, j) if 0 <= i - 1 < row and 0 <= j < pre and matrix[i - 1][j] > val else 0,
#             #     dfs(i, j + 1) if 0 <= i < row and 0 <= j + 1 < pre and matrix[i][j + 1] > val else 0,
#             #     dfs(i, j - 1) if 0 <= i < row and 0 <= j - 1 < pre and matrix[i][j - 1] > val else 0,
#             # )
#             # 方法三
#             # lookup[i][j] = 1 + max(
#             #     [dfs(i + x, y + j) for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]] \
#             #      if 0 <= (i + x) < row and 0 <= (j + y) < pre and matrix[i + x][j + y] > matrix[i][j]] or [0]
#             # )
#
#             return lookup[i][j]
#
#         return max(dfs(i, j) for i in range(row) for j in range(col))


def main():
    sol = Solution()
    nums = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
    res = sol.longestIncreasingPath(nums)
    print(res)

    nums = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
    res = sol.longestIncreasingPath(nums)
    print(res)

    nums = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
            [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
            [39, 38, 37, 36, 35, 34, 33, 32, 31, 30],
            [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
            [59, 58, 57, 56, 55, 54, 53, 52, 51, 50],
            [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
            [79, 78, 77, 76, 75, 74, 73, 72, 71, 70],
            [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
            [99, 98, 97, 96, 95, 94, 93, 92, 91, 90],
            [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
            [119, 118, 117, 116, 115, 114, 113, 112, 111, 110],
            [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
            [139, 138, 137, 136, 135, 134, 133, 132, 131, 130],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    res = sol.longestIncreasingPath(nums)
    print(res)

    nums = [[7, 7, 5],
            [2, 4, 6],
            [8, 2, 0]]
    res = sol.longestIncreasingPath(nums)
    print(res)


if __name__ == '__main__':
    main()
