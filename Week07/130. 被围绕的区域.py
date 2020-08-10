# 130. 被围绕的区域.py
from typing import List


# 思路：
# 这道题我们拿到基本就可以确定是图的 dfs、bfs 遍历的题目了。
# 题目中解释说被包围的区间不会存在于边界上，所以我们会想到边界上的 OO 要特殊处理，
# 只要把边界上的 OO 特殊处理了，那么剩下的 OO 替换成 XX 就可以了。问题转化为，
# 如何寻找和边界联通的 OO，我们需要考虑如下情况。
#
#
# X X X X
# X O O X
# X X O X
# X O O X
# 这时候的 OO 是不做替换的。因为和边界是连通的。
# 为了记录这种状态，我们把这种情况下的 OO 换成 # 作为占位符，待搜索结束之后，
# 遇到 OO 替换为 XX（和边界不连通的 OO）；遇到 #，替换回 $O(和边界连通的 OO)。
#
# 如何寻找和边界联通的OO? 从边界出发，对图进行 dfs 和 bfs 即可。这里简单总结下 dfs 和 dfs。
#
# bfs 递归。可以想想二叉树中如何递归的进行层序遍历。
# bfs 非递归。一般用队列存储。
# dfs 递归。最常用，如二叉树的先序遍历。
# dfs 非递归。一般用 stack。
# 那么基于上面这种想法，我们有四种方式实现。

# 过一遍并查集
# dummy node 用来和所有的边上的O相连
# 最后遍历，只要不与dummy node相连的所有O，就变为X

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
            # 说明p的规模比较小
            self.uf[q_root] += self.uf[p_root]
            self.uf[p_root] = q_root
        else:
            self.uf[p_root] += self.uf[q_root]
            self.uf[q_root] = p_root

        self.sets_count -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        h, w = len(board), len(board[0])
        uf = UnionFind(h * w)

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    idx = i * w + j
                    if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                        uf.union(idx, h * w)
                    if i < h - 1 and board[i + 1][j] == 'O':
                        uf.union(idx, idx + w)
                    if j < w - 1 and board[i][j + 1] == 'O':
                        uf.union(idx, idx + 1)

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    if not uf.is_connected(i * w + j, h * w):
                        board[i][j] = 'X'


# 以下为自我练习

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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        h, w = len(board), len(board[0])
        dummy = h * w

        uf = UnionFind(dummy)

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    idx = i * w + j
                    if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                        uf.union(idx, dummy)
                    if i < h - 1 and j < w - 1:
                        if board[i + 1][j] == 'O':
                            uf.union(idx, idx + w)
                        if board[i][j + 1] == 'O':
                            uf.union(idx, idx + 1)

        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O' and not uf.is_connected(i * w + j, dummy):
                    board[i][j] = 'X'


# 以下为自我练习
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
            self.uf[q_root] += self.uf[p_root]
            self.uf[p_root] = q_root
        else:
            self.uf[p_root] += self.uf[q_root]
            self.uf[q_root] = p_root
        self.sets_count -= 1

    def is_connected(self, p, q):
        return self.find(p) == self.find(q)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        _i, _j = i + di, j + dj
                        if -1 < _i < m and -1 < _j < n and board[_i][_j] == 'O':
                            uf.union(i * n + j, _i * n + _j)
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    uf.union(i * n + j, m * n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not uf.is_connected(i * n + j, m * n):
                    board[i][j] = 'X'


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
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        uf = UnionFind(m * n)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    if i in {0, m - 1} or j in {0, n - 1}:
                        uf.union(i * n + j, m * n)
                    if i + 1 < m and board[i + 1][j] == 'O':
                        uf.union(i * n + j, (i + 1) * n + j)
                    if j + 1 < n and board[i][j + 1] == 'O':
                        uf.union(i * n + j, i * n + j + 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not uf.is_connected(i * n + j, m * n):
                    board[i][j] = 'X'


def main():
    sol = Solution()

    board = [['X', 'X', 'O'], ['X', 'O', 'X'], ['O', 'X', 'X']]
    sol.solve(board)
    print(board)

    board = [['O']]
    sol.solve(board)
    print(board)


if __name__ == '__main__':
    main()
