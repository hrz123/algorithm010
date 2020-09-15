# 1260. 二维网格迁移.py
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m * n
        res = [e for row in reversed(grid) for e in reversed(row)]
        res[:k] = res[:k][::-1]
        res[k:] = res[k:][::-1]
        return [[e for e in res[i:i + n]] for i in range(0, m * n, n)]


def main():
    sol = Solution()
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1
    res = sol.shiftGrid(grid, k)
    print(res)

    grid = [[1], [2], [3], [4], [7], [6], [5]]
    k = 23
    res = sol.shiftGrid(grid, k)
    print(res)


if __name__ == '__main__':
    main()
