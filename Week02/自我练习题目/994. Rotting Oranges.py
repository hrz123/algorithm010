# 994. Rotting Oranges.py
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        # 记录下一回即将变rotting的位置
        rotting = {(i, j) for i in range(row) for j in range(col) if
                   grid[i][j] == 2}
        # 记录目前还是fresh的位置
        fresh = {(i, j) for i in range(row) for j in range(col) if
                 grid[i][j] == 1}
        timer = 0
        while fresh:
            if not rotting:
                return -1
            rotting = {(i + di, j + dj) for i, j in rotting for di, dj in
                       [(0, 1), (1, 0), (0, -1), (-1, 0)] if
                       (i + di, j + dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer


def main():
    pass


if __name__ == '__main__':
    main()
