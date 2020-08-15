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
#         def dfs(start, j):
#             if lookup[start][j] != 0:
#                 return lookup[start][j]
#             # 方法一
#             res = 1
#             for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
#                 tmp_i = x + start
#                 tmp_j = y + j
#                 if 0 <= tmp_i < row and 0 <= tmp_j < col and \
#                         matrix[tmp_i][tmp_j] > matrix[start][j]:
#                     res = max(res, 1 + dfs(tmp_i, tmp_j))
#             lookup[start][j] = max(res, lookup[start][j])
#             # 方法二
#             # val = matrix[start][j]
#             # lookup[start][j] = 1 + max(
#             #     dfs(start + 1, j) if 0 <= start + 1 < row and 0 <= j < pre and matrix[start + 1][j] > val else 0,
#             #     dfs(start - 1, j) if 0 <= start - 1 < row and 0 <= j < pre and matrix[start - 1][j] > val else 0,
#             #     dfs(start, j + 1) if 0 <= start < row and 0 <= j + 1 < pre and matrix[start][j + 1] > val else 0,
#             #     dfs(start, j - 1) if 0 <= start < row and 0 <= j - 1 < pre and matrix[start][j - 1] > val else 0,
#             # )
#             # 方法三
#             # lookup[start][j] = 1 + max(
#             #     [dfs(start + x, y + j) for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]] \
#             #      if 0 <= (start + x) < row and 0 <= (j + y) < pre and matrix[start + x][j + y] > matrix[start][j]] or [0]
#             # )
#
#             return lookup[start][j]
#
#         return max(dfs(start, j) for start in range(row) for j in range(col))


# 以下为自我练习
# dfs
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        h, w = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[i, j]
            memo[i, j] = 1
            cur = matrix[i][j]
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + di, j + dj
                if -1 < _i < h and -1 < _j < w \
                        and matrix[_i][_j] > cur:
                    memo[i, j] = max(memo[i, j], 1 + dfs(_i, _j))
            return memo[i, j]

        return max(dfs(i, j) for i in range(h) for j in range(w))


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        h, w = len(matrix), len(matrix[0])
        memo = [[0] * w for _ in range(h)]

        def dfs(i, j):
            if memo[i][j]:
                return memo[i][j]
            memo[i][j] = 1
            cur = matrix[i][j]
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                _i, _j = i + dx, j + dy
                if -1 < _i < h and -1 < _j < w \
                        and matrix[_i][_j] > cur:
                    memo[i][j] = max(memo[i][j], 1 + dfs(_i, _j))
            return memo[i][j]

        return max(dfs(i, j) for i, j in itertools.product(range(h), range(w)))


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        memo = {}
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(matrix), len(matrix[0])

        # 这个函数寻找i， j为起始的最长路径
        def dfs(i, j):
            if (i, j) in memo:
                return memo[i, j]
            res = 1
            cur = matrix[i][j]
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and matrix[_i][_j] > cur:
                    res = max(res, 1 + dfs(_i, _j))
            memo[i, j] = res
            return res

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m, n = len(matrix), len(matrix[0])
        import functools
        @functools.lru_cache(None)
        def dfs(i, j):
            res = 1
            val = matrix[i][j]
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and matrix[_i][_j] > val:
                    res = max(res, 1 + dfs(_i, _j))
            return res

        res = 1
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


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
