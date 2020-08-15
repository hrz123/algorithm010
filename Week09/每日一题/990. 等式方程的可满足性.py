# 990. 等式方程的可满足性.py
from typing import List


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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        for e in equations:
            if e[1] == "=":
                uf.union(ord(e[0]) - ord('a'), ord(e[3]) - ord('a'))
        for e in equations:
            if e[1] == '!':
                if uf.is_connected(ord(e[0]) - ord('a'), ord(e[3]) - ord('a')):
                    return False
        return True


# 以下为自我练习

class UnionFind:
    def __init__(self, k):
        self.uf = [-1] * (k + 1)
        self.sets_count = k

    def find(self, p):
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find((self.uf[p]))
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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        a = ord('a')
        for e in equations:
            if e[1] == '=':
                uf.union(ord(e[0]) - a, ord(e[3]) - a)
        for e in equations:
            if e[1] == '!':
                if uf.is_connected(ord(e[0]) - a, ord(e[3]) - a):
                    return False
        return True


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
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        a_uni = ord('a')
        for e in equations:
            if e[1] == '=':
                uf.union(ord(e[0]) - a_uni, ord(e[3]) - a_uni)
        for e in equations:
            if e[1] == '!':
                if uf.is_connected(ord(e[0]) - a_uni, ord(e[3]) - a_uni):
                    return False
        return True


def main():
    pass


if __name__ == '__main__':
    main()
