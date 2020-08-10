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


# 以下为自我练习
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(i, j):
            grid[i][j] = 0
            res = 1
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n \
                        and grid[_i][_j] == 1:
                    res += dfs(_i, _j)
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()

        def dfs(i, j):
            res = 1
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n \
                        and (_i, _j) not in visited \
                        and grid[_i][_j] == 1:
                    visited.add((_i, _j))
                    res += dfs(_i, _j)
            return res

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    res = max(res, dfs(i, j))
        return res


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = set()
        ans = 0

        def dfs(i, j):
            res = 1
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n \
                        and (_i, _j) not in visited \
                        and grid[_i][_j]:
                    visited.add((_i, _j))
                    res += dfs(_i, _j)
            return res

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j]:
                    visited.add((i, j))
                    ans = max(ans, dfs(i, j))
        return ans


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
