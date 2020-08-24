# 200. 岛屿数量.py
from typing import List


# dfs flooding filling 算法
# 也有并查集算法
class UnionFind:
    def __init__(self, n):
        self.uf = [-1] * (n + 1)
        self.sets_count = n

    def find(self, p):
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.uf[p_root] > self.uf[q_root]:
            # 说明p_root的规模较小
            self.uf[q_root] += self.uf[p_root]
            self.uf[p_root] = q_root
        else:
            self.uf[p_root] += self.uf[q_root]
            self.uf[q_root] = p_root
        self.sets_count -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        h, w = len(grid), len(grid[0])
        uf = UnionFind(h * w + 1)

        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    idx = i * w + j
                    # 上下左右并在一起
                    if i > 0 and grid[i - 1][j] == "1":
                        uf.union(idx, idx - w)
                    if i < h - 1 and grid[i + 1][j] == '1':
                        uf.union(idx, idx + w)
                    if j > 0 and grid[i][j - 1] == '1':
                        uf.union(idx, idx - 1)
                    if j < w - 1 and grid[i][j + 1] == '1':
                        uf.union(idx, idx + 1)

                elif grid[i][j] == '0':
                    # 每链接一个就小一个集合
                    uf.union(i * w + j, h * w)

        return uf.sets_count


# 以下为自我练习
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        h, w = len(grid), len(grid[0])

        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs_marking(i, j, grid, h, w)

        return res

    def dfs_marking(self, i, j, grid, h, w):
        grid[i][j] = '2'
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            _i, _j = i + dx, j + dy
            if -1 < _i < h and -1 < _j < w \
                    and grid[_i][_j] == '1':
                self.dfs_marking(_i, _j, grid, h, w)


class UnionFind(object):
    def __init__(self, n):
        self.uf = [-1] * (n + 1)
        self.sets_count = n

    def find(self, p):
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)

        # 注意
        if p_root == q_root:
            return

        if self.uf[p_root] > self.uf[q_root]:
            # 说明p_root的规模较小
            self.uf[q_root] += self.uf[p_root]
            self.uf[p_root] = q_root
        else:
            self.uf[p_root] += self.uf[q_root]
            self.uf[q_root] = p_root
        self.sets_count -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        h, w = len(grid), len(grid[0])
        d = h * w
        uf = UnionFind(d + 1)

        for i in range(h):
            for j in range(w):
                idx = i * w + j
                if grid[i][j] == '1':
                    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        _i, _j = i + dx, j + dy
                        if -1 < _i < h and -1 < _j < w and grid[_i][_j] == '1':
                            uf.union(idx, _i * w + _j)
                else:
                    uf.union(idx, d)
        return uf.sets_count - 1


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        h, w = len(grid), len(grid[0])
        res = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs_marking(i, j, grid, h, w)
        return res

    def dfs_marking(self, i, j, grid, h, w):
        grid[i][j] = '#'
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            _i, _j = i + dx, j + dy
            if -1 < _i < h and -1 < _j < w \
                    and grid[_i][_j] == '1':
                self.dfs_marking(_i, _j, grid, h, w)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = 0

        def dfs_marking(i, j):
            grid[i][j] = '#'
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and grid[_i][_j] == '1':
                    dfs_marking(_i, _j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs_marking(i, j)
        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        res = 0
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs_marking(i, j):
            grid[i][j] = 'B'
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and grid[_i][_j] == '1':
                    dfs_marking(_i, _j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs_marking(i, j)
        return res


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs_marking(i, j):
            grid[i][j] = '#'
            for di, dj in dirs:
                _i, _j = i + di, j + dj
                if -1 < _i < m and -1 < _j < n and grid[_i][_j] == '1':
                    dfs_marking(_i, _j)

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs_marking(i, j)
        return res


class UnionFind:
    def __init__(self, k):
        self.uf = [-1] * (k + 1)
        self.sets_count = k

    def find(self, p):
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        if self.uf[p_root] > self.uf[q_root]:
            self.uf[q_root] += self.uf[p_root]
            self.uf[p_root] = q_root
        else:
            self.uf[p_root] += self.uf[q_root]
            self.uf[q_root] = p_root
        self.sets_count -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dummy = m * n
        uf = UnionFind(dummy)
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if grid[i][j] == '1':
                    if i + 1 < m and grid[i + 1][j] == '1':
                        uf.union(idx, idx + n)
                    if j + 1 < n and grid[i][j + 1] == '1':
                        uf.union(idx, idx + 1)
                else:
                    uf.union(idx, dummy)
        return uf.sets_count


def main():
    sol = Solution()
    grid = [["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"]]
    res = sol.numIslands(grid)
    print(res)

    grid = [["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]]
    res = sol.numIslands(grid)
    print(res)


if __name__ == '__main__':
    main()
