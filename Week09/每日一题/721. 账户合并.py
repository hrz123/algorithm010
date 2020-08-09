# 721. 账户合并.py
from collections import defaultdict
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(10000)
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                uf.union(em_to_id[acc[1]], em_to_id[email])
        ans = defaultdict(list)
        for email in em_to_name:
            ans[uf.find(em_to_id[email])].append(email)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]


# 以下为自我练习
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(10000)
        em_to_name = {}
        em_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                em_to_name[email] = name
                if email not in em_to_id:
                    em_to_id[email] = i
                    i += 1
                uf.union(em_to_id[acc[1]], em_to_id[email])
        ans = defaultdict(list)
        for email in em_to_name:
            ans[uf.find(em_to_id[email])].append(email)
        return [[em_to_name[v[0]]] + sorted(v) for v in ans.values()]


def main():
    sol = Solution()

    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
                ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
                ["Mary", "mary@mail.com"]]
    res = sol.accountsMerge(accounts)
    Output = [["John", 'john00@mail.com', 'john_newyork@mail.com',
               'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"],
              ["Mary", "mary@mail.com"]]
    assert res == Output


if __name__ == '__main__':
    main()
