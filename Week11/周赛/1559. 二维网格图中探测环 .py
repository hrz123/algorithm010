# 1559. 二维网格图中探测环 .py
from typing import List


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = {}
        import sys
        sys.setrecursionlimit(10000000)

        def dfs(i, j, val, size, k):
            for di, dj in dirs[k:] + dirs[:k]:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and grid[_i][_j] == val:
                    if (_i, _j) not in visited:
                        visited[_i, _j] = size + 1
                        if dfs(_i, _j, val, size + 1, (k + 1) & 3):
                            return True
                    elif visited[i, j] - visited[_i, _j] >= 3:
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    visited[i, j] = 0
                    if dfs(i, j, grid[i][j], 0, 0):
                        return True
        return False


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = {}
        import sys
        sys.setrecursionlimit(100000000)

        def dfs(i, j, size, val, k):
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and grid[_i][_j] == val:
                    if (_i, _j) not in visited:
                        visited[_i, _j] = size + 1
                        if dfs(_i, _j, size + 1, val, (k + 1) & 3):
                            return True
                    elif visited[i, j] - visited[_i, _j] >= 3:
                        return True
            return False

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    visited[i, j] = 0
                    if dfs(i, j, 0, grid[i][j], 0):
                        return True
        return False


def main():
    sol = Solution()

    grid = [["b", "a", "c"],
            ["c", "a", "c"],
            ["d", "d", "c"],
            ["b", "c", "c"]]
    res = sol.containsCycle(grid)
    print(res)

    grid = [["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"],
            ["a", "a", "a", "a"]]
    res = sol.containsCycle(grid)
    print(res)

    grid = [["c", "a", "d"],
            ["a", "a", "a"],
            ["a", "a", "d"],
            ["a", "c", "d"],
            ["a", "b", "c"]]
    res = sol.containsCycle(grid)
    print(res)


if __name__ == '__main__':
    main()
