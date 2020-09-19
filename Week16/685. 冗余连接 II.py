# 685. 冗余连接 II.py
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
            return True
        if self.uf[p_root] > self.uf[q_root]:
            self.uf[q_root] += self.uf[p_root]
            self.uf[p_root] = q_root
        else:
            self.uf[p_root] += self.uf[q_root]
            self.uf[q_root] = p_root
        self.sets_count -= 1
        return False


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) \
            -> List[int]:
        n = len(edges)
        uf = UnionFind(n)

        last = []
        parent = {}
        candidates = []
        for st, ed in edges:
            if ed in parent:
                candidates.append([parent[ed], ed])
                candidates.append([st, ed])
            else:
                parent[ed] = st
                if uf.union(st, ed):
                    last = [st, ed]
        if not candidates:
            return last
        return candidates[0] if last else candidates[1]


def main():
    pass


if __name__ == '__main__':
    main()
