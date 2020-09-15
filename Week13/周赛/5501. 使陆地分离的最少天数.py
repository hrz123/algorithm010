# 5501. 使陆地分离的最少天数.py
from typing import List


class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        land = {(i, j) for i in range(m) for j in range(n) if grid[i][j]}
        if not self.is_connected(land, dirs):
            return 0
        for node in land:
            n_land = land - {node}
            if not self.is_connected(n_land, dirs):
                return 1
        return 2

    def is_connected(self, land, dirs):
        if not land:
            return False
        visited = set()

        def dfs(x, y):
            for dx, dy in dirs:
                _x, _y = x + dx, y + dy
                if (_x, _y) in land:
                    if (_x, _y) not in visited:
                        visited.add((_x, _y))
                        dfs(_x, _y)

        x, y = list(land)[0]
        visited.add((x, y))
        dfs(x, y)
        return len(visited) == len(land)


def main():
    sol = Solution()
    grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    res = sol.minDays(grid)
    print(res)

    grid = [[1, 1]]
    res = sol.minDays(grid)
    print(res)

    grid = [[1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    res = sol.minDays(grid)
    print(res)


if __name__ == '__main__':
    main()
