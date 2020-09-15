# 1351. 统计有序矩阵中的负数.py
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        c = 0
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if grid[i][j] >= 0:
                j += 1
                c += m - i - 1
            else:
                i -= 1
        if i == -1:
            c += (n - j) * m
        return c


# 以下为自我练习
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        c = 0
        while i >= 0 and j < n:
            if grid[i][j] >= 0:
                c += m - i - 1
                j += 1
            else:
                i -= 1
        if i == -1:
            c += (n - j) * m
        return c


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        c = 0
        while i >= 0 and j < n:
            if grid[i][j] >= 0:
                c += m - i - 1
                j += 1
            else:
                i -= 1
        if i == -1:
            c += (n - j) * m
        return c


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = m - 1, 0
        c = 0
        while i >= 0 and j < n:
            if grid[i][j] < 0:
                i -= 1
            else:
                c += m - i - 1
                j += 1
        if j < n:
            c += (n - j) * m
        return c


def main():
    sol = Solution()
    grid = [[4, 3, 2, -1],
            [3, 2, 1, -1],
            [1, 1, -1, -2],
            [-1, -1, -2, -3]]
    res = sol.countNegatives(grid)
    print(res)
    assert res == 8


if __name__ == '__main__':
    main()
