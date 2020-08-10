# 980. 不同路径 III.py
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res = 0
        m, n = len(grid), len(grid[0])
        empty = set()
        start = end = None
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    empty.add((i, j))
                elif grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def backtrace(i, j):
            if (i, j) == end:
                self.res += 1
                return
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n:
                    if empty:
                        if (_i, _j) in empty:
                            empty.remove((_i, _j))
                            backtrace(_i, _j)
                            empty.add((_i, _j))
                    else:
                        if (_i, _j) == end:
                            backtrace(_i, _j)

        backtrace(start[0], start[1])

        return self.res


# 以下为自我练习
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = None
        end = None
        empty = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif not grid[i][j]:
                    empty.add((i, j))
        res = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(level, i, j, visited):
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n:
                    if level == len(empty):
                        if (_i, _j) == end:
                            nonlocal res
                            res += 1
                    else:
                        if (_i, _j) not in visited \
                                and (_i, _j) in empty:
                            visited.add((_i, _j))
                            dfs(level + 1, _i, _j, visited)
                            visited.remove((_i, _j))

        dfs(0, start[0], start[1], {start})
        return res


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start = None
        end = None
        empty = set()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif not grid[i][j]:
                    empty.add((i, j))
        res = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def backtrace(i, j):
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n:
                    if not empty:
                        if (_i, _j) == end:
                            nonlocal res
                            res += 1
                    else:
                        if (_i, _j) in empty:
                            empty.remove((_i, _j))
                            backtrace(_i, _j)
                            empty.add((_i, _j))

        backtrace(start[0], start[1])
        return res


def main():
    pass


if __name__ == '__main__':
    main()
