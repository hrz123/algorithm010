# 695. 岛屿的最大面积.py
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        if not grid or not grid[0]:
            return res
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()

        def dfs(i, j):
            ans = 1
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n \
                        and grid[_i][_j] \
                        and (_i, _j) not in visited:
                    visited.add((_i, _j))
                    ans += dfs(_i, _j)
            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    visited.add((i, j))
                    res = max(res, dfs(i, j))
        return res


def main():
    sol = Solution()

    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    res = sol.maxAreaOfIsland(grid)
    print(res)


if __name__ == '__main__':
    main()
