# 547. 朋友圈.py
from typing import List


class UnionFind(object):
    """并查集类"""

    def __init__(self, n):
        """长度为n的并查集"""
        self.uf = [-1 for _ in range(n + 1)]  # 列表0位置空出
        self.sets_count = n  # 判断并查集里共有几个集合, 初始化默认互相独立

    # def find(self, p):
    #     """查找p的根结点(祖先)"""
    #     r = p  # 初始p
    #     while self.uf[p] > 0:
    #         p = self.uf[p]
    #     while r != p:  # 路径压缩, 把搜索下来的结点祖先全指向根结点
    #         self.uf[r], r = p, self.uf[r]
    #     return p

    # def find(self, p):
    #     while self.uf[p] >= 0:
    #         p = self.uf[p]
    #     return p

    def find(self, p):
        """尾递归，同时将遍历到的路径节点指向根节点"""
        if self.uf[p] < 0:
            return p
        self.uf[p] = self.find(self.uf[p])
        return self.uf[p]

    def union(self, p, q):
        """连通p,q 让q指向p，规模小的指向规模大的"""
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        if self.uf[proot] > self.uf[qroot]:  # 负数比较, 左边规模更小
            self.uf[qroot] += self.uf[proot]
            self.uf[proot] = qroot
        else:
            self.uf[proot] += self.uf[qroot]  # 规模相加
            self.uf[qroot] = proot
        self.sets_count -= 1  # 连通后集合总数减一

    def is_connected(self, p, q):
        """判断pq是否已经连通"""
        return self.find(p) == self.find(q)  # 即判断两个结点是否是属于同一个祖先


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        union_find = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    union_find.union(i, j)
        return union_find.sets_count


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M or not M[0]:
            return 0
        n = len(M)
        visited = [0] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                self.dfs(M, visited, i)
                res += 1
        return res

    def dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(M, visited, j)


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
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j]:
                    uf.union(i, j)
        return uf.sets_count


# dfs做法
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                self.__dfs(M, visited, i)
                res += 1
        return res

    def __dfs(self, M, visited, i):
        for j in range(len(M)):
            if M[i][j] and not visited[j]:
                visited[j] = True
                self.__dfs(M, visited, j)


# 思路
# 对于每一个人，如果没被访问过，将它的所有好友（包括自己）都记录为访问过
# 记录他好友的好友，只要没被访问，也记为访问过
# dfs直到他好友以及好友的好友，只要有关联，都被记为访问过
# count + 1
# 如果已经被访问，继续下一个
# 这边遍历完的结果就得到了
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        visited = [False] * n
        res = 0
        for i in range(n):
            if not visited[i]:
                self._dfs(i, M, visited, n)
                res += 1
        return res

    def _dfs(self, i, M, visited, n):
        for j in range(n):
            if M[i][j] and not visited[j]:
                visited[j] = True
                self._dfs(j, M, visited, n)


def main():
    sol = Solution()

    M = [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    res = sol.findCircleNum(M)
    print(res)

    M = [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]]
    res = sol.findCircleNum(M)
    print(res)

    M = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [1, 0, 1, 1]]
    res = sol.findCircleNum(M)
    print(res)


if __name__ == '__main__':
    main()
