# 130. 被围绕的区域.py
from typing import List


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


def main():
    pass


if __name__ == '__main__':
    main()
