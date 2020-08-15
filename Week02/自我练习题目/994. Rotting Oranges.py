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


# 以下为自我练习
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        rotting = {(i, j) for i in range(row) for j in range(col) if grid[i][
            j] == 2}
        fresh = {(i, j) for i in range(row) for j in range(col) if grid[i][j]
                 == 1}

        timer = 0
        while fresh:
            if not rotting:
                return -1
            # 只有fresh才能变rotting
            rotting = {(i + di, j + dj) for i, j in rotting
                       for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)] if (
                           i + di, j + dj) in fresh}
            fresh -= rotting
            timer += 1
        return timer


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        fresh = {(i, j) for i in range(h) for j in range(w) if grid[i][j] == 1}
        rotten = {(i, j) for i in range(h) for j in range(w) if grid[i][j] == 2}
        count = 0
        while fresh:
            if not rotten:
                return -1
            rotten = {(i, j) for i, j in fresh
                      for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0))
                      if (i + dx, j + dy) in rotten}
            fresh -= rotten
            count += 1
        return count


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        rotten = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2}
        timer = 0
        while fresh:
            if not rotten:
                return -1
            rotten = {(i, j) for i, j in fresh
                      for (di, dj) in ((0, 1), (1, 0), (0, -1), (-1, 0))
                      if (i + di, j + dj) in rotten}
            fresh -= rotten
            timer += 1
        return timer


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1}
        if not fresh:
            return 0
        rotten = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2}
        timer = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        while rotten:
            timer += 1
            rotten = {(i, j) for i, j in fresh for di, dj in dirs
                      if (i + di, j + dj) in rotten}
            fresh -= rotten
            if not fresh:
                return timer
        return -1


def main():
    sol = Solution()

    nums = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    res = sol.orangesRotting(nums)
    print(res)
    assert res == 4

    nums = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    res = sol.orangesRotting(nums)
    print(res)
    assert res == -1

    nums = [[0]]
    res = sol.orangesRotting(nums)
    print(res)
    assert res == 0


if __name__ == '__main__':
    main()
