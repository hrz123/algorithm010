# 200. 岛屿数量.py
from collections import deque
from typing import List


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
        # process current level logic
        grid[i][j] = '0'
        # drill down
        for k in range(4):
            self.__DFSMarking(grid, row, col, i + self.dx[k], j + self.dy[k])


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
