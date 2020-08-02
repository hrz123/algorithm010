# 200. 岛屿数量.py
from collections import deque
from typing import List


# dfs
class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        res = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    self.__DFSMarking(grid, row, col, i, j)

        return res

    def __DFSMarking(self, grid, row, col, i, j):
        # recursion terminator
        if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == '0':
            return
        # process current row logic
        grid[i][j] = '0'
        # drill down
        for k in range(4):
            self.__DFSMarking(grid, row, col, i + self.dx[k], j + self.dy[k])


# bfs
class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        res = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    # bfs所需的队列，先添加进第一个为1的索引
                    deq = deque([(i, j)])
                    # 记录访问过的元素，先添加进当前索引
                    visited = {(i, j)}
                    while deq:
                        curi, curj = deq.popleft()
                        grid[curi][curj] = '0'
                        for k in range(4):
                            newi = curi + self.dx[k]
                            newj = curj + self.dy[k]
                            # 只有当新索引没被访问过
                            # 且在矩阵范围内
                            # 且索引对应值为1是，加入队列
                            if (newi, newj) not in visited and \
                                    0 <= newi < row and 0 <= newj < col and \
                                    grid[newi][newj] == '1':
                                deq.append((newi, newj))
                                # 同时加入已访问元素
                                visited.add((newi, newj))

        return res


# 并查集的思想


# 以下为自我练习
class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])

        def dfs_marking(r, c):
            # recursion terminator
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return

            # process current row logic
            grid[r][c] = 0

            # drill down
            for i in range(4):
                dfs_marking(r + self.dx[i], c + self.dy[i])

            # reverse current row status if needed

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs_marking(i, j)

        return res


class Solution:
    def __init__(self):
        self.dx = [0, 1, 0, -1]
        self.dy = [1, 0, -1, 0]

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        row = len(grid)
        col = len(grid[0])

        res = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    res += 1
                    self.__dfs_marking(grid, r, c, row, col)
        return res

    def __dfs_marking(self, grid, r, c, row, col):
        if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != '1':
            return

        grid[r][c] = '0'

        for i in range(4):
            self.__dfs_marking(grid, r + self.dx[i], c + self.dy[i], row, col)


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        res = 0

        row = len(grid)
        col = len(grid[0])

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    res += 1
                    deq = deque([(r, c)])
                    visited = {(r, c)}

                    while deq:
                        i, j = deq.popleft()
                        grid[i][j] = '0'

                        for k in range(4):
                            curr = i + dx[k]
                            curc = j + dy[k]
                            if (curr, curc) not in visited \
                                    and 0 <= curr < row \
                                    and 0 <= curc < col \
                                    and grid[curr][curc] == '1':
                                deq.append((curr, curc))
                                visited.add((curr, curc))

        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        dx = (0, 1, 0, -1)
        dy = (1, 0, -1, 0)

        def dfs(grid, i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return

            grid[i][j] = '0'
            for k in range(4):
                dfs(grid, i + dx[k], j + dy[k])

        res = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)
        return res


class Solution:
    def __init__(self):
        self.dx = (0, 1, 0, -1)
        self.dy = (1, 0, -1, 0)

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.__dfs_marking(grid, i, j, m, n)
                    res += 1
        return res

    def __dfs_marking(self, grid, i, j, m, n):
        # recursion terminator
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        grid[i][j] = '0'
        for k in range(4):
            self.__dfs_marking(grid, i + self.dx[k], j + self.dy[k], m, n)





def main():
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    sol = Solution()
    res = sol.numIslands(grid)
    print(res)


if __name__ == '__main__':
    main()
