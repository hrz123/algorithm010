# 5465. 子树中标签相同的节点数.py
from collections import deque, defaultdict
from typing import List


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]],
                      labels: str) -> List[int]:
        ans = [1] * n

        deq = deque([(0, None)])
        # level traversal
        levels = []
        while deq:
            output = []
            size = len(deq)
            for _ in range(size):
                node, parent = deq.popleft()
                output.append((node, parent))
                for e in reversed(edges):
                    if node in set(e):
                        deq.append((e[1 - e.index(node)], node))
                        edges.remove(e)
            levels.append(output)

        # bottom to up
        tree = defaultdict(set)

        for lvl in reversed(levels):
            for node, parent in lvl:
                res = 1
                for c in tree[node]:
                    if labels[c] == labels[node]:
                        res += 1
                ans[node] = res
                tree[parent].add(node)
                tree[parent].update(tree[node])
        return ans


class Solution:
    def countSubTrees(self, n: int, ed: List[List[int]], lab: str) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in ed:
            g[u].append(v)
            g[v].append(u)

        res = [0] * n

        def dfs(u, f):
            r1 = [0] * 26
            ir = ord(lab[u]) - ord('a')
            r1[ir] += 1
            for v in g[u]:
                if v == f:
                    continue
                r2 = dfs(v, u)
                for i in range(26):
                    r1[i] += r2[i]
            res[u] = r1[ir]
            return r1

        dfs(0, -1)

        return res


def main():
    sol = Solution()

    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    labels = "abaedcd"
    res = sol.countSubTrees(n, edges, labels)
    print(res)

    n = 4
    edges = [[0, 1], [1, 2], [0, 3]]
    labels = "bbbb"
    res = sol.countSubTrees(n, edges, labels)
    print(res)

    n = 5
    edges = [[0, 1], [0, 2], [1, 3], [0, 4]]
    labels = "aabab"
    res = sol.countSubTrees(n, edges, labels)
    print(res)

    n = 6
    edges = [[0, 1], [0, 2], [1, 3], [3, 4], [4, 5]]
    labels = "cbabaa"
    res = sol.countSubTrees(n, edges, labels)
    print(res)

    n = 7
    edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]
    labels = "aaabaaa"
    res = sol.countSubTrees(n, edges, labels)
    print(res)


if __name__ == '__main__':
    main()
