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


def main():
    pass


if __name__ == '__main__':
    main()
